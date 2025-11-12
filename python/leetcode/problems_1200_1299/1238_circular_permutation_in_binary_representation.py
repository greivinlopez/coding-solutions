# ---------------------------------------------------
# 1238. Circular Permutation in Binary Representation
# ---------------------------------------------------

# Problem: https://leetcode.com/problems/circular-permutation-in-binary-representation
#
# Given 2 integers n and start. Your task is return any permutation p of
# (0,1,2.....,2^n -1) such that :
# 
#   * p[0] = start
#   * p[i] and p[i+1] differ by only one bit in their binary representation.
#   * p[0] and p[2^n -1] must also differ by only one bit in their binary
#     representation.
# 
# Example 1:
# 
# Input: n = 2, start = 3
# Output: [3,2,0,1]
# 
# Explanation: The binary representation of the permutation is (11,10,00,01).
# All the adjacent element differ by one bit. Another valid permutation is
# [3,1,0,2]
# 
# Example 2:
# 
# Input: n = 3, start = 2
# Output: [2,6,7,5,4,0,1,3]
# 
# Explanation: The binary representation of the permutation is
# (010,110,111,101,100,000,001,011).
# 
# 
# Constraints:
#         1 <= n <= 16
#         0 <= start < 2 ^ n


# Solution: https://algo.monster/liteproblems/1238
# Credit: AlgoMonster
def circular_permutation(n, start):
    # Generate Gray code sequence for n bits
    # Gray code formula: G(i) = i XOR (i >> 1)
    # This creates a sequence where adjacent numbers differ by exactly one bit
    gray_code_sequence = [i ^ (i >> 1) for i in range(1 << n)]
    
    # Find the index where the start value appears in the Gray code sequence
    start_index = gray_code_sequence.index(start)
    
    # Rotate the sequence to begin with the start value
    # Concatenate the sequence from start_index to end with the sequence from beginning to start_index
    return gray_code_sequence[start_index:] + gray_code_sequence[:start_index]
    # Time: O(2ⁿ)
    # Space: O(2ⁿ)


def main():
    result = circular_permutation(n = 2, start = 3)
    print(result) # [3, 2, 0, 1]

    result = circular_permutation(n = 3, start = 2)
    print(result) # [2, 6, 7, 5, 4, 0, 1, 3]

if __name__ == "__main__":
    main()
