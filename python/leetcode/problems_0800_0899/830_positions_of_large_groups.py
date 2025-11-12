# ------------------------------
# 830. Positions of Large Groups
# ------------------------------

# Problem: https://leetcode.com/problems/positions-of-large-groups
#
# In a string s of lowercase letters, these letters form consecutive groups of the
# same character.
# 
# For example, a string like s = "abbxxxxzyy" has the groups "a", "bb", "xxxx",
# "z", and "yy".
# 
# A group is identified by an interval [start, end], where start and end denote
# the start and end indices (inclusive) of the group. In the above
# example, "xxxx" has the interval [3,6].
# 
# A group is considered large if it has 3 or more characters.
# 
# Return the intervals of every large group sorted in increasing order by start
# index.
# 
# Example 1:
# 
# Input: s = "abbxxxxzzy"
# Output: [[3,6]]
# 
# Explanation: "xxxx" is the only large group with start index 3 and end index 6.
# 
# Example 2:
# 
# Input: s = "abc"
# Output: []
# 
# Explanation: We have groups "a", "b", and "c", none of which are large groups.
# 
# Example 3:
# 
# Input: s = "abcdddeeeeaabbbcd"
# Output: [[3,5],[6,9],[12,14]]
# 
# Explanation: The large groups are "ddd", "eeee", and "bbb".
# 
# 
# Constraints:
#         1 <= s.length <= 1000
#         s contains lowercase English letters only.


# Solution: https://algo.monster/liteproblems/830
# Credit: AlgoMonster
def large_group_positions(s):
    # Initialize pointer and get string length
    current_index = 0
    string_length = len(s)
    result = []
    
    # Iterate through the string
    while current_index < string_length:
        # Start of current group
        group_start = current_index
        
        # Find the end of current group of identical characters
        while current_index < string_length and s[current_index] == s[group_start]:
            current_index += 1
        
        # Check if group is large (3 or more characters)
        group_size = current_index - group_start
        if group_size >= 3:
            # Add [start, end] position to result (end is inclusive)
            result.append([group_start, current_index - 1])
        
        # Move to the next group (current_index already points to next different character)
    
    return result
    # Time: O(n)
    # Space: O(1)

# Source: https://leetcode.com/problems/positions-of-large-groups/solutions/618672/python-two-pointer-o-n-time-complexity-in-top-92
# Credit: John Howard -> https://leetcode.com/u/leeik/
def large_group_positions_alt(s):
    left = 0 
    return_list = []
    s += '1'
    for index, letter in enumerate(s):
        if letter != s[left]:
            if index - left >= 3:
                return_list.append([left, index - 1])
            left = index
    return return_list
    # Time: O(n)
    # Space: O(n)


def main():
    result = large_group_positions(s = "abbxxxxzzy")
    print(result) # [[3,6]]

    result = large_group_positions(s = "abc")
    print(result) # []

    result = large_group_positions(s = "abcdddeeeeaabbbcd")
    print(result) # [[3,5],[6,9],[12,14]]

if __name__ == "__main__":
    main()
