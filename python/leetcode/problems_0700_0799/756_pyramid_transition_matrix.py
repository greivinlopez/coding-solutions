# ------------------------------
# 756. Pyramid Transition Matrix
# ------------------------------

# Problem: https://leetcode.com/problems/pyramid-transition-matrix
#
# You are stacking blocks to form a pyramid. Each block has a color, which is
# represented by a single letter. Each row of blocks contains one less block than
# the row beneath it and is centered on top.
# 
# To make the pyramid aesthetically pleasing, there are only specific triangular
# patterns that are allowed. A triangular pattern consists of a single block
# stacked on top of two blocks. The patterns are given as a list of three-letter
# strings allowed, where the first two characters of a pattern represent the left
# and right bottom blocks respectively, and the third character is the top block.
#         
#   * For example, "ABC" represents a triangular pattern with a 'C' block
#     stacked on top of an 'A' (left) and 'B' (right) block. Note that this is
#     different from "BAC" where 'B' is on the left bottom and 'A' is on the right
#     bottom.
# 
# You start with a bottom row of blocks bottom, given as a single string, that you
# must use as the base of the pyramid.
# 
# Given bottom and allowed, return true if you can build the pyramid all the way
# to the top such that every triangular pattern in the pyramid is in allowed, or
# false otherwise.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2021/08/26/pyramid1-grid.jpg
# 
# Input: bottom = "BCD", allowed = ["BCC","CDE","CEA","FFF"]
# Output: true
# 
# Explanation: The allowed triangular patterns are shown on the right.
# Starting from the bottom (level 3), we can build "CE" on level 2 and then build
# "A" on level 1.
# There are three triangular patterns in the pyramid, which are "BCC", "CDE", and
# "CEA". All are allowed.
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2021/08/26/pyramid2-grid.jpg
# 
# Input: bottom = "AAAA", allowed = ["AAB","AAC","BCD","BBE","DEF"]
# Output: false
# 
# Explanation: The allowed triangular patterns are shown on the right.
# Starting from the bottom (level 4), there are multiple ways to build level 3,
# but trying all the possibilites, you will get always stuck before building level
# 1.
# 
# 
# Constraints:
#         2 <= bottom.length <= 6
#         0 <= allowed.length <= 216
#         allowed[i].length == 3
#         The letters in all input strings are from the set {'A', 'B', 'C', 'D',
# 'E', 'F'}.
#         All the values of allowed are unique.

from functools import cache
from collections import defaultdict
# from itertools import pairwise, product

# This solution will not work on Python previous to 3.10
# In previous versions you will have to install more-tools
# ----------------------------
# pip install more-itertools
# ----------------------------
# And then:
#   from more_itertools import pairwise

# Solution: https://algo.monster/liteproblems/756
# Credit: AlgoMonster
def pyramid_transition_alt(bottom, allowed):
    # Build a mapping from (left_block, right_block) -> list of possible top blocks
    transitions_map = defaultdict(list)
    for transition in allowed:
        left_block, right_block, top_block = transition[0], transition[1], transition[2]
        transitions_map[left_block, right_block].append(top_block)
    
    @cache
    def can_build_pyramid(current_level: str) -> bool:
        # Base case: if we reach the top (single block), pyramid is complete
        if len(current_level) == 1:
            return True
        
        # Build all possible options for the next level
        next_level_options = []
        
        # For each adjacent pair in current level, find possible blocks above them
        for left_block, right_block in pairwise(current_level):
            possible_blocks = transitions_map[left_block, right_block]
            
            # If no valid block can be placed above this pair, pyramid cannot be built
            if not possible_blocks:
                return False
            
            next_level_options.append(possible_blocks)
        
        # Try all combinations of blocks for the next level
        # product(*next_level_options) generates all possible combinations
        for next_level_combination in product(*next_level_options):
            next_level_string = ''.join(next_level_combination)
            if can_build_pyramid(next_level_string):
                return True
        
        return False
    
    # Start building from the bottom
    return can_build_pyramid(bottom)
    # Time: O(bⁿ * n)
    # Space: O(bⁿ * n)
    # n = the length of the bottom string
    # b = the branching factor (maximum number of possible characters for any pair).


# Solution: https://leetcode.com/problems/pyramid-transition-matrix/solutions/2268424/python-3-bfs-and-dfs
# Credit: Abhay Gupta -> https://leetcode.com/u/gabhay/
def pyramid_transition(bottom, allowed):
    def get_states(s,i,new,allowed):
        nonlocal res

        if i==len(s):
            res.append(''.join(new))
            return 
        for x in allowed[s[i-1]+s[i]]:
            new.append(x)
            get_states(s,i+1,new,allowed)
            new.pop()

    a=defaultdict(list)
    for s in allowed:
        a[s[:2]].append(s[2])
    res=[bottom]
    for x in res:
        if len(x)==1:
            return True
        get_states(x,1,[],a)
    return False
	# Time: O(bⁿ * n)
    # Space: O(bⁿ * n)
    # n = the length of the bottom string
    # b = the branching factor (maximum number of possible characters for any pair).	


def main():
    result = pyramid_transition(bottom = "BCD", allowed = ["BCC","CDE","CEA","FFF"])
    print(result) # True

    result = pyramid_transition(bottom = "AAAA", allowed = ["AAB","AAC","BCD","BBE","DEF"])
    print(result) # False

if __name__ == "__main__":
    main()
