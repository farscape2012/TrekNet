def maximizeValueGivenKSwap(string, k):
    """ Given a positive integer (string), find possible maximum number by doing at-most K swap operations on its digits.
    :type string: string of integer
    :rtype: int / float    

    Complexity:
        Time : O(k*log(n))
        Space : O(1)
    """
    def __str_swap(string, i, j):
        if i > len(string) or j > len(string):
            return string
        lst = list(string)
        lst[i], lst[j] = lst[j], lst[i]
        return ''.join(lst)
    def __recursive_func(string, k, start=0):
        if len(string[start:]) <= 1 or k <= 0:
            return string
        max_str = max(string[start:])
        index = string.rfind(max_str)
        if index == 0:
            return string
        #print string[start:], k, start, index
        # swap highest with left smallest value
        for i in xrange(start, index):
            if string[i] < max_str:
                string = __str_swap(string, i, index)
                k -= 1
                break
        start += 1
        return __recursive_func(string, k, start)
    return __recursive_func(string, k, start=0)
def maximizeValueGivenKSwapAdjacentDigit(string, k):
    """ Given a positive integer, find Maximum number possible by doing at-most K swaps on the adjacent digits
    :type string: string of integer
    :rtype: int / float    

    Complexity:
        Time : O(k*log(n))
        Space : O(1)
    """
    def __str_swap(string, i, j):
        if i > len(string) or j > len(string):
            return string
        lst = list(string)
        lst[i], lst[j] = lst[j], lst[i]
        return ''.join(lst)
    def __recursive_func(string, k, start=0):
        end = k+start+1
        if len(string[start:end]) <= 1 or k <= 0:
            return string
        max_str = max(string[start:end])
        # find highest index (right)
        index = string[start:end].find(max_str) + start
        #print string[start: end], k, start, index, max_str
        # swap highest with left smallest value
        for i in xrange(index, start, -1):
            if i > 0:
                string = __str_swap(string, i, i-1)
                k -= 1
        start += 1
        return __recursive_func(string, k, start)
    return __recursive_func(string, k, start=0)
