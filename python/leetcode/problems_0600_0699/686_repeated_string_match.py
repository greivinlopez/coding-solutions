# --------------------------
# 686. Repeated String Match
# --------------------------

# Problem: https://leetcode.com/problems/repeated-string-match
#
# Given two strings a and b, return the minimum number of times you should repeat
# string a so that string b is a substring of it. If it is impossible for b​​​​​​
# to be a substring of a after repeating it, return -1.
# 
# Notice: string "abc" repeated 0 times is "", repeated 1 time is "abc" and
# repeated 2 times is "abcabc".
# 
# Example 1:
# 
# Input: a = "abcd", b = "cdabcdab"
# Output: 3
# 
# Explanation: We return 3 because by repeating a three times "abcdabcdabcd", b is
# a substring of it.
# 
# Example 2:
# 
# Input: a = "a", b = "aa"
# Output: 2
# 
# 
# Constraints:
#         1 <= a.length, b.length <= 10⁴
#         a and b consist of lowercase English letters.

from math import ceil

# Solution: https://algo.monster/liteproblems/686
# Credit: AlgoMonster
def repeated_string_match_alt(a, b):
    # Get lengths of both strings
    len_a, len_b = len(a), len(b)
    
    # Calculate minimum number of repetitions needed
    # This is the theoretical minimum based on lengths
    min_repetitions = ceil(len_b / len_a)
    
    # Build initial repeated string with minimum repetitions
    repeated_string_list = [a] * min_repetitions
    
    # Check if b is a substring, trying up to 3 additional repetitions
    # This handles edge cases where b might start/end in the middle of a
    for _ in range(3):
        # Join the list to form the repeated string and check if b is a substring
        repeated_string = ''.join(repeated_string_list)
        if b in repeated_string:
            return min_repetitions
        
        # If not found, add one more repetition and try again
        min_repetitions += 1
        repeated_string_list.append(a)
    
    # If b is not found after trying additional repetitions, return -1
    return -1
    # Time: O(n * (n + m))
    # Space: O(n + m)

# Solution: https://leetcode.com/problems/repeated-string-match/solutions/108090/intuitive-python-2-liner
def repeated_string_match(a, b):
    times = -(-len(b) // len(a)) # Equal to ceil(len(b) / len(a))
    for i in range(2):
        if b in (a * (times + i)):
            return times + i
    return -1
    # Time: O(n + m)
    # Space: O(n + m)


def main():
    result = repeated_string_match(a = "abcd", b = "cdabcdab")
    print(result) # True

    result = repeated_string_match(a = "a", b = "aa")
    print(result) # True

if __name__ == "__main__":
    main()
