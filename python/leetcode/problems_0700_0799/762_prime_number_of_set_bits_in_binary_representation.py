# ------------------------------------------------------
# 762. Prime Number of Set Bits in Binary Representation
# ------------------------------------------------------

# Problem: https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation
#
# Given two integers left and right, return the count of numbers in the inclusive
# range [left, right] having a prime number of set bits in their binary
# representation.
# 
# Recall that the number of set bits an integer has is the number of 1's present
# when written in binary.
#         
#   * For example, 21 written in binary is 10101, which has 3 set bits.
# 
# Example 1:
# 
# Input: left = 6, right = 10
# Output: 4
# 
# Explanation:
# 6  -> 110 (2 set bits, 2 is prime)
# 7  -> 111 (3 set bits, 3 is prime)
# 8  -> 1000 (1 set bit, 1 is not prime)
# 9  -> 1001 (2 set bits, 2 is prime)
# 10 -> 1010 (2 set bits, 2 is prime)
# 4 numbers have a prime number of set bits.
# 
# Example 2:
# 
# Input: left = 10, right = 15
# Output: 5
# 
# Explanation:
# 10 -> 1010 (2 set bits, 2 is prime)
# 11 -> 1011 (3 set bits, 3 is prime)
# 12 -> 1100 (2 set bits, 2 is prime)
# 13 -> 1101 (3 set bits, 3 is prime)
# 14 -> 1110 (3 set bits, 3 is prime)
# 15 -> 1111 (4 set bits, 4 is not prime)
# 5 numbers have a prime number of set bits.
# 
# 
# Constraints:
#         1 <= left <= right <= 10⁶
#         0 <= right - left <= 10⁴


# Solution: https://algo.monster/liteproblems/762
# Credit: AlgoMonster
def count_prime_set_bits(left, right):
    # Set of prime numbers up to 19 (maximum possible bit count for 32-bit integers)
    # Since right <= 10^6 < 2^20, we only need primes up to 19
    prime_numbers = {2, 3, 5, 7, 11, 13, 17, 19}
    
    # Count how many numbers have prime number of set bits
    count = 0
    for num in range(left, right + 1):
        # Get the number of set bits (1s) in binary representation
        # set_bits_count = num.bit_count()  for Python 3.10+
        set_bits_count = bin(num).count('1')
        
        # Check if the count of set bits is a prime number
        if set_bits_count in prime_numbers:
            count += 1
            
    return count
    # Time: O(n)
    # Space: O(1)
    # n = right - left + 1


def main():
    result = count_prime_set_bits(left = 6, right = 10)
    print(result) # 4

    result = count_prime_set_bits(left = 10, right = 15)
    print(result) # 5

if __name__ == "__main__":
    main()
