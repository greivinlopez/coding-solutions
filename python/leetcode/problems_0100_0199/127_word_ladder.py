# -----------------
# 127. Word Ladder
# -----------------

# Problem: https://leetcode.com/problems/word-ladder/
# 
# A transformation sequence from word beginWord to word endWord using a dictionary 
# wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:
# 
# - Every adjacent pair of words differs by a single letter.
# - Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
# - sk == endWord
# 
# Given two words, beginWord and endWord, and a dictionary wordList, return the 
# number of words in the shortest transformation sequence from beginWord to 
# endWord, or 0 if no such sequence exists.

from collections import defaultdict, deque

# Solution: https://youtu.be/h9iTnkgv05E
# Credit: Navdeep Singh founder of NeetCode
def ladder_length(beginWord, endWord, wordList):
    if endWord not in wordList:
        return 0

    nei = defaultdict(list)
    wordList.append(beginWord)
    for word in wordList:
        for j in range(len(word)):
            pattern = word[:j] + "*" + word[j + 1 :]
            nei[pattern].append(word)

    visit = set([beginWord])
    q = deque([beginWord])
    res = 1
    while q:
        for i in range(len(q)):
            word = q.popleft()
            if word == endWord:
                return res
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1 :]
                for neiWord in nei[pattern]:
                    if neiWord not in visit:
                        visit.add(neiWord)
                        q.append(neiWord)
        res += 1
    return 0


def main():
    result = ladder_length("hit", "cog", ["hot","dot","dog","lot","log","cog"])
    print(result) # 5

    result = ladder_length("hit", "cog", ["hot","dot","dog","lot","log"])
    print(result) # 0

if __name__ == "__main__":
    main()