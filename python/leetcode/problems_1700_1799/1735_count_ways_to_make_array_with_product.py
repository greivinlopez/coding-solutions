# -------------------------------------------
# 1735. Count Ways to Make Array With Product
# -------------------------------------------

# Problem: https://leetcode.com/problems/count-ways-to-make-array-with-product
#
# You are given a 2D integer array, queries. For each queries[i], where queries[i]
# = [ni, ki], find the number of different ways you can place positive integers
# into an array of size ni such that the product of the integers is ki. As the
# number of ways may be too large, the answer to the ith query is the number of
# ways modulo 109 + 7.
# Return an integer array answer where answer.length == queries.length, and
# answer[i] is the answer to the ith query.
# Example 1:
# Input: queries = [[2,6],[5,1],[73,660]]
# Output: [4,1,50734910]
# Explanation: Each query is independent.
# [2,6]: There are 4 ways to fill an array of size 2 that multiply to 6: [1,6],
# [2,3], [3,2], [6,1].
# [5,1]: There is 1 way to fill an array of size 5 that multiply to 1:
# [1,1,1,1,1].
# [73,660]: There are 1050734917 ways to fill an array of size 73 that multiply to
# 660. 1050734917 modulo 109 + 7 = 50734910.
# Example 2:
# Input: queries = [[1,1],[2,2],[3,3],[4,4],[5,5]]
# Output: [1,2,3,10,5]
# Constraints:
#         1 <= queries.length <= 104
#         1 <= ni, ki <= 104


# Solution: https://algo.monster/liteproblems/1735
# Credit: AlgoMonster
def ways_to_fill_array(queries):
    from collections import defaultdict

    def combination(n, k):
        return factorials[n] * factorial_inverses[k] * factorial_inverses[n - k] % MOD

    # Constants
    MAX_VALUE = 10020
    MOD = 10**9 + 7

    # Precompute factorials and their modular inverses
    factorials = [1] * MAX_VALUE
    factorial_inverses = [1] * MAX_VALUE

    # Precompute prime factorizations
    prime_factorizations = defaultdict(list)

    # Initialize factorials, their inverses, and prime factorizations
    for i in range(1, MAX_VALUE):
        # Compute factorial: i! = (i-1)! * i
        factorials[i] = factorials[i - 1] * i % MOD
    
        # Compute modular inverse of factorial using Fermat's Little Theorem
        # Since MOD is prime, inverse of a is a^(MOD-2) mod MOD
        factorial_inverses[i] = pow(factorials[i], MOD - 2, MOD)
    
        # Find prime factorization of i
        current_number = i
        divisor = 2
    
        # Check divisors up to sqrt(current_number)
        while divisor <= current_number // divisor:
            if current_number % divisor == 0:
                # Count the power of this prime factor
                exponent = 0
                while current_number % divisor == 0:
                    exponent += 1
                    current_number //= divisor
                # Store the exponent of this prime factor
                prime_factorizations[i].append(exponent)
            divisor += 1
  
    # If remaining number > 1, it's a prime factor with exponent 1
    if current_number > 1:
        prime_factorizations[i].append(1)

    result = []
    
    for array_size, target_product in queries:
        ways = 1
        
        # For each prime factor's exponent in the factorization of target_product
        for exponent in prime_factorizations[target_product]:
            # Apply stars and bars: distribute 'exponent' items into 'array_size' bins
            # This is equivalent to C(exponent + array_size - 1, array_size - 1)
            ways = ways * combination(exponent + array_size - 1, array_size - 1) % MOD
        
        result.append(ways)
    
    return result
    # Time: O(K × √K + N + m × log K)
    # Space: O(N)


def main():
    result = ways_to_fill_array(queries = [[2,6],[5,1],[73,660]])
    print(result) # [2, 1, 14393629]

    result = ways_to_fill_array(queries = [[1,1],[2,2],[3,3],[4,4],[5,5]])
    print(result) # [1, 1, 1, 10, 1]

if __name__ == "__main__":
    main()
