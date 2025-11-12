# ----------------------------
# 1324. Print Words Vertically
# ----------------------------

# Problem: https://leetcode.com/problems/print-words-vertically
#
# Given a string s. Return all the words vertically in the same order in which
# they appear in s.
# 
# Words are returned as a list of strings, complete with spaces when is necessary.
# (Trailing spaces are not allowed).
# 
# Each word would be put on only one column and that in one column there will be
# only one word.
# 
# Example 1:
# 
# Input: s = "HOW ARE YOU"
# Output: ["HAY","ORO","WEU"]
# 
# Explanation: Each word is printed vertically.
#  "HAY"
#  "ORO"
#  "WEU"
# 
# Example 2:
# 
# Input: s = "TO BE OR NOT TO BE"
# Output: ["TBONTB","OEROOE","   T"]
# 
# Explanation: Trailing spaces is not allowed.
# "TBONTB"
# "OEROOE"
# "   T"
# 
# Example 3:
# 
# Input: s = "CONTEST IS COMING"
# Output: ["CIC","OSO","N M","T I","E N","S G","T"]
# 
# 
# Constraints:
#         1 <= s.length <= 200
#         s contains only upper case English letters.
#         It's guaranteed that there is only one space between 2 words.


# Solution: https://algo.monster/liteproblems/1324
# Credit: AlgoMonster
def print_vertically(s):
    # Split the input string into individual words
    words = s.split()
    
    # Find the maximum length among all words
    max_length = max(len(word) for word in words)
    
    # Initialize result list to store vertical strings
    result = []
    
    # Iterate through each column position (0 to max_length-1)
    for col_index in range(max_length):
        # Build current column by extracting character at col_index from each word
        # If word is shorter than col_index, use space as placeholder
        current_column = []
        for word in words:
            if col_index < len(word):
                current_column.append(word[col_index])
            else:
                current_column.append(' ')
        
        # Remove trailing spaces from the current column
        while current_column and current_column[-1] == ' ':
            current_column.pop()
        
        # Join characters to form the vertical string and add to result
        result.append(''.join(current_column))
    
    return result
    # Time: O(m * n)
    # Space: O(m * n)


def main():
    result = print_vertically(s = "HOW ARE YOU")
    print(result) # ['HAY', 'ORO', 'WEU']

    result = print_vertically(s = "TO BE OR NOT TO BE")
    print(result) # ['TBONTB', 'OEROOE', '   T']

    result = print_vertically(s = "CONTEST IS COMING")
    print(result) # ['CIC', 'OSO', 'N M', 'T I', 'E N', 'S G', 'T']

if __name__ == "__main__":
    main()
