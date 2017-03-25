class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
 
class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()
    
    def findMaxValueInEachLevel(self, root):
    """ Find max value in Each Tree Row.
    :type root: TreeNode
    :rtype: List[int]
    """
    maxes = []
    row = [root]
    while any(row):
        maxes.append(max(node.val for node in row))
        row = [kid for node in row for kid in (node.left, node.right) if kid]
    return maxes
    def findMaxValueInEachLevelV2(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        next_stack = [root]
        maxlist = []
        while len(next_stack) > 0:
            stack = next_stack[:]
            next_stack = []
            maxv = None
            while len(stack) > 0:
                node = stack.pop()
                if maxv is None:
                    maxv = node.val
                if maxv < node.val:
                    maxv = node.val
                if node.left is not None:
                    next_stack.append(node.left)
                if node.right is not None:
                    next_stack.append(node.right)
            maxlist.append(maxv)
        return maxlist
