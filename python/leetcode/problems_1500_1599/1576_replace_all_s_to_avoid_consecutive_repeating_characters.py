# ---------------------------------------------------------------
# 1576. Replace All ?'s to Avoid Consecutive Repeating Characters
# ---------------------------------------------------------------

# Problem: https://leetcode.com/problems/replace-all-s-to-avoid-consecutive-repeating-characters
#
# Given a string s containing only lowercase English letters and the '?'
# character, convert all the '?' characters into lowercase letters such that the
# final string does not contain any consecutive repeating characters. You cannot
# modify the non '?' characters.
# 
# It is guaranteed that there are no consecutive repeating characters in the given
# string except for '?'.
# 
# Return the final string after all the conversions (possibly zero) have been
# made. If there is more than one solution, return any of them. It can be shown
# that an answer is always possible with the given constraints.
# 
# Example 1:
# 
# Input: s = "?zs"
# Output: "azs"
# 
# Explanation: There are 25 solutions for this problem. From "azs" to "yzs", all
# are valid. Only "z" is an invalid modification as the string will consist of
# consecutive repeating characters in "zzs".
# 
# Example 2:
# 
# Input: s = "ubv?w"
# Output: "ubvaw"
# 
# Explanation: There are 24 solutions for this problem. Only "v" and "w" are
# invalid modifications as the strings will consist of consecutive repeating
# characters in "ubvvw" and "ubvww".
# 
# 
# Constraints:
#         1 <= s.length <= 100
#         s consist of lowercase English letters and '?'.


# Solution: https://algo.monster/liteproblems/1576
# Credit: AlgoMonster
def modify_string(s):
    # Convert string to list for in-place modification
    char_list = list(s)
    n = len(char_list)
    
    # Iterate through each character in the string
    for i in range(n):
        # Check if current character is a question mark
        if char_list[i] == "?":
            # Try each character from 'a', 'b', 'c'
            for replacement_char in "abc":
                # Check if the replacement character conflicts with neighbors
                has_left_conflict = (i > 0 and char_list[i - 1] == replacement_char)
                has_right_conflict = (i + 1 < n and char_list[i + 1] == replacement_char)
                
                # Skip this character if it matches either neighbor
                if has_left_conflict or has_right_conflict:
                    continue
                
                # Valid character found, replace the '?' and break
                char_list[i] = replacement_char
                break
    
    # Convert list back to string and return
    return "".join(char_list)
    # Time: O(n)
    # Space: O(n)


def main():
    result = modify_string(s = "?zs")
    print(result) # "azs"

    result = modify_string(s = "ubv?w")
    print(result) # "ubvaw"

if __name__ == "__main__":
    main()
