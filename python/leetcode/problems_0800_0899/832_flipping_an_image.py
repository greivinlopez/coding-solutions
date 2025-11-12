# ----------------------
# 832. Flipping an Image
# ----------------------

# Problem: https://leetcode.com/problems/flipping-an-image
#
# Given an n x n binary matrix image, flip the image horizontally, then invert it,
# and return the resulting image.
# 
# To flip an image horizontally means that each row of the image is reversed.
#         
#   * For example, flipping [1,1,0] horizontally results in [0,1,1].
# 
# To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.
#         
#   * For example, inverting [0,1,1] results in [1,0,0].
# 
# Example 1:
# 
# Input: image = [[1,1,0],[1,0,1],[0,0,0]]
# Output: [[1,0,0],[0,1,0],[1,1,1]]
# 
# Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
# Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]
# 
# Example 2:
# 
# Input: image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
# Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
# 
# Explanation: First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]].
# Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
# 
# 
# Constraints:
#         n == image.length
#         n == image[i].length
#         1 <= n <= 20
#         images[i][j] is either 0 or 1.


# Solution: https://algo.monster/liteproblems/832
# Credit: AlgoMonster
def flip_and_invert_image(image):
    n = len(image)
    
    # Process each row in the image
    for row in image:
        left = 0
        right = n - 1
        
        # Use two pointers to process the row from both ends
        while left < right:
            # If values at symmetric positions are equal,
            # after flip they remain at same positions but need inversion
            if row[left] == row[right]:
                row[left] ^= 1  # Invert left element using XOR
                row[right] ^= 1  # Invert right element using XOR
            # If values are different, swapping during flip
            # automatically gives us the inverted result
            
            # Move pointers toward center
            left += 1
            right -= 1
        
        # Handle middle element for odd-length rows
        # Middle element stays in place but needs inversion
        if left == right:
            row[left] ^= 1
            
    return image
    # Time: O(n²)
    # Space: O(1)

# Alternative Solution: One line
# Solution: https://leetcode.com/problems/flipping-an-image/solutions/550889/the-python3-one-liner
def flip_and_invert_image_short(image):
    return [[1 ^ bit for bit in row[::-1]] for row in image]


def main():
    result = flip_and_invert_image(image = [[1,1,0],[1,0,1],[0,0,0]])
    print(result) # [[1, 0, 0], [0, 1, 0], [1, 1, 1]]

    result = flip_and_invert_image(image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]])
    print(result) # [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 0, 1], [1, 0, 1, 0]]

if __name__ == "__main__":
    main()
