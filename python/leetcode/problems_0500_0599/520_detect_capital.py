# -------------------
# 520. Detect Capital
# -------------------

# Problem: https://leetcode.com/problems/detect-capital
#
# We define the usage of capitals in a word to be right when one of the following
# cases holds:
# 
#         All letters in this word are capitals, like "USA".
#         All letters in this word are not capitals, like "leetcode".
#         Only the first letter in this word is capital, like "Google".
# 
# Given a string word, return true if the usage of capitals in it is right.
# 
# Example 1:
# 
# Input: word = "USA"
# Output: true
# 
# Example 2:
# 
# Input: word = "FlaG"
# Output: false
# 
# 
# Constraints:
#         1 <= word.length <= 100
#         word consists of lowercase and uppercase English letters.


# Solution: https://algo.monster/liteproblems/520
# Credit: AlgoMonster
def detect_capital_use(word):
    # Count the number of uppercase letters in the word
    uppercase_count = sum(1 for char in word if char.isupper())
    
    # Check if the word follows one of the three valid patterns:
    # 1. No uppercase letters (all lowercase)
    # 2. All uppercase letters
    # 3. Exactly one uppercase letter at the beginning
    return (uppercase_count == 0 or 
            uppercase_count == len(word) or 
            (uppercase_count == 1 and word[0].isupper()))
    # Time: O(n)
    # Space: O(1)


def main():
    result = detect_capital_use("USA")
    print(result) # True

    result = detect_capital_use("FlaG")
    print(result) # False

if __name__ == "__main__":
    main()
