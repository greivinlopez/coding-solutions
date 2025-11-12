# ------------------------------
# 1004. Max Consecutive Ones III
# ------------------------------

# Problem: https://leetcode.com/problems/max-consecutive-ones-iii/
# 
# Given a binary array nums and an integer k, return the maximum number of 
# consecutive 1's in the array if you can flip at most k 0's.
# 
#  
# Example 1:
# 
# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
# 
# Example 2:
# 
# Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
# Output: 10
# Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
#  
# 
# Constraints:
# 
#   1 <= nums.length <= 10^5
#   nums[i] is either 0 or 1.
#   0 <= k <= nums.length


# Solution: https://youtu.be/HsGKI02yw6M
# Credit: Greg Hogg
def longest_ones(nums, k):
    max_w = 0
    num_zeros = 0
    n = len(nums)
    l = 0

    for r in range(n):
        if nums[r] == 0:
            num_zeros += 1

        while num_zeros > k:
            if nums[l] == 0:
                num_zeros -= 1
            l += 1
        w = r - l + 1
        max_w = max(max_w, w)

    return max_w
    # Time: O(n)
    # Space: O(1)


def main():
    result = longest_ones(nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2)
    print(result) # 6

    result = longest_ones(nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3)
    print(result) # 10

if __name__ == "__main__":
    main()
