# ------------------
# 835. Image Overlap
# ------------------

# Problem: https://leetcode.com/problems/image-overlap
#
# You are given two images, img1 and img2, represented as binary, square matrices
# of size n x n. A binary matrix has only 0s and 1s as values.
# 
# We translate one image however we choose by sliding all the 1 bits left, right,
# up, and/or down any number of units. We then place it on top of the other image.
# 
# We can then calculate the overlap by counting the number of positions that have
# a 1 in both images.
# 
# Note also that a translation does not include any kind of rotation. Any 1 bits
# that are translated outside of the matrix borders are erased.
# 
# Return the largest possible overlap.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2020/09/09/overlap1.jpg
# 
# Input: img1 = [[1,1,0],[0,1,0],[0,1,0]], img2 = [[0,0,0],[0,1,1],[0,0,1]]
# Output: 3
# 
# Explanation: We translate img1 to right by 1 unit and down by 1 unit.
# https://assets.leetcode.com/uploads/2020/09/09/overlap_step1.jpg
# 
# The number of positions that have a 1 in both images is 3 (shown in red).
# https://assets.leetcode.com/uploads/2020/09/09/overlap_step2.jpg
# 
# Example 2:
# 
# Input: img1 = [[1]], img2 = [[1]]
# Output: 1
# 
# Example 3:
# 
# Input: img1 = [[0]], img2 = [[0]]
# Output: 0
# 
# 
# Constraints:
#         n == img1.length == img1[i].length
#         n == img2.length == img2[i].length
#         1 <= n <= 30
#         img1[i][j] is either 0 or 1.
#         img2[i][j] is either 0 or 1.

from collections import Counter

# Solution: https://algo.monster/liteproblems/835
# Credit: AlgoMonster
def largest_overlap(img1, img2):
    n = len(img1)
    
    # Dictionary to count overlaps for each translation vector (row_shift, col_shift)
    translation_count = Counter()
    
    # Iterate through all positions in img1
    for row1 in range(n):
        for col1 in range(n):
            # If current position in img1 contains a 1
            if img1[row1][col1] == 1:
                # Check all positions in img2
                for row2 in range(n):
                    for col2 in range(n):
                        # If current position in img2 contains a 1
                        if img2[row2][col2] == 1:
                            # Calculate the translation vector needed to align
                            # these two 1's (from img1 position to img2 position)
                            translation_vector = (row1 - row2, col1 - col2)
                            
                            # Increment count for this translation
                            translation_count[translation_vector] += 1
    
    # Return the maximum overlap count, or 0 if no overlaps exist
    return max(translation_count.values()) if translation_count else 0
    # Time: O(n⁴)
    # Space: O(n²)


def main():
    result = largest_overlap(img1 = [[1,1,0],[0,1,0],[0,1,0]], img2 = [[0,0,0],[0,1,1],[0,0,1]])
    print(result) # 3

    result = largest_overlap(img1 = [[1]], img2 = [[1]])
    print(result) # 1

    result = largest_overlap(img1 = [[0]], img2 = [[0]])
    print(result) # 0

if __name__ == "__main__":
    main()
