# ----------------------------------------------------------
# 1320. Minimum Distance to Type a Word Using Two Fingers ⌨️
# ----------------------------------------------------------

# Problem: https://leetcode.com/problems/minimum-distance-to-type-a-word-using-two-fingers
#
# https://assets.leetcode.com/uploads/2020/01/02/leetcode_keyboard.png
# 
# You have a keyboard layout as shown above in the X-Y plane, where each English
# uppercase letter is located at some coordinate.
#         
#   * For example, the letter 'A' is located at coordinate (0, 0), the letter
#     'B' is located at coordinate (0, 1), the letter 'P' is located at coordinate 
#     (2, 3) and the letter 'Z' is located at coordinate (4, 1).
# 
# Given the string word, return the minimum total distance to type such string
# using only two fingers.
# 
# The distance between coordinates (x₁, y₁) and (x₂, y₂) is |x₁ - x₂| + |y₁ - y₂|.
# 
# Note that the initial positions of your two fingers are considered free so do
# not count towards your total distance, also your two fingers do not have to
# start at the first letter or the first two letters.
# 
# Example 1:
# 
# Input: word = "CAKE"
# Output: 3
# 
# Explanation: Using two fingers, one optimal way to type "CAKE" is:
# Finger 1 on letter 'C' -> cost = 0
# Finger 1 on letter 'A' -> cost = Distance from letter 'C' to letter 'A' = 2
# Finger 2 on letter 'K' -> cost = 0
# Finger 2 on letter 'E' -> cost = Distance from letter 'K' to letter 'E' = 1
# Total distance = 3
# 
# Example 2:
# 
# Input: word = "HAPPY"
# Output: 6
# 
# Explanation: Using two fingers, one optimal way to type "HAPPY" is:
# Finger 1 on letter 'H' -> cost = 0
# Finger 1 on letter 'A' -> cost = Distance from letter 'H' to letter 'A' = 2
# Finger 2 on letter 'P' -> cost = 0
# Finger 2 on letter 'P' -> cost = Distance from letter 'P' to letter 'P' = 0
# Finger 1 on letter 'Y' -> cost = Distance from letter 'A' to letter 'Y' = 4
# Total distance = 6
# 
# 
# Constraints:
#         2 <= word.length <= 300
#         word consists of uppercase English letters.


# Solution: https://algo.monster/liteproblems/1320
# Credit: AlgoMonster
def minimum_distance(word):

    def calculate_distance(char1: int, char2: int) -> int:
        row1, col1 = divmod(char1, 6)
        row2, col2 = divmod(char2, 6)
        return abs(row1 - row2) + abs(col1 - col2)
    
    word_length = len(word)
    
    # dp[i][left_finger][right_finger] represents minimum distance after typing
    # word[0:i+1] with left finger at position left_finger and right finger at right_finger
    dp = [[[float('inf')] * 26 for _ in range(26)] for _ in range(word_length)]
    
    # Initialize first character - can be typed by either finger with 0 cost
    first_char_index = ord(word[0]) - ord('A')
    for finger_pos in range(26):
        dp[0][first_char_index][finger_pos] = 0  # Left finger typed first char
        dp[0][finger_pos][first_char_index] = 0  # Right finger typed first char
    
    # Process each subsequent character
    for i in range(1, word_length):
        prev_char_index = ord(word[i - 1]) - ord('A')
        curr_char_index = ord(word[i]) - ord('A')
        distance_between_chars = calculate_distance(prev_char_index, curr_char_index)
        
        for other_finger in range(26):
            # Case 1: Same finger that typed previous character types current character
            # Left finger was at prev_char, moves to curr_char
            dp[i][curr_char_index][other_finger] = min(
                dp[i][curr_char_index][other_finger],
                dp[i - 1][prev_char_index][other_finger] + distance_between_chars
            )
            # Right finger was at prev_char, moves to curr_char
            dp[i][other_finger][curr_char_index] = min(
                dp[i][other_finger][curr_char_index],
                dp[i - 1][other_finger][prev_char_index] + distance_between_chars
            )
            
            # Case 2: The other finger (not at prev_char) types current character
            if other_finger == prev_char_index:
                for previous_position in range(26):
                    distance_to_current = calculate_distance(previous_position, curr_char_index)
                    # Left finger moves from previous_position to curr_char
                    dp[i][curr_char_index][other_finger] = min(
                        dp[i][curr_char_index][other_finger],
                        dp[i - 1][previous_position][prev_char_index] + distance_to_current
                    )
                    # Right finger moves from previous_position to curr_char
                    dp[i][other_finger][curr_char_index] = min(
                        dp[i][other_finger][curr_char_index],
                        dp[i - 1][prev_char_index][previous_position] + distance_to_current
                    )
    
    # Find minimum distance among all valid final states
    last_char_index = ord(word[-1]) - ord('A')
    
    # Minimum when left finger is at last character
    min_left_finger = min(dp[word_length - 1][last_char_index])
    
    # Minimum when right finger is at last character
    min_right_finger = min(dp[word_length - 1][j][last_char_index] for j in range(26))
    
    return int(min(min_left_finger, min_right_finger))
    # Time: O(n)
    # Space: O(n)
    # In both cases is O(n × |Σ|²), where n is the length of the string word 
    # and |Σ| = 26 represents the size of the alphabet.


def main():
    result = minimum_distance(word = "CAKE")
    print(result) # 3

    result = minimum_distance(word = "HAPPY")
    print(result) # 6

if __name__ == "__main__":
    main()
