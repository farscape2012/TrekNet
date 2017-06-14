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

def charRemove(string, i, j=None):
    """ Remove character(s) indexed from i to j (exclude j). If j is None, the ith element is removed
    :type string: string
    :type i, j: integer (j default None)
    :rtype: string
    """
    if i > len(string) or j > len(string):
        return string
    if j is None:
        j = i + 1
    return string[:i] + string[j:]
