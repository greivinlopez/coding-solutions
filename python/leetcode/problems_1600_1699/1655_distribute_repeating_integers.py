# -----------------------------------
# 1655. Distribute Repeating Integers
# -----------------------------------

# Problem: https://leetcode.com/problems/distribute-repeating-integers
#
# You are given an array of n integers, nums, where there are at most 50 unique
# values in the array. You are also given an array of m customer order quantities,
# quantity, where quantity[i] is the amount of integers the iᵗʰ customer ordered.
# Determine if it is possible to distribute nums such that:
#         
#   * The iᵗʰ customer gets exactly quantity[i] integers,
#   * The integers the iᵗʰ customer gets are all equal, and
#   * Every customer is satisfied.
# 
# Return true if it is possible to distribute nums according to the above
# conditions.
# 
# Example 1:
# 
# Input: nums = [1,2,3,4], quantity = [2]
# Output: false
# 
# Explanation: The 0th customer cannot be given two different integers.
# 
# Example 2:
# 
# Input: nums = [1,2,3,3], quantity = [2]
# Output: true
# 
# Explanation: The 0th customer is given [3,3]. The integers [1,2] are not used.
# 
# Example 3:
# 
# Input: nums = [1,1,2,2], quantity = [2,2]
# Output: true
# 
# Explanation: The 0th customer is given [1,1], and the 1st customer is given
# [2,2].
# 
# 
# Constraints:
#         n == nums.length
#         1 <= n <= 10⁵
#         1 <= nums[i] <= 1000
#         m == quantity.length
#         1 <= m <= 10
#         1 <= quantity[i] <= 10⁵
#         There are at most 50 unique values in nums.


# Solution: https://algo.monster/liteproblems/1655
# Credit: AlgoMonster
def can_distribute(nums, quantity):
    from collections import Counter

    num_customers = len(quantity)
    
    # Precompute sum of quantities for each subset of customers
    # subset_sum[mask] = total quantity needed for customers in mask
    subset_sum = [0] * (1 << num_customers)
    for mask in range(1, 1 << num_customers):
        # Find the first set bit and calculate sum incrementally
        for customer_idx in range(num_customers):
            if mask >> customer_idx & 1:
                # Remove this customer from mask and add their quantity
                subset_sum[mask] = subset_sum[mask ^ (1 << customer_idx)] + quantity[customer_idx]
                break
    
    # Count frequency of each number in nums
    frequency_map = Counter(nums)
    unique_values = list(frequency_map.values())
    num_unique = len(unique_values)
    
    # dp[i][mask] = True if we can satisfy customers in mask using first i+1 unique numbers
    dp = [[False] * (1 << num_customers) for _ in range(num_unique)]
    
    # Base case: empty set of customers can always be satisfied
    for i in range(num_unique):
        dp[i][0] = True
    
    # Fill the DP table
    for idx, count in enumerate(unique_values):
        for customer_mask in range(1, 1 << num_customers):
            # Case 1: If we could satisfy this mask without current number
            if idx > 0 and dp[idx - 1][customer_mask]:
                dp[idx][customer_mask] = True
                continue
            
            # Case 2: Try to use current number for some subset of customers
            subset = customer_mask
            while subset:
                # Check if we can satisfy 'subset' with current number
                # and remaining customers with previous numbers
                can_use_previous = (customer_mask == subset if idx == 0 
                                    else dp[idx - 1][customer_mask ^ subset])
                can_satisfy_subset = subset_sum[subset] <= count
                
                if can_use_previous and can_satisfy_subset:
                    dp[idx][customer_mask] = True
                    break
                
                # Move to next subset of customer_mask
                subset = (subset - 1) & customer_mask
    
    # Return whether we can satisfy all customers using all unique numbers
    return dp[-1][-1]
    # Time: O(n * 3ᵐ)
    # Space: O(n * 2ᵐ)


def main():
    result = can_distribute(nums = [1,2,3,4], quantity = [2])
    print(result) # False

    result = can_distribute(nums = [1,2,3,3], quantity = [2])
    print(result) # True

    result = can_distribute(nums = [1,1,2,2], quantity = [2,2])
    print(result) # True

if __name__ == "__main__":
    main()
