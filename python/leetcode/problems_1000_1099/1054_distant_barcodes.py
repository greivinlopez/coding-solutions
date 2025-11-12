# ----------------------
# 1054. Distant Barcodes
# ----------------------

# Problem: https://leetcode.com/problems/distant-barcodes
#
# In a warehouse, there is a row of barcodes, where the iᵗʰ barcode is
# barcodes[i].
# 
# Rearrange the barcodes so that no two adjacent barcodes are equal. You may
# return any answer, and it is guaranteed an answer exists.
# 
# Example 1:
# 
# Input: barcodes = [1,1,1,2,2,2]
# Output: [2,1,2,1,2,1]
# 
# Example 2:
# 
# Input: barcodes = [1,1,1,1,2,2,3,3]
# Output: [1,3,1,3,1,2,1,2]
# 
# 
# Constraints:
#         1 <= barcodes.length <= 10000
#         1 <= barcodes[i] <= 10000

from collections import Counter

# Solution: https://algo.monster/liteproblems/1054
# Credit: AlgoMonster
def rearrange_barcodes(barcodes):
    # Count frequency of each barcode
    frequency_map = Counter(barcodes)
    
    # Sort barcodes by frequency (descending) and value (ascending as tiebreaker)
    # This ensures most frequent elements are placed first
    barcodes.sort(key=lambda barcode: (-frequency_map[barcode], barcode))
    
    # Get the length of the array
    n = len(barcodes)
    
    # Initialize result array with zeros
    result = [0] * n
    
    # Place first half of sorted barcodes at even indices (0, 2, 4, ...)
    # This ensures the most frequent element is spread out maximally
    result[::2] = barcodes[:(n + 1) // 2]
    
    # Place second half of sorted barcodes at odd indices (1, 3, 5, ...)
    result[1::2] = barcodes[(n + 1) // 2:]
    
    return result
    # Time: O(n * log(n))
    # Space: O(n)


def main():
    result = rearrange_barcodes([1,1,1,2,2,2])
    print(result) # [1, 2, 1, 2, 1, 2]

    result = rearrange_barcodes([1,1,1,1,2,2,3,3])
    print(result) # [1, 2, 1, 2, 1, 3, 1, 3]

if __name__ == "__main__":
    main()
