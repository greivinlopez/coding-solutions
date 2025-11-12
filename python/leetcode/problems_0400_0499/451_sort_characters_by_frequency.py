# ---------------------------------
# 451. Sort Characters By Frequency
# ---------------------------------

# Problem: https://leetcode.com/problems/sort-characters-by-frequency
#
# Given a string s, sort it in decreasing order based on the frequency of the
# characters. The frequency of a character is the number of times it appears in
# the string.
# 
# Return the sorted string. If there are multiple answers, return any of them.
# 
# Example 1:
# 
# Input: s = "tree"
# Output: "eert"
# 
# Explanation: 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid
# answer.
# 
# Example 2:
# 
# Input: s = "cccaaa"
# Output: "aaaccc"
# 
# Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc"
# are valid answers.
# Note that "cacaca" is incorrect, as the same characters must be together.
# 
# Example 3:
# 
# Input: s = "Aabb"
# Output: "bbAa"
# 
# Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
# Note that 'A' and 'a' are treated as two different characters.
# 
# 
# Constraints:
#         1 <= s.length <= 5 * 10⁵
#         s consists of uppercase and lowercase English letters and digits.

from collections import Counter, defaultdict

# Solution: https://youtu.be/OXdXc9HTrIg
# Credit: Navdeep Singh founder of NeetCode
def frequency_sort(s):
    count = Counter(s)
    buckets = defaultdict(list)
    for char, cnt in count.items():
        buckets[cnt].append(char)
    res = []
    for i in range(len(s), 0, -1):
        for c in buckets[i]:
            res.append(c * i)
    return "".join(res)
    # Time: O(n) 
    # Space: O(n)

# Credit: Jeel Gajera -> https://github.com/JeelGajera
def frequency_sort_alt(s):
    freq = Counter(s)
    arr = sorted(freq.keys(), key=freq.get, reverse=True)
    res = ""
    for i in arr:
        res += i*freq[i]

    return res
    # Time: O(n²) 
    # Space: O(n)


def main():
    result = frequency_sort(s = "tree")
    print(result) # "eert"

    result = frequency_sort(s = "cccaaa")
    print(result) # "aaaccc"

    result = frequency_sort(s = "Aabb")
    print(result) # "bbAa"

if __name__ == "__main__":
    main()
