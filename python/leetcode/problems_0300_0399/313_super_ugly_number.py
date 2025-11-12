# ----------------------
# 313. Super Ugly Number
# ----------------------

# Problem: https://leetcode.com/problems/super-ugly-number
#
# A super ugly number is a positive integer whose prime factors are in the array
# primes.
# 
# Given an integer n and an array of integers primes, return the nth super ugly
# number.
# 
# The nth super ugly number is guaranteed to fit in a 32-bit signed integer.
# 
# Example 1:
# 
# Input: n = 12, primes = [2,7,13,19]
# Output: 32
# 
# Explanation: [1,2,4,7,8,13,14,16,19,26,28,32] is the sequence of the first 12
# super ugly numbers given primes = [2,7,13,19].
# 
# Example 2:
# 
# Input: n = 1, primes = [2,3,5]
# Output: 1
# 
# Explanation: 1 has no prime factors, therefore all of its prime factors are in
# the array primes = [2,3,5].
# 
# 
# Constraints:
#         1 <= n <= 10⁵
#         1 <= primes.length <= 100
#         2 <= primes[i] <= 1000
#         primes[i] is guaranteed to be a prime number.
#         All the values of primes are unique and sorted in ascending order.

import heapq

# Solution: https://leetcode.com/problems/super-ugly-number/solutions/868948/python3-l-faster-than-99-35-using-heapq
def nth_super_ugly_number(n, primes):
    queue = [1]
    while n > 1:
        n -= 1
        num = heapq.heappop(queue)
        for prime in primes:
            heapq.heappush(queue, prime * num)
            if num % prime == 0:
                break
    return queue[0]
    # Time: O(n * m * log(n * m))
    # Space: O(n * m)
    # n = the target index
    # m = the number of primes


def main():
    result = nth_super_ugly_number(n = 12, primes = [2,7,13,19])
    print(result) # 32

    result = nth_super_ugly_number(n = 1, primes = [2,3,5])
    print(result) # 1

if __name__ == "__main__":
    main()
