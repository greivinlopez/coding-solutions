# -------------------------------
# 717. 1-bit and 2-bit Characters
# -------------------------------

# Problem: https://leetcode.com/problems/1-bit-and-2-bit-characters
#
# We have two special characters:
#         
#   * The first character can be represented by one bit 0.
#   * The second character can be represented by two bits (10 or 11).
# 
# Given a binary array bits that ends with 0, return true if the last character
# must be a one-bit character.
# 
# Example 1:
# 
# Input: bits = [1,0,0]
# Output: true
# 
# Explanation: The only way to decode it is two-bit character and one-bit
# character.
# So the last character is one-bit character.
# 
# Example 2:
# 
# Input: bits = [1,1,1,0]
# Output: false
# 
# Explanation: The only way to decode it is two-bit character and two-bit
# character.
# So the last character is not one-bit character.
# 
# 
# Constraints:
#         1 <= bits.length <= 1000
#         bits[i] is either 0 or 1.


# Credit: Jaweria Batool -> https://github.com/Jaweria-B
def is_one_bit_character(bits):
    if len(bits) == 1:
        return True
    
    i = 0
    while i < len(bits):            
        if bits[i] == 1:
            i += 2  
        else:
            i += 1
            
        if i == len(bits)-1:
            return True
    
    return False
    # Time: O(n)
    # Space: O(1)


def main():
    result = is_one_bit_character(bits = [1,0,0])
    print(result) # True

    result = is_one_bit_character(bits = [1,1,1,0])
    print(result) # False

if __name__ == "__main__":
    main()
