def findKthLargest(arr, k):
    """ Find kth largest element in the list
    :type arr: List[int]
    :type k: int
    :rtype: int
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
    if k <= len(right):
        return findKthLargest(right, k)
    elif (k - len(right)) <= len(equal):
        return equal[0]
    else:
        return findKthLargest(left, k - len(right) - len(equal))
