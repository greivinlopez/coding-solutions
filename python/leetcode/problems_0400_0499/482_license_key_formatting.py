# ------------------------------
# 482. License Key Formatting 🔑
# ------------------------------

# Problem: https://leetcode.com/problems/license-key-formatting
#
# You are given a license key represented as a string s that consists of only
# alphanumeric characters and dashes. The string is separated into n + 1 groups by
# n dashes. You are also given an integer k.
# 
# We want to reformat the string s such that each group contains exactly k
# characters, except for the first group, which could be shorter than k but still
# must contain at least one character. Furthermore, there must be a dash inserted
# between two groups, and you should convert all lowercase letters to uppercase.
# 
# Return the reformatted license key.
# 
# Example 1:
# Input: s = "5F3Z-2e-9-w", k = 4
# Output: "5F3Z-2E9W"
# 
# Explanation: The string s has been split into two parts, each part has 4
# characters.
# Note that the two extra dashes are not needed and can be removed.
# 
# Example 2:
# 
# Input: s = "2-5g-3-J", k = 2
# Output: "2-5G-3J"
# 
# Explanation: The string s has been split into three parts, each part has 2
# characters except the first part as it could be shorter as mentioned above.
# 
# 
# Constraints:
#         1 <= s.length <= 10⁵
#         s consists of English letters, digits, and dashes '-'.
#         1 <= k <= 10⁴


# Solution: https://algo.monster/liteproblems/482
# Credit: AlgoMonster
def license_key_formatting(s, k):
    # Calculate total length and number of non-dash characters
    total_length = len(s)
    dash_count = s.count("-")
    char_count = total_length - dash_count
    
    # Determine the size of the first group
    # If char_count % k == 0, first group has k characters
    # Otherwise, first group has (char_count % k) characters
    first_group_size = char_count % k
    if first_group_size == 0:
        first_group_size = k
    
    # Build the result string
    result = []
    current_group_count = first_group_size
    
    for index, character in enumerate(s):
        # Skip dash characters from the original string
        if character == "-":
            continue
        
        # Add the uppercase version of the character
        result.append(character.upper())
        current_group_count -= 1
        
        # Check if we've completed a group
        if current_group_count == 0:
            # Reset counter for the next group
            current_group_count = k
            
            # Add dash separator if not at the end
            if index != total_length - 1:
                result.append("-")
    
    # Join the result and remove any trailing dash
    # (in case the last character in original string was a dash)
    return "".join(result).rstrip("-")
    # Time: O(n)
    # Space: O(n)


def main():
    result = license_key_formatting(s = "5F3Z-2e-9-w", k = 4)
    print(result) # "5F3Z-2E9W"

    result = license_key_formatting(s = "2-5g-3-J", k = 2)
    print(result) # "2-5G-3J"

if __name__ == "__main__":
    main()
