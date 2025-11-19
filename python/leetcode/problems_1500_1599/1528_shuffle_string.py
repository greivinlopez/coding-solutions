# --------------------
# 1528. Shuffle String
# --------------------

# Problem: https://leetcode.com/problems/shuffle-string
#
# You are given a string s and an integer array indices of the same length. The
# string s will be shuffled such that the character at the ith position moves to
# indices[i] in the shuffled string.
# 
# Return the shuffled string.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2020/07/09/q1.jpg
# 
# Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
# Output: "leetcode"
# 
# Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.
# 
# Example 2:
# 
# Input: s = "abc", indices = [0,1,2]
# Output: "abc"
# 
# Explanation: After shuffling, each character remains in its position.
# 
# 
# Constraints:
#         s.length == indices.length == n
#         1 <= n <= 100
#         s consists of only lowercase English letters.
#         0 <= indices[i] < n
#         All values of indices are unique.


# Solution: https://algo.monster/liteproblems/1528
# Credit: AlgoMonster
def restore_string(s, indices):
    # Initialize a result list with the same length as the input string
    result = [''] * len(s)
    
    # Iterate through each character and its index in the original string
    for current_index, character in enumerate(s):
        # Place the character at its target position specified by indices array
        target_position = indices[current_index]
        result[target_position] = character
    
    # Join all characters in the result list to form the final string
    return ''.join(result)
    # Time: O(n)
    # Space: O(n)


def main():
    result = restore_string(s = "codeleet", indices = [4,5,6,7,0,2,1,3])
    print(result) # "leetcode"

    result = restore_string(s = "abc", indices = [0,1,2])
    print(result) # "abc"

if __name__ == "__main__":
    main()
