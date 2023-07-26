#!/usr/bin/python3
"""
Contains a method that determines if a given data set
represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Check if data os a valid UTF-8 encoding

    Args:
        data: A list of bytes.

    Returns:
        True if data is a valid UTF-8 encoding, False otherwise.
    """
    for byte in data:
        if byte >> 7 == 0:
            continue
        elif byte >> 5 == 0b110:
            continue
        elif byte >> 4 == 0b1110:
            continue
        elif byte >> 3 == 0b11110:
            continue
        else:
            return False
    return True
