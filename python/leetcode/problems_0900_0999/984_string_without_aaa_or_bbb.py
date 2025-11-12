# ------------------------------
# 984. String Without AAA or BBB
# ------------------------------

# Problem: https://leetcode.com/problems/string-without-aaa-or-bbb
#
# Given two integers a and b, return any string s such that:
#         
#   * s has length a + b and contains exactly a 'a' letters, and exactly b 'b'
#     letters,
#   * The substring 'aaa' does not occur in s, and
#   * The substring 'bbb' does not occur in s.
# 
# Example 1:
# 
# Input: a = 1, b = 2
# Output: "abb"
# 
# Explanation: "abb", "bab" and "bba" are all correct answers.
# 
# Example 2:
# 
# Input: a = 4, b = 1
# Output: "aabaa"
# 
# 
# Constraints:
#         0 <= a, b <= 100
#         It is guaranteed such an s exists for the given a and b.


# Solution: https://algo.monster/liteproblems/984
# Credit: AlgoMonster
def str_without_3a_3b(a, b):
    result = []
    
    # Process while we have both 'a' and 'b' characters remaining
    while a > 0 and b > 0:
        if a > b:
            # When we have more 'a's, use pattern 'aab' to consume more 'a's
            result.append('aab')
            a -= 2
            b -= 1
        elif a < b:
            # When we have more 'b's, use pattern 'bba' to consume more 'b's
            result.append('bba')
            a -= 1
            b -= 2
        else:
            # When counts are equal, use simple alternating pattern 'ab'
            result.append('ab')
            a -= 1
            b -= 1
    
    # Append any remaining 'a' characters (will be at most 2)
    if a > 0:
        result.append('a' * a)
    
    # Append any remaining 'b' characters (will be at most 2)
    if b > 0:
        result.append('b' * b)
    
    # Join all parts into final string
    return ''.join(result)
    # Time: O(a + b)
    # Space: O(a + b)


def main():
    result = str_without_3a_3b(a = 1, b = 2)
    print(result) # "abb"

    result = str_without_3a_3b(a = 4, b = 1)
    print(result) # "aabaa"

if __name__ == "__main__":
    main()
