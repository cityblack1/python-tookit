SET = 'jO2iqWbFt0nM5EPGSmDXNpoygezRY9L1x8CTl6rUBKQHwVuIkh4fZ7cv3sdJaA'


def to_tiny(id):
    """Converts from an integer to a tinified string."""
    id = int(id)
    hexn = ""
    radix = len(SET)
    while True:
        r = id % radix
        hexn = SET[r] + hexn
        id = (id - r) / radix
        if id == 0:
            break
    return hexn


def from_tiny(s):
    """Converts from a tinified string to an integer.
    If any illegal characters are used in the string, return a -1.
    These tiny urls are almost always used to look up a database item by
    primary key, so this ensures that the database item is not found,
    and a normal 404 page is thrown.  If we instead threw an exception
    we'd have a different exception to handle and the normal 404 page would
    not be shown.
    """
    radix = len(SET)
    strlen = len(s)
    n = 0
    i = 0
    while i < strlen:
        p = SET.find(s[i])
        if (p < 0):
            return -1
        c = p * pow(radix, strlen - i - 1)
        n += c
        i += 1
    return n
