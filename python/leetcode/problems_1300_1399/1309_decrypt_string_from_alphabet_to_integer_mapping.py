# -----------------------------------------------------
# 1309. Decrypt String from Alphabet to Integer Mapping
# -----------------------------------------------------

# Problem: https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping
#
# You are given a string s formed by digits and '#'. We want to map s to English
# lowercase characters as follows:
#         
#   * Characters ('a' to 'i') are represented by ('1' to '9') respectively.
#   * Characters ('j' to 'z') are represented by ('10#' to '26#') respectively.
# 
# Return the string formed after mapping.
# 
# The test cases are generated so that a unique mapping will always exist.
# 
# Example 1:
# 
# Input: s = "10#11#12"
# Output: "jkab"
# 
# Explanation: "j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".
# 
# Example 2:
# 
# Input: s = "1326#"
# Output: "acz"
# 
# 
# Constraints:
#         1 <= s.length <= 1000
#         s consists of digits and the '#' letter.
#         s will be a valid string such that mapping is always possible.


# Solution: https://algo.monster/liteproblems/1309
# Credit: AlgoMonster
def freq_alphabets(s):
    result = []
    index = 0
    string_length = len(s)
    
    # Traverse the string from left to right
    while index < string_length:
        # Check if current position forms a two-digit number with '#'
        # (represents letters 'j' through 'z')
        if index + 2 < string_length and s[index + 2] == '#':
            # Extract two-digit number and convert to corresponding letter
            two_digit_num = int(s[index:index + 2])
            # Convert number to letter (10 -> 'j', 11 -> 'k', etc.)
            letter = chr(two_digit_num + ord('a') - 1)
            result.append(letter)
            # Move index past the two digits and '#'
            index += 3
        else:
            # Single digit number (represents letters 'a' through 'i')
            single_digit_num = int(s[index])
            # Convert number to letter (1 -> 'a', 2 -> 'b', etc.)
            letter = chr(single_digit_num + ord('a') - 1)
            result.append(letter)
            # Move to next character
            index += 1
    
    # Join all decoded letters into final string
    return ''.join(result)
    # Time: O(n)
    # Space: O(n)

# Solution: https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/solutions/470770/python-3-two-lines-beats-100-16-ms-with-0h636
# Credit: Junaid Mansuri -> https://leetcode.com/u/junaidmansuri/
def freq_alphabets_short(s):
    for i in range(26, 0, -1): 
        s = s.replace(str(i) + '#' * (i > 9), chr(96 + i))
    return s
    # Time: O(n)
    # Space: O(n)


def main():
    result = freq_alphabets(s = "10#11#12")
    print(result) # "jkab"

    result = freq_alphabets(s = "1326#")
    print(result) # "acz"

if __name__ == "__main__":
    main()
