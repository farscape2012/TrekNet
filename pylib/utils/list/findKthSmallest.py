def findKthSmallest(arr, k):
    """
    :type arr: List[int/float]
    :type k: int
    :rtype: int/float
        Note:
        Time complexity: O(n) on average; O(n^2) in worst case
        Space complexity: O(n) on average; O(n^2) in worst case
    """
    if k > len(arr):
        return None
    pivot = arr[0]
    left  = [l for l in arr if l < pivot]
    equal = [e for e in arr if e == pivot]
    right = [r for r in arr if r > pivot]
    if k <= len(left):
        return findKthSmallest(left, k)
    elif (k - len(left)) <= len(equal):
        return equal[0]
    else:
        return findKthSmallest(right, k - len(left) - len(equal))
