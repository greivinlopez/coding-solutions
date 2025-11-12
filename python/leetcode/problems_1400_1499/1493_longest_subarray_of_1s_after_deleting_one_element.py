# --------------------------------------------------------
# 1493. Longest Subarray of 1's After Deleting One Element
# --------------------------------------------------------

# Problem: https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element
#
# Given a binary array nums, you should delete one element from it.
# 
# Return the size of the longest non-empty subarray containing only 1's in the
# resulting array. Return 0 if there is no such subarray.
# 
# Example 1:
# 
# Input: nums = [1,1,0,1]
# Output: 3
# 
# Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers
# with value of 1's.
# 
# Example 2:
# 
# Input: nums = [0,1,1,1,0,1,1,0,1]
# Output: 5
# 
# Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest
# subarray with value of 1's is [1,1,1,1,1].
# 
# Example 3:
# 
# Input: nums = [1,1,1]
# Output: 2
# 
# Explanation: You must delete one element.
# 
# 
# Constraints:
#         1 <= nums.length <= 10⁵
#         nums[i] is either 0 or 1.


# Credit: Jaweria Batool -> https://github.com/Jaweria-B
def longest_subarray(nums):
    left = 0
    right = 0  
    k = 1
    max_len = 0
    
    while right < len(nums):      
        if nums[right] == 0:
            k -= 1
            
        while k < 0:
            if nums[left] == 0:
                k += 1    
            left += 1
        
        max_len = max( max_len, right - left)        
        right += 1
    
    return max_len
    # Time: O(n)
    # Space: O(1)


def main():
    result = longest_subarray(nums = [1,1,0,1])
    print(result) # 3

    result = longest_subarray(nums = [0,1,1,1,0,1,1,0,1])
    print(result) # 5

    result = longest_subarray(nums = [1,1,1])
    print(result) # 2

if __name__ == "__main__":
    main()
