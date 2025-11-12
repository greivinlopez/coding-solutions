# -----------------------
# 68. Text Justification
# -----------------------

# Problem: https://leetcode.com/problems/text-justification/
# 
# Given an array of strings words and a width maxWidth, format the text such that each 
# line has exactly maxWidth characters and is fully (left and right) justified.
# 
# You should pack your words in a greedy approach; that is, pack as many words as you 
# can in each line. Pad extra spaces ' ' when necessary so that each line has exactly 
# maxWidth characters.
# 
# Extra spaces between words should be distributed as evenly as possible. If the number 
# of spaces on a line does not divide evenly between words, the empty slots on the left 
# will be assigned more spaces than the slots on the right.
# 
# For the last line of text, it should be left-justified, and no extra space is inserted between words.
# 
# Note:
# 
# - A word is defined as a character sequence consisting of non-space characters only.
# - Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
# - The input array words contains at least one word.

# Solution: https://youtu.be/TzMl4Z7pVh8
# Credit: Navdeep Singh founder of NeetCode 
def full_justify(words, maxWidth):
    res = []
    line = []  # Words in current line
    length = 0  # Current line length
    i = 0
    while i < len(words):
        if length + len(line) + len(words[i]) > maxWidth:
            # Line complete
            extra_space = maxWidth - length
            word_cnt = len(line) - 1
            spaces = extra_space // max(1, word_cnt)
            remainder = extra_space % max(1, word_cnt)

            for j in range(max(1, len(line) - 1)):
                line[j] += " " * spaces
                if remainder:
                    line[j] += " "
                    remainder -= 1

            res.append("".join(line))
            line, length = [], 0  # Reset line and length
        
        line.append(words[i])
        length += len(words[i])
        i += 1

    # Handling the last line
    last_line = " ".join(line)
    trail_spaces = maxWidth - len(last_line)
    res.append(last_line + (trail_spaces * " "))

    return res


def main():
    result = full_justify(["This", "is", "an", "example", "of", "text", "justification."], 16) 
    # Expected Output: ["This    is    an","example  of text","justification.  "]
    print(result)
    result = full_justify(["What","must","be","acknowledgment","shall","be"], 16)
    # Expected Output: ["What   must   be", "acknowledgment  ", "shall be        "]
    print(result)

if __name__ == "__main__":
    main()