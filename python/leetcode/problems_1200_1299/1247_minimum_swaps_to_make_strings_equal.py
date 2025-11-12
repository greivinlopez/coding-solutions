# -----------------------------------------
# 1247. Minimum Swaps to Make Strings Equal
# -----------------------------------------

# Problem: https://leetcode.com/problems/minimum-swaps-to-make-strings-equal
#
# You are given two strings s1 and s2 of equal length consisting of letters "x"
# and "y" only. Your task is to make these two strings equal to each other. You
# can swap any two characters that belong to different strings, which means: swap
# s1[i] and s2[j].
# 
# Return the minimum number of swaps required to make s1 and s2 equal, or return
# -1 if it is impossible to do so.
# 
# Example 1:
# 
# Input: s1 = "xx", s2 = "yy"
# Output: 1
# 
# Explanation: Swap s1[0] and s2[1], s1 = "yx", s2 = "yx".
# 
# Example 2:
# 
# Input: s1 = "xy", s2 = "yx"
# Output: 2
# 
# Explanation: Swap s1[0] and s2[0], s1 = "yy", s2 = "xx".
# Swap s1[0] and s2[1], s1 = "xy", s2 = "xy".
# Note that you cannot swap s1[0] and s1[1] to make s1 equal to "yx", cause we can
# only swap chars in different strings.
# 
# Example 3:
# 
# Input: s1 = "xx", s2 = "xy"
# Output: -1
# 
# 
# Constraints:
#         1 <= s1.length, s2.length <= 1000
#         s1.length == s2.length
#         s1, s2 only contain 'x' or 'y'.


# Solution: https://algo.monster/liteproblems/1247
# Credit: AlgoMonster
def minimum_swap(s1, s2):
    # Count mismatches where s1[i] = 'x' and s2[i] = 'y'
    x_y_mismatch_count = 0
    # Count mismatches where s1[i] = 'y' and s2[i] = 'x'
    y_x_mismatch_count = 0
    
    # Iterate through both strings simultaneously
    for char1, char2 in zip(s1, s2):
        # When char1 is 'x' and char2 is 'y' (since 'x' < 'y')
        x_y_mismatch_count += char1 < char2
        # When char1 is 'y' and char2 is 'x' (since 'y' > 'x')
        y_x_mismatch_count += char1 > char2
    
    # If total mismatches is odd, it's impossible to make strings equal
    if (x_y_mismatch_count + y_x_mismatch_count) % 2:
        return -1
    
    # Calculate minimum swaps needed:
    # - Each pair of same type mismatches needs 1 swap (xy-xy or yx-yx)
    # - Remaining unpaired mismatches (one xy and one yx) need 2 swaps
    return (x_y_mismatch_count // 2 + 
            y_x_mismatch_count // 2 + 
            x_y_mismatch_count % 2 + 
            y_x_mismatch_count % 2)
    # Time: O(n)
    # Space: O(1)


def main():
    result = minimum_swap(s1 = "xx", s2 = "yy")
    print(result) # 1

    result = minimum_swap(s1 = "xy", s2 = "yx")
    print(result) # 2

    result = minimum_swap(s1 = "xx", s2 = "xy")
    print(result) # -1

if __name__ == "__main__":
    main()
