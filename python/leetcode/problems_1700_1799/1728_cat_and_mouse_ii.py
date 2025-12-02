# --------------------------
# 1728. Cat and Mouse II 🐱🐭
# --------------------------

# Problem: https://leetcode.com/problems/cat-and-mouse-ii
#
# A game is played by a cat and a mouse named Cat and Mouse.
# 
# The environment is represented by a grid of size rows x cols, where each element
# is a wall, floor, player (Cat, Mouse), or food.
#         
#   * Players are represented by the characters 'C'(Cat),'M'(Mouse).
#   * Floors are represented by the character '.' and can be walked on.
#   * Walls are represented by the character '#' and cannot be walked on.
#   * Food is represented by the character 'F' and can be walked on.
#   * There is only one of each character 'C', 'M', and 'F' in grid.
#
# Mouse and Cat play according to the following rules:
#         
#   * Mouse moves first, then they take turns to move.
#   * During each turn, Cat and Mouse can jump in one of the four directions
#     (left, right, up, down). They cannot jump over the wall nor outside of the grid.
#   * catJump, mouseJump are the maximum lengths Cat and Mouse can jump at a time, 
#     respectively. Cat and Mouse can jump less than the maximum length.
#   * Staying in the same position is allowed.
#   * Mouse can jump over Cat.
# 
# The game can end in 4 ways:
#         
#   * If Cat occupies the same position as Mouse, Cat wins.
#   * If Cat reaches the food first, Cat wins.
#   * If Mouse reaches the food first, Mouse wins.
#   * If Mouse cannot get to the food within 1000 turns, Cat wins.
# 
# Given a rows x cols matrix grid and two integers catJump and mouseJump, return
# true if Mouse can win the game if both Cat and Mouse play optimally, otherwise
# return false.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2020/09/12/sample_111_1955.png
# 
# Input: grid = ["####F","#C...","M...."], catJump = 1, mouseJump = 2
# Output: true
# 
# Explanation: Cat cannot catch Mouse on its turn nor can it get the food before
# Mouse.
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2020/09/12/sample_2_1955.png
# 
# Input: grid = ["M.C...F"], catJump = 1, mouseJump = 4
# Output: true
# 
# Example 3:
# 
# Input: grid = ["M.C...F"], catJump = 1, mouseJump = 3
# Output: false
# 
# 
# Constraints:
#         rows == grid.length
#         cols = grid[i].length
#         1 <= rows, cols <= 8
#         grid[i][j] consist only of characters 'C', 'M', 'F', '.', and '#'.
#         There is only one of each character 'C', 'M', and 'F' in grid.
#         1 <= catJump, mouseJump <= 8


# Note: Due to the use of pairwise this solution works for Python 3.10+
# Solution: https://algo.monster/liteproblems/1728
# Credit: AlgoMonster
def can_mouse_win(grid, catJump, mouseJump):
    from itertools import pairwise

    rows, cols = len(grid), len(grid[0])
    cat_position = mouse_position = food_position = 0
    
    # Direction vectors for 4 directions (up, right, down, left)
    directions = (-1, 0, 1, 0, -1)
    
    # Build adjacency lists for mouse and cat movements
    mouse_graph = [[] for _ in range(rows * cols)]
    cat_graph = [[] for _ in range(rows * cols)]
    
    # Parse grid and build movement graphs
    for row_idx, row in enumerate(grid):
        for col_idx, cell in enumerate(row):
            if cell == "#":  # Skip walls
                continue
                
            # Convert 2D position to 1D index
            current_pos = row_idx * cols + col_idx
            
            # Record special positions
            if cell == "C":
                cat_position = current_pos
            elif cell == "M":
                mouse_position = current_pos
            elif cell == "F":
                food_position = current_pos
            
            # Build possible moves for both mouse and cat
            for dx, dy in pairwise(directions):
                # Add mouse's possible moves (including stay at same position)
                for jump_dist in range(mouseJump + 1):
                    new_row, new_col = row_idx + jump_dist * dx, col_idx + jump_dist * dy
                    
                    # Check boundaries and walls
                    if not (0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] != "#"):
                        break
                    mouse_graph[current_pos].append(new_row * cols + new_col)
                
                # Add cat's possible moves (including stay at same position)
                for jump_dist in range(catJump + 1):
                    new_row, new_col = row_idx + jump_dist * dx, col_idx + jump_dist * dy
                    
                    # Check boundaries and walls
                    if not (0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] != "#"):
                        break
                    cat_graph[current_pos].append(new_row * cols + new_col)
    
    # Calculate game outcome using minimax algorithm
    result = calc(mouse_graph, cat_graph, mouse_position, cat_position, food_position)
    return result == 1  # Return True if mouse wins (result == 1)
    # Time: O(n² * m² * (catJump + mouseJump))
    # Space: O(n² * m²)

