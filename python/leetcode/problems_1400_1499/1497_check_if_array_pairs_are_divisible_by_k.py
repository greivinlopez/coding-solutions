# ---------------------------------------------
# 1497. Check If Array Pairs Are Divisible by k
# ---------------------------------------------

# Problem: https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k
#
# Given an array of integers arr of even length n and an integer k.
# 
# We want to divide the array into exactly n / 2 pairs such that the sum of each
# pair is divisible by k.
# 
# Return true If you can find a way to do that or false otherwise.
# 
# Example 1:
# 
# Input: arr = [1,2,3,4,5,10,6,7,8,9], k = 5
# Output: true
# 
# Explanation: Pairs are (1,9),(2,8),(3,7),(4,6) and (5,10).
# 
# Example 2:
# 
# Input: arr = [1,2,3,4,5,6], k = 7
# Output: true
# 
# Explanation: Pairs are (1,6),(2,5) and(3,4).
# 
# Example 3:
# 
# Input: arr = [1,2,3,4,5,6], k = 10
# Output: false
# 
# Explanation: You can try all possible pairs to see that there is no way to
# divide arr into 3 pairs each with sum divisible by 10.
# 
# 
# Constraints:
#         arr.length == n
#         1 <= n <= 10⁵
#         n is even.
#         -10⁹ <= arr[i] <= 10⁹
#         1 <= k <= 10⁵

from collections import Counter

# Solution: https://algo.monster/liteproblems/1497
# Credit: AlgoMonster
def can_arrange(arr, k):
    # Count frequency of each remainder when divided by k
    # Using modulo k to normalize all values to range [0, k-1]
    remainder_count = Counter(x % k for x in arr)
    
    # Check if pairs can be formed:
    # 1. Elements with remainder 0 must pair with themselves (need even count)
    # 2. Elements with remainder i must pair with remainder (k-i)
    
    # Check if count of remainder 0 is even (they pair with each other)
    if remainder_count[0] % 2 != 0:
        return False
    
    # Check if each remainder i has matching count with remainder (k-i)
    # Only need to check up to k//2 to avoid double checking
    for i in range(1, (k + 1) // 2):
        if remainder_count[i] != remainder_count[k - i]:
            return False
    
    # Special case: if k is even, remainder k/2 must pair with itself
    if k % 2 == 0 and remainder_count[k // 2] % 2 != 0:
        return False
    
    return True
    # Time: O(n + k)
    # Space: O(k)


def main():
    result = can_arrange(arr = [1,2,3,4,5,10,6,7,8,9], k = 5)
    print(result) # True

    result = can_arrange(arr = [1,2,3,4,5,6], k = 7)
    print(result) # True

    result = can_arrange(arr = [1,2,3,4,5,6], k = 10)
    print(result) # False

if __name__ == "__main__":
    main()
