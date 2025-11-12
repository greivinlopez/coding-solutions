# -----------------------------------
# 434. Number of Segments in a String
# -----------------------------------

# Problem: https://leetcode.com/problems/number-of-segments-in-a-string
#
# Given a string s, return the number of segments in the string.
# 
# A segment is defined to be a contiguous sequence of non-space characters.
# 
# Example 1:
# 
# Input: s = "Hello, my name is John"
# Output: 5
# 
# Explanation: The five segments are ["Hello,", "my", "name", "is", "John"]
# 
# Example 2:
# 
# Input: s = "Hello"
# Output: 1
# 
# Constraints:
#   0 <= s.length <= 300
#   s consists of lowercase and uppercase English letters, digits, or one of the 
#     following characters "!@#$%^&*()_+-=',.:".
#   The only space character in s is ' '.


# Solution: https://leetcode.com/problems/number-of-segments-in-a-string/solutions/91619/Python-One-liner-without-split
def count_segments(s):
    return sum(s[i] != ' ' and (i == 0 or s[i-1] == ' ') for i in range(len(s)))

# Solution: https://algo.monster/liteproblems/434
# Credit: AlgoMonster
def count_segments_alt(s):
    count = 0
    in_segment = False
  
    for char in s:
        if char != ' ':
            if not in_segment:
                count += 1
                in_segment = True
        else:
            in_segment = False
  
    return count


def main():
    result = count_segments(s = "Hello, my name is John")
    print(result) # 5

    result = count_segments(s = "Hello")
    print(result) # 1

if __name__ == "__main__":
    main()
