# -------------------------------------
# 2053. Kth Distinct String in an Array
# -------------------------------------

# Problem: https://leetcode.com/problems/kth-distinct-string-in-an-array
#
# A distinct string is a string that is present only once in an array.
# 
# Given an array of strings arr, and an integer k, return the kth distinct string
# present in arr. If there are fewer than k distinct strings, return an empty
# string "".
# 
# Note that the strings are considered in the order in which they appear in the
# array.
# 
# Example 1:
# 
# Input: arr = ["d","b","c","b","c","a"], k = 2
# Output: "a"
# 
# Explanation:
# The only distinct strings in arr are "d" and "a".
# "d" appears 1st, so it is the 1st distinct string.
# "a" appears 2nd, so it is the 2nd distinct string.
# Since k == 2, "a" is returned.
# 
# Example 2:
# 
# Input: arr = ["aaa","aa","a"], k = 1
# Output: "aaa"
# 
# Explanation:
# All strings in arr are distinct, so the 1st string "aaa" is returned.
# 
# Example 3:
# 
# Input: arr = ["a","b","a"], k = 3
# Output: ""
# 
# Explanation:
# The only distinct string is "b". Since there are fewer than 3 distinct strings,
# we return an empty string "".
# 
# 
# Constraints:
#         1 <= k <= arr.length <= 1000
#         1 <= arr[i].length <= 5
#         arr[i] consists of lowercase English letters.


# Solution: https://youtu.be/1KOnvGPv9Mo
# Credit: Navdeep Singh founder of NeetCode
def kth_distinct_alt(arr, k):
    for i in range(len(arr)):
        distinct_flag = True
        for j in range(len(arr)):
            if i == j:
                continue
            if arr[i] == arr[j]:
                distinct_flag = False
                break
        
        if distinct_flag:
            k -= 1
        if k == 0:
            return arr[i]
            
    return ""
    # Time: O(n²)
    # Space: O(1)

def kth_distinct(arr, k):
    # Optimized solution
    count = {}
    
    for s in arr:
        if s not in count:
            count[s] = 0
        count[s] += 1
        
    for s in arr:
        if count[s] == 1:
            k -= 1
            if k == 0:
                return s
    
    return ""
    # Time: O(n)
    # Space: O(1)


def main():
    result = kth_distinct(arr = ["d","b","c","b","c","a"], k = 2)
    print(result) # "a"

    result = kth_distinct(arr = ["aaa","aa","a"], k = 1)
    print(result) # "aaa"

    result = kth_distinct(arr = ["a","b","a"], k = 3)
    print(result) # ""

if __name__ == "__main__":
    main()
