# --------------------------------
# 491. Non-decreasing Subsequences
# --------------------------------

# Problem: https://leetcode.com/problems/non-decreasing-subsequences
#
# Given an integer array nums, return all the different possible non-decreasing
# subsequences of the given array with at least two elements. You may return the
# answer in any order.
# 
# Example 1:
# 
# Input: nums = [4,6,7,7]
# Output: [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]
# 
# Example 2:
# 
# Input: nums = [4,4,3,2,1]
# Output: [[4,4]]
# 
# 
# Constraints:
#         1 <= nums.length <= 15
#         -100 <= nums[i] <= 100


# Solution: https://leetcode.com/problems/non-decreasing-subsequences/solutions/702479/python-very-simple-solution
def find_subsequences_alt(nums):     
    def backtrack(curr, nums):
        if( len(curr) >= 2 and curr[-1] < curr[-2] ): return
        if( len(curr) >= 2 and curr[:] not in result):
            result.add(curr[:])
        for i in range(len(nums)):
            backtrack( curr + (nums[i],), nums[i+1:] )  # using tuples for curr instead of list
    result = set()
    backtrack( (), nums)
    return result
    # Time: O(n²)
    # Space: O(n²)


# Solution: https://algo.monster/liteproblems/491
# Credit: AlgoMonster
def find_subsequences(nums):
    def dfs(index, last_value, current_path):
        # Base case: reached end of array
        if index == len(nums):
            # Add valid subsequence (length > 1) to result
            if len(current_path) > 1:
                result.append(current_path[:])  # Make a copy
            return
        
        # Choice 1: Include current element if it maintains non-decreasing order
        if nums[index] >= last_value:
            current_path.append(nums[index])
            dfs(index + 1, nums[index], current_path)
            current_path.pop()  # Backtrack
        
        # Choice 2: Skip current element (avoid duplicates at same recursion level)
        # Only skip if current element is different from last_value
        # This prevents duplicate subsequences
        if nums[index] != last_value:
            dfs(index + 1, last_value, current_path)
    
    # Initialize result list
    result = []
    
    # Start DFS with initial values
    # -1000 as initial last_value since -100 <= nums[i] <= 100
    dfs(0, -1000, [])
    
    return result
    # Time: O(n * 2ⁿ)
    # Space: O(n * 2ⁿ)


def main():
    result = find_subsequences([4,6,7,7])
    print(result) # [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]

    result = find_subsequences([4,4,3,2,1])
    print(result) # [[4,4]]

if __name__ == "__main__":
    main()
