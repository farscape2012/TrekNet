def findMeidan(arr):
    """ Find meidan element in the list.
    :type arr: List[int/float]
    :rtype: int / float
    Note:
        Time complexity: O(nlog(n)) on average; O(n^2) in worst case
        Space complexity: O(nlog(n)) on average; O(n^2) in worst case
    """
    def findKthLargest(arr, k):
        """ Find kth largest element in the list
        :type arr: List[int/float]
        :type k: int
        :rtype: int / float
        """
        if k > len(arr):
            return None
        pivot = nums[0]
        left  = [l for l in arr if l < pivot]
        equal = [e for e in arr if e == pivot]
        right = [r for r in arr if r > pivot]
        if k <= len(right):
            return findKthLargest(right, k)
        elif (k - len(right)) <= len(equal):
            return equal[0]
        else:
            return findKthLargest(left, k - len(right) - len(equal))
    if len(arr) == 0 or nums is None:
        return None
    if len(arr) % 2 == 0:
        ks = [len(arr)/2, len(arr)/2+1]
    else:
        ks = [len(arr)/2 + 1]
    medians = []
    for k in ks:
        medians.append(findKthLargest(arr, k))
    return medians[0] if len(medians) == 1 else sum(medians)/2.0
