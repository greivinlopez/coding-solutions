# --------------------------
# 629. K Inverse Pairs Array
# --------------------------

# Problem: https://leetcode.com/problems/k-inverse-pairs-array
#
# For an integer array nums, an inverse pair is a pair of integers [i, j] where 
# 0 <= i < j < nums.length and nums[i] > nums[j].
# 
# Given two integers n and k, return the number of different arrays consisting of
# numbers from 1 to n such that there are exactly k inverse pairs. Since the
# answer can be huge, return it modulo 10⁹ + 7.
# 
# Example 1:
# 
# Input: n = 3, k = 0
# Output: 1
# 
# Explanation: Only the array [1,2,3] which consists of numbers from 1 to 3 has
# exactly 0 inverse pairs.
# 
# Example 2:
# 
# Input: n = 3, k = 1
# Output: 2
# 
# Explanation: The array [1,3,2] and [2,1,3] have exactly 1 inverse pair.
# 
# 
# Constraints:
#         1 <= n <= 1000
#         0 <= k <= 1000


# Solution: https://youtu.be/dglwb30bUKI
# Credit: Navdeep Singh founder of NeetCode
def k_inverse_pairs_rec(n, k):
    # Recursive Solution
    MOD = 10**9 + 7
    cache = {}

    def count(n, k):
        if n == 0:
            return 1 if k == 0 else 0
        if k < 0:
            return 0
        if (n, k) in cache:
            return cache[(n, k)]

        cache[(n, k)] = 0
        for i in range(n):
            cache[(n, k)] = (cache[(n, k)] + count(n - 1, k - i)) % MOD
        
        return cache[(n, k)]

    return count(n, k)
    # Time: O(n² * k)
    # Space: O(n * k)

def k_inverse_pairs_dp(n, k):
    # Dynamic programming solution - Safe some space
    MOD = 10**9 + 7
    prev = [0] * (k + 1)
    prev[0] = 1

    for N in range(1, n + 1):
        cur = [0] * (k + 1)
        for K in range(0, k + 1):
            for pairs in range(N):
                if K - pairs >= 0:
                    cur[K] += prev[K - pairs]

        prev = cur
    
    return prev[k]
    # Time: O(n² * k)
    # Space: O(k)

def k_inverse_pairs(n, k):
    # Sliding window solution. Optimal solution
    MOD = 10**9 + 7
    prev = [0] * (k + 1)
    prev[0] = 1

    for N in range(1, n + 1):
        cur = [0] * (k + 1)
        total = 0  # sliding window
        for K in range(0, k + 1):
            if K >= N:
                total -= prev[K - N]
            total = (total + prev[K]) % MOD
            cur[K] = total
        
        prev = cur
    
    return prev[k]
    # Time: O(n * k)
    # Space: O(k)


def main():
    result = k_inverse_pairs(n = 3, k = 0)
    print(result) # 1

    result = k_inverse_pairs(n = 3, k = 1)
    print(result) # 2

if __name__ == "__main__":
    main()
