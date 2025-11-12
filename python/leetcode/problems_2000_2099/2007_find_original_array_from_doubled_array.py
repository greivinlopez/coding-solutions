# --------------------------------------------
# 2007. Find Original Array From Doubled Array
# --------------------------------------------

# Problem: https://leetcode.com/problems/find-original-array-from-doubled-array
#
# An integer array original is transformed into a doubled array changed by
# appending twice the value of every element in original, and then randomly
# shuffling the resulting array.
# 
# Given an array changed, return original if changed is a doubled array. If
# changed is not a doubled array, return an empty array. The elements in original
# may be returned in any order.
# 
# Example 1:
# 
# Input: changed = [1,3,4,2,6,8]
# Output: [1,3,4]
# 
# Explanation: One possible original array could be [1,3,4]:
# - Twice the value of 1 is 1 * 2 = 2.
# - Twice the value of 3 is 3 * 2 = 6.
# - Twice the value of 4 is 4 * 2 = 8.
# Other original arrays could be [4,3,1] or [3,1,4].
# 
# Example 2:
# 
# Input: changed = [6,3,0,1]
# Output: []
# 
# Explanation: changed is not a doubled array.
# 
# Example 3:
# Input: changed = [1]
# Output: []
# 
# Explanation: changed is not a doubled array.
# 
# 
# Constraints:
#         1 <= changed.length <= 10⁵
#         0 <= changed[i] <= 10⁵

import collections

# Credit: Jaweria Batool -> https://github.com/Jaweria-B
def find_original_array(changed):
    dic = collections.Counter(changed)
    ans = []
    for ele in sorted(dic):
        if dic[ele] > dic[ele*2]:
            return []
        
        if ele == 0:
            if dic[ele]%2 != 0:
                return []
            else:
                ans += ([0]*(dic[ele]//2))
        else:
            dic[ele*2] -= dic[ele]
        
    for k, v in dic.items():
        if k != 0:
            ans += [k]*v

    return ans
    # Time: O(n * log(n))
    # Space: O(n)


def main():
    result = find_original_array([1,3,4,2,6,8])
    print(result) # [1,3,4]

    result = find_original_array([6,3,0,1])
    print(result) # []

    result = find_original_array([1])
    print(result) # []

if __name__ == "__main__":
    main()
