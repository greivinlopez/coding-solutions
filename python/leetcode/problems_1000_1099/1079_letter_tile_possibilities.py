# -------------------------------
# 1079. Letter Tile Possibilities
# -------------------------------

# Problem: https://leetcode.com/problems/letter-tile-possibilities
#
# You have n  tiles, where each tile has one letter tiles[i] printed on it.
# 
# Return the number of possible non-empty sequences of letters you can make using
# the letters printed on those tiles.
# 
# Example 1:
# 
# Input: tiles = "AAB"
# Output: 8
# 
# Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB",
# "ABA", "BAA".
# 
# Example 2:
# 
# Input: tiles = "AAABBC"
# Output: 188
# 
# Example 3:
# 
# Input: tiles = "V"
# Output: 1
# 
# 
# Constraints:
#         1 <= tiles.length <= 7
#         tiles consists of uppercase English letters.

from collections import Counter

# Solution: https://youtu.be/8FrJX-P_DnE
# Credit: Navdeep Singh founder of NeetCode
def num_tile_possibilities(tiles):
    count = Counter(tiles)

    def backtrack():
        res = 0
        for c in count:
            if count[c] > 0:
                count[c] -= 1
                res += 1
                res += backtrack()
                count[c] += 1
        return res

    return backtrack()


def main():
    result = num_tile_possibilities("AAB")
    print(result) # 8

    result = num_tile_possibilities("AAABBC")
    print(result) # 188

    result = num_tile_possibilities("V")
    print(result) # 1

if __name__ == "__main__":
    main()
