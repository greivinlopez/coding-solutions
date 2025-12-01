# ------------------------
# 1720. Decode XORed Array
# ------------------------

# Problem: https://leetcode.com/problems/decode-xored-array
#
# There is a hidden integer array arr that consists of n non-negative integers.
# 
# It was encoded into another integer array encoded of length n - 1, such that
# encoded[i] = arr[i] XOR arr[i + 1]. For example, if arr = [1,0,2,1], then
# encoded = [1,2,3].
# 
# You are given the encoded array. You are also given an integer first, that is
# the first element of arr, i.e. arr[0].
# 
# Return the original array arr. It can be proved that the answer exists and is
# unique.
# 
# Example 1:
# 
# Input: encoded = [1,2,3], first = 1
# Output: [1,0,2,1]
# 
# Explanation: If arr = [1,0,2,1], then first = 1 and encoded = [1 XOR 0, 0 XOR 2,
# 2 XOR 1] = [1,2,3]
# 
# Example 2:
# 
# Input: encoded = [6,2,7,3], first = 4
# Output: [4,2,0,7,4]
# 
# 
# Constraints:
#         2 <= n <= 10⁴
#         encoded.length == n - 1
#         0 <= encoded[i] <= 10⁵
#         0 <= first <= 10⁵


# Solution: https://algo.monster/liteproblems/1720
# Credit: AlgoMonster
def decode(encoded, first):
    # Initialize result array with the first element
    result = [first]
    
    # Iterate through each encoded value
    for encoded_value in encoded:
        # Calculate next original value using XOR property:
        # If encoded[i] = original[i] XOR original[i+1]
        # Then original[i+1] = original[i] XOR encoded[i]
        next_value = result[-1] ^ encoded_value
        result.append(next_value)
    
    return result
    # Time: O(n)
    # Space: O(n)


def main():
    result = decode(encoded = [1,2,3], first = 1)
    print(result) # [1, 0, 2, 1]

    result = decode(encoded = [6,2,7,3], first = 4)
    print(result) # [4, 2, 0, 7, 4]

if __name__ == "__main__":
    main()
