def characterSwap(string, i, j):
    if i > len(string) or j > len(string):
        return string
    lst = list(string)
    lst[i], lst[j] = lst[j], lst[i]
    return ''.join(lst)
