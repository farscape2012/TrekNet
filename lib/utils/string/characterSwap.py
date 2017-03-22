def charSwap(string, i, j):
    """ Swap two characters indexed by i and j in a string.
    :type string: string
    :type i, j: integer
    :rtype: string 
    """
    if i > len(string) or j > len(string):
        return string
    lst = list(string)
    lst[i], lst[j] = lst[j], lst[i]
    return ''.join(lst)
