# -----------------------
# 913. Cat and Mouse 🐱🐭
# -----------------------

# Problem: https://leetcode.com/problems/cat-and-mouse
#
# A game on an undirected graph is played by two players, Mouse and Cat, who
# alternate turns.
# 
# The graph is given as follows: graph[a] is a list of all nodes b such that ab is
# an edge of the graph.
# 
# The mouse starts at node 1 and goes first, the cat starts at node 2 and goes
# second, and there is a hole at node 0.
# 
# During each player's turn, they must travel along one edge of the graph that
# meets where they are.  For example, if the Mouse is at node 1, it must travel to
# any node in graph[1].
# 
# Additionally, it is not allowed for the Cat to travel to the Hole (node 0).
# 
# Then, the game can end in three ways:
# 
#   * If ever the Cat occupies the same node as the Mouse, the Cat wins.
#   * If ever the Mouse reaches the Hole, the Mouse wins.
#   * If ever a position is repeated (i.e., the players are in the same position 
#     as a previous turn, and it is the same player's turn to move), the game
#     is a draw.
# 
# Given a graph, and assuming both players play optimally, return
# 
#         1 if the mouse wins the game,
#         2 if the cat wins the game, or
#         0 if the game is a draw.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2020/11/17/cat1.jpg
# 
# Input: graph = [[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]]
# Output: 0
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2020/11/17/cat2.jpg
# 
# Input: graph = [[1,3],[0],[3],[0,2]]
# Output: 1
# 
# 
# Constraints:
#         3 <= graph.length <= 50
#         1 <= graph[i].length < graph.length
#         0 <= graph[i][j] < graph.length
#         graph[i][j] != i
#         graph[i] is unique.
#         The mouse and the cat can always move.

from collections import deque

# Solution: https://algo.monster/liteproblems/913
# Credit: AlgoMonster
def cat_mouse_game(graph):
    # Game constants
    HOLE, MOUSE_START, CAT_START = 0, 1, 2
    MOUSE_TURN, CAT_TURN = 0, 1
    MOUSE_WIN, CAT_WIN, TIE = 1, 2, 0
    
    def get_previous_states(current_state):
        mouse_pos, cat_pos, turn = current_state
        previous_turn = turn ^ 1  # Toggle turn using XOR
        previous_states = []
        
        if previous_turn == CAT_TURN:
            # If it was cat's turn, cat could have moved from any adjacent position
            for previous_cat_pos in graph[cat_pos]:
                if previous_cat_pos != HOLE:  # Cat cannot be at hole
                    previous_states.append((mouse_pos, previous_cat_pos, previous_turn))
        else:
            # If it was mouse's turn, mouse could have moved from any adjacent position
            for previous_mouse_pos in graph[mouse_pos]:
                previous_states.append((previous_mouse_pos, cat_pos, previous_turn))
        
        return previous_states
    
    n = len(graph)
    
    # Initialize result array: result[mouse][cat][turn] = game outcome
    result = [[[0, 0] for _ in range(n)] for _ in range(n)]
    
    # Initialize degree array: tracks number of possible moves from each state
    degree = [[[0, 0] for _ in range(n)] for _ in range(n)]
    
    # Calculate degrees for each state
    for mouse_pos in range(n):
        for cat_pos in range(1, n):  # Cat cannot be at position 0 (hole)
            degree[mouse_pos][cat_pos][MOUSE_TURN] = len(graph[mouse_pos])
            degree[mouse_pos][cat_pos][CAT_TURN] = len(graph[cat_pos])
        
        # Adjust cat's degree since it cannot move to hole
        for adjacent_to_hole in graph[HOLE]:
            degree[mouse_pos][adjacent_to_hole][CAT_TURN] -= 1
    
    # BFS queue for processing states
    queue = deque()
    
    # Initialize known winning states: mouse at hole
    for cat_pos in range(1, n):
        result[0][cat_pos][MOUSE_TURN] = MOUSE_WIN
        result[0][cat_pos][CAT_TURN] = MOUSE_WIN
        queue.append((0, cat_pos, MOUSE_TURN))
        queue.append((0, cat_pos, CAT_TURN))
    
    # Initialize known winning states: cat catches mouse
    for pos in range(1, n):
        result[pos][pos][MOUSE_TURN] = CAT_WIN
        result[pos][pos][CAT_TURN] = CAT_WIN
        queue.append((pos, pos, MOUSE_TURN))
        queue.append((pos, pos, CAT_TURN))
    
    # Process states using BFS
    while queue:
        current_state = queue.popleft()
        current_mouse, current_cat, current_turn = current_state
        current_result = result[current_mouse][current_cat][current_turn]
        
        # Check all states that could lead to current state
        for previous_state in get_previous_states(current_state):
            prev_mouse, prev_cat, prev_turn = previous_state
            
            # Skip if this previous state already has a determined outcome
            if result[prev_mouse][prev_cat][prev_turn] != TIE:
                continue
            
            # Check if previous player can force a win
            is_winning_move = (
                (current_result == MOUSE_WIN and prev_turn == MOUSE_TURN) or
                (current_result == CAT_WIN and prev_turn == CAT_TURN)
            )
            
            if is_winning_move:
                # Previous player found a winning move
                result[prev_mouse][prev_cat][prev_turn] = current_result
                queue.append(previous_state)
            else:
                # Decrease the degree (number of unexplored moves)
                degree[prev_mouse][prev_cat][prev_turn] -= 1
                
                # If all moves lead to loss, previous player loses
                if degree[prev_mouse][prev_cat][prev_turn] == 0:
                    result[prev_mouse][prev_cat][prev_turn] = current_result
                    queue.append(previous_state)
    
    # Return the result for initial state
    return result[MOUSE_START][CAT_START][MOUSE_TURN]
    # Time: O(n³)
    # Space: O(n²)


def main():
    result = cat_mouse_game(graph = [[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]])
    print(result) # 0

    result = cat_mouse_game(graph = [[1,3],[0],[3],[0,2]])
    print(result) # 1

if __name__ == "__main__":
    main()
