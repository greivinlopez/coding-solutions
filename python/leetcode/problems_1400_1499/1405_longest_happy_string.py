# --------------------------
# 1405. Longest Happy String
# --------------------------

# Problem: https://leetcode.com/problems/longest-happy-string
#
# A string s is called happy if it satisfies the following conditions:
#         
#   * s only contains the letters 'a', 'b', and 'c'.
#   * s does not contain any of "aaa", "bbb", or "ccc" as a substring.
#   * s contains at most a occurrences of the letter 'a'.
#   * s contains at most b occurrences of the letter 'b'.
#   * s contains at most c occurrences of the letter 'c'.
# 
# Given three integers a, b, and c, return the longest possible happy string. If
# there are multiple longest happy strings, return any of them. If there is no
# such string, return the empty string "".
# 
# A substring is a contiguous sequence of characters within a string.
# 
# Example 1:
# 
# Input: a = 1, b = 1, c = 7
# Output: "ccaccbcc"
# 
# Explanation: "ccbccacc" would also be a correct answer.
# 
# Example 2:
# 
# Input: a = 7, b = 1, c = 0
# Output: "aabaa"
# 
# Explanation: It is the only correct answer in this case.
# 
# 
# Constraints:
#         0 <= a, b, c <= 100
#         a + b + c > 0

import heapq

# Solution: https://youtu.be/8u-H6O_XQKE
# Credit: Navdeep Singh founder of NeetCode
def longest_diverse_string(a, b, c):
    res = ""
    max_heap = []
    
    for count, char in [(-a, "a"), (-b, "b"), (-c, "c")]:
        if count != 0:
            heapq.heappush(max_heap, (count, char))

    while max_heap:
        count, char = heapq.heappop(max_heap)
        
        if len(res) > 1 and res[-1] == res[-2] == char:
            if not max_heap:
                break
            count2, char2 = heapq.heappop(max_heap)
            res += char2
            count2 += 1
            if count2:
                heapq.heappush(max_heap, (count2, char2))
            
        else:
            res += char
            count += 1
        
        if count:
            heapq.heappush(max_heap, (count, char))
            
    return res
    # Time: O((a + b + c) log(k))
    # Space: O(1)


def main():
    result = longest_diverse_string(a = 1, b = 1, c = 7)
    print(result) # "ccaccbcc"

    result = longest_diverse_string(a = 7, b = 1, c = 0)
    print(result) # "aabaa"

if __name__ == "__main__":
    main()
