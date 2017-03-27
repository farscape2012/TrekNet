def kadaneAlg(arr, rindex=True):
    """ Kadane's algorithm to find maximum subarray given an array
    :type arr: List[int/float]
    :rtype: int 
    """
    maxv = arr[0]
    maxstart = maxend = 0
    curstart = curend = 0
    curmax = arr[0]
    for i in xrange(1, len(arr)):
        if arr[i] > curmax + arr[i]:
            curstart = i
            curend = i
            curmax = arr[i]
        else:
            curmax = curmax + arr[i]
            curend = i
        if curmax > maxv:
            maxstart = curstart
            maxend = curend
            maxv = curmax
    if rindex:
        return maxstart, maxend, maxv
    else:
        return maxv
