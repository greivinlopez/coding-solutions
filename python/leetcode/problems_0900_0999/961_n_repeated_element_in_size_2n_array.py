# ----------------------------------------
# 961. N-Repeated Element in Size 2N Array
# ----------------------------------------

# Problem: https://leetcode.com/problems/n-repeated-element-in-size-2n-array
#
# You are given an integer array nums with the following properties:
#         
#   * nums.length == 2 * n.
#   * nums contains n + 1 unique elements.
#   * Exactly one element of nums is repeated n times.
# 
# Return the element that is repeated n times.
# 
# Example 1:
# 
# Input: nums = [1,2,3,3]
# Output: 3
# 
# Example 2:
# 
# Input: nums = [2,1,2,5,3,2]
# Output: 2
# 
# Example 3:
# 
# Input: nums = [5,1,5,2,5,3,5,4]
# Output: 5
# 
# 
# Constraints:
#         2 <= n <= 5000
#         nums.length == 2 * n
#         0 <= nums[i] <= 10⁴
#         nums contains n + 1 unique elements and one of them is repeated exactly n times.


# Solution: https://algo.monster/liteproblems/961
# Credit: AlgoMonster
def repeated_n_times(nums):
    # Set to track elements we've already seen
    seen_elements = set()
    
    # Iterate through each element in the array
    for num in nums:
        # If we've seen this element before, it must be the one repeated N times
        if num in seen_elements:
            return num
        
        # Add the current element to our set of seen elements
        seen_elements.add(num)
    # Time: O(n)
    # Space: O(n)


def main():
    result = repeated_n_times(nums = [1,2,3,3])
    print(result) # 3

    result = repeated_n_times(nums = [2,1,2,5,3,2])
    print(result) # 2

    result = repeated_n_times(nums = [5,1,5,2,5,3,5,4])
    print(result) # 5

if __name__ == "__main__":
    main()
