# --------------------------------------
# 985. Sum of Even Numbers After Queries
# --------------------------------------

# Problem: https://leetcode.com/problems/sum-of-even-numbers-after-queries
#
# You are given an integer array nums and an array queries where queries[i] =
# [vali, indexi].
# 
# For each query i, first, apply nums[indexi] = nums[indexi] + vali, then print
# the sum of the even values of nums.
# 
# Return an integer array answer where answer[i] is the answer to the ith query.
# 
# Example 1:
# 
# Input: nums = [1,2,3,4], queries = [[1,0],[-3,1],[-4,0],[2,3]]
# Output: [8,6,2,4]
# 
# Explanation: At the beginning, the array is [1,2,3,4].
# After adding 1 to nums[0], the array is [2,2,3,4], and the sum of even values is
# 2 + 2 + 4 = 8.
# After adding -3 to nums[1], the array is [2,-1,3,4], and the sum of even values
# is 2 + 4 = 6.
# After adding -4 to nums[0], the array is [-2,-1,3,4], and the sum of even values
# is -2 + 4 = 2.
# After adding 2 to nums[3], the array is [-2,-1,3,6], and the sum of even values
# is -2 + 6 = 4.
# 
# Example 2:
# 
# Input: nums = [1], queries = [[4,0]]
# Output: [0]
# 
# 
# Constraints:
#         1 <= nums.length <= 10⁴
#         -10⁴ <= nums[i] <= 10⁴
#         1 <= queries.length <= 10⁴
#         -10⁴ <= valᵢ <= 10⁴
#         0 <= indexᵢ < nums.length


# Solution: https://algo.monster/liteproblems/985
# Credit: AlgoMonster
def sum_even_after_queries(nums, queries):
    # Calculate initial sum of all even numbers in the array
    even_sum = sum(num for num in nums if num % 2 == 0)
    
    # Store results for each query
    result = []
    
    # Process each query [value, index]
    for value, index in queries:
        # If the current number at index is even, remove it from even_sum
        # (since it will be modified)
        if nums[index] % 2 == 0:
            even_sum -= nums[index]
        
        # Apply the query: add value to nums[index]
        nums[index] += value
        
        # If the new number at index is even, add it to even_sum
        if nums[index] % 2 == 0:
            even_sum += nums[index]
        
        # Append current even sum to results
        result.append(even_sum)
    
    return result
    # Time: O(n + m)
    # Space: O(1)


def main():
    result = sum_even_after_queries(nums = [1,2,3,4], queries = [[1,0],[-3,1],[-4,0],[2,3]])
    print(result) # [8, 6, 2, 4]

    result = sum_even_after_queries(nums = [1], queries = [[4,0]])
    print(result) # [0]

if __name__ == "__main__":
    main()
