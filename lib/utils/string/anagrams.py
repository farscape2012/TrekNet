def isAnagram(s1, s2):
    """ Write a program to find the first non-repeated (unique) character in a given string
    This implementation works under the assumption that all characters in both strings are in lowercase and they consist only of the characters a -z.

    Assuming the shorter string is of length k and the longer of length n, there are atmost (n - k + 1) anagram checks.
    Since the anagram check runs in O(k), I would say the overall algo complexity is O(n).
    However, my implementation is limited by the assumptions that all characters are in lowercase and only in the range a-z. 
    Yours is a more general implementation.
    """
    s1 = s1.lower()
    s2 = s2.lower()
    c1 = [0] * 26
    c2 = [0] * 26
    # increase character counts for each string
    for i in s1:
        c1[ord(i) - 97] += 1
    for i in s2:
        c2[ord(i) - 97] += 1
    # if the character counts are same, they are anagrams
    for i in range(26):
        if c1[i] != c2[i]:
            return False
    return True

def isSubAnagram(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    l = len(s1)
    # s2[start:end] represents the substring in s2
    start = 0
    end = l
    while(end <= len(s2)):
        sub = s2[start:end]
        if isAnagram(s1, sub):
            return True
        elif sub[-1] not in s1:
            start += l
            end += l
        else:
            start += 1
            end += 1
    return False
