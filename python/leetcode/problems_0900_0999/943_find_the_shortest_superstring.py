# ----------------------------------
# 943. Find the Shortest Superstring
# ----------------------------------

# Problem: https://leetcode.com/problems/find-the-shortest-superstring
#
# Given an array of strings words, return the smallest string that contains each
# string in words as a substring. If there are multiple valid strings of the
# smallest length, return any of them.
# 
# You may assume that no string in words is a substring of another string in
# words.
# 
# Example 1:
# 
# Input: words = ["alex","loves","leetcode"]
# Output: "alexlovesleetcode"
# 
# Explanation: All permutations of "alex","loves","leetcode" would also be
# accepted.
# 
# Example 2:
# 
# Input: words = ["catg","ctaagt","gcta","ttca","atgcatc"]
# Output: "gctaagttcatgcatc"
# 
# 
# Constraints:
#         1 <= words.length <= 12
#         1 <= words[i].length <= 20
#         words[i] consists of lowercase English letters.
#         All the strings of words are unique.


# Solution: https://algo.monster/liteproblems/943
# Credit: AlgoMonster
def shortest_superstring(words):
    # Number of words
    num_words = len(words)
    
    # Graph g where g[i][j] represents the length of overlap if word i is followed by word j
    overlap = [[0] * num_words for _ in range(num_words)]
    
    # Calculate the maximum overlap of each pair of words
    for i, word1 in enumerate(words):
        for j, word2 in enumerate(words):
            if i != j:
                # Check the maximum prefix of word2 that's a suffix of word1
                for k in range(min(len(word1), len(word2)), 0, -1):
                    if word1[-k:] == word2[:k]:
                        overlap[i][j] = k
                        break
    
    # Dynamic programming table, where dp[mask][i] holds the highest overlap with mask and ending with word i
    dp = [[0] * num_words for _ in range(1 << num_words)]
    
    # Parent table to reconstruct the path
    parent = [[-1] * num_words for _ in range(1 << num_words)]
    
    # Fill dp[] and parent[]
    for mask in range(1 << num_words):
        for j in range(num_words):
            if (mask >> j) & 1:
                # Previous mask before adding word j
                prev_mask = mask ^ (1 << j)
                for k in range(num_words):
                    if (prev_mask >> k) & 1:
                        value = dp[prev_mask][k] + overlap[k][j]
                        if value > dp[mask][j]:
                            dp[mask][j] = value
                            parent[mask][j] = k
    
    # Recover the last word in the optimal arrangement
    last = max(range(num_words), key=lambda i: dp[-1][i])
    
    # Recover the order of words in the optimal superstring
    order = []
    mask = (1 << num_words) - 1
    while last != -1:
        prev = parent[mask][last]
        order.append(last)
        mask ^= (1 << last)
        last = prev
    order.reverse()
    
    # Add words that are not in the optimal order (could happen if all overlaps are 0)
    order.extend(j for j in range(num_words) if j not in order)
    
    # Build the shortest superstring based on the order
    result = [words[order[0]]]
    for i in range(1, len(order)):
        index = order[i]
        prev_index = order[i - 1]
        result.append(words[index][overlap[prev_index][index]:])
    
    return ''.join(result)
    # Time: O(n² * 2ⁿ + n² * w)
    # Space: O(n² * 2ⁿ + n²)
    # n = the number of words
    # w = the maximum length of a word.


def main():
    result = shortest_superstring(words = ["alex","loves","leetcode"])
    print(result) # "alexlovesleetcode"

    result = shortest_superstring(words = ["catg","ctaagt","gcta","ttca","atgcatc"])
    print(result) # "gctaagttcatgcatc"

if __name__ == "__main__":
    main()
