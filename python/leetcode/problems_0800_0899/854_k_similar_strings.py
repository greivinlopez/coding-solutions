# ----------------------
# 854. K-Similar Strings
# ----------------------

# Problem: https://leetcode.com/problems/k-similar-strings
#
# Strings s1 and s2 are k-similar (for some non-negative integer k) if we can swap
# the positions of two letters in s1 exactly k times so that the resulting string
# equals s2.
# 
# Given two anagrams s1 and s2, return the smallest k for which s1 and s2 are
# k-similar.
# 
# Example 1:
# 
# Input: s1 = "ab", s2 = "ba"
# Output: 1
# 
# Explanation: The two string are 1-similar because we can use one swap to change
# s1 to s2: "ab" --> "ba".
# 
# Example 2:
# 
# Input: s1 = "abc", s2 = "bca"
# Output: 2
# 
# Explanation: The two strings are 2-similar because we can use two swaps to
# change s1 to s2: "abc" --> "bac" --> "bca".
# 
# 
# Constraints:
#   1 <= s1.length <= 20
#   s2.length == s1.length
#   s1 and s2 contain only lowercase letters from the set {'a','b','c','d','e','f'}.
#   s2 is an anagram of s1.

from collections import deque

# Solution: https://algo.monster/liteproblems/854
# Credit: AlgoMonster
def k_similarity(s1, s2):
    def get_next_states(current_string):
        # Find the first position where current string differs from target
        first_diff_index = 0
        while current_string[first_diff_index] == s2[first_diff_index]:
            first_diff_index += 1
        
        next_states = []
        # Look for positions to swap with
        for swap_index in range(first_diff_index + 1, string_length):
            # Only swap if:
            # 1. The character at swap_index matches what we need at first_diff_index
            # 2. The character at swap_index is not already in its correct position
            if (current_string[swap_index] == s2[first_diff_index] and 
                current_string[swap_index] != s2[swap_index]):
                # Create new string with characters swapped
                swapped_string = (s2[:first_diff_index + 1] + 
                                current_string[first_diff_index + 1:swap_index] + 
                                current_string[first_diff_index] + 
                                current_string[swap_index + 1:])
                next_states.append(swapped_string)
        
        return next_states
    
    # BFS initialization
    queue = deque([s1])
    visited = {s1}
    swap_count = 0
    string_length = len(s1)
    
    # BFS to find minimum swaps
    while True:
        # Process all strings at current level
        for _ in range(len(queue)):
            current = queue.popleft()
            
            # Check if we've reached the target
            if current == s2:
                return swap_count
            
            # Generate and enqueue all valid next states
            for next_state in get_next_states(current):
                if next_state not in visited:
                    visited.add(next_state)
                    queue.append(next_state)
        
        # Increment swap count after processing each level
        swap_count += 1
    # Time: O(n! * n²)
    # Space: O(n! * n)


def main():
    result = k_similarity(s1 = "ab", s2 = "ba")
    print(result) # 1

    result = k_similarity(s1 = "abc", s2 = "bca")
    print(result) # 2

if __name__ == "__main__":
    main()
