def is_digit(s):
    return s in ['0', '1', '2']


def is_float(s):
    for char in s:
        if not is_digit(char):
            return False
