# ------------------------------------------
# 2225. Find Players With Zero or One Losses
# ------------------------------------------

# Problem: https://leetcode.com/problems/find-players-with-zero-or-one-losses
#
# You are given an integer array matches where matches[i] = [winnerᵢ, loserᵢ]
# indicates that the player winnerᵢ defeated player loserᵢ in a match.
# 
# Return a list answer of size 2 where:
# 
#         answer[0] is a list of all players that have not lost any matches.
#         answer[1] is a list of all players that have lost exactly one match.
# 
# The values in the two lists should be returned in increasing order.
# 
# Note:
#   * You should only consider the players that have played at least one match.
#   * The testcases will be generated such that no two matches will have the same 
#     outcome.
# 
# Example 1:
# 
# Input: matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
# Output: [[1,2,10],[4,5,7,8]]
# 
# Explanation:
# Players 1, 2, and 10 have not lost any matches.
# Players 4, 5, 7, and 8 each have lost one match.
# Players 3, 6, and 9 each have lost two matches.
# Thus, answer[0] = [1,2,10] and answer[1] = [4,5,7,8].
# 
# Example 2:
# 
# Input: matches = [[2,3],[1,3],[5,4],[6,4]]
# Output: [[1,2,5,6],[]]
# 
# Explanation:
# Players 1, 2, 5, and 6 have not lost any matches.
# Players 3 and 4 each have lost two matches.
# Thus, answer[0] = [1,2,5,6] and answer[1] = [].
# 
# 
# Constraints:
#         1 <= matches.length <= 10⁵
#         matches[i].length == 2
#         1 <= winnerᵢ, loserᵢ <= 10⁵
#         winnerᵢ != loserᵢ
#         All matches[i] are unique.


# Credit: Jaweria Batool -> https://github.com/Jaweria-B
def find_winners(matches):
    zeroLoss, oneLoss, moreLoss = set(), set(), set()

    for match in matches:
        winner, loser = match[0], match[1]

        # Add winner.
        if winner not in oneLoss and winner not in moreLoss:
            zeroLoss.add(winner)

        # Add or move loser.
        if loser in zeroLoss:
            zeroLoss.remove(loser)
            oneLoss.add(loser)
        elif loser in oneLoss:
            oneLoss.remove(loser)
            moreLoss.add(loser)
        elif loser in moreLoss:
            continue
        else:
            oneLoss.add(loser)

    answer = [sorted(list(zeroLoss)), sorted(list(oneLoss))]
    return answer
    # Time: O(n * log(n))
    # Space: O(n)


def main():
    matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
    result = find_winners(matches)
    print(result) # [[1,2,10],[4,5,7,8]]

    matches = [[2,3],[1,3],[5,4],[6,4]]
    result = find_winners(matches)
    print(result) # [[1,2,5,6],[]]

if __name__ == "__main__":
    main()
