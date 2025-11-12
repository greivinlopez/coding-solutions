# ----------------------------------------
# 2185. Counting Words With a Given Prefix
# ----------------------------------------

# Problem: https://leetcode.com/problems/counting-words-with-a-given-prefix
#
# You are given an array of strings words and a string pref.
# 
# Return the number of strings in words that contain pref as a prefix.
# 
# A prefix of a string s is any leading contiguous substring of s.
# 
# Example 1:
# 
# Input: words = ["pay","attention","practice","attend"], pref = "at"
# Output: 2
# 
# Explanation: The 2 strings that contain "at" as a prefix are: "attention" and
# "attend".
# 
# Example 2:
# 
# Input: words = ["leetcode","win","loops","success"], pref = "code"
# Output: 0
# 
# Explanation: There are no strings that contain "code" as a prefix.
# 
# 
# Constraints:
#         1 <= words.length <= 100
#         1 <= words[i].length, pref.length <= 100
#         words[i] and pref consist of lowercase English letters.


# Solution: https://youtu.be/B26hW8fBMj0
# Credit: Navdeep Singh founder of NeetCode
class PrefixNode:
    def __init__(self):
        self.children = {}  # a -> PrefixNode
        self.count = 0

class PrefixTree:
    def __init__(self):
        self.root = PrefixNode()

    def add(self, w, length):
        cur = self.root
        for i in range(min(len(w), length)):
            c = w[i]
            if c not in cur.children:
                cur.children[c] = PrefixNode()
            cur = cur.children[c]
            cur.count += 1

    def count(self, pref):
        cur = self.root
        for c in pref:
            if c not in cur.children:
                return 0
            cur = cur.children[c]
        return cur.count

def prefix_count(words, pref):
    prefix_tree = PrefixTree()
    
    for w in words:
        if len(w) >= len(pref):
            prefix_tree.add(w, len(pref))
            
    return prefix_tree.count(pref)


def main():
    result = prefix_count(words = ["pay","attention","practice","attend"], pref = "at")
    print(result) # 2

    result = prefix_count(words = ["leetcode","win","loops","success"], pref = "code")
    print(result) # 0

if __name__ == "__main__":
    main()
