def kadaneAlg(arr):
    """ Kadane's algorithm to find maximum subarray given an array
    :type arr: List[int/float]
    :rtype: int 
    """
    maxv = arr[0]
    cur_sum = arr[0]
    for x in arr[1:]:
        cur_sum = max(x, maxv + x)
        maxv = cur_sum
    return maxv
