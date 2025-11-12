# ----------------------
# 767. Reorganize String
# ----------------------

# Problem: https://leetcode.com/problems/reorganize-string/
# 
# Given a string s, rearrange the characters of s so that any two adjacent 
# characters are not the same.
# 
# Return any possible rearrangement of s or return "" if not possible.
# 
#  
# Example 1:
# 
# Input: s = "aab"
# Output: "aba"
# 
# Example 2:
# 
# Input: s = "aaab"
# Output: ""
#  
# 
# Constraints:
# 
#   1 <= s.length <= 500
#   s consists of lowercase English letters.

from collections import Counter
import heapq

# Solution: https://youtu.be/2g_b1aYTHeg
# Credit: Navdeep Singh founder of NeetCode
def reorganize_string(s):
    count = Counter(s)  # Hashmap, count each char
    maxHeap = [[-cnt, char] for char, cnt in count.items()]
    heapq.heapify(maxHeap)  # O(n)

    prev = None
    res = ""
    while maxHeap or prev:
        if prev and not maxHeap:
            return ""
        # most frequent, except prev
        cnt, char = heapq.heappop(maxHeap)
        res += char
        cnt += 1

        if prev:
            heapq.heappush(maxHeap, prev)
            prev = None
        if cnt != 0:
            prev = [cnt, char]
    return res


def main():
    result = reorganize_string("aab")
    print(result) # "aba"

    result = reorganize_string("aaab")
    print(result) # ""

if __name__ == "__main__":
    main()
