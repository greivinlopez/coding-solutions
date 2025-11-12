# -----------------------------------
# 2559. Count Vowel Strings in Ranges
# -----------------------------------

# Problem: https://leetcode.com/problems/count-vowel-strings-in-ranges
#
# You are given a 0-indexed array of strings words and a 2D array of integers
# queries.
# 
# Each query queries[i] = [li, ri] asks us to find the number of strings present
# at the indices ranging from li to ri (both inclusive) of words that start and
# end with a vowel.
# 
# Return an array ans of size queries.length, where ans[i] is the answer to the
# ith query.
# 
# Note that the vowel letters are 'a', 'e', 'i', 'o', and 'u'.
# 
# Example 1:
# 
# Input: words = ["aba","bcb","ece","aa","e"], queries = [[0,2],[1,4],[1,1]]
# Output: [2,3,0]
# 
# Explanation: The strings starting and ending with a vowel are "aba", "ece", "aa"
# and "e".
# The answer to the query [0,2] is 2 (strings "aba" and "ece").
# to query [1,4] is 3 (strings "ece", "aa", "e").
# to query [1,1] is 0.
# We return [2,3,0].
# 
# Example 2:
# 
# Input: words = ["a","e","i"], queries = [[0,2],[0,1],[2,2]]
# Output: [3,2,1]
# 
# Explanation: Every string satisfies the conditions, so we return [3,2,1].
# 
# 
# Constraints:
#         1 <= words.length <= 10^5
#         1 <= words[i].length <= 40
#         words[i] consists only of lowercase English letters.
#         sum(words[i].length) <= 3 * 10^5
#         1 <= queries.length <= 10^5
#         0 <= li <= ri < words.length


# Solution: https://youtu.be/TLJd7W-z-yc
# Credit: Navdeep Singh founder of NeetCode
def vowel_strings(words, queries):
    vowel_set = set("aeiou")

    prefix_cnt = [0] * (len(words) + 1)
    prev = 0
    for i, w in enumerate(words):
        if w[0] in vowel_set and w[-1] in vowel_set:
            prev += 1
        prefix_cnt[i + 1] = prev

    res = [0] * len(queries)
    for i, q in enumerate(queries):
        l, r = q
        res[i] = prefix_cnt[r + 1] - prefix_cnt[l]

    return res
    # Time: O(n)


def main():
    result = vowel_strings(words = ["aba","bcb","ece","aa","e"], queries = [[0,2],[1,4],[1,1]])
    print(result) # [2,3,0]

    result = vowel_strings(words = ["a","e","i"], queries = [[0,2],[0,1],[2,2]])
    print(result) # [3,2,1]

if __name__ == "__main__":
    main()
