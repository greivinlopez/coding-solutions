# ------------------------
# 216. Combination Sum III
# ------------------------

# Problem: https://leetcode.com/problems/combination-sum-iii
#
# Find all valid combinations of k numbers that sum up to n such that the
# following conditions are true:
#         
#   * Only numbers 1 through 9 are used.
#   * Each number is used at most once.
# 
# Return a list of all possible valid combinations. The list must not contain the
# same combination twice, and the combinations may be returned in any order.
# 
# Example 1:
# 
# Input: k = 3, n = 7
# Output: [[1,2,4]]
# 
# Explanation:
# 1 + 2 + 4 = 7
# There are no other valid combinations.
# 
# Example 2:
# 
# Input: k = 3, n = 9
# Output: [[1,2,6],[1,3,5],[2,3,4]]
# 
# Explanation:
# 1 + 2 + 6 = 9
# 1 + 3 + 5 = 9
# 2 + 3 + 4 = 9
# There are no other valid combinations.
# 
# Example 3:
# 
# Input: k = 4, n = 1
# Output: []
# 
# Explanation: There are no valid combinations.
# Using 4 different numbers in the range [1,9], the smallest sum we can get is
# 1+2+3+4 = 10 and since 10 > 1, there are no valid combination.
# 
# 
# Constraints:
#         2 <= k <= 9
#         1 <= n <= 60


# Credit: Jaweria Batool -> https://github.com/Jaweria-B
def combination_sum_3(k, n):
    global ans
    ans = []
    nums = [1,2,3,4,5,6,7,8,9]
    def calculate(nums, k, n, path, ind):
        global ans
        if k < 0 or n < 0:
            return
        
        if n == 0 and k == 0:
            ans.append(path[:])
            return
        
        for i in range(ind, len(nums)):
            path.append(nums[i])
            calculate(nums, k-1, n-nums[i], path, i+1)
            path.pop()
            
    calculate(nums, k, n, [], 0)
    
    return ans
    # Time: O(C(9,k) × k)
    # Space: O(C(9,k) × k)
    # C(9,k): Number of possible k-combinations from 9 numbers


def main():
    result = combination_sum_3(k = 3, n = 7)
    print(result) # [[1,2,4]]

    result = combination_sum_3(k = 3, n = 9)
    print(result) # [[1,2,6],[1,3,5],[2,3,4]]

    result = combination_sum_3(k = 4, n = 1)
    print(result) # []

if __name__ == "__main__":
    main()
