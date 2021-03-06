def FindKRepeatElement(arr, freq='most'):
    """
        Find (most / least / K ) frequent elements and frequency. Normally it is slow ( O(n log n) for sorting ) or uses too much memory ( O(n) for a hash table )
        :type arr: List[int]
        :type freq: string (most, least or a number)
        :rtype: int, List[int]
        """
    def __linearTimeAuxiliarySpace(arr, freq=most):
        """
            Requirements:
                This algorithm only works if the length of array is larger than the maximum value of the array.
            :type arr: List[int]
            :type freq: string (most, least or a number)
            :rtype: int

            Note:
                Time complexity: O(n) in worst-case
                Space complexity: O(1)
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
    def __linearTimeLinearSpace(arr, freq='most'):
        """ using dict (hash table) to save frequency
        
        :type arr: List[int]
        :type freq: string (most, least or a number)
        :rtype: int
        Note:
            Time complexity: O(n) in worst-case
            Space complexity: O(n)
        """
        def __findMaxRepeat(dict):
            """Find maximum repeats """
            return max(dict.values())
        def __findMinRepeat(dict):
            """Find minimum repeats """
            return min(dict.values())
        def __findRepeatElement(dict, repeats):
            """Get elements with the repeats"""
            return [i for i,v in dict.items() if v == repeats]
        def __createHash(arr):
            dict = {}
            for i in arr:
                try:
                    dict[i] += 1
                except KeyError:
                    dict[i] = 1
            return dict
        dict = __createHash(arr)
        # find the max/min number of repeats
        if freq == 'most':
            repeats = __findMaxRepeat(dict)
        elif freq == 'least':
            repeats = __findMinRepeat(dict)
        else: # certain number
            try:
                repeats = int(freq)
            except ValueError:
                raise ValueError
        # find all repeating values given frequency (repeats)
        repeat_value = __findRepeatElement(dict, repeats)
        return repeats, repeat_value

    if len(arr) >= max(arr) + 1 and min(arr) >= 0:
        return __linearTimeAuxiliarySpace(arr, freq=freq)
    else:
        return __linearTimeLinearSpace(arr,freq=freq)

    
    def removeRepeatedElement(arr):
    """ Remove repeats/duplicated values for a list of int.
        :type arr: List[int]
        :rtype: int, List[int]
    Note:
        Time complexity: O(n^2)
        space complexity: O(n)
    """
    def __noneLinearTime(arr):
        """ This algorithm can be optimized by sort the array first (using in-place merge-sort algorithm ( complexity: O(nlog(n)) )) and comparing adjacent elements: if they are the same then they are duplicates
        """
        i = 0
        while len(arr) > 0 and i < len(arr):
            for j in xrange(len(arr)-1, i-1, -1):
                if arr[i] == arr[j] and i < j:
                    del arr[j]
            i += 1
        return arr
    return __noneLinearTime(arr)


def findRepeatedElement(arr):
    """Find repeated elements. No need to return frequency. Two algorithms are implemented. Time complexity is O(n) and O(n^2).
    Algorithm 1 works for an array which contains element from 0 to n-1 where n is smaller than the length of array.
    Algorithm 2 works for any array but slower than the other.
    """
    def __linearTimeAuxiliarySpace(arr):
        """ remove duplicates/repeats from an array which contains element from 0 to n-1 where n is smaller than the length of array
            Find duplicates in O(n) time and O(1) extra space"""
        for i in xrange(len(arr)-1,0,-1):
            if arr[abs(arr[i])] > 0:
                arr[abs(arr[i])]  = - arr[abs(arr[i])]
        rtn = set()
        for i in xrange(len(arr)-1, 0, -1):
            if arr[abs(arr[i])] < 0:
                rtn.add(abs(arr[i]))
        return list(rtn)
    def __noneLinearTime(arr):
        """ This algorithm can be optimized by sort the array first (using in-place merge-sort algorithm ( complexity: O(nlog(n)) )) and comparing adjacent elements: if they are the same then they are duplicates
        """
        i = 0
        rtn = set()
        while len(arr) > 0 and i < len(arr):
            for j in xrange(len(arr)-1, i-1, -1):
                if arr[i] == arr[j] and i < j:
                    rtn.add(arr[i])
                    break
            i += 1
        return list(rtn)
    if min(arr) >= 0 and len(arr) >= max(arr) + 1:
        return __linearTimeAuxiliarySpace(arr)
    else:
        return __noneLinearTime(arr)
