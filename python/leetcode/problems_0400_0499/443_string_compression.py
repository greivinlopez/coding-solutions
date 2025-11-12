# -----------------------
# 443. String Compression
# -----------------------

# Problem: https://leetcode.com/problems/string-compression
#
# Given an array of characters chars, compress it using the following algorithm:
# 
# Begin with an empty string s. For each group of consecutive repeating characters
# in chars:
# 
#   * If the group's length is 1, append the character to s.
#   * Otherwise, append the character followed by the group's length.
# 
# The compressed string s should not be returned separately, but instead, be
# stored in the input character array chars. Note that group lengths that are 10
# or longer will be split into multiple characters in chars.
# 
# After you are done modifying the input array, return the new length of the
# array.
# 
# You must write an algorithm that uses only constant extra space.
# 
# Note: The characters in the array beyond the returned length do not matter and
# should be ignored.
# 
# Example 1:
# 
# Input: chars = ["a","a","b","b","c","c","c"]
# Output: Return 6, and the first 6 characters of the input array should be:
# ["a","2","b","2","c","3"]
# 
# Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
# 
# Example 2:
# 
# Input: chars = ["a"]
# Output: Return 1, and the first character of the input array should be: ["a"]
# 
# Explanation: The only group is "a", which remains uncompressed since it's a
# single character.
# 
# Example 3:
# 
# Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
# Output: Return 4, and the first 4 characters of the input array should be:
# ["a","b","1","2"].
# 
# Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".
# 
# Constraints:
#   1 <= chars.length <= 2000
#   chars[i] is a lowercase English letter, uppercase English letter, digit, 
#    or symbol.


# Solution: https://algo.monster/liteproblems/443
# Credit: AlgoMonster
def compress(chars):
    # Initialize pointers and get array length
    read_index = 0  # Pointer to read characters
    write_index = 0  # Pointer to write compressed result
    array_length = len(chars)
    
    # Process all characters in the array
    while read_index < array_length:
        # Find the end of the current character group
        group_end = read_index + 1
        while group_end < array_length and chars[group_end] == chars[read_index]:
            group_end += 1
        
        # Write the character to the compressed position
        chars[write_index] = chars[read_index]
        write_index += 1
        
        # Calculate the count of consecutive characters
        count = group_end - read_index
        
        # If count > 1, write the count digits
        if count > 1:
            count_str = str(count)
            for digit in count_str:
                chars[write_index] = digit
                write_index += 1
        
        # Move to the next group of characters
        read_index = group_end
    
    # Return the length of the compressed array
    return write_index
    # Time: O(n)
    # Space: O(1)


def main():
    result = compress(["a","a","b","b","c","c","c"])
    print(result) # 6

    result = compress(["a"])
    print(result) # 1

    result = compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"])
    print(result) # 4

if __name__ == "__main__":
    main()
