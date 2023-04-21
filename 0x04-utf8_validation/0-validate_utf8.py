#!/usr/bin/python3
"""UTF-8 Validator
"""


def validUTF8(data):
    """
    data: list integers
    return: if data is valid UTF-8, True
    """
    total_count = 0
    for i in data:
        if total_count == 0:
            if i & 128 == 0:
                total_count = 0
            elif i & 224 == 192:
                total_count = 1
            elif i & 240 == 224:
                total_count = 2
            elif i & 248 == 240:
                total_count = 3
            else:
                return False
        else:
            if i & 192 != 128:
                return False
            total_count -= 1
    if total_count == 0:
        return True
    return False
