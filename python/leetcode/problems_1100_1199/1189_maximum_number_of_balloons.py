# -------------------------------
# 1189. Maximum Number Of Balloons
# -------------------------------

# Problem: https://leetcode.com/problems/maximum-number-of-balloons
#
# Given a string text, you want to use the characters of text to form as many
# instances of the word "balloon" as possible.
# 
# You can use each character in text at most once. Return the maximum number of
# instances that can be formed.
# 
# 
# Example 1:
# Input: text = "nlaebolko"
# Output: 1
# 
# Example 2:
# Input: text = "loonbalxballpoon"
# Output: 2
# 
# Example 3:
# 
# Input: text = "leetcode"
# Output: 0
# 
# 
# Constraints:
#         1 <= text.length <= 104
#         text consists of lower case English letters only.
# 
# Note: This question is the same as 2287: Rearrange Characters to Make Target
# String.

from collections import Counter
from collections import defaultdict

# Solution: https://youtu.be/G9xeB2-7PqY
# Credit: Navdeep Singh founder of NeetCode
def max_number_of_balloons(text):
    countText = Counter(text)
    balloon = Counter("balloon")

    res = len(text)  # or float("inf")
    for c in balloon:
        res = min(res, countText[c] // balloon[c])
    return res

# Solution: https://youtu.be/fVCBqMHwhww
# Credit: Greg Hogg
def max_number_of_balloons_alt(text):
    counter = defaultdict(int)
    balloon = "balloon"
    
    for c in text:
        if c in balloon:
            counter[c] += 1
    
    if any(c not in counter for c in balloon):
        return 0
    else:
        return min(counter["b"], counter["a"], counter["l"] // 2, counter["o"] // 2, counter["n"])

def main():
    result = max_number_of_balloons("nlaebolko")
    print(result) # 1

    result = max_number_of_balloons("loonbalxballpoon")
    print(result) # 2

    result = max_number_of_balloons("leetcode")
    print(result) # 0

if __name__ == "__main__":
    main()
