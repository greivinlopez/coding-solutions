# -------------------------------------------
# 1178. Number of Valid Words for Each Puzzle
# -------------------------------------------

# Problem: https://leetcode.com/problems/number-of-valid-words-for-each-puzzle
#
# With respect to a given puzzle string, a word is valid if both the following
# conditions are satisfied:
#         
#   * word contains the first letter of puzzle.
#   * For each letter in word, that letter is in puzzle.
#       * For example, if the puzzle is "abcdefg", then valid words are "faced", 
#         "cabbage", and "baggage", while
#       * invalid words are "beefed" (does not include 'a') and "based" (includes 
#         's' which is not in the puzzle).
# 
# Return an array answer, where answer[i] is the number of words in the given word
# list words that is valid with respect to the puzzle puzzles[i].
# 
# Example 1:
# 
# Input: words = ["aaaa","asas","able","ability","actt","actor","access"], puzzles
# = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]
# Output: [1,1,3,2,4,0]
# 
# Explanation:
# 1 valid word for "aboveyz" : "aaaa"
# 1 valid word for "abrodyz" : "aaaa"
# 3 valid words for "abslute" : "aaaa", "asas", "able"
# 2 valid words for "absoryz" : "aaaa", "asas"
# 4 valid words for "actresz" : "aaaa", "asas", "actt", "access"
# There are no valid words for "gaswxyz" cause none of the words in the list
# contains letter 'g'.
# 
# Example 2:
# 
# Input: words = ["apple","pleas","please"], puzzles =
# ["aelwxyz","aelpxyz","aelpsxy","saelpxy","xaelpsy"]
# Output: [0,1,3,2,0]
# 
# 
# Constraints:
#         1 <= words.length <= 10⁵
#         4 <= words[i].length <= 50
#         1 <= puzzles.length <= 10⁴
#         puzzles[i].length == 7
#         words[i] and puzzles[i] consist of lowercase English letters.
#         Each puzzles[i] does not contain repeated characters.

from collections import Counter

# Solution: https://algo.monster/liteproblems/1178
# Credit: AlgoMonster
def find_num_of_valid_words(words, puzzles):
    # Count frequency of each word's letter bitmask
    # Each bit position represents a letter (a=0, b=1, ..., z=25)
    word_bitmask_count = Counter()
    
    for word in words:
        bitmask = 0
        # Convert word to bitmask representation
        for char in word:
            bit_position = ord(char) - ord('a')
            bitmask |= 1 << bit_position
        word_bitmask_count[bitmask] += 1
    
    result = []
    
    for puzzle in puzzles:
        # Create bitmask for puzzle letters
        puzzle_bitmask = 0
        for char in puzzle:
            bit_position = ord(char) - ord('a')
            puzzle_bitmask |= 1 << bit_position
        
        # Count valid words for this puzzle
        valid_word_count = 0
        first_letter_bit = ord(puzzle[0]) - ord('a')
        
        # Iterate through all subsets of puzzle_bitmask that contain the first letter
        # Using technique: iterate through subsets by decrementing and ANDing with original mask
        subset = puzzle_bitmask
        while subset:
            # Check if subset contains the first letter of puzzle
            if (subset >> first_letter_bit) & 1:
                valid_word_count += word_bitmask_count[subset]
            # Move to next subset of puzzle_bitmask
            subset = (subset - 1) & puzzle_bitmask
        
        result.append(valid_word_count)
    
    return result
    # Time: O(m * w + n * 2ᵖ)
    # Space: O(m)
    # m = length of the words array
    # n = length of the puzzles array
    # w = maximum length of words in the words array
    # p = length of puzzles (typically 7 in this problem)


def main():
    result = find_num_of_valid_words(words = ["aaaa","asas","able","ability","actt","actor","access"], 
                                     puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"])
    print(result) # [1,1,3,2,4,0]

    result = find_num_of_valid_words(words = ["apple","pleas","please"], 
                                     puzzles = ["aelwxyz","aelpxyz","aelpsxy","saelpxy","xaelpsy"])
    print(result) # [0,1,3,2,0]

if __name__ == "__main__":
    main()
