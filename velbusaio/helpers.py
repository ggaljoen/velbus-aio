"""
Helper functions
"""
import re


def keys_exists(element, *keys):
    """
    Check if *keys (nested) exists in `element` (dict).
    """
    if not isinstance(element, dict):
        raise AttributeError("keys_exists() expects dict as first argument.")
    if len(keys) == 0:
        raise AttributeError("keys_exists() expects at least two arguments, one given.")

    _element = element
    for key in keys:
        try:
            _element = _element[key]
        except KeyError:
            return False
    return _element


def checksum(arr):
    """
    Calculate checksum of the given array.
    The checksum is calculated by summing all values in an array, then performing the two's complement.
    :param arr: The array of bytes of which the checksum has to be calculated of.
    :return: The checksum of the given array.
    """
    crc = sum(arr)
    crc = crc ^ 255
    crc = crc + 1
    crc = crc & 255
    return crc


def h2(inp):
    """
    Format as hex upercase
    """
    return format(inp, "02x").upper()


def handle_match(match_dict, data):
    """
    Handle memory match from the module data
    """
    match_result = {}
    binary_data = f"{int(data):08b}"
    for num, match_data in match_dict.items():
        tmp = {}
        for match, res in match_data.items():
            if re.fullmatch(match[1:], binary_data):
                res2 = res.copy()
                res2["Data"] = int(data)
                tmp.update(res2)
        match_result[num] = tmp
    result = {}
    for res in match_result.values():
        if "Channel" in res:
            result[int(res["Channel"])] = {}
            if "SubName" in res and "Value" in res and res["Value"] != "PulsePerUnits":
                result[int(res["Channel"])] = {res["SubName"]: res["Value"]}
            else:
                # Very specifick for vmb7in
                # a = bit 0 to 5 = 0 to 63
                # b = a * 100
                multi = (data & 0x3F) * 100
                # c = bit 6 + 7
                #   00 = x1
                #   01 = x2,5
                #   10 = x0.05
                #   11 = x0.01
                # d = b * c
                if data >> 5 == 3:
                    val = multi * 0.01
                elif data >> 5 == 2:
                    val = multi * 0.05
                elif data >> 5 == 1:
                    val = multi * 2.5
                else:
                    val = multi
                result[int(res["Channel"])] = {res["Value"]: val}
    return result
