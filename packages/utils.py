"""Small pure helpers shared by several modules."""

import hashlib
import ipaddress


def md5_hex(text):
    """MD5 hash of the text as lowercase hexadecimal, which is what the dot2 expects as password."""
    return hashlib.md5(text.encode("utf-8")).hexdigest()


def is_valid_ipv4(text):
    """True when text is a well formed IPv4 address: four numbers from 0 to 255 separated by dots."""
    try:
        ipaddress.IPv4Address(text.strip())
    except (ValueError, AttributeError):
        return False
    return True
