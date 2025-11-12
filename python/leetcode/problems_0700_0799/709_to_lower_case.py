# ------------------
# 709. To Lower Case
# ------------------

# Problem: https://leetcode.com/problems/to-lower-case
#
# Given a string s, return the string after replacing every uppercase letter with
# the same lowercase letter.
# 
# Example 1:
# 
# Input: s = "Hello"
# Output: "hello"
# 
# Example 2:
# 
# Input: s = "here"
# Output: "here"
# 
# Example 3:
# 
# Input: s = "LOVELY"
# Output: "lovely"
# 
# 
# Constraints:
#         1 <= s.length <= 100
#         s consists of printable ASCII characters.


# Solution: https://leetcode.com/problems/to-lower-case/
# Credit: AlgoMonster
def to_lower_case(s):
    # Build the result by iterating through each character
    result = []
    
    for char in s:
        if char.isupper():
            # Convert uppercase to lowercase using bitwise OR with 32
            # ASCII difference between uppercase and lowercase is 32
            # Setting the 6th bit (32 = 0b100000) converts upper to lower
            lowercase_char = chr(ord(char) | 32)
            result.append(lowercase_char)
        else:
            # Keep non-uppercase characters unchanged
            result.append(char)
    
    # Join all characters to form the final string
    return "".join(result)
    # Time: O(n)
    # Space: O(n)


def main():
    result = to_lower_case(s = "Hello")
    print(result) # "hello"

    result = to_lower_case(s = "here")
    print(result) # "here"

    result = to_lower_case(s = "LOVELY")
    print(result) # "lovely"

if __name__ == "__main__":
    main()
