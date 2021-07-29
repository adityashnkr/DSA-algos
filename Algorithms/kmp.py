"""
KMP(Knuth–Morris–Pratt) algorithm is pattern matching algorithm. This algorithm saves time as we end up going thorugh thr text(haystack) only once
The time complexity is O(m+n) where m is the length of the text and n is the length of pattern.
Space complexity is O(m)

"""

# this is the initial step where we find some prefix that occurs again in the pattern to reduce the # of comparisions
# Eg: lps array for "abcdabeabf" -> [0, 0, 0, 0, 1, 2, 0, 1, 2, 0] as "ab" match at 2 locations
# Similarly for "abcdeabfabc" ->  [0, 0, 0, 0, 0, 1, 2, 0, 1, 2, 3] where the last "abc" is the longest match


def create_lps(pattern):
    n = len(pattern)  # length of pattern
    lps = [0] * n  # creating an array filled with 0's for lps
    index = 1  # index starting from 1 as not to check character with itself
    common = 0  # index for maintaining # of common characters
    while index < n:
        # if we find a matches then add an one to the common and append it to the lps array
        if pattern[index] == pattern[common]:
            lps[index] = common + 1
            index += 1
            common += 1
        elif common != 0:
            # a mis-match has occured! so we go back to the last matching character or to the start
            common = lps[common - 1]
        else:
            # no match so just move forward
            index += 1
    return lps  # return the lps array

# this is the main algorithm for finding the pattern


def KMP(text, pattern):
    if pattern == "":
        # for edge case
        return 0
    index = 0  # index for text
    common = 0  # index to check if pattern is ma with a substring
    m = len(text)  # length of text(haystack)
    n = len(pattern)  # length of pattern(needle)
    lps = create_lps(pattern)  # get the lps of pattern
    while index < m:
        if text[index] == pattern[common]:
            # it's a Match! we check if rest of the characters are matches as well
            common += 1
            index += 1
        elif common != 0:
            # a mis-match has occured! so we go back to the last matching character or to the start
            common = lps[common-1]
        else:
            # no match so just move forward
            index += 1
        if common == n:
            # we have reached the end of the pattern that means we have found a complete match in the text(haystack)
            # will give us the starting index of the pattern(needle) in text(haystack)
            return index - n
    return -1  # if pattern(needle) is not present


print(KMP("adcadcaddcadde", "adcadde"))
print(create_lps("abcdabeabf"))