def calc(mouse_graph, cat_graph, mouse_start, cat_start, food_pos):
    from collections import deque
    def get_previous_states(state):
        mouse_pos, cat_pos, turn = state
        previous_turn = turn ^ 1  # Toggle turn (0->1 or 1->0)
        previous_states = []
        
        if previous_turn == 1:  # Previous turn was cat's
            # Find all positions cat could have been at
            for prev_cat_pos in cat_graph[cat_pos]:
                if game_results[mouse_pos][prev_cat_pos][1] == 0:
                    previous_states.append((mouse_pos, prev_cat_pos, previous_turn))
        else:  # Previous turn was mouse's
            # Find all positions mouse could have been at
            for prev_mouse_pos in mouse_graph[mouse_pos]:
                if game_results[prev_mouse_pos][cat_pos][0] == 0:
                    previous_states.append((prev_mouse_pos, cat_pos, 0))
        
        return previous_states
    
    num_positions = len(mouse_graph)
    
    # Initialize degree array (number of possible moves from each state)
    # degree[mouse_pos][cat_pos][turn] = number of moves
    degree = [[[0, 0] for _ in range(num_positions)] for _ in range(num_positions)]
    for mouse_pos in range(num_positions):
        for cat_pos in range(num_positions):
            degree[mouse_pos][cat_pos][0] = len(mouse_graph[mouse_pos])  # Mouse's turn
            degree[mouse_pos][cat_pos][1] = len(cat_graph[cat_pos])      # Cat's turn
    
    # Initialize game results array
    # game_results[mouse_pos][cat_pos][turn] = outcome (0: unknown, 1: mouse wins, 2: cat wins)
    game_results = [[[0, 0] for _ in range(num_positions)] for _ in range(num_positions)]
    
    # Queue for BFS
    queue = deque()
    
    # Initialize terminal states
    for pos in range(num_positions):
        # Mouse reaches food (mouse wins regardless of cat position)
        game_results[food_pos][pos][1] = 1
        queue.append((food_pos, pos, 1))
        
        # Cat reaches food (cat wins)
        game_results[pos][food_pos][0] = 2
        queue.append((pos, food_pos, 0))
        
        # Mouse and cat at same position (cat wins)
        game_results[pos][pos][0] = game_results[pos][pos][1] = 2
        queue.append((pos, pos, 0))
        queue.append((pos, pos, 1))
    
    # Perform retrograde analysis using BFS
    while queue:
        current_state = queue.popleft()
        current_result = game_results[current_state[0]][current_state[1]][current_state[2]]
        
        # Process all states that could lead to current state
        for prev_state in get_previous_states(current_state):
            prev_mouse_pos, prev_cat_pos, prev_turn = prev_state
            
            # If previous player can force the same outcome
            if prev_turn == current_result - 1:
                game_results[prev_mouse_pos][prev_cat_pos][prev_turn] = current_result
                queue.append(prev_state)
            else:
                # Decrease degree (one less option leads to unfavorable outcome)
                degree[prev_mouse_pos][prev_cat_pos][prev_turn] -= 1
                
                # If all moves lead to unfavorable outcome
                if degree[prev_mouse_pos][prev_cat_pos][prev_turn] == 0:
                    game_results[prev_mouse_pos][prev_cat_pos][prev_turn] = current_result
                    queue.append(prev_state)
    
    # Return result for initial state (mouse's turn)
    return game_results[mouse_start][cat_start][0]


def main():
    result = can_mouse_win(grid = ["####F","#C...","M...."], catJump = 1, mouseJump = 2)
    print(result) # True

    result = can_mouse_win(grid = ["M.C...F"], catJump = 1, mouseJump = 4)
    print(result) # True

    result = can_mouse_win(grid = ["M.C...F"], catJump = 1, mouseJump = 3)
    print(result) # False

if __name__ == "__main__":
    main()
