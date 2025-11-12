# -------------------------
# 1366. Rank Teams by Votes
# -------------------------

# Problem: https://leetcode.com/problems/rank-teams-by-votes
#
# In a special ranking system, each voter gives a rank from highest to lowest to
# all teams participating in the competition.
# 
# The ordering of teams is decided by who received the most position-one votes. If
# two or more teams tie in the first position, we consider the second position to
# resolve the conflict, if they tie again, we continue this process until the ties
# are resolved. If two or more teams are still tied after considering all
# positions, we rank them alphabetically based on their team letter.
# 
# You are given an array of strings votes which is the votes of all voters in the
# ranking systems. Sort all teams according to the ranking system described above.
# 
# Return a string of all teams sorted by the ranking system.
# 
# Example 1:
# 
# Input: votes = ["ABC","ACB","ABC","ACB","ACB"]
# Output: "ACB"
# 
# Explanation:
# Team A was ranked first place by 5 voters. No other team was voted as first
# place, so team A is the first team.
# Team B was ranked second by 2 voters and ranked third by 3 voters.
# Team C was ranked second by 3 voters and ranked third by 2 voters.
# As most of the voters ranked C second, team C is the second team, and team B is
# the third.
# 
# Example 2:
# 
# Input: votes = ["WXYZ","XYZW"]
# Output: "XWYZ"
# 
# Explanation:
# X is the winner due to the tie-breaking rule. X has the same votes as W for the
# first position, but X has one vote in the second position, while W does not have
# any votes in the second position.
# 
# Example 3:
# 
# Input: votes = ["ZMNAGUEDSJYLBOPHRQICWFXTVK"]
# Output: "ZMNAGUEDSJYLBOPHRQICWFXTVK"
# 
# Explanation: Only one voter, so their votes are used for the ranking.
# 
# 
# Constraints:
#         1 <= votes.length <= 1000
#         1 <= votes[i].length <= 26
#         votes[i].length == votes[j].length for 0 <= i, j < votes.length.
#         votes[i][j] is an English uppercase letter.
#         All characters of votes[i] are unique.
#         All the characters that occur in votes[0] also occur in votes[j] 
#         where 1 <= j < votes.length.

from collections import defaultdict

# Solution: https://algo.monster/liteproblems/1366
# Credit: AlgoMonster
def rank_teams(votes):
    # Get the number of positions (length of each vote)
    num_positions = len(votes[0])
    
    # Initialize a dictionary to track vote counts for each team at each position
    # Each team will have a list of counts [1st_place_count, 2nd_place_count, ...]
    vote_counts = defaultdict(lambda: [0] * num_positions)
    
    # Count votes for each team at each position
    for vote in votes:
        for position, team in enumerate(vote):
            vote_counts[team][position] += 1
    
    # Sort teams based on:
    # 1. Vote counts at each position (higher is better, so reverse=True)
    # 2. Alphabetical order as tiebreaker (smaller ASCII value is better, so negative ord)
    sorted_teams = sorted(
        vote_counts.keys(), 
        key=lambda team: (vote_counts[team], -ord(team)), 
        reverse=True
    )
    
    # Join the sorted teams into a string
    return "".join(sorted_teams)
    # Time: O(n * m + m² * log m)
    # Space: O(m²)


def main():
    result = rank_teams(votes = ["ABC","ACB","ABC","ACB","ACB"])
    print(result) # "ACB"

    result = rank_teams(votes = ["WXYZ","XYZW"])
    print(result) # "XWYZ"

    result = rank_teams(votes = ["ZMNAGUEDSJYLBOPHRQICWFXTVK"])
    print(result) # "ZMNAGUEDSJYLBOPHRQICWFXTVK"

if __name__ == "__main__":
    main()
