# -------------------------
# 2381. Shifting Letters II
# -------------------------

# Problem: https://leetcode.com/problems/shifting-letters-ii/
#
# You are given a string s of lowercase English letters and a 2D integer array 
# shifts where shifts[i] = [starti, endi, directioni]. For every i, shift the 
# characters in s from the index starti to the index endi (inclusive) forward 
# if directioni = 1, or shift the characters backward if directioni = 0.
# 
# Shifting a character forward means replacing it with the next letter in the 
# alphabet (wrapping around so that 'z' becomes 'a'). Similarly, shifting a 
# character backward means replacing it with the previous letter in the alphabet 
# (wrapping around so that 'a' becomes 'z').
# 
# Return the final string after all such shifts to s are applied.
#  
# 
# Example 1:
# 
# Input: s = "abc", shifts = [[0,1,0],[1,2,1],[0,2,1]]
# Output: "ace"
# Explanation: Firstly, shift the characters from index 0 to index 1 backward. Now s = "zac".
# Secondly, shift the characters from index 1 to index 2 forward. Now s = "zbd".
# Finally, shift the characters from index 0 to index 2 forward. Now s = "ace".
# 
# Example 2:
# 
# Input: s = "dztz", shifts = [[0,0,0],[1,1,1]]
# Output: "catz"
# Explanation: Firstly, shift the characters from index 0 to index 0 backward. Now s = "cztz".
# Finally, shift the characters from index 1 to index 1 forward. Now s = "catz".
#  
# 
# Constraints:
# 
#   1 <= s.length, shifts.length <= 5 * 10^4
#   shifts[i].length == 3
#   0 <= starti <= endi < s.length
#   0 <= directioni <= 1
#   s consists of lowercase English letters.


# Solution: https://youtu.be/eEUjVY7wK3k
# Credit: Navdeep Singh founder of NeetCode
def shifting_letters(s, shifts):
    prefix_diff = [0] * (len(s) + 1)

    for left, right, d in shifts:
        prefix_diff[right + 1] += 1 if d else -1
        prefix_diff[left] += -1 if d else 1

    diff = 0
    res = [ord(c) - ord('a') for c in s]

    for i in reversed(range(len(prefix_diff))):
        diff += prefix_diff[i]
        res [i - 1] = (diff + res[i - 1] + 26) % 26

    s = [chr(ord('a') + n) for n in res]
    return ''.join(s)


def main():
    result = shifting_letters(s = "abc", shifts = [[0,1,0],[1,2,1],[0,2,1]])
    print(result) # "ace"

    result = shifting_letters(s = "dztz", shifts = [[0,0,0],[1,1,1]])
    print(result) # "catz"

if __name__ == "__main__":
    main()
