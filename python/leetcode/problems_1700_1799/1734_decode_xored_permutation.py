# ------------------------------
# 1734. Decode XORed Permutation
# ------------------------------

# Problem: https://leetcode.com/problems/decode-xored-permutation
#
# There is an integer array perm that is a permutation of the first n positive
# integers, where n is always odd.
# 
# It was encoded into another integer array encoded of length n - 1, such that
# encoded[i] = perm[i] XOR perm[i + 1]. For example, if perm = [1,3,2], then
# encoded = [2,1].
# 
# Given the encoded array, return the original array perm. It is guaranteed that
# the answer exists and is unique.
# 
# Example 1:
# 
# Input: encoded = [3,1]
# Output: [1,2,3]
# 
# Explanation: If perm = [1,2,3], then encoded = [1 XOR 2,2 XOR 3] = [3,1]
# 
# Example 2:
# 
# Input: encoded = [6,5,4,6]
# Output: [2,4,1,5,3]
# 
# 
# Constraints:
#         3 <= n < 10⁵
#         n is odd.
#         encoded.length == n - 1


# Solution: https://algo.monster/liteproblems/1734
# Credit: AlgoMonster
def decode(encoded):
    # Calculate the length of the original permutation
    # Since encoded has n-1 elements, the permutation has n elements
    n = len(encoded) + 1
    
    # Calculate XOR of elements at even indices in encoded array
    # This represents: perm[0] ^ perm[1] ^ perm[2] ^ perm[3] ^ ... (excluding last element)
    xor_even_indices = 0
    for i in range(0, n - 1, 2):
        xor_even_indices ^= encoded[i]
    
    # Calculate XOR of all numbers from 1 to n
    # Since perm is a permutation of [1, 2, ..., n], this gives us XOR of all elements
    xor_all_numbers = 0
    for i in range(1, n + 1):
        xor_all_numbers ^= i
    
    # Initialize the result permutation array
    permutation = [0] * n
    
    # Find the last element of the permutation
    # xor_even_indices gives us XOR of all elements except the last one
    # xor_all_numbers ^ xor_even_indices cancels out all except the last element
    permutation[-1] = xor_even_indices ^ xor_all_numbers
    
    # Reconstruct the permutation from right to left
    # Since encoded[i] = permutation[i] ^ permutation[i+1]
    # We can get permutation[i] = encoded[i] ^ permutation[i+1]
    for i in range(n - 2, -1, -1):
        permutation[i] = encoded[i] ^ permutation[i + 1]
    
    return permutation
    # Time: O(n)
    # Space: O(n)


def main():
    result = decode(encoded = [3,1])
    print(result) # [1, 2, 3]

    result = decode(encoded = [6,5,4,6])
    print(result) # [2, 4, 1, 5, 3]

if __name__ == "__main__":
    main()
