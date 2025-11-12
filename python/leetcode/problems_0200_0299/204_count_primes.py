# -----------------
# 204. Count Primes
# -----------------

# Problem: https://leetcode.com/problems/count-primes
#
# Given an integer n, return the number of prime numbers that are strictly less
# than n.
# 
# Example 1:
# 
# Input: n = 10
# Output: 4
#
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
# 
# Example 2:
# 
# Input: n = 0
# Output: 0
# 
# Example 3:
# 
# Input: n = 1
# Output: 0
# 
# 
# Constraints:
#         0 <= n <= 5 * 10⁶


# My Solution based on Adnan Aziz / Tsung-Hsien Lee / Amit Prakash book
# Elements of Programming Interviews in Python
def count_primes(n):
    count = 0 
    is_prime = [False, False,] + [True] * (n - 1)
    for i in range(2, n):
        if is_prime[i]:
            count += 1
            for j in range(i, n+1, i):
                is_prime[j] = False
    return count
    # Time: O(n * log(log(n)))
    # Space: O(n)


def main():
    result = count_primes(10)
    print(result) # 4

    result = count_primes(0)
    print(result) # 0

    result = count_primes(1)
    print(result) # 0

if __name__ == "__main__":
    main()
