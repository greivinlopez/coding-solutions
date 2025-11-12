# ----------------------------
# 1002. Find Common Characters
# ----------------------------

# Problem: https://leetcode.com/problems/find-common-characters
#
# Given a string array words, return an array of all characters that show up in
# all strings within the words (including duplicates). You may return the answer
# in any order.
# 
# Example 1:
# 
# Input: words = ["bella","label","roller"]
# Output: ["e","l","l"]
# 
# Example 2:
# 
# Input: words = ["cool","lock","cook"]
# Output: ["c","o"]
# 
# 
# Constraints:
#         1 <= words.length <= 100
#         1 <= words[i].length <= 100
#         words[i] consists of lowercase English letters.

from collections import Counter

# Solution: https://youtu.be/QEESBA2Q_88
# Credit: Navdeep Singh founder of NeetCode
def common_chars(words):
    cnt = Counter(words[0])

    for w in words:
        cur_cnt = Counter(w)
        for c in cnt:
            cnt[c] = min(cnt[c], cur_cnt[c])

    res = []
    for c in cnt:
        for i in range(cnt[c]):
            res.append(c)
    return res
    # Time: O(n * m)

def main():
    result = common_chars(["bella","label","roller"])
    print(result) # ["e","l","l"]

    result = common_chars(["cool","lock","cook"])
    print(result) # ["c","o"]

if __name__ == "__main__":
    main()
