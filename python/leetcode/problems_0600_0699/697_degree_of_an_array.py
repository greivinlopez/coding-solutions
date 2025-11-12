# -----------------------
# 697. Degree of an Array
# -----------------------

# Problem: https://leetcode.com/problems/degree-of-an-array
#
# Given a non-empty array of non-negative integers nums, the degree of this array
# is defined as the maximum frequency of any one of its elements.
# 
# Your task is to find the smallest possible length of a (contiguous) subarray of
# nums, that has the same degree as nums.
# 
# Example 1:
# 
# Input: nums = [1,2,2,3,1]
# Output: 2
# 
# Explanation:
# The input array has a degree of 2 because both elements 1 and 2 appear twice.
# Of the subarrays that have the same degree:
# [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
# The shortest length is 2. So return 2.
# 
# Example 2:
# 
# Input: nums = [1,2,2,3,1,4,2]
# Output: 6
# 
# Explanation:
# The degree is 3 because the element 2 is repeated 3 times.
# So [2,2,3,1,4,2] is the shortest subarray, therefore returning 6.
# 
# 
# Constraints:
#         nums.length will be between 1 and 50,000.
#         nums[i] will be an integer between 0 and 49,999.


# Credit: Jaweria Batool -> https://github.com/Jaweria-B
def find_shortest_sub_array(nums):
    dic = {}
    
    for i in nums:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    
    degree = max(dic.values())
    
    l = {}
    r = {}
    
    for i in range(len(nums)):
        if nums[i] not in l:
            l[nums[i]] = i
            
        r[nums[i]] = i
    
    ans = float("inf")
    
    for num in dic:
        if dic[num] == degree:
            ans = min(ans, r[num]-l[num]+1)
    
    return ans
    # Time: O(n)
    # Space: O(n)


def main():
    result = find_shortest_sub_array(nums = [1,2,2,3,1])
    print(result) # 2

    result = find_shortest_sub_array(nums = [1,2,2,3,1,4,2])
    print(result) # 6

if __name__ == "__main__":
    main()
