# ------------------------
# 1175. Prime Arrangements
# ------------------------

# Problem: https://leetcode.com/problems/prime-arrangements
#
# Return the number of permutations of 1 to n so that prime numbers are at prime
# indices (1-indexed.)
# 
# (Recall that an integer is prime if and only if it is greater than 1, and cannot
# be written as a product of two positive integers both smaller than it.)
# 
# Since the answer may be large, return the answer modulo 10^9 + 7.
# 
# Example 1:
# 
# Input: n = 5
# Output: 12
# 
# Explanation: For example [1,2,5,4,3] is a valid permutation, but [5,2,3,4,1] is
# not because the prime number 5 is at index 1.
# 
# Example 2:
# 
# Input: n = 100
# Output: 682289015
# 
# 
# Constraints:
#         1 <= n <= 100


# Solution: https://algo.monster/liteproblems/1175
# Credit: AlgoMonster
def num_prime_arrangements(n):
    def count_primes(n):
        # Initialize count of primes
        prime_count = 0
        
        # Create a boolean array to track prime numbers (index represents the number)
        is_prime = [True] * (n + 1)
        
        # 0 and 1 are not prime numbers
        if n >= 0:
            is_prime[0] = False
        if n >= 1:
            is_prime[1] = False
        
        # Sieve of Eratosthenes algorithm
        for i in range(2, n + 1):
            if is_prime[i]:
                # Found a prime number
                prime_count += 1
                
                # Mark all multiples of i as non-prime
                for j in range(i * 2, n + 1, i):
                    is_prime[j] = False
        
        return prime_count
    
    def factorial(num):
        result = 1
        for i in range(1, num + 1):
            result *= i
        return result
    
    # Count how many prime numbers exist from 1 to n
    prime_count = count_primes(n)
    
    # Count of non-prime numbers
    non_prime_count = n - prime_count
    
    # Calculate total arrangements:
    # - Primes can be arranged in prime_count! ways
    # - Non-primes can be arranged in non_prime_count! ways
    # - Total arrangements = prime_count! * non_prime_count!
    total_arrangements = factorial(prime_count) * factorial(non_prime_count)
    
    # Return result modulo 10^9 + 7 to prevent overflow
    MOD = 10**9 + 7
    return total_arrangements % MOD
    # Time: O(n × log log n)
    # Space: O(n)


def main():
    result = num_prime_arrangements(n = 5)
    print(result) # 12

    result = num_prime_arrangements(n = 100)
    print(result) # 682289015

if __name__ == "__main__":
    main()
