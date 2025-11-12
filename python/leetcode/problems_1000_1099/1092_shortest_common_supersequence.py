# -----------------------------------
# 1092. Shortest Common Supersequence 
# -----------------------------------

# Problem: https://leetcode.com/problems/shortest-common-supersequence
#
# Given two strings str1 and str2, return the shortest string that has both str1
# and str2 as subsequences. If there are multiple valid strings, return any of
# them.
# 
# A string s is a subsequence of string t if deleting some number of characters
# from t (possibly 0) results in the string s.
# 
# Example 1:
# 
# Input: str1 = "abac", str2 = "cab"
# Output: "cabac"
# 
# Explanation:
# str1 = "abac" is a subsequence of "cabac" because we can delete the first "c".
# str2 = "cab" is a subsequence of "cabac" because we can delete the last "ac".
# The answer provided is the shortest such string that satisfies these properties.
# 
# Example 2:
# 
# Input: str1 = "aaaaaaaa", str2 = "aaaaaaaa"
# Output: "aaaaaaaa"
# 
# 
# Constraints:
#         1 <= str1.length, str2.length <= 1000
#         str1 and str2 consist of lowercase English letters.


# Solution: https://youtu.be/JkjQNJSxXN0
# Credit: Navdeep Singh founder of NeetCode
def shortest_common_supersequence(str1, str2):
    N, M = len(str1), len(str2)

    prev = [str2[j:] for j in range(M)]
    prev.append("")

    for i in reversed(range(N)):
        cur = [""] * M
        cur.append(str1[i:])

        for j in reversed(range(M)):
            if str1[i] == str2[j]:
                cur[j] = str1[i] + prev[j + 1]
            else:
                res1 = str1[i] + prev[j]
                res2 = str2[j] + cur[j + 1]
                if len(res1) < len(res2):
                    cur[j] = res1
                else:
                    cur[j] = res2
        prev = cur

    return cur[0]
    # Time: O(n * m * (n + m))
    # Space: O(n * (n + m))

def main():
    result = shortest_common_supersequence(str1 = "abac", str2 = "cab")
    print(result) # "cabac"

    result = shortest_common_supersequence(str1 = "aaaaaaaa", str2 = "aaaaaaaa")
    print(result) # "aaaaaaaa"

if __name__ == "__main__":
    main()
