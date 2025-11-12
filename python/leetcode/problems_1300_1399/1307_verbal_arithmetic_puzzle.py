# ------------------------------
# 1307. Verbal Arithmetic Puzzle
# ------------------------------

# Problem: https://leetcode.com/problems/verbal-arithmetic-puzzle
#
# Given an equation, represented by words on the left side and the result on the
# right side.
# 
# You need to check if the equation is solvable under the following rules:
#         
#   * Each character is decoded as one digit (0 - 9).
#   * No two characters can map to the same digit.
#   * Each words[i] and result are decoded as one number without leading zeros.
#   * Sum of numbers on the left side (words) will equal to the number on the
#     right side (result).
# 
# Return true if the equation is solvable, otherwise return false.
# 
# Example 1:
# 
# Input: words = ["SEND","MORE"], result = "MONEY"
# Output: true
# 
# Explanation: Map 'S'-> 9, 'E'->5, 'N'->6, 'D'->7, 'M'->1, 'O'->0, 'R'->8,
# 'Y'->'2'
# Such that: "SEND" + "MORE" = "MONEY" ,  9567 + 1085 = 10652
# 
# Example 2:
# 
# Input: words = ["SIX","SEVEN","SEVEN"], result = "TWENTY"
# Output: true
# 
# Explanation: Map 'S'-> 6, 'I'->5, 'X'->0, 'E'->8, 'V'->7, 'N'->2, 'T'->1,
# 'W'->'3', 'Y'->4
# Such that: "SIX" + "SEVEN" + "SEVEN" = "TWENTY" ,  650 + 68782 + 68782 = 138214
# 
# Example 3:
# 
# Input: words = ["LEET","CODE"], result = "POINT"
# Output: false
# 
# Explanation: There is no possible mapping to satisfy the equation, so we return
# false. Note that two different characters cannot map to the same digit.
# 
# 
# Constraints:
#         2 <= words.length <= 5
#         1 <= words[i].length, result.length <= 7
#         words[i], result contain only uppercase English letters.
#         The number of different characters used in the expression is at most 10.


# Solution: https://algo.monster/liteproblems/1307
# Credit: AlgoMonster
def is_any_mapping(
    words, row, col, balance, letter_to_digit, digit_to_letter, total_rows, total_cols
):
    # Base case: Processed all columns successfully
    if col == total_cols:
        return balance == 0

    # Finished processing current column, move to next column
    if row == total_rows:
        # Check if current column sums to 0 (mod 10) and propagate carry
        return balance % 10 == 0 and is_any_mapping(
            words, 0, col + 1, balance // 10, letter_to_digit, digit_to_letter, total_rows, total_cols
        )

    current_word = words[row]

    # Skip if current word doesn't have a character at this column position
    if col >= len(current_word):
        return is_any_mapping(
            words, row + 1, col, balance, letter_to_digit, digit_to_letter, total_rows, total_cols
        )

    # Get the letter at current position (counting from right)
    letter = current_word[len(current_word) - 1 - col]

    # Determine sign: positive for addends, negative for result (last word)
    sign = 1 if row < total_rows - 1 else -1

    # Case 1: Letter already has a digit mapping
    if letter in letter_to_digit:
        digit = letter_to_digit[letter]
        
        # Check for leading zero constraint
        is_leading_position = (col == len(current_word) - 1)
        is_single_char_word = (len(current_word) == 1)
        
        # Leading zeros are only allowed for single-character words
        if digit != 0 or is_single_char_word or not is_leading_position:
            return is_any_mapping(
                words,
                row + 1,
                col,
                balance + sign * digit,
                letter_to_digit,
                digit_to_letter,
                total_rows,
                total_cols,
            )
        else:
            return False

    # Case 2: Letter needs a new digit mapping
    else:
        # Try each available digit
        for digit in range(10):
            # Check if digit is available
            if digit_to_letter[digit] == "-":
                # Check leading zero constraint
                is_leading_position = (col == len(current_word) - 1)
                is_single_char_word = (len(current_word) == 1)
                
                # Skip if this would create an invalid leading zero
                if digit == 0 and is_leading_position and not is_single_char_word:
                    continue
                
                # Make the assignment
                digit_to_letter[digit] = letter
                letter_to_digit[letter] = digit

                # Recursively check if this assignment works
                if is_any_mapping(
                    words,
                    row + 1,
                    col,
                    balance + sign * digit,
                    letter_to_digit,
                    digit_to_letter,
                    total_rows,
                    total_cols,
                ):
                    return True

                # Backtrack: undo the assignment
                digit_to_letter[digit] = "-"
                if letter in letter_to_digit:
                    del letter_to_digit[letter]

    # No valid mapping found
    return False

def is_solvable(words, result):
    # Combine all words into a single list (result goes last)
    all_words = words + [result]

    # Count total words and find maximum word length
    total_rows = len(all_words)
    total_cols = max(len(word) for word in all_words)

    # Initialize mapping structures
    letter_to_digit = {}  # Maps each letter to its assigned digit
    digit_to_letter = ["-"] * 10  # Maps each digit to its assigned letter ("-" means unassigned)

    # Start the recursive search
    return is_any_mapping(
        all_words, 0, 0, 0, letter_to_digit, digit_to_letter, total_rows, total_cols
    )
    # Time: O(n * 10ᵐ)
    # Space: O(n + m)
    # n = total number of characters across all word
    # m = the number of unique letters.


def main():
    result = is_solvable(words = ["SEND","MORE"], result = "MONEY")
    print(result) # True

    result = is_solvable(words = ["SIX","SEVEN","SEVEN"], result = "TWENTY")
    print(result) # True

    result = is_solvable(words = ["LEET","CODE"], result = "POINT")
    print(result) # False

if __name__ == "__main__":
    main()
