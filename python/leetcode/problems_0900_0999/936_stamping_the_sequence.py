# --------------------------
# 936. Stamping The Sequence
# --------------------------

# Problem: https://leetcode.com/problems/stamping-the-sequence
#
# You are given two strings stamp and target. Initially, there is a string s of
# length target.length with all s[i] == '?'.
# In one turn, you can place stamp over s and replace every letter in the s with
# the corresponding letter from stamp.
#         
#   * For example, if stamp = "abc" and target = "abcba", then s is "?????"
#     initially. In one turn you can:
#   * place stamp at index 0 of s to obtain "abc??",
#   * place stamp at index 1 of s to obtain "?abc?", or
#   * place stamp at index 2 of s to obtain "??abc".
#         
#   Note that stamp must be fully contained in the boundaries of s in order
#   to stamp (i.e., you cannot place stamp at index 3 of s).
# 
# We want to convert s to target using at most 10 * target.length turns.
# 
# Return an array of the index of the left-most letter being stamped at each turn.
# If we cannot obtain target from s within 10 * target.length turns, return an
# empty array.
# 
# Example 1:
# 
# Input: stamp = "abc", target = "ababc"
# Output: [0,2]
# 
# Explanation: Initially s = "?????".
# - Place stamp at index 0 to get "abc??".
# - Place stamp at index 2 to get "ababc".
# [1,0,2] would also be accepted as an answer, as well as some other answers.
# 
# Example 2:
# 
# Input: stamp = "abca", target = "aabcaca"
# Output: [3,0,1]
# 
# Explanation: Initially s = "???????".
# - Place stamp at index 3 to get "???abca".
# - Place stamp at index 0 to get "abcabca".
# - Place stamp at index 1 to get "aabcaca".
# 
# 
# Constraints:
#         1 <= stamp.length <= target.length <= 1000
#         stamp and target consist of lowercase English letters.

from collections import deque

# Solution: https://algo.monster/liteproblems/936
# Credit: AlgoMonster
def moves_to_stamp(stamp, target):
    stamp_length, target_length = len(stamp), len(target)
    
    # Track how many characters at each position still need to match
    # to successfully place stamp at that position
    unmatched_count = [stamp_length] * (target_length - stamp_length + 1)
    
    # Queue for positions that can be stamped (all characters match)
    ready_positions = deque()
    
    # Build dependency graph: for each target position, track which
    # stamp positions depend on it for matching
    dependencies = [[] for _ in range(target_length)]
    
    # Initialize unmatched counts and find initially ready positions
    for stamp_pos in range(target_length - stamp_length + 1):
        for offset, stamp_char in enumerate(stamp):
            target_pos = stamp_pos + offset
            
            if target[target_pos] == stamp_char:
                # This character already matches
                unmatched_count[stamp_pos] -= 1
                if unmatched_count[stamp_pos] == 0:
                    # All characters match, can stamp here
                    ready_positions.append(stamp_pos)
            else:
                # This stamp position depends on target_pos being wildcard
                dependencies[target_pos].append(stamp_pos)
    
    # Process positions in reverse order (unstamping)
    stamp_sequence = []
    is_covered = [False] * target_length
    
    while ready_positions:
        # Process next ready position
        current_stamp_pos = ready_positions.popleft()
        stamp_sequence.append(current_stamp_pos)
        
        # Mark all positions covered by this stamp as wildcards
        for offset in range(stamp_length):
            target_pos = current_stamp_pos + offset
            
            if not is_covered[target_pos]:
                is_covered[target_pos] = True
                
                # Update all stamp positions that were waiting for this wildcard
                for dependent_stamp_pos in dependencies[target_pos]:
                    unmatched_count[dependent_stamp_pos] -= 1
                    if unmatched_count[dependent_stamp_pos] == 0:
                        ready_positions.append(dependent_stamp_pos)
    
    # Check if all positions are covered and return result
    # Reverse the sequence since we found it backwards (unstamping order)
    return stamp_sequence[::-1] if all(is_covered) else []
    # Time: O(n * (n - m + 1))
    # Space: O(n * (n - m + 1))


def main():
    result = moves_to_stamp(stamp = "abc", target = "ababc")
    print(result) # [1, 0, 2]

    result = moves_to_stamp(stamp = "abca", target = "aabcaca")
    print(result) # [2, 3, 0, 1]

if __name__ == "__main__":
    main()
