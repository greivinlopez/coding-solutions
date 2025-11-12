# ----------------------------
# 420. Strong Password Checker
# ----------------------------

# Problem: https://leetcode.com/problems/strong-password-checker
#
# A password is considered strong if the below conditions are all met:    
#   * It has at least 6 characters and at most 20 characters.
#   * It contains at least one lowercase letter, at least one uppercase letter, 
#     and at least one digit.
#   * It does not contain three repeating characters in a row (i.e., "Baaabb0"
#     is weak, but "Baaba0" is strong).
# 
# Given a string password, return the minimum number of steps required to make
# password strong. if password is already strong, return 0.
# 
# In one step, you can:
#         Insert one character to password,
#         Delete one character from password, or
#         Replace one character of password with another character.
# 
# Example 1:
# 
# Input: password = "a"
# Output: 5
# 
# Example 2:
# 
# Input: password = "aA1"
# Output: 3
# 
# Example 3:
# 
# Input: password = "1337C0d3"
# Output: 0
# 
# 
# Constraints:
#         1 <= password.length <= 50
#         password consists of letters, digits, dot '.' or exclamation mark '!'.


# Solution: https://algo.monster/liteproblems/420
# Credit: AlgoMonster
def strong_password_checker(password):
    def count_character_types(s):
        has_lower = has_upper = has_digit = 0
        
        for char in s:
            if char.islower():
                has_lower = 1
            elif char.isupper():
                has_upper = 1
            elif char.isdigit():
                has_digit = 1
        
        return has_lower + has_upper + has_digit
    
    # Count existing character types and get password length
    existing_types = count_character_types(password)
    password_length = len(password)
    
    # Case 1: Password is too short (less than 6 characters)
    if password_length < 6:
        # Need to add characters to reach 6, and ensure we have all 3 types
        chars_to_add = 6 - password_length
        types_to_add = 3 - existing_types
        return max(chars_to_add, types_to_add)
    
    # Case 2: Password length is acceptable (6-20 characters)
    if password_length <= 20:
        # Count replacements needed to break sequences of 3+ repeating characters
        replacements_needed = 0
        consecutive_count = 1
        previous_char = '~'  # Use a non-password character as initial value
        
        for current_char in password:
            if current_char == previous_char:
                consecutive_count += 1
            else:
                # For every 3 consecutive chars, we need 1 replacement
                replacements_needed += consecutive_count // 3
                consecutive_count = 1
                previous_char = current_char
        
        # Don't forget the last sequence
        replacements_needed += consecutive_count // 3
        
        # Need to fix both repeating sequences and missing character types
        types_to_add = 3 - existing_types
        return max(replacements_needed, types_to_add)
    
    # Case 3: Password is too long (more than 20 characters)
    # Strategy: Remove excess characters optimally to minimize replacements
    
    replacements_needed = 0
    consecutive_count = 1
    chars_to_remove = password_length - 20
    
    # Track sequences with remainder 1 when divided by 3
    # These are priority for using 2-char removals
    sequences_with_remainder_1 = 0
    
    previous_char = '~'
    
    for current_char in password:
        if current_char == previous_char:
            consecutive_count += 1
        else:
            if chars_to_remove > 0 and consecutive_count >= 3:
                # Sequences divisible by 3: removing 1 char saves 1 replacement
                if consecutive_count % 3 == 0:
                    chars_to_remove -= 1
                    replacements_needed -= 1
                # Sequences with remainder 1: good candidates for 2-char removal
                elif consecutive_count % 3 == 1:
                    sequences_with_remainder_1 += 1
            
            replacements_needed += consecutive_count // 3
            consecutive_count = 1
            previous_char = current_char
    
    # Process the last sequence
    if chars_to_remove > 0 and consecutive_count >= 3:
        if consecutive_count % 3 == 0:
            chars_to_remove -= 1
            replacements_needed -= 1
        elif consecutive_count % 3 == 1:
            sequences_with_remainder_1 += 1
    
    replacements_needed += consecutive_count // 3
    
    # Use remaining removals optimally
    # Priority 1: Remove 2 chars from sequences with remainder 1
    two_char_removals = min(replacements_needed, sequences_with_remainder_1, chars_to_remove // 2)
    replacements_needed -= two_char_removals
    chars_to_remove -= two_char_removals * 2
    
    # Priority 2: Remove 3 chars to eliminate entire replacement needs
    three_char_removals = min(replacements_needed, chars_to_remove // 3)
    replacements_needed -= three_char_removals
    chars_to_remove -= three_char_removals * 3
    
    # Total operations = deletions + max(remaining replacements, missing types)
    types_to_add = 3 - existing_types
    return (password_length - 20) + max(replacements_needed, types_to_add)
    # Time: O(n)
    # Space: O(1)


def main():
    result = strong_password_checker("a")
    print(result) # 5

    result = strong_password_checker("aA1")
    print(result) # 3

    result = strong_password_checker("1337C0d3")
    print(result) # 0

if __name__ == "__main__":
    main()
