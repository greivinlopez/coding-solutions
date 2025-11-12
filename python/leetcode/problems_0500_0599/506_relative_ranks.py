# -------------------
# 506. Relative Ranks
# -------------------

# Problem: https://leetcode.com/problems/relative-ranks
#
# You are given an integer array score of size n, where score[i] is the score of
# the ith athlete in a competition. All the scores are guaranteed to be unique.
# 
# The athletes are placed based on their scores, where the 1st place athlete has
# the highest score, the 2nd place athlete has the 2nd highest score, and so on.
# 
# The placement of each athlete determines their rank:
# 
#         * The 1st place athlete's rank is "Gold Medal".
#         * The 2nd place athlete's rank is "Silver Medal".
#         * The 3rd place athlete's rank is "Bronze Medal".
#         * For the 4th place to the nth place athlete, their rank is their
#           placement number (i.e., the xth place athlete's rank is "x").
# 
# Return an array answer of size n where answer[i] is the rank of the ith athlete.
# 
# Example 1:
# 
# Input: score = [5,4,3,2,1]
# Output: ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
# 
# Explanation: The placements are [1st, 2nd, 3rd, 4th, 5th].
# 
# Example 2:
# 
# Input: score = [10,3,8,9,4]
# Output: ["Gold Medal","5","Bronze Medal","Silver Medal","4"]
# 
# Explanation: The placements are [1st, 5th, 3rd, 2nd, 4th].
# 
# 
# Constraints:
#         n == score.length
#         1 <= n <= 10⁴
#         0 <= score[i] <= 10⁶
#         All the values in score are unique.

# Credit: Jaweria Batool -> https://github.com/Jaweria-B
def find_relative_ranks(score):
    N = len(score)

    def find_max(score):
        max_score = 0
        for s in score:
            if s > max_score :
                max_score = s
        return max_score

    # Add the original index of each score to the array
    # Where the score is the key
    M = find_max(score)
    score_to_index = [0] * (M + 1)
    for i in range(N):
        score_to_index[score[i]] = i + 1

    MEDALS = ["Gold Medal", "Silver Medal", "Bronze Medal"]

    # Assign ranks to athletes
    rank = [None] * N
    place = 1
    for i in range(M, -1, -1):
        if score_to_index[i] != 0:
            original_index = score_to_index[i] - 1
            if place < 4:
                rank[original_index] = MEDALS[place - 1]
            else:
                rank[original_index] = str(place)
            place += 1
    return rank
    # Time: O(n + m)
    # Space: O(n + m)
    # n = number of scores
    # m = maximum possible score


def main():
    result = find_relative_ranks(score = [5,4,3,2,1])
    print(result) # ["Gold Medal","Silver Medal","Bronze Medal","4","5"]

    result = find_relative_ranks(score = [10,3,8,9,4])
    print(result) # ["Gold Medal","5","Bronze Medal","Silver Medal","4"]

if __name__ == "__main__":
    main()
