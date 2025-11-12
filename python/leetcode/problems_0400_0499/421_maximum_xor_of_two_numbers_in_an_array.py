# -------------------------------------------
# 421. Maximum XOR of Two Numbers in an Array
# -------------------------------------------

# Problem: https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array
#
# Given an integer array nums, return the maximum result of nums[i] XOR nums[j],
# where 0 <= i <= j < n.
# 
# Example 1:
# 
# Input: nums = [3,10,5,25,2,8]
# Output: 28
# 
# Explanation: The maximum result is 5 XOR 25 = 28.
# 
# Example 2:
# 
# Input: nums = [14,70,53,83,49,91,36,80,92,51,66,70]
# Output: 127
# 
# 
# Constraints:
#         1 <= nums.length <= 2 * 10⁵
#         0 <= nums[i] <= 2³¹ - 1


# My Solution based on:
# https://leetcodethehardway.com/solutions/0400-0499/maximum-xor-of-two-numbers-in-an-array
def find_maximum_xor(nums):
    ans = 0
    mask = 0
    
    # Process from most significant bit to least significant bit
    for i in range(31, -1, -1):
        # Build mask to extract prefixes up to current bit position
        mask |= (1 << i)
        
        # Store all prefixes (masked values) in a set
        s = set()
        for x in nums:
            s.add(mask & x)
        
        # Try to set current bit to 1 in the answer
        best = ans | (1 << i)
        
        # Check if we can achieve 'best' by XORing two prefixes
        for pref in s:
            # If pref ^ best exists in s, then pref ^ (pref ^ best) = best
            if (pref ^ best) in s:
                ans = best
                break
    return ans


def main():
    result = find_maximum_xor(nums = [3,10,5,25,2,8])
    print(result) # 28

    result = find_maximum_xor(nums = [14,70,53,83,49,91,36,80,92,51,66,70])
    print(result) # 127

if __name__ == "__main__":
    main()
