"""Small pure helpers shared by several modules."""

import hashlib
import ipaddress


def md5_hex(text):
    """MD5 hash of the text as lowercase hexadecimal, which is what the dot2 expects as password."""
    return hashlib.md5(text.encode("utf-8")).hexdigest()


DARK_TEXT = "#000000"
LIGHT_TEXT = "#FFFFFF"


def relative_luminance(hex_color):
    """
    Perceived brightness of "#RRGGBB" from 0 (black) to 1 (white), as defined by the
    WCAG accessibility guidelines. Green counts much more than blue to the human eye.
    """
    hex_color = hex_color.lstrip("#")
    if len(hex_color) != 6:
        raise ValueError(f"Invalid hex color: {hex_color}")

    def linear(channel_hex):
        value = int(channel_hex, 16) / 255
        return value / 12.92 if value <= 0.04045 else ((value + 0.055) / 1.055) ** 2.4

    red, green, blue = linear(hex_color[0:2]), linear(hex_color[2:4]), linear(hex_color[4:6])
    return 0.2126 * red + 0.7152 * green + 0.0722 * blue


def contrast_ratio(luminance_a, luminance_b):
    """WCAG contrast ratio between two luminances: 1 (no contrast) to 21 (black on white)."""
    lighter, darker = max(luminance_a, luminance_b), min(luminance_a, luminance_b)
    return (lighter + 0.05) / (darker + 0.05)


def readable_text_color(background_hex):
    """Black or white, whichever is easier to read on the background color."""
    background = relative_luminance(background_hex)
    on_dark_text = contrast_ratio(background, 0.0)   # black text
    on_light_text = contrast_ratio(background, 1.0)  # white text
    return DARK_TEXT if on_dark_text >= on_light_text else LIGHT_TEXT


def is_valid_ipv4(text):
    """True when text is a well formed IPv4 address: four numbers from 0 to 255 separated by dots."""
    try:
        ipaddress.IPv4Address(text.strip())
    except (ValueError, AttributeError):
        return False
    return True
