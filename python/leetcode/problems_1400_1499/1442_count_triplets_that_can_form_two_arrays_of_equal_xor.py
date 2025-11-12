# ---------------------------------------------------------
# 1442. Count Triplets That Can Form Two Arrays of Equal XOR
# ---------------------------------------------------------

# Problem: https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor
#
# Given an array of integers arr.
# 
# We want to select three indices i, j and k where (0 <= i < j <= k < arr.length).
# 
# Let's define a and b as follows:
#         a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
#         b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]
# 
# Note that ^ denotes the bitwise-xor operation.
# 
# Return the number of triplets (i, j and k) Where a == b.
# 
# Example 1:
# 
# nput: arr = [2,3,1,6,7]
# Output: 4
# 
# Explanation: The triplets are (0,1,2), (0,2,2), (2,3,4) and (2,4,4)
# 
# Example 2:
# 
# Input: arr = [1,1,1,1,1]
# Output: 10
# 
# 
# Constraints:
#         1 <= arr.length <= 300
#         1 <= arr[i] <= 10^8

from collections import defaultdict

# Solution: https://youtu.be/e4Yx9KjqzQ8
# Credit: Navdeep Singh founder of NeetCode
def count_triplets(arr):
    n = len(arr)
    res = 0

    prefix = 0
    prev_xor_cnt = defaultdict(int)
    prev_xor_cnt[0] = 1
    prev_xor_index_sum = defaultdict(int)

    for i in range(n):
        prefix ^= arr[i]

        if prev_xor_cnt[prefix]:
            res += i * prev_xor_cnt[prefix] - prev_xor_index_sum[prefix]

        prev_xor_cnt[prefix] += 1
        prev_xor_index_sum[prefix] += i + 1

    return res
    # Time: O(n)


def main():
    result = count_triplets([2,3,1,6,7])
    print(result) # 4

    result = count_triplets([1,1,1,1,1])
    print(result) # 10

if __name__ == "__main__":
    main()
