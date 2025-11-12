# -------------------------------------------------
# 1403. Minimum Subsequence in Non-Increasing Order
# -------------------------------------------------

# Problem: https://leetcode.com/problems/minimum-subsequence-in-non-increasing-order
#
# Given the array nums, obtain a subsequence of the array whose sum of elements is
# strictly greater than the sum of the non included elements in such subsequence. 
# 
# If there are multiple solutions, return the subsequence with minimum size and if
# there still exist multiple solutions, return the subsequence with the maximum
# total sum of all its elements. A subsequence of an array can be obtained by
# erasing some (possibly zero) elements from the array. 
#
# Note that the solution with the given constraints is guaranteed to be unique.
# Also return the answer sorted in non-increasing order.
# 
# Example 1:
# 
# Input: nums = [4,3,10,9,8]
# Output: [10,9]
# 
# Explanation: The subsequences [10,9] and [10,8] are minimal such that the sum of
# their elements is strictly greater than the sum of elements not included.
# However, the subsequence [10,9] has the maximum total sum of its elements. 
# 
# Example 2:
# 
# Input: nums = [4,4,7,6,7]
# Output: [7,7,6]
# 
# Explanation: The subsequence [7,7] has the sum of its elements equal to 14 which
# is not strictly greater than the sum of elements not included (14 = 4 + 4 + 6).
# Therefore, the subsequence [7,6,7] is the minimal satisfying the conditions.
# Note the subsequence has to be returned in non-increasing order.
# 
# 
# Constraints:
#         1 <= nums.length <= 500
#         1 <= nums[i] <= 100


# Solution: https://algo.monster/liteproblems/1403
# Credit: AlgoMonster
def min_subsequence(nums):
    # Initialize result list to store the subsequence
    result = []
    
    # Calculate total sum of all elements
    total_sum = sum(nums)
    
    # Initialize sum of selected elements
    selected_sum = 0
    
    # Sort array in descending order to greedily pick largest elements first
    sorted_nums = sorted(nums, reverse=True)
    
    # Iterate through sorted array and keep adding elements to subsequence
    for num in sorted_nums:
        # Add current element to selected sum
        selected_sum += num
        
        # Add current element to result subsequence
        result.append(num)
        
        # Check if selected sum is greater than remaining sum
        # remaining_sum = total_sum - selected_sum
        if selected_sum > total_sum - selected_sum:
            break
            
    return result
    # Time: O(n * log n)
    # Space: O(log n)


def main():
    result = min_subsequence(nums = [4,3,10,9,8])
    print(result) # [10, 9]

    result = min_subsequence(nums = [4,4,7,6,7])
    print(result) # [7, 7, 6]

if __name__ == "__main__":
    main()
