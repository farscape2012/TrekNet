def FindFrequentElement(arr, freq='most'):
    """ Find (most / least / K ) frequent elements and frequency. Normally it is slow ( O(n log n) for sorting ) or uses too much memory ( O(n) for a hash table )
    :type arr: List[int]
    :type freq: string (most, least or a number)
    :rtype: int

    
    Note: 
        Time complexity: O(n) in worst-case
        Space complexity: O(1)
    Limitation:
        This algorithm only works if the length of array is larger than the maximum value of the array.
    
    When freq = "least", algorithm sometimes fails if there are elements whose frequency is one.
    
    Example:
          Note: Such an algorithm only works if the length of array is larger than the maximum value of the array.
          Given an integer array, find the most frequent number and it's count in the array. Write the
          code in O(1) space. Eg 1 , 3, 4, 5, 2, 2, 3, 2 Output Most frequent number is 2. The
          frequency is 3. Return the output as string in 'number: frequency' format. e.g. 2: 3 (Please
          note the space after : and frequency. If multiple numbers have the same highest frequency
          return the smallest number.
    """
    def __findMaxRepeat(arr, maxv):
        """Find maximum repeats """
        repeat = 0
        for i in arr:
            if i / maxv > repeat:
                repeat = i / maxv
        return repeat
    def __findMinRepeat(arr, maxv):
        """Find minimum repeats """
        repeat = float('inf')
        for i in arr:
            if i / maxv < repeat:
                repeat = i / maxv
        return repeat
    def __findRepeatElement(arr, repeats):
        repeat_value = []
        for i in xrange(len(arr)):
            if arr[i] / maxv == repeats:
                repeat_value.append(i)
        return repeat_value
    maxv = max(arr) + 1
    if len(arr) < maxv:
        print 'Length of input array should be larger than maximum of the array'
        raise Exception
    # key of this algorithm
    for i in xrange(len(arr)):
        arr[ arr[i] % maxv ] += maxv
    # find the max/min number of repeats
    if freq == 'most':
        repeats = __findMaxRepeat(arr, maxv)
    elif freq == 'least':
        repeats = __findMinRepeat(arr, maxv)
        if repeats == 0:
            print('Can not find frequency 1 elements')
            raise ValueError
    else: # certain number
        try:
            repeats = int(freq)
        except ValueError:
            raise ValueError
    # find all repeating values given frequency (repeats)
    repeat_value = __findRepeatElement(arr, repeats)
    return repeats, repeat_value
