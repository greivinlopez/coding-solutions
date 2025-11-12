# ---------------------------------
# 1408. String Matching in an Array
# ---------------------------------

# Problem: https://leetcode.com/problems/string-matching-in-an-array
#
# Given an array of string words, return all strings in words that are a substring
# of another word. You can return the answer in any order.
# 
# Example 1:
# 
# Input: words = ["mass","as","hero","superhero"]
# Output: ["as","hero"]
# 
# Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
# ["hero","as"] is also a valid answer.
# 
# Example 2:
# 
# Input: words = ["leetcode","et","code"]
# Output: ["et","code"]
# 
# Explanation: "et", "code" are substring of "leetcode".
# 
# Example 3:
# 
# Input: words = ["blue","green","bu"]
# Output: []
# 
# Explanation: No string of words is substring of another string.
# 
# 
# Constraints:
#         1 <= words.length <= 100
#         1 <= words[i].length <= 30
#         words[i] contains only lowercase English letters.
#         All the strings of words are unique.


# Solution: https://youtu.be/7K2BjgjCFDo
# Credit: Navdeep Singh founder of NeetCode
def string_matching(words):
    res = []
    
    for i in range(len(words)):
        for j in range(len(words)):
            if i == j:
                continue
            
            if words[i] in words[j]:
                res.append(words[i])
                break
    
    return res
    # Time: O(n^2 * l^2)  n = len(words), l = avg length of words 
    # Space: O(k) k = number of words that are substrings of other words


def main():
    result = string_matching(words = ["mass","as","hero","superhero"])
    print(result) # ["as","hero"]

    result = string_matching(words = ["leetcode","et","code"])
    print(result) # ["et","code"]

    result = string_matching(words = ["blue","green","bu"])
    print(result) # []

if __name__ == "__main__":
    main()
