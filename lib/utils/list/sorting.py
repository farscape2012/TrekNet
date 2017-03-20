def quickSort(arr):
    """ sort an array using quick sort algorithm
    :type arr: List
    :rtype: int/float    
    Note:
        Time complexity: best case O(nlog(n)) or O(n); O(nlog(n)) on average; O(N^2) in worst case
        Space complexity: O(n) 
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    left = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return qsort(left) + equal + qsort(right)
    
def mergeSort(arr):
    """ sort an array using merge sort algorithm
    :type arr: List
    :rtype: int/float    
    Note:
        Time complexity: O(nlog(n)) or O(n) in best-case; O(nlog(n)) on average; O(nlog(n)) in worst case
        Space complexity: O(n) 
    """
    if len(arr)>1:
        mid = len(arr)//2
        lefthalf = arr[:mid]
        righthalf = arr[mid:]
        mergeSort(lefthalf)
        mergeSort(righthalf)
        i=0
        j=0
        k=0
        lenleft = len(lefthalf)
        lenright = len(righthalf)
        while i < lenleft and j < lenright:
            if lefthalf[i] < righthalf[j]:
                arr[k]=lefthalf[i]
                i=i+1
            else:
                arr[k]=righthalf[j]
                j=j+1
            k=k+1
        while i < len(lefthalf):
            arr[k]=lefthalf[i]
            i=i+1
            k=k+1
        while j < len(righthalf):
            arr[k]=righthalf[j]
            j=j+1
            k=k+1
    return arr

def countSort(arr):
    """ sort an array using count sort algorithm
    This algorithm is useful when the length of list is much larger than the range of elements,i.e., it is useful the range is limited and there ar many repeats.
    Use extra memory (0 - max(array)) to save index.
    Faster than quicksort
    :type arr: List[int/float]
    :rtype: int/float    
    Note:
        Time complexity: O(n) in best-case; O(n) on average; O(n) in worst case
        Space complexity: O(n) 
    """
    dict = {}
    for i in arr:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    rtn = []
    for i in xrange(min(arr), max(arr)+1):
        try:
            rtn.extend([i] * dict[i])
        except:
            pass
    return rtn

def insertionSort(arr):
    """ sort an array using insertion sort algorithm
    :type arr: List[int/float]
    :rtype: int/float    
    Note:
        Time complexity: O(n) in best-case; O(n^2) on average; O(n^2) in worst case
        Space complexity: O(n) 
    """
    total = 0
    for i in xrange(1, len(arr)):
        j = i
        count = 0
        while j > 0 and arr[j-1] > arr[j]:
            tmp =  arr[j]
            arr[j] = arr[j-1]
            arr[j-1] = tmp
            j -= 1
            count += 1
        total += count
    return arr
