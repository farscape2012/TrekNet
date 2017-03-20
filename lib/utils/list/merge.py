def mergeSortedList(lst1, lst2, algorithm='linear'):
    """ Merge two unsorted lists into a single sorted list.
    :type lst1,lst2: List[int/float]
    :algorithm:
            'linear': use extra memory
            others : No extra memory used
    :rtype: List[int/float]
    """
    def __withoutExtraSpace(lst1, lst2):
        """ No extra space are allowed.
        This algorithm assumes taht the lists are descendant order.
        Note:
            Time complexity: O(mn)
            Space complexity: O(1)
        """
        for i in xrange(len(lst2)-1, -1, -1):
            last = lst1[-1]
            for j in xrange(len(lst1)-2, -1, -1):
                if lst1[j] > lst2[i]:
                    lst1[j+1] = lst1[j]
                else:
                    if last > lst2[i]:
                        lst1[j+1] = lst2[i]
                        lst2[i] = last
                    break
                if j == 0 :
                    lst1[0] = lst2[i]
                    lst2[i] = last
        return lst1 + lst2
    def __withExtraSpace(lst1, lst2):
        """ Merge two unsorted array into a single sorted array and extra space are allowed.
        Note:
            Time complexity: O(m+n)
            Space complexity: O(m+n)
        """
        new_list = [0] * (len(lst1) + len(lst2))
        i=0
        j = 0
        k=0
        while i < len(lst1) and j < len(lst2):
            if lst1[i] <= lst2[j]:
                new_list[k] = lst1[i]
                i += 1
            else:
                new_list[k] = lst2[j]
                j += 1
            k += 1
        while i < len(lst1):
            new_list[k] = lst1[i]
            i += 1
            k += 1
        while j < len(lst2):
            new_list[k] = lst2[j]
            j += 1
            k += 1
        return new_list
    if algorithm == 'linear':
        return __withExtraSpace(lst1, lst2)
    else:
        return __withoutExtraSpace(lst1, lst2)
