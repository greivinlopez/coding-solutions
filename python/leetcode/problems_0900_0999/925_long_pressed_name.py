# ----------------------
# 925. Long Pressed Name
# ----------------------

# Problem: https://leetcode.com/problems/long-pressed-name
#
# Your friend is typing his name into a keyboard. Sometimes, when typing a
# character c, the key might get long pressed, and the character will be typed 1
# or more times.
# 
# You examine the typed characters of the keyboard. Return True if it is possible
# that it was your friends name, with some characters (possibly none) being long
# pressed.
# 
# Example 1:
# 
# Input: name = "alex", typed = "aaleex"
# Output: true
# 
# Explanation: 'a' and 'e' in 'alex' were long pressed.
# 
# Example 2:
# 
# Input: name = "saeed", typed = "ssaaedd"
# Output: false
# 
# Explanation: 'e' must have been pressed twice, but it was not in the typed
# output.
# 
# 
# Constraints:
#         1 <= name.length, typed.length <= 1000
#         name and typed consist of only lowercase English letters.


# Solution: https://algo.monster/liteproblems/925
# Credit: AlgoMonster
def is_long_pressed_name(name, typed):
    name_length = len(name)
    typed_length = len(typed)
    
    # Initialize pointers for both strings
    name_index = 0
    typed_index = 0
    
    # Process both strings simultaneously
    while name_index < name_length and typed_index < typed_length:
        # Characters must match at current positions
        if name[name_index] != typed[typed_index]:
            return False
        
        # Count consecutive occurrences of current character in name
        next_name_index = name_index + 1
        while next_name_index < name_length and name[next_name_index] == name[name_index]:
            next_name_index += 1
        
        # Count consecutive occurrences of current character in typed
        next_typed_index = typed_index + 1
        while next_typed_index < typed_length and typed[next_typed_index] == typed[typed_index]:
            next_typed_index += 1
        
        # Calculate the count of current character in both strings
        name_char_count = next_name_index - name_index
        typed_char_count = next_typed_index - typed_index
        
        # Typed must have at least as many occurrences as name (can have more due to long press)
        if name_char_count > typed_char_count:
            return False
        
        # Move pointers to the next different character
        name_index = next_name_index
        typed_index = next_typed_index
    
    # Both strings must be fully processed
    return name_index == name_length and typed_index == typed_length
    # Time: O(m + n)
    # Space: O(1)


def main():
    result = is_long_pressed_name(name = "alex", typed = "aaleex")
    print(result) # True

    result = is_long_pressed_name(name = "saeed", typed = "ssaaedd")
    print(result) # False

if __name__ == "__main__":
    main()
