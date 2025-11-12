# ----------------------------------------
# 2182. Construct String With Repeat Limit
# ----------------------------------------

# Problem: https://leetcode.com/problems/construct-string-with-repeat-limit
#
# You are given a string s and an integer repeatLimit. Construct a new string
# repeatLimitedString using the characters of s such that no letter appears more
# than repeatLimit times in a row. You do not have to use all characters from s.
# 
# Return the lexicographically largest repeatLimitedString possible.
# 
# A string a is lexicographically larger than a string b if in the first position
# where a and b differ, string a has a letter that appears later in the alphabet
# than the corresponding letter in b. If the first min(a.length, b.length)
# characters do not differ, then the longer string is the lexicographically larger
# one.
# 
# Example 1:
# 
# Input: s = "cczazcc", repeatLimit = 3
# Output: "zzcccac"
# 
# Explanation: We use all of the characters from s to construct the
# repeatLimitedString "zzcccac".
# The letter 'a' appears at most 1 time in a row.
# The letter 'c' appears at most 3 times in a row.
# The letter 'z' appears at most 2 times in a row.
# Hence, no letter appears more than repeatLimit times in a row and the string is
# a valid repeatLimitedString.
# The string is the lexicographically largest repeatLimitedString possible so we
# return "zzcccac".
# Note that the string "zzcccca" is lexicographically larger but the letter 'c'
# appears more than 3 times in a row, so it is not a valid repeatLimitedString.
# 
# Example 2:
# 
# Input: s = "aababab", repeatLimit = 2
# Output: "bbabaa"
# 
# Explanation: We use only some of the characters from s to construct the
# repeatLimitedString "bbabaa".
# The letter 'a' appears at most 2 times in a row.
# The letter 'b' appears at most 2 times in a row.
# Hence, no letter appears more than repeatLimit times in a row and the string is
# a valid repeatLimitedString.
# The string is the lexicographically largest repeatLimitedString possible so we
# return "bbabaa".
# Note that the string "bbabaaa" is lexicographically larger but the letter 'a'
# appears more than 2 times in a row, so it is not a valid repeatLimitedString.
# 
# Constraints:
#         1 <= repeatLimit <= s.length <= 10^5
#         s consists of lowercase English letters.

from collections import Counter
import heapq

# Solution: https://youtu.be/Um9_VT78nfg
# Credit: Navdeep Singh founder of NeetCode
def repeat_limited_string(s, repeat_limit):
    count = Counter(s)
    
    max_heap = [(-ord(c), cnt) for c, cnt in count.items()]
    heapq.heapify(max_heap)
    res = []

    while max_heap:
        # State 1
        char_ord, cnt = heapq.heappop(max_heap)
        char = chr(-char_ord)
        cur_cnt = min(cnt, repeat_limit)
        res.append(char * cur_cnt)

        # State 2
        if cnt - cur_cnt > 0 and max_heap:
            nxt_char_ord, nxt_cnt = heapq.heappop(max_heap)
            nxt_char = chr(-nxt_char_ord)
            res.append(nxt_char)

            if nxt_cnt > 1:
                heapq.heappush(max_heap, (nxt_char_ord, nxt_cnt - 1))
            
            heapq.heappush(max_heap, (char_ord, cnt - cur_cnt))
        
        if cnt - cur_cnt > 0 and not max_heap:
            return "".join(res)
    
    return "".join(res)
    # Time: O(n+klogk), where n is the length of the input string and k is the number of unique characters.  
    # Space: O(n+k)


def main():
    result = repeat_limited_string("cczazcc", 3)
    print(result) # "zzcccac"

    result = repeat_limited_string("aababab", 2)
    print(result) # "bbabaa"

if __name__ == "__main__":
    main()
