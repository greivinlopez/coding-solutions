# ---------------------------------------------
# 1155. Number of Dice Rolls With Target Sum 🎲
# ---------------------------------------------

# Problem: https://leetcode.com/problems/number-of-dice-rolls-with-target-sum
#
# You have n dice, and each dice has k faces numbered from 1 to k.
# 
# Given three integers n, k, and target, return the number of possible ways (out
# of the kn total ways) to roll the dice, so the sum of the face-up numbers equals
# target. Since the answer may be too large, return it modulo 10⁹ + 7.
# 
# Example 1:
# 
# Input: n = 1, k = 6, target = 3
# Output: 1
# 
# Explanation: You throw one die with 6 faces.
# There is only one way to get a sum of 3.
# 
# Example 2:
# 
# Input: n = 2, k = 6, target = 7
# Output: 6
# 
# Explanation: You throw two dice, each with 6 faces.
# There are 6 ways to get a sum of 7: 1+6, 2+5, 3+4, 4+3, 5+2, 6+1.
# 
# Example 3:
# 
# Input: n = 30, k = 30, target = 500
# Output: 222616187
# 
# Explanation: The answer must be returned modulo 109 + 7.
# 
# 
# Constraints:
#         1 <= n, k <= 30
#         1 <= target <= 1000


# Solution: https://youtu.be/hfUxjdjVQN4
# Credit: Navdeep Singh founder of NeetCode
def num_rolls_to_target_memo(n, k, target):
    # Memoization Solution
    MOD = 10**9 + 7
    cache = {}  # (n, target) -> count
    
    def count(n, target):
        if n == 0:
            return 1 if target == 0 else 0
        if (n, target) in cache:
            return cache[(n, target)]
        
        res = 0
        for val in range(1, k + 1):
            res = (res + count(n - 1, target - val)) % MOD
        cache[(n, target)] = res
        return res
    
    return count(n, target)
    # Time: O(n * t * k)
    # Space: O(n * t)
    # n = number of dice remaining
    # t = target sum remaining

def num_rolls_to_target(n, k, target):
    # Dynamic Programming Solution
    dp = [0] * (target + 1)
    dp[0] = 1
    MOD = 10**9 + 7

    for dice in range(n):
        next_dp = [0] * (target + 1)
        for val in range(1, k + 1):
            for total in range(val, target + 1):
                next_dp[total] = (next_dp[total] + dp[total - val]) % MOD
        dp = next_dp
    
    return dp[target]
    # Time: O(n * t * k)
    # Space: O(n * t)
    # n = number of dice remaining
    # t = target sum remaining


def main():
    result = num_rolls_to_target(n = 1, k = 6, target = 3)
    print(result) # True

    result = num_rolls_to_target(n = 2, k = 6, target = 7)
    print(result) # True

    result = num_rolls_to_target(n = 30, k = 30, target = 500)
    print(result) # False

if __name__ == "__main__":
    main()
