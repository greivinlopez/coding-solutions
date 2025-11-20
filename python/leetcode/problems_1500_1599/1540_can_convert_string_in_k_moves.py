# -----------------------------------
# 1540. Can Convert String in K Moves
# -----------------------------------

# Problem: https://leetcode.com/problems/can-convert-string-in-k-moves
#
# Given two strings s and t, your goal is to convert s into t in k moves or less.
# 
# During the iᵗʰ (1 <= i <= k) move you can:
#         
#   * Choose any index j (1-indexed) from s, such that 1 <= j <= s.length and
#     j has not been chosen in any previous move, and shift the character at that
#     index i times.
#   * Do nothing.
# 
# Shifting a character means replacing it by the next letter in the
# alphabet (wrapping around so that 'z' becomes 'a'). Shifting a character
# by i means applying the shift operations i times.
# 
# Remember that any index j can be picked at most once.
# 
# Return true if it's possible to convert s into t in no more than k moves,
# otherwise return false.
# 
# Example 1:
# 
# Input: s = "input", t = "ouput", k = 9
# Output: true
# 
# Explanation: In the 6th move, we shift 'i' 6 times to get 'o'. And in the 7th
# move we shift 'n' to get 'u'.
# 
# Example 2:
# 
# Input: s = "abc", t = "bcd", k = 10
# Output: false
# 
# Explanation: We need to shift each character in s one time to convert it into t.
# We can shift 'a' to 'b' during the 1st move. However, there is no way to shift
# the other characters in the remaining moves to obtain t from s.
# 
# Example 3:
# 
# Input: s = "aab", t = "bbb", k = 27
# Output: true
# 
# Explanation: In the 1st move, we shift the first 'a' 1 time to get 'b'. In the
# 27th move, we shift the second 'a' 27 times to get 'b'.
# 
# 
# Constraints:
#         1 <= s.length, t.length <= 10⁵
#         0 <= k <= 10⁹
#         s, t contain only lowercase English letters.


# Solution: https://algo.monster/liteproblems/1540
# Credit: AlgoMonster
def can_convert_string(s, t, k):
    # If strings have different lengths, conversion is impossible
    if len(s) != len(t):
        return False
    
    # Array to count the frequency of each shift distance (0-25)
    shift_count = [0] * 26
    
    # Calculate the shift distance needed for each character pair
    for char_s, char_t in zip(s, t):
        # Calculate circular shift distance from char_s to char_t
        # Adding 26 ensures positive result before modulo
        shift_distance = (ord(char_t) - ord(char_s) + 26) % 26
        shift_count[shift_distance] += 1
    
    # Check if all required shifts can be performed within k moves
    for shift in range(1, 26):
        # For each shift distance, if we need it multiple times,
        # we must use moves: shift, shift+26, shift+52, etc.
        # The last move for this shift would be: shift + 26*(count-1)
        max_move_for_shift = shift + 26 * (shift_count[shift] - 1)
        if max_move_for_shift > k:
            return False
    
    return True
    # Time: O(n)
    # Space: O(1)


def main():
    result = can_convert_string(s = "input", t = "ouput", k = 9)
    print(result) # True

    result = can_convert_string(s = "abc", t = "bcd", k = 10)
    print(result) # False

    result = can_convert_string(s = "aab", t = "bbb", k = 27)
    print(result) # True

if __name__ == "__main__":
    main()
