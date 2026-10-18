import json
import threading
import websocket

from packages.utils import md5_hex

# Values returned by connection_status()
STATUS_CONNECTING = "connecting"
STATUS_CONNECTED = "connected"
STATUS_LOGIN_FAILED = "login_failed"
STATUS_UNREACHABLE = "unreachable"


class Dot2WebSocketHandler:
    def __init__(self,
                 host="10.0.0.50",
                 password="1",
                 heartbeat_step=10,
                 debug=True
                 ):
        self.USERNAME = "remote"
        self.HEARTBEAT_STEP = heartbeat_step
        self.DEBUG = debug
        self.update_credentials(host, password)

        self.ws = None
        self._ws_thread = None
        self._heartbeat_thread = None
        self._stop_event = threading.Event()
        self._reset_connection_state()

        # Callback registry: { "requestType": [callable, ...] }
        self._callbacks = {}
        # One-shot callbacks waiting for next matching message
        self._one_shot_callbacks = {}
        self._callbacks_lock = threading.Lock()

        self.BWING_START_INDEX = [300, 400, 500, 600, 700, 800]
        self.BWING_ITEMS_COUNT = [16, 16, 16, 16, 16, 16]
        self.BWING_ITEMS_TYPE = [3, 3, 3, 3, 3, 3]
        self.BWING_VIEW = 3
        self.BWING_EXEC_VIEW_MODE = 2

        self.FWING_START_INDEX = [0, 100, 200]
        self.FWING_ITEMS_COUNT = [22, 22, 22]
        self.FWING_ITEMS_TYPE = [2, 3, 3]
        self.FWING_VIEW = 2
        self.FWING_EXEC_VIEW_MODE = 1

    ###################################################
    #                    Callbacks                    #
    ###################################################

    def on(self, request_type, callback):
        """
        Register a persistent callback for a given requestType (or any key in the response).
        The callback receives the full parsed message dict.

        Example:
            dot2_ws.on("playbacks", handle_playbacks)
        """
        with self._callbacks_lock:
            if request_type not in self._callbacks:
                self._callbacks[request_type] = []
            self._callbacks[request_type].append(callback)

    def off(self, request_type, callback=None):
        """
        Remove a persistent callback.
        If callback is None, removes all callbacks for that request_type.
        """
        with self._callbacks_lock:
            if request_type not in self._callbacks:
                return
            if callback is None:
                del self._callbacks[request_type]
            else:
                self._callbacks[request_type] = [
                    cb for cb in self._callbacks[request_type] if cb != callback
                ]

    def once(self, request_type, callback):
        """
        Register a one-shot callback that fires only on the next matching message then removes itself.

        Example:
            dot2_ws.once("playbacks", handle_single_playback_response)
        """
        with self._callbacks_lock:
            if request_type not in self._one_shot_callbacks:
                self._one_shot_callbacks[request_type] = []
            self._one_shot_callbacks[request_type].append(callback)

    def _dispatch(self, data):
        # Build the set of keys to match against
        keys_to_check = set(data.keys())

        # Also add the value of responseType as a matchable key
        if "responseType" in data:
            keys_to_check.add(data["responseType"])

        with self._callbacks_lock:
            persistent = {k: list(v) for k, v in self._callbacks.items()}
            one_shot = {k: list(v) for k, v in self._one_shot_callbacks.items()}
            for key in one_shot:
                if key in keys_to_check:
                    self._one_shot_callbacks.pop(key, None)

        for key, callbacks in persistent.items():
            if key in keys_to_check:
                for cb in callbacks:
                    try:
                        cb(data)
                    except Exception as e:
                        if self.DEBUG:
                            print(f"Callback error [{key}]: {e}")

        for key, callbacks in one_shot.items():
            if key in keys_to_check:
                for cb in callbacks:
                    try:
                        cb(data)
                    except Exception as e:
                        if self.DEBUG:
                            print(f"One-shot callback error [{key}]: {e}")

    ###################################################
    #                   WS Internals                  #
    ###################################################

    def _send(self, obj):
        if self.ws is None:
            return
        try:
            self.ws.send(json.dumps(obj, separators=(",", ":")))
        except Exception as error:  # Socket already closed, console switched off...
            if self.DEBUG:
                print("Send failed:", error)

    def _is_current(self, ws):
        """False for callbacks coming from a previous connection that is being replaced."""
        return ws is self.ws

    def _on_open(self, ws):
        if not self._is_current(ws):
            return
        if self.DEBUG:
            print("WS open")

    def _on_message(self, ws, msg):
        if not self._is_current(ws):
            return
        try:
            data = json.loads(msg)
        except Exception:
            if self.DEBUG:
                print("<< (non-JSON)", msg[:120])
            return

        if self.DEBUG:
            print("<<", data)

        # Internal handshake handling
        if data.get("status") == "server ready":
            self._send({"session": 0})
            return

        if "session" in data and self.session_id is None:
            self.session_id = data["session"]
            if self.DEBUG:
                print("Assigned session:", self.session_id)
            if data.get("forceLogin", True):
                self._send({
                    "requestType": "login",
                    "username": self.USERNAME,
                    "password": self.PASSWORD_MD5,
                    "session": self.session_id,
                    "maxRequests": 10
                })
            else:
                self.logged_in = True
            return

        if data.get("responseType") == "login":
            if data.get("result") is True:
                if self.DEBUG:
                    print("Login OK")
                self.logged_in = True
            else:
                self.login_failed = True
                if self.DEBUG:
                    print("Login FAILED")
            return

        # Dispatch to user callbacks
        self._dispatch(data)

    def _on_error(self, ws, err):
        if not self._is_current(ws):
            return
        self.last_error = str(err)
        if self.DEBUG:
            print("ERR", err)

    def _on_close(self, ws, code, reason):
        if not self._is_current(ws):
            return
        self.connection_closed = True
        self.logged_in = False
        if self.DEBUG:
            print("CLOSE", code, reason)

    ###################################################
    #                   Public API                    #
    ###################################################

    def update_credentials(self, host, password):
        """Changes the console address and password used by the next connect()."""
        self.HOST = host
        self.URL = f"ws://{host}/?ma=1"
        self.ORIGIN = f"http://{host}"
        self.PLAINTEXT_PASSWORD = password
        self.PASSWORD_MD5 = md5_hex(password)

    def connection_status(self):
        """One of STATUS_CONNECTED, STATUS_LOGIN_FAILED, STATUS_UNREACHABLE (refused or dropped) or STATUS_CONNECTING."""
        if self.logged_in:
            return STATUS_CONNECTED
        if self.login_failed:
            return STATUS_LOGIN_FAILED
        if self.connection_closed:
            return STATUS_UNREACHABLE
        return STATUS_CONNECTING

    def _reset_connection_state(self):
        self.session_id = None
        self.logged_in = False
        self.login_failed = False
        self.connection_closed = False
        self.last_error = None
        self._stop_event = threading.Event()

    def connect(self):
        """
        Opens the websocket in a background thread and logs in. Does not block:
        follow the progress with connection_status().
        """
        self._reset_connection_state()
        ws = websocket.WebSocketApp(
            self.URL,
            header=[f"Origin: {self.ORIGIN}"],
            on_open=self._on_open,
            on_message=self._on_message,
            on_error=self._on_error,
            on_close=self._on_close
        )
        self.ws = ws
        self._ws_thread = threading.Thread(
            target=lambda: ws.run_forever(skip_utf8_validation=True),
            daemon=True
        )
        self._ws_thread.start()
        self._heartbeat_thread = threading.Thread(
            target=self._heartbeat, args=(ws, self._stop_event), daemon=True
        )
        self._heartbeat_thread.start()

    def _heartbeat(self, ws, stop_event):
        """Keeps the session alive until disconnect() sets the stop event of this connection."""
        while not stop_event.wait(self.HEARTBEAT_STEP):
            if self._is_current(ws) and self.session_id is not None:
                self._send({"session": self.session_id})

    def disconnect(self):
        self._stop_event.set()
        self.logged_in = False
        if self.ws:
            self.ws.close()

    def send_playback_click(self, executor_index, page_index=0, button_id=0, ptype=0, pressed=True):
        if not self.logged_in or self.session_id is None:
            if self.DEBUG:
                print("Not ready; cannot send userInput yet.")
            return

        payload = {
            "requestType": "playbacks_userInput",
            "cmdline": "",
            "execIndex": int(executor_index),
            "pageIndex": page_index,
            "buttonId": button_id,
            "pressed": pressed,
            "released": not pressed,
            "type": ptype,
            "session": self.session_id,
            "maxRequests": 0
        }
        self._send(payload)

    def send_playback_fader(self, fader_index, fader_value, page_index=0, type=1):
        if not self.logged_in or self.session_id is None:
            if self.DEBUG:
                print("Not ready; cannot send userInput yet.")
            return

        payload = {
            "requestType": "playbacks_userInput",
            "execIndex": fader_index,
            "pageIndex": page_index,
            "faderValue": fader_value,
            "type": type,
            "session": self.session_id,
            "maxRequests": 0
        }
        self._send(payload)

    def poll_exec_state(self):
        if self.session_id is None:
            if self.DEBUG:
                print("No session yet")
            return

        # Poll B-Wings
        self._send({
        "requestType": "playbacks",
        "startIndex": self.BWING_START_INDEX,
        "itemsCount": self.BWING_ITEMS_COUNT,
        "pageIndex": 0,
        "itemsType": self.BWING_ITEMS_TYPE,
        "view": self.BWING_VIEW,
        "execButtonViewMode": self.BWING_EXEC_VIEW_MODE,
        "buttonsViewMode": 0,
        "session": self.session_id,
        "maxRequests": 1
    })

        # Poll F-Wings
        self._send({
            "requestType": "playbacks",
            "startIndex": self.FWING_START_INDEX,
            "itemsCount": self.FWING_ITEMS_COUNT,
            "pageIndex": 0,
            "itemsType": self.FWING_ITEMS_TYPE,
            "view": self.FWING_VIEW,
            "execButtonViewMode": self.FWING_EXEC_VIEW_MODE,
            "buttonsViewMode": 0,
            "session": self.session_id,
            "maxRequests": 1
        })
