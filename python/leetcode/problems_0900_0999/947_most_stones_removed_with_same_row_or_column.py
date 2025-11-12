# ------------------------------------------------
# 947. Most Stones Removed with Same Row or Column
# ------------------------------------------------

# Problem: https://leetcode.com/problems/most-stones-removed-with-same-row-or-column
#
# On a 2D plane, we place n stones at some integer coordinate points. Each
# coordinate point may have at most one stone.
# 
# A stone can be removed if it shares either the same row or the same column as
# another stone that has not been removed.
# 
# Given an array stones of length n where stones[i] = [xᵢ, yᵢ] represents the
# location of the ith stone, return the largest possible number of stones that can
# be removed.
# 
# Example 1:
# 
# Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
# Output: 5
# 
# Explanation: One way to remove 5 stones is as follows:
# 1. Remove stone [2,2] because it shares the same row as [2,1].
# 2. Remove stone [2,1] because it shares the same column as [0,1].
# 3. Remove stone [1,2] because it shares the same row as [1,0].
# 4. Remove stone [1,0] because it shares the same column as [0,0].
# 5. Remove stone [0,1] because it shares the same row as [0,0].
# Stone [0,0] cannot be removed since it does not share a row/column with another
# stone still on the plane.
# 
# Example 2:
# 
# Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
# Output: 3
# 
# Explanation: One way to make 3 moves is as follows:
# 1. Remove stone [2,2] because it shares the same row as [2,0].
# 2. Remove stone [2,0] because it shares the same column as [0,0].
# 3. Remove stone [0,2] because it shares the same row as [0,0].
# Stones [0,0] and [1,1] cannot be removed since they do not share a row/column
# with another stone still on the plane.
# 
# Example 3:
# 
# Input: stones = [[0,0]]
# Output: 0
# 
# Explanation: [0,0] is the only stone on the plane, so you cannot remove it.
# 
# 
# Constraints:
#         1 <= stones.length <= 1000
#         0 <= xᵢ, yᵢ <= 10⁴
#         No two stones are at the same coordinate point.


# Solution: https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/solutions/5705563/dsu-approach-with-tc-o-n-n-beats-100-in-all-languages
# Credit: Fabio breo -> https://leetcode.com/u/Fabiobreo/ | Naruto Uchiha -> https://leetcode.com/u/Solution_Assist/
def remove_stones(stones):
    connected_component_count = 0

    def find_representative(element, set_representatives):
        nonlocal connected_component_count
        if set_representatives[element] == 0:
            set_representatives[element] = element
            connected_component_count += 1
        if set_representatives[element] != element:
            set_representatives[element] = find_representative(set_representatives[element], set_representatives)
        return set_representatives[element]

    def merge_components(element_a, element_b, set_representatives):
        nonlocal connected_component_count
        rep_a = find_representative(element_a, set_representatives)
        rep_b = find_representative(element_b, set_representatives)
        if rep_a != rep_b:
            set_representatives[rep_b] = rep_a
            connected_component_count -= 1

    set_representatives = [0] * 20003
    for stone_position in stones:
        merge_components(stone_position[0] + 1, stone_position[1] + 10002, set_representatives)
    return len(stones) - connected_component_count
    # Time: O(n * α(n) + k)
    # Space: O(n)
    # n = the number of stones
    # α(n) = the inverse Ackermann function
    # k = 20003 (the size of the setRepresentatives array). 


def main():
    result = remove_stones(stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]])
    print(result) # 5

    result = remove_stones(stones = [[0,0],[0,2],[1,1],[2,0],[2,2]])
    print(result) # 3

    result = remove_stones(stones = [[0,0]])
    print(result) # 0

if __name__ == "__main__":
    main()
