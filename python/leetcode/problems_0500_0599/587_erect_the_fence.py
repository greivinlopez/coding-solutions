# -----------------------
# 587. Erect the Fence 🌲
# -----------------------

# Problem: https://leetcode.com/problems/erect-the-fence
#
# You are given an array trees where trees[i] = [xi, yi] represents the location
# of a tree in the garden.
# 
# Fence the entire garden using the minimum length of rope, as it is expensive.
# The garden is well-fenced only if all the trees are enclosed.
# 
# Return the coordinates of trees that are exactly located on the fence perimeter.
# You may return the answer in any order.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2021/04/24/erect2-plane.jpg
# 
# Input: trees = [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
# Output: [[1,1],[2,0],[4,2],[3,3],[2,4]]
# 
# Explanation: All the trees will be on the perimeter of the fence except the tree
# at [2, 2], which will be inside the fence.
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2021/04/24/erect1-plane.jpg
# 
# Input: trees = [[1,2],[2,2],[4,2]]
# Output: [[4,2],[2,2],[1,2]]
# 
# Explanation: The fence forms a line that passes through all the trees.
# 
# 
# Constraints:
#         1 <= trees.length <= 3000
#         trees[i].length == 2
#         0 <= xᵢ, yᵢ <= 100
#         All the given positions are unique.


# Solution: https://algo.monster/liteproblems/587
# Credit: AlgoMonster
def outer_trees(trees):
    def calculate_cross_product(index_a, index_b, index_c):
        point_a, point_b, point_c = trees[index_a], trees[index_b], trees[index_c]
        vector_ab_x = point_b[0] - point_a[0]
        vector_ab_y = point_b[1] - point_a[1]
        vector_bc_x = point_c[0] - point_b[0]
        vector_bc_y = point_c[1] - point_b[1]
        
        return vector_ab_x * vector_bc_y - vector_ab_y * vector_bc_x
    
    num_trees = len(trees)
    
    # If there are 3 or fewer trees, they all form the convex hull
    if num_trees < 4:
        return trees
    
    # Sort trees by x-coordinate first, then by y-coordinate
    trees.sort()
    
    # Track which points have been visited in the lower hull
    is_visited = [False] * num_trees
    
    # Stack to store indices of points in the convex hull
    hull_stack = [0]
    
    # Build lower hull (left to right)
    for current_index in range(1, num_trees):
        # Remove points that create a clockwise turn (not part of convex hull)
        while len(hull_stack) > 1 and calculate_cross_product(
            hull_stack[-2], hull_stack[-1], current_index
        ) < 0:
            removed_index = hull_stack.pop()
            is_visited[removed_index] = False
        
        is_visited[current_index] = True
        hull_stack.append(current_index)
    
    # Mark the size of lower hull to know when to stop popping during upper hull construction
    lower_hull_size = len(hull_stack)
    
    # Build upper hull (right to left)
    for current_index in range(num_trees - 2, -1, -1):
        # Skip points already in the lower hull
        if is_visited[current_index]:
            continue
        
        # Remove points that create a clockwise turn
        while len(hull_stack) > lower_hull_size and calculate_cross_product(
            hull_stack[-2], hull_stack[-1], current_index
        ) < 0:
            hull_stack.pop()
        
        hull_stack.append(current_index)
    
    # Remove the last point as it's the same as the first point (closes the hull)
    hull_stack.pop()
    
    # Convert indices back to coordinates
    return [trees[index] for index in hull_stack]
    # Time: O(n * log(n))
    # Space: O(n)


def main():
    result = outer_trees(trees = [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]])
    print(result) # [[1,1],[2,0],[4,2],[3,3],[2,4]]

    result = outer_trees(trees = [[1,2],[2,2],[4,2]])
    print(result) # [[4,2],[2,2],[1,2]]

if __name__ == "__main__":
    main()
