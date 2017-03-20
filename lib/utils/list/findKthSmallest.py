def findKthSmallest(nums, k):
    """
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
    if k <= len(left):
        return findKthSmallest(left, k)
    elif (k - len(left)) <= len(equal):
        return equal[0]
    else:
        return findKthSmallest(right, k - len(left) - len(equal))
