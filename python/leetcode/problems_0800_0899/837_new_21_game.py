# ----------------
# 837. New 21 Game
# ----------------

# Problem: https://leetcode.com/problems/new-21-game
#
# Alice plays the following game, loosely based on the card game "21".
# Alice starts with 0 points and draws numbers while she has less than k points.
# During each draw, she gains an integer number of points randomly from the range
# [1, maxPts], where maxPts is an integer. Each draw is independent and the
# outcomes have equal probabilities.
# Alice stops drawing numbers when she gets k or more points.
# Return the probability that Alice has n or fewer points.
# Answers within 10-5 of the actual answer are considered accepted.
# Example 1:
# Input: n = 10, k = 1, maxPts = 10
# Output: 1.00000
# Explanation: Alice gets a single card, then stops.
# Example 2:
# Input: n = 6, k = 1, maxPts = 10
# Output: 0.60000
# Explanation: Alice gets a single card, then stops.
# In 6 out of 10 possibilities, she is at or below 6 points.
# Example 3:
# Input: n = 21, k = 17, maxPts = 10
# Output: 0.73278
# Constraints:
#         0 <= k <= n <= 104
#         1 <= maxPts <= 104


# Solution: https://youtu.be/zKi4LzjK27k
# Credit: Navdeep Singh founder of NeetCode
def new_21_game(n, k, max_pts):
    cache = {}

    def dfs(score):
        if score >= k:
            return 1 if score <= n else 0
        if score in cache:
            return cache[score]

        prob = 0
        for i in range(1, max_pts + 1):
            prob += dfs(score + i)

        cache[score] = prob / max_pts
        return cache[score]

    return dfs(0)
    # Time: O(n ^ 2)

def new_21_game_alt(n, k, max_pts):
    # Optimized solution
    if k == 0:
        return 1.0

    window_sum = 0
    for i in range(k, k + max_pts):
        window_sum += 1 if i <= n else 0

    dp = {}
    for i in range(k - 1, -1, -1):
        dp[i] = window_sum / max_pts
        remove = 0
        if i + max_pts <= n:
            remove = dp.get(i + max_pts, 1)
        window_sum += dp[i] - remove

    return dp[0]
    # Time: O(n)

def main():
    result = new_21_game(n = 10, k = 1, max_pts = 10)
    print(result) # 1.0

    result = new_21_game(n = 6, k = 1, max_pts = 10)
    print(result) # 0.6

    result = new_21_game(n = 21, k = 17, max_pts = 10)
    print(result) # 0.73278

if __name__ == "__main__":
    main()
