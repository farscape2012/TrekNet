def firstNoneRepeatedCharacter(string):
    """
    find the first non-repeated (unique) character in a given string.
    """
    dict = {}
    for i in string:
        try:
            dict[i] += 1
        except KeyError:
            dict[i] = 1
    for i in string:
        if dict[i] == 1:
            return i
