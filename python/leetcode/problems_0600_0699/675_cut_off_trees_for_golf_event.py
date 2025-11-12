# ------------------------------------
# 675. Cut Off Trees for Golf Event 🏌🏻
# ------------------------------------

# Problem: https://leetcode.com/problems/cut-off-trees-for-golf-event
#
# You are asked to cut off all the trees in a forest for a golf event. The forest
# is represented as an m x n matrix. In this matrix:
#
#   * 0 means the cell cannot be walked through.
#   * 1 represents an empty cell that can be walked through.
#   * A number greater than 1 represents a tree in a cell that can be walked
#     through, and this number is the tree's height.
# 
# In one step, you can walk in any of the four directions: north, east, south, and
# west. If you are standing in a cell with a tree, you can choose whether to cut
# it off.
# 
# You must cut off the trees in order from shortest to tallest. When you cut off a
# tree, the value at its cell becomes 1 (an empty cell).
# 
# Starting from the point (0, 0), return the minimum steps you need to walk to cut
# off all the trees. If you cannot cut off all the trees, return -1.
# 
# Note: The input is generated such that no two trees have the same height, and
# there is at least one tree needs to be cut off.
# 
# Example 1:
# 
# Input: forest = [[1,2,3],[0,0,4],[7,6,5]]
# Output: 6
# 
# Explanation: Following the path above allows you to cut off the trees from
# shortest to tallest in 6 steps.
# 
# Example 2:
# 
# Input: forest = [[1,2,3],[0,0,0],[7,6,5]]
# Output: -1
# 
# Explanation: The trees in the bottom row cannot be accessed as the middle row is
# blocked.
# 
# Example 3:
# 
# Input: forest = [[2,3,4],[0,0,5],[8,7,6]]
# Output: 6
# 
# Explanation: You can follow the same path as Example 1 to cut off all the trees.
# Note that you can cut off the first tree at (0, 0) before making any steps.
# 
# 
# Constraints:
#         m == forest.length
#         n == forest[i].length
#         1 <= m, n <= 50
#         0 <= forest[i][j] <= 10⁹
#         Heights of all trees are distinct.

from heapq import heappop, heappush

# Solution: https://algo.monster/liteproblems/675
# Credit: AlgoMonster
def cut_off_tree(forest):
    def heuristic(row1, col1, row2, col2):
        return abs(row1 - row2) + abs(col1 - col2)
    
    def find_shortest_path(start_row, start_col, 
                            target_row, target_col):
        # Priority queue: (f_score, row, col) where f_score = g_score + heuristic
        priority_queue = [(heuristic(start_row, start_col, target_row, target_col), 
                            start_row, start_col)]
        
        # Store minimum distance to each cell using flattened index
        distances = {start_row * cols + start_col: 0}
        
        while priority_queue:
            _, current_row, current_col = heappop(priority_queue)
            current_distance = distances[current_row * cols + current_col]
            
            # Check if we reached the target
            if (current_row, current_col) == (target_row, target_col):
                return current_distance
            
            # Explore four directions: up, down, left, right
            for delta_row, delta_col in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
                next_row = current_row + delta_row
                next_col = current_col + delta_col
                
                # Check if next position is valid and walkable (not 0)
                if (0 <= next_row < rows and 
                    0 <= next_col < cols and 
                    forest[next_row][next_col] > 0):
                    
                    next_distance = current_distance + 1
                    next_index = next_row * cols + next_col
                    
                    # Update if we found a shorter path or visiting for first time
                    if (next_index not in distances or 
                        distances[next_index] > next_distance):
                        
                        distances[next_index] = next_distance
                        f_score = next_distance + heuristic(next_row, next_col, 
                                                            target_row, target_col)
                        heappush(priority_queue, (f_score, next_row, next_col))
        
        # Target is unreachable
        return -1
    
    # Get grid dimensions
    rows, cols = len(forest), len(forest[0])
    
    # Collect all trees (height > 1) with their positions
    trees = [(forest[row][col], row, col) 
                for row in range(rows) 
                for col in range(cols) 
                if forest[row][col] > 1]
    
    # Sort trees by height to determine cutting order
    trees.sort()
    
    # Start from top-left corner
    current_row = current_col = 0
    total_steps = 0
    
    # Visit each tree in ascending height order
    for _, target_row, target_col in trees:
        steps_to_tree = find_shortest_path(current_row, current_col, 
                                            target_row, target_col)
        
        # If any tree is unreachable, the task is impossible
        if steps_to_tree == -1:
            return -1
        
        total_steps += steps_to_tree
        # Update current position to the tree we just cut
        current_row, current_col = target_row, target_col
    
    return total_steps
    # Time: O(m²n² * (m + n))
    # Space: O(m * n)
 

def main():
    result = cut_off_tree(forest = [[1,2,3],[0,0,4],[7,6,5]])
    print(result) # 6

    result = cut_off_tree(forest = [[1,2,3],[0,0,0],[7,6,5]])
    print(result) # -1

    result = cut_off_tree(forest = [[2,3,4],[0,0,5],[8,7,6]])
    print(result) # 6

if __name__ == "__main__":
    main()
