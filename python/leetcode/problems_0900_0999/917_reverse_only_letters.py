# -------------------------
# 917. Reverse Only Letters
# -------------------------

# Problem: https://leetcode.com/problems/reverse-only-letters
#
# Given a string s, reverse the string according to the following rules:
#         
#   * All the characters that are not English letters remain in the same
#     position.
#   * All the English letters (lowercase or uppercase) should be reversed.
# 
# Return s after reversing it.
# 
# Example 1:
# 
# Input: s = "ab-cd"
# Output: "dc-ba"
# 
# Example 2:
# 
# Input: s = "a-bC-dEf-ghIj"
# Output: "j-Ih-gfE-dCba"
# 
# Example 3:
# 
# Input: s = "Test1ng-Leet=code-Q!"
# Output: "Qedo1ct-eeLg=ntse-T!"
# 
# 
# Constraints:
#         1 <= s.length <= 100
#         s consists of characters with ASCII values in the range [33, 122].
#         s does not contain '\"' or '\\'.


# Solution: https://algo.monster/liteproblems/917
# Credit: AlgoMonster
def reverse_only_letters(s):
    # Convert string to list for in-place character swapping
    char_list = list(s)
    
    # Initialize two pointers at the start and end of the list
    left = 0
    right = len(char_list) - 1
    
    # Process until the two pointers meet
    while left < right:
        # Move left pointer forward until we find an alphabetic character
        while left < right and not char_list[left].isalpha():
            left += 1
        
        # Move right pointer backward until we find an alphabetic character
        while left < right and not char_list[right].isalpha():
            right -= 1
        
        # If both pointers are at alphabetic characters, swap them
        if left < right:
            char_list[left], char_list[right] = char_list[right], char_list[left]
            left += 1
            right -= 1
    
    # Convert the list back to string and return
    return "".join(char_list)
    # Time: O(n)
    # Space: O(n)


def main():
    result = reverse_only_letters(s = "ab-cd")
    print(result) # "dc-ba"

    result = reverse_only_letters(s = "a-bC-dEf-ghIj")
    print(result) # "j-Ih-gfE-dCba"

    result = reverse_only_letters(s = "Test1ng-Leet=code-Q!")
    print(result) # "Qedo1ct-eeLg=ntse-T!"

if __name__ == "__main__":
    main()
