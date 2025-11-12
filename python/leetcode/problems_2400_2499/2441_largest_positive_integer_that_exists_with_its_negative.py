# ------------------------------------------------------------
# 2441. Largest Positive Integer That Exists With Its Negative
# ------------------------------------------------------------

# Problem: https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative
#
# Given an integer array nums that does not contain any zeros, find the largest
# positive integer k such that -k also exists in the array.
# 
# Return the positive integer k. If there is no such integer, return -1.
# 
# Example 1:
# 
# Input: nums = [-1,2,-3,3]
# Output: 3
# 
# Explanation: 3 is the only valid k we can find in the array.
# 
# Example 2:
# 
# Input: nums = [-1,10,6,7,-7,1]
# Output: 7
# 
# Explanation: Both 1 and 7 have their corresponding negative values in the array.
# 7 has a larger value.
# 
# Example 3:
# 
# Input: nums = [-10,8,6,7,-2,-3]
# Output: -1
# 
# Explanation: There is no a single valid k, we return -1.
# 
# Constraints:
#         1 <= nums.length <= 1000
#         -1000 <= nums[i] <= 1000
#         nums[i] != 0

# Credit: Jaweria Batool -> https://github.com/Jaweria-B
def find_max_k(nums):
    ans = -1

    # Initialize a set to keep track of seen numbers
    seen = set()

    for num in nums:
        abs_num = abs(num)

        # If the absolute value is greater than the current answer
        # and its negation was seen before,
        # update the answer
        if abs_num > ans and -num + 1024 in seen:
            ans = abs_num
        # Mark the current number as seen
        seen.add(num + 1024)

    return ans
    # Time: O(n)
    # Space: O(n)


def main():
    result = find_max_k([-1,2,-3,3])
    print(result) # 3

    result = find_max_k([-1,10,6,7,-7,1])
    print(result) # 7

    result = find_max_k([-10,8,6,7,-2,-3])
    print(result) # -1

if __name__ == "__main__":
    main()
