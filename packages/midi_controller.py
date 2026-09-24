"""A single physical MIDI controller (one wing)."""
from tkinter import simpledialog
import tkinter as tk
import mido
import json
import time

class MidiController:
    FADER_NOTES = tuple(range(81, 99))
    NORMAL_BUTTON_NOTES = tuple(range(65))
    SPECIAL_BUTTON_NOTES = (100,101,102,103,104,105,106,107,112,113,114,115,116,117,118,119)
    SHIFT_KEY = 122
    NOTE_COLOR_MAP = {0:'#000000',1:'#1E1E1E',2:'#7F7F7F',3:'#FFFFFF',4:'#FF4C4C',5:'#FF0000',6:'#590000',7:'#190000',8:'#FFBD6C',9:'#FF5400',10:'#591D00',11:'#271B00',12:'#FFFF4C',13:'#FFFF00',14:'#595900',15:'#191900',16:'#88FF4C',17:'#54FF00',18:'#1D5900',19:'#142B00',20:'#4CFF4C',21:'#00FF00',22:'#005900',23:'#001900',24:'#4CFF5E',25:'#00FF19',26:'#00590D',27:'#001902',28:'#4CFF88',29:'#00FF55',30:'#00591D',31:'#001F12',32:'#4CFFB7',33:'#00FF99',34:'#005935',35:'#001912',36:'#4CC3FF',37:'#00A9FF',38:'#004152',39:'#001019',40:'#4C88FF',41:'#0055FF',42:'#001D59',43:'#000819',44:'#4C4CFF',45:'#0000FF',46:'#000059',47:'#000019',48:'#874CFF',49:'#5400FF',50:'#190064',51:'#0F0030',52:'#FF4CFF',53:'#FF00FF',54:'#590059',55:'#190019',56:'#FF4C87',57:'#FF0054',58:'#59001D',59:'#220013',60:'#FF1500',61:'#993500',62:'#795100',63:'#436400',64:'#033900',65:'#005735',66:'#00547F',67:'#0000FF',68:'#00454F',69:'#2500CC',70:'#7F7F7F',71:'#202020',72:'#FF0000',73:'#BDFF2D',74:'#AFED06',75:'#64FF09',76:'#108B00',77:'#00FF87',78:'#00A9FF',79:'#002AFF',80:'#3F00FF',81:'#7A00FF',82:'#B21A7D',83:'#402100',84:'#FF4A00',85:'#88E106',86:'#72FF15',87:'#00FF00',88:'#3BFF26',89:'#59FF71',90:'#38FFCC',91:'#5B8AFF',92:'#3151C6',93:'#877FE9',94:'#D31DFF',95:'#FF005D',96:'#FF7F00',97:'#B9B000',98:'#90FF00',99:'#835D07',100:'#392b00',101:'#144C10',102:'#0D5038',103:'#15152A',104:'#16205A',105:'#693C1C',106:'#A8000A',107:'#DE513D',108:'#D86A1C',109:'#FFE126',110:'#9EE12F',111:'#67B50F',112:'#1E1E30',113:'#DCFF6B',114:'#80FFBD',115:'#9A99FF',116:'#8E66FF',117:'#404040',118:'#757575',119:'#E0FFFF',120:'#A00000',121:'#350000',122:'#1AD000',123:'#074200',124:'#B9B000',125:'#3F3100',126:'#B35F00',127:'#4B1502'}
    def __init__(self, controller_id, data, gui_instance=None, websocket_callback=None):
        self.controller_id = controller_id
        self.gui_instance = gui_instance
        self.websocket_callback = websocket_callback
        self.midi_inport = None
        self.midi_outport = None
        self.data = data or {}
        self.note_executor_dictionary = self.data.setdefault("executors", {})
        self.cc_fader_index_dictionary = self.data.setdefault("cc_faders", {})
        self.default_midi_inport = self.data.get("default", "")
        self.default_midi_outport = self.data.get("default", "")
        self.fader_last_value_dictionary = {str(cc): 0.0 for cc in self.cc_fader_index_dictionary}
        self.default_brightness_level = 6
        self.default_blink_channel = 10
        self.BUTTON_COLORS = list(range(0,64)) if controller_id == 1 else list(range(64,128))
    def send_gui_instance(self, gui_instance): self.gui_instance = gui_instance
    @staticmethod
    def ask_input(prompt=""):
        root=tk.Tk(); root.withdraw(); result=simpledialog.askstring("Input",prompt); print(result); root.destroy(); return result
    def ask_labels(self):
        short_label=self.ask_input('Please Input the "Short" Label'); long_label=self.ask_input('Please Input the "Long" Label')
        return short_label, (short_label if long_label is None else long_label)
    def load_data(self, data):
        self.data=data or {}; self.note_executor_dictionary=self.data.setdefault("executors",{}); self.cc_fader_index_dictionary=self.data.setdefault("cc_faders",{}); self.default_midi_inport=self.data.get("default",""); self.default_midi_outport=self.default_midi_inport; self.fader_last_value_dictionary={str(cc):0.0 for cc in self.cc_fader_index_dictionary}
    def get_persisted_data(self):
        self.data["executors"]=self.note_executor_dictionary; self.data["cc_faders"]=self.cc_fader_index_dictionary; self.data["default"]=self.default_midi_inport; return self.data
    def load_labels(self):
        for button_id,data in self.note_executor_dictionary.items():
            if data.get("short_label") is not None: self.set_button_label(button_id, data["short_label"], data.get("long_label") or data["short_label"])
    def set_button_label(self, button_id, short_label, long_label): self.gui_instance.set_button_label(button_id=int(button_id), short_label=short_label, long_label=long_label)
    def set_gui_button_color(self, button_id, color_note): self.gui_instance.set_button_color(button_id=int(button_id), hex_color=self.get_hex_color_from_note(color_note))
    def set_gui_fader_value(self, fader_id, value): self.gui_instance.set_fader_value(fader_id=fader_id, value=value)
    def get_hex_color_from_note(self,note): return self.NOTE_COLOR_MAP.get(int(note))
    def _prompt_for_port(self,names,label):
        print(f"Please select the {label}\n", '\n '.join(f"{i+1}- {x}" for i,x in enumerate(names))); return names[int(self.ask_input("Please select an available port"))-1]
    def select_midi_ports(self):
        ins=mido.get_input_names(); outs=mido.get_output_names()
        if self.default_midi_inport not in ins: self.default_midi_inport=self._prompt_for_port(ins,f"device {self.controller_id} Input")
        if self.default_midi_outport not in outs: self.default_midi_outport=self._prompt_for_port(outs,f"device {self.controller_id} Output")
        self.midi_inport=mido.open_input(self.default_midi_inport); self.midi_outport=mido.open_output(self.default_midi_outport)
    def send_midi_message(self,midi_message_type,channel,note,velocity): self.midi_outport.send(mido.Message(type=str(midi_message_type),channel=int(channel),note=int(note),velocity=int(velocity)))
    def set_all_pads(self,velocity=0,channel=None):
        for pad in self.NORMAL_BUTTON_NOTES: self.send_midi_message("note_on",self.default_brightness_level if channel is None else channel,pad,velocity)
    def choose_color(self):
        for pad,color in enumerate(self.BUTTON_COLORS): self.send_midi_message('note_on',self.default_brightness_level,pad,color); self.set_gui_button_color(pad,color)
        for pad in self.SPECIAL_BUTTON_NOTES: self.send_midi_message('note_on',0,pad,0); self.set_gui_button_color(pad,0)
        message=self.midi_inport.receive()
        while message.type != 'note_on' or message.note not in self.NORMAL_BUTTON_NOTES: message=self.midi_inport.receive()
        return self.BUTTON_COLORS[message.note]
    def append_note(self,note,executor_index,short_label,long_label,color=None):
        entry={"executor_index":executor_index,"color":color,"short_label":short_label,"long_label":long_label}; self.note_executor_dictionary[str(note)]=entry
    def append_cc(self,cc,note): self.cc_fader_index_dictionary[str(cc)]=note
    def link_executor_note(self,note):
        entry=self.note_executor_dictionary.get(str(note)); executor_index=entry["executor_index"] if entry else int(self.ask_input("Please input the id of the executor"))-1
        short_label,long_label=self.ask_labels(); color=self.choose_color() if note in self.NORMAL_BUTTON_NOTES else 1; self.append_note(note,executor_index,short_label,long_label,color); self.set_button_label(note,short_label,long_label)
    def link_cc_note(self,cc): self.append_cc(cc,int(self.ask_input("Please input the id of the note")))
    def get_fader_index_from_cc(self,cc): return self.cc_fader_index_dictionary.get(str(cc))
    def control_change_handler(self,cc,value):
        fader_index=self.get_fader_index_from_cc(cc); self.set_gui_fader_value(cc,value); value=round(value/127,2); last=self.fader_last_value_dictionary[str(cc)]
        if last != value: self.websocket_callback("fader",fader_index,value); self.fader_last_value_dictionary[str(cc)]=value
    def toggle_blink_note(self,note,toggle_on):
        entry=self.note_executor_dictionary.get(str(note));
        if not entry or entry.get("color",-1)<0: return
        self.send_midi_message("note_on",self.default_blink_channel if toggle_on else self.default_brightness_level,note,entry["color"])
    def update_colors(self):
        self.set_all_pads();
        for note,entry in self.note_executor_dictionary.items():
            color=entry.get("color",-1)
            if color >= 0: self.send_midi_message('note_on',self.default_brightness_level,int(note),color); self.set_gui_button_color(note,color)
    def note_loop(self,message,config_mode=False):
        if message.type == "control_change":
            if config_mode: self.link_cc_note(message.control); return
            if str(message.control) in self.cc_fader_index_dictionary: self.control_change_handler(message.control,message.value)
        elif message.type in ("note_on","note_off"):
            if message.type=='note_on' and config_mode: self.link_executor_note(message.note); return
            entry=self.note_executor_dictionary.get(str(message.note))
            if entry: self.websocket_callback("click",entry["executor_index"],pressed=message.velocity==127)
    def imitate_midi_message(self,type,channel,note=None,velocity=None,cc=None,value=None,config_mode=False):
        if type=="control_change": self.note_loop(mido.Message(type=type,channel=int(channel),control=int(cc),value=int(value)),config_mode)
        elif type in ("note_on","note_off"): self.note_loop(mido.Message(type=type,channel=int(channel),note=int(note),velocity=int(velocity)),config_mode)
    def poll(self,config_mode=False):
        for msg in self.midi_inport.iter_pending(): self.note_loop(msg,config_mode)
