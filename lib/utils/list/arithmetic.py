def plusElement(arr1, arr2):
     """ Add ith element in arr1 and arr2
    :type arr1: List[int/float]
    :type arr2: List[int/float]
    :rtype: array 
    """
    if len(arr1) != len(arr2):
        return None
    if not (any(arr1) and any(arr2)):
        return None
    return [arr1[i] + arr2[i] for i in xrange(len(arr1))]

def minusElement(arr1, arr2):
    """ subtract ith element in arr2 from arr1
    :type arr1: List[int/float]
    :type arr2: List[int/float]
    :rtype: array 
    """
    if len(arr1) != len(arr2):
        return None
    if not (any(arr1) and any(arr2)):
        return None
    return [arr1[i] - arr2[i] for i in xrange(len(arr1))]
def multiplyElement(arr1, arr2):
    """ Multiply ith elements in arr1 and arr2
    :type arr1: List[int/float]
    :type arr2: List[int/float]
    :rtype: array
    """
    if len(arr1) != len(arr2):
        return None
    if not (any(arr1) and any(arr2)):
        return None
    return [arr1[i] * arr2[i] for i in xrange(len(arr1))]  
def multiplyFactor(arr, factor):
    """ Multiply ith elements in arr1 and arr2
    :type arr1: List[int/float]
    :type factor: Number
    :rtype: array
    """
    if not any(arr):
        return None
    return [arr[i] * factor for i in xrange(len(arr))]   
