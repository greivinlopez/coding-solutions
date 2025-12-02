# -----------------------------------------------------------
# 1725. Number Of Rectangles That Can Form The Largest Square
# -----------------------------------------------------------

# Problem: https://leetcode.com/problems/number-of-rectangles-that-can-form-the-largest-square
#
# You are given an array rectangles where rectangles[i] = [lᵢ, wᵢ] represents the
# iᵗʰ rectangle of length lᵢ and width wᵢ.
# 
# You can cut the iᵗʰ rectangle to form a square with a side length of k if both k
# <= lᵢ and k <= wᵢ. For example, if you have a rectangle [4,6], you can cut it to
# get a square with a side length of at most 4.
# 
# Let maxLen be the side length of the largest square you can obtain from any of
# the given rectangles.
# 
# Return the number of rectangles that can make a square with a side length of
# maxLen.
# 
# Example 1:
# 
# Input: rectangles = [[5,8],[3,9],[5,12],[16,5]]
# Output: 3
# 
# Explanation: The largest squares you can get from each rectangle are of lengths
# [5,3,5,5].
# The largest possible square is of length 5, and you can get it out of 3
# rectangles.
# 
# Example 2:
# 
# Input: rectangles = [[2,3],[3,7],[4,3],[3,7]]
# Output: 3
# 
# 
# Constraints:
#         1 <= rectangles.length <= 1000
#         rectangles[i].length == 2
#         1 <= lᵢ, wᵢ <= 10⁹
#         lᵢ != wᵢ


# Solution: https://algo.monster/liteproblems/1725
# Credit: AlgoMonster
def count_good_rectangles(rectangles):
    # Initialize counter and maximum square side length
    count = 0
    max_side = 0
    
    # Iterate through each rectangle
    for length, width in rectangles:
        # Find the maximum square that can fit in this rectangle
        # The side length is limited by the smaller dimension
        square_side = min(length, width)
        
        # If we found a larger square, reset count to 1
        if square_side > max_side:
            count = 1
            max_side = square_side
        # If square has same size as current maximum, increment count
        elif square_side == max_side:
            count += 1
    
    return count
    # Time: O(n)
    # Space: O(1)


def main():
    result = count_good_rectangles(rectangles = [[5,8],[3,9],[5,12],[16,5]])
    print(result) # 3

    result = count_good_rectangles(rectangles = [[2,3],[3,7],[4,3],[3,7]])
    print(result) # 3

if __name__ == "__main__":
    main()
