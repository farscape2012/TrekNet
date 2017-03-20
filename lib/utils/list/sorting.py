def quicksort(arr):
    """ sort an array using quick sort algorithm
    
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
    
