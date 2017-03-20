def findMeidan(nums):
    """ Find meidan element in the list.
    :type nums: List[int]
    :rtype: int / float
    Note:
        Time complexity: O(n) on average; O(n^2) in worst case
        Space complexity: O(n) on average; O(n^2) in worst case
    """
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
    if len(nums) == 0 or nums is None:
        return None
    if len(nums) % 2 == 0:
        ks = [len(nums)/2, len(nums)/2+1]
    else:
        ks = [len(nums)/2 + 1]
    medians = []
    for k in ks:
        medians.append(findKthLargest(nums, k))
    return medians[0] if len(medians) == 1 else sum(medians)/2.0
