def answer(s1, s2):
    """
    Args:
        s1 (String): First string
        s2 (String): Second string
    Returns:
        boolean. True if the 2nd string is a rotation of the first, and False
        otherwise
    """

    # isSubstring checks if one word is substring of another


    # first checks if the length is the same
    if len(s1) != len(s2):
        rot = False

    # find the index of the first letter of s2 in s1
    start_index = s1.find(s2[0]) # O(n)
    # index: after found, proceed to check that all indices from
    if s2[:len(s1) - start_index] == s1[start_index:]: # O(n)
        # proceed to check that the remaining part of s2 is within s1
        assert len(s1[:start_index]) == len(s2[len(s1)-start_index:])
        rot = isSubstring(s1[:start_index], s2[len(s1)-start_index:])

    else:
        rot = False

    return rot

def isSubstring(s1, s2):
    return s1 in s2


def main():
    print(answer("happy",  "appyh"))

main()
