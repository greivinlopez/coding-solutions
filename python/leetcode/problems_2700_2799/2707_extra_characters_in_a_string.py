# ----------------------------------
# 2707. Extra Characters in a String
# ----------------------------------

# Problem: https://leetcode.com/problems/extra-characters-in-a-string
#
# You are given a 0-indexed string s and a dictionary of words dictionary. You
# have to break s into one or more non-overlapping substrings such that each
# substring is present in dictionary. There may be some extra characters in s
# which are not present in any of the substrings.
# 
# Return the minimum number of extra characters left over if you break up s
# optimally.
# 
# Example 1:
# 
# Input: s = "leetscode", dictionary = ["leet","code","leetcode"]
# Output: 1
# 
# Explanation: We can break s in two substrings: "leet" from index 0 to 3 and
# "code" from index 5 to 8. There is only 1 unused character (at index 4), so we
# return 1.
# 
# Example 2:
# 
# Input: s = "sayhelloworld", dictionary = ["hello","world"]
# Output: 3
# 
# Explanation: We can break s in two substrings: "hello" from index 3 to 7 and
# "world" from index 8 to 12. The characters at indices 0, 1, 2 are not used in
# any substring and thus are considered as extra characters. Hence, we return 3.
# 
# 
# Constraints:
#         1 <= s.length <= 50
#         1 <= dictionary.length <= 50
#         1 <= dictionary[i].length <= 50
#         dictionary[i] and s consists of only lowercase English letters
#         dictionary contains distinct words


# Solution: https://youtu.be/ONstwO1cD7c
# Credit: Navdeep Singh founder of NeetCode
def min_extra_char(s, dictionary):
    # Memoization solution
    words = set(dictionary)
    dp = {len(s): 0}

    def dfs(i):
        if i in dp:
            return dp[i]

        res = 1 + dfs(i + 1)  # skip curr char
        for j in range(i, len(s)):
            if s[i : j + 1] in words:
                res = min(res, dfs(j + 1))

        dp[i] = res
        return res

    return dfs(0)
    # Time: O(n³)
    # Space: O(n + m * k)
    # n is the length of the string s
    # m is the number of words
    # k is the average length of a word

# Trie solution
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class Trie:
    def __init__(self, words):
        self.root = TrieNode()
        for w in words:
            curr = self.root
            for c in w:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.word = True

def min_extra_char_trie(s, dictionary):
    dp = {len(s): 0}
    trie = Trie(dictionary).root

    def dfs(i):
        if i in dp:
            return dp[i]

        res = 1 + dfs(i + 1)
        curr = trie
        for j in range(i, len(s)):
            if s[j] not in curr.children:
                break
            curr = curr.children[s[j]]
            if curr.word:
                res = min(res, dfs(j + 1))

        dp[i] = res
        return res

    return dfs(0)


def main():
    result = min_extra_char(s = "leetscode", dictionary = ["leet","code","leetcode"])
    print(result) # 1

    result = min_extra_char(s = "sayhelloworld", dictionary = ["hello","world"])
    print(result) # 3

if __name__ == "__main__":
    main()
