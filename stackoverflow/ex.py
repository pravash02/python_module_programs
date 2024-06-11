import re
import string


weird_string = 'Nikon\x00\x02\x00\x00\x00II*\x00\x08\x00\x00\x00\x15\x00\x01\x00\x07\x00\x04\x00\x00\x00\x00\x02\x00\x00\x02\x00\x03\x00\x02\x00\x00\x00\x00\x00\x00\x00\x03\x00\x02\x00\x06\x00\x00\x00\n\x01\x00\x00\x04\x00\x02\x00\x07\x00\x00\x00\x10\x01\x00\x00\x05\x00\x02\x00\r\x00\x00\x00\x18\x01\x00\x00\x06\x00\x02\x00\x07\x00\x00\x00&\x01\x00\x00\x07\x00\x02\x00\x07\x00\x00\x00.\x01\x00\x00\x08\x00\x02\x00\x08\x00\x00\x006\x01\x00\x00\n\x00\x05\x00\x01\x00\x00\x00>\x01\x00\x00\x0f\x00\x02\x00\x07\x00\x00\x00F\x01\x00\x00\x00\x02\x00\x0e\x00\x00\x00N\x01\x00\x00\x00\x02\x00\r\x00\x00\x00\\\x01\x00\x00\x00\x05\x00\x01\x00\x00\x00j\x01\x00\x00\x00\x05\x00\x01\x00\x00\x00r\x01\x00\x00\x00\x07\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x10\x00\x00\x00z\x01\x00\x00\x00\x08\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x05\x00\x00\x00\x01\x00\x00\x10\x00\x07\x00\x00\x00\x00\x01\x00\x00\x11\x00\x04\x00\x01\x00\x00\x00\x02\x00\x00\x00\x01\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00COLOR\x00FINE  \x00\x00AUTO        \x00\x00AUTO  \x00\x00AF-S  \x00\x00       \x00"\x00\x00\x03\x00\x00AUTO  \x00\x00AUTO         \x00OFF         \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x00\x00\x00d\x00\x00\x00               \x00OFF \x00\x00\x05\x02\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00a\x05\x00\x00\x00\x03r\x00`\x14\x00\x01!\x00\x00\x06{\x00\x00\x00\x00\x00\x00\x1f\x05\x0b\x00\x1b\x07\x06&\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07*]\x00\x00\x06\x07\x00\x00\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x007\x06\x00\x00J\x02\x15\x1b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02C\x16\x00\x00\x00\x00\x04\x07\x00\x1a\x00\x00\x00\x00\x19a\x121uv\x1b\x17\x12\x18\x14\x15\x15\x17\x00\x00\x00\x00\x0c\x00\r\x01\x02 R\x00\x03\x03z\x00\x00\x00\x0fch\x0cU\x0ed\x00d\x00\x0e\x12\x06\x06\x01\x02L\x00\x02\x00\x00@\x00M\x00\x00\x00\x11\x00\x00\x00\x00\x11\x11\x11\x11\x00\x00\x00c\x00\x00\x03\x00\x00\x00\x00\x04\x00\x00\x00\x00\x00\x0b\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00eC!\x07\x00\x03\x01\x03\x00\x01\x00\x00\x00\x06\x00\x00\x00\x1a\x01\x05\x00\x01\x00\x00\x00\x02\x00\x00\x1b\x01\x05\x00\x01\x00\x00\x00\x02\x00\x00(\x01\x03\x00\x01\x00\x00\x00\x02\x00\x00\x00\x01\x02\x04\x00\x01\x00\x00\x00\x134\x00\x00\x02\x02\x04\x00\x01\x00\x00\x00%\x00\x00\x13\x02\x03\x00\x01\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00,\x01\x00\x00\x01\x00\x00\x00,\x01\x00\x00\x01\x00\x00\x00'


def decode_weird_string(weird_string):
    # Create a translation table to replace whitespace characters
    translation_table = str.maketrans({
        '\x00': '',  # Null character
        '\x01': '\n',  # Start of Heading
        '\x02': '\t',  # Start of Text
        '\x03': '',  # End of Text
        '\x04': '',  # End of Transmission
        '\x05': '',  # Enquiry
        '\x06': '',  # Acknowledgement
        '\x07': '',  # Bell
        '\x08': '',  # Backspace
        '\x0B': '',  # Vertical Tab
        '\x0C': '\n',  # Form Feed
        '\x0E': '',  # Shift Out
        '\x0F': '',  # Shift In
    })

    filtered_string = ''.join(c if c in string.printable else ' ' for c in weird_string)

    decoded_string = filtered_string.translate(translation_table)
    print(decoded_string)

    return decoded_string.strip()


decoded = decode_weird_string(weird_string)
# print(decoded)