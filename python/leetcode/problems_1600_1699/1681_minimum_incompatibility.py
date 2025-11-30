# -----------------------------
# 1681. Minimum Incompatibility
# -----------------------------

# Problem: https://leetcode.com/problems/minimum-incompatibility
#
# You are given an integer array nums​​​ and an integer k. You are asked to
# distribute this array into k subsets of equal size such that there are no two
# equal elements in the same subset.
# 
# A subset's incompatibility is the difference between the maximum and minimum
# elements in that array.
# 
# Return the minimum possible sum of incompatibilities of the k subsets after
# distributing the array optimally, or return -1 if it is not possible.
# 
# A subset is a group integers that appear in the array with no particular order.
# 
# Example 1:
# 
# Input: nums = [1,2,1,4], k = 2
# Output: 4
# 
# Explanation: The optimal distribution of subsets is [1,2] and [1,4].
# The incompatibility is (2-1) + (4-1) = 4.
# Note that [1,1] and [2,4] would result in a smaller sum, but the first subset
# contains 2 equal elements.
# 
# Example 2:
# 
# Input: nums = [6,3,8,1,3,1,2,2], k = 4
# Output: 6
# 
# Explanation: The optimal distribution of subsets is [1,2], [2,3], [6,8], and
# [1,3].
# The incompatibility is (2-1) + (3-2) + (8-6) + (3-1) = 6.
# 
# Example 3:
# 
# Input: nums = [5,3,3,6,3,3], k = 3
# Output: -1
# 
# Explanation: It is impossible to distribute nums into 3 subsets where no two
# elements are equal in the same subset.
# 
# 
# Constraints:
#         1 <= k <= nums.length <= 16
#         nums.length is divisible by k
#         1 <= nums[i] <= nums.length


# Solution: https://algo.monster/liteproblems/1681
# Credit: AlgoMonster
def minimum_incompatibility(nums, k):
    n = len(nums)
    subset_size = n // k  # Size of each subset
    
    # incompatibility[mask] stores the incompatibility of the subset represented by mask
    # -1 means invalid subset (has duplicates or wrong size)
    incompatibility = [-1] * (1 << n)
    
    # Precompute incompatibility for all valid subsets of size subset_size
    for mask in range(1, 1 << n):
        if bin(mask).count('1') != subset_size:
            continue
        
        subset_elements = set()
        min_val, max_val = 20, 0  # Initialize with extreme values (nums[i] <= 16)
        
        # Check if this subset is valid (no duplicates) and find min/max
        for idx, num in enumerate(nums):
            if mask >> idx & 1:  # If idx-th bit is set in mask
                if num in subset_elements:
                    # Duplicate found, invalid subset
                    break
                subset_elements.add(num)
                min_val = min(min_val, num)
                max_val = max(max_val, num)
        
        # If subset has no duplicates, store its incompatibility
        if len(subset_elements) == subset_size:
            incompatibility[mask] = max_val - min_val
    
    # dp[mask] = minimum sum of incompatibilities for elements selected by mask
    dp = [float('inf')] * (1 << n)
    dp[0] = 0  # Base case: empty set has 0 incompatibility
    
    # Try all possible states
    for used_mask in range(1 << n):
        if dp[used_mask] == float('inf'):
            continue
        
        # Find all unused elements and their first occurrence positions
        unused_elements = set()
        available_mask = 0
        for idx, num in enumerate(nums):
            if (used_mask >> idx & 1) == 0 and num not in unused_elements:
                unused_elements.add(num)
                available_mask |= 1 << idx
        
        # Need at least subset_size unused distinct elements to form next subset
        if len(unused_elements) < subset_size:
            continue
        
        # Try all possible subsets from available positions
        subset_mask = available_mask
        while subset_mask:
            if incompatibility[subset_mask] != -1:
                # Update dp for state including this new subset
                dp[used_mask | subset_mask] = min(
                    dp[used_mask | subset_mask], 
                    dp[used_mask] + incompatibility[subset_mask]
                )
            # Generate next subset of available_mask
            subset_mask = (subset_mask - 1) & available_mask
    
    # Return result for all elements used, or -1 if impossible
    return dp[-1] if dp[-1] != float('inf') else -1
    # Time: O(3ⁿ)
    # Space: O(2ⁿ)


def main():
    result = minimum_incompatibility(nums = [1,2,1,4], k = 2)
    print(result) # 4

    result = minimum_incompatibility(nums = [6,3,8,1,3,1,2,2], k = 4)
    print(result) # 6

    result = minimum_incompatibility(nums = [5,3,3,6,3,3], k = 3)
    print(result) # -1

if __name__ == "__main__":
    main()
