def findKthLargest(nums, k):
    """ Find kth largest element in the list
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    if k > len(nums):
        return None
    pivot = nums[0]
    left  = [l for l in nums if l < pivot]
    equal = [e for e in nums if e == pivot]
    right = [r for r in nums if r > pivot]
    if k <= len(right):
        return findKthLargest(right, k)
    elif (k - len(right)) <= len(equal):
        return equal[0]
    else:
        return findKthLargest(left, k - len(right) - len(equal))
