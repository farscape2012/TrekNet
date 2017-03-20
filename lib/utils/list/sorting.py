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
