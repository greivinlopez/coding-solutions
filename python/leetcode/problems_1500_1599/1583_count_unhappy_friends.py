# ------------------------------
# 1583. Count Unhappy Friends 🙁
# ------------------------------

# Problem: https://leetcode.com/problems/count-unhappy-friends
#
# You are given a list of preferences for n friends, where n is always even.
# 
# For each person i, preferences[i] contains a list of friends sorted in the order
# of preference. In other words, a friend earlier in the list is more preferred
# than a friend later in the list. Friends in each list are denoted by integers
# from 0 to n-1.
# 
# All the friends are divided into pairs. The pairings are given in a
# list pairs, where pairs[i] = [xᵢ, yᵢ] denotes xᵢ is paired with yᵢ and yᵢ is
# paired with xᵢ.
# 
# However, this pairing may cause some of the friends to be unhappy. A friend x is
# unhappy if x is paired with y and there exists a friend u who is paired with
# v but:
#         
#   * x prefers u over y, and
#   * u prefers x over v.
# 
# Return the number of unhappy friends.
# 
# Example 1:
# Input: n = 4, preferences = [[1, 2, 3], [3, 2, 0], [3, 1, 0], [1, 2, 0]], pairs
# = [[0, 1], [2, 3]]
# Output: 2
# 
# Explanation:
# Friend 1 is unhappy because:
# - 1 is paired with 0 but prefers 3 over 0, and
# - 3 prefers 1 over 2.
# Friend 3 is unhappy because:
# - 3 is paired with 2 but prefers 1 over 2, and
# - 1 prefers 3 over 0.
# Friends 0 and 2 are happy.
# 
# Example 2:
# 
# Input: n = 2, preferences = [[1], [0]], pairs = [[1, 0]]
# Output: 0
# 
# Explanation: Both friends 0 and 1 are happy.
# 
# Example 3:
# 
# Input: n = 4, preferences = [[1, 3, 2], [2, 3, 0], [1, 3, 0], [0, 2, 1]], pairs
# = [[1, 3], [0, 2]]
# Output: 4
# 
# 
# Constraints:
#         2 <= n <= 500
#         n is even.
#         preferences.length == n
#         preferences[i].length == n - 1
#         0 <= preferences[i][j] <= n - 1
#         preferences[i] does not contain i.
#         All values in preferences[i] are unique.
#         pairs.length == n/2
#         pairs[i].length == 2
#         xᵢ != yᵢ
#         0 <= xᵢ, yᵢ <= n - 1
#         Each person is contained in exactly one pair.


# Solution: https://algo.monster/liteproblems/1583
# Credit: AlgoMonster
def unhappy_friends(n, preferences, pairs):
    # Build preference ranking dictionaries for each person
    # preference_rank[person][friend] = rank (lower rank means higher preference)
    preference_rank = []
    for person_preferences in preferences:
        rank_dict = {}
        for rank, friend in enumerate(person_preferences):
            rank_dict[friend] = rank
        preference_rank.append(rank_dict)
    
    # Build a dictionary to store each person's paired partner
    # partner_map[person] = their_partner
    partner_map = {}
    for person_x, person_y in pairs:
        partner_map[person_x] = person_y
        partner_map[person_y] = person_x
    
    # Count the number of unhappy people
    unhappy_count = 0
    
    # Check each person to see if they are unhappy
    for person_x in range(n):
        # Get x's current partner
        partner_y = partner_map[person_x]
        
        # Check all people that x prefers over their current partner y
        rank_of_y = preference_rank[person_x][partner_y]
        for rank in range(rank_of_y):
            # Get a person u that x prefers over y
            preferred_person_u = preferences[person_x][rank]
            
            # Get u's current partner
            partner_v = partner_map[preferred_person_u]
            
            # Check if u also prefers x over their current partner v
            # If u's rank for x is less than u's rank for v, then u prefers x over v
            if preference_rank[preferred_person_u][person_x] < preference_rank[preferred_person_u][partner_v]:
                # Found a case where x and u prefer each other over their current partners
                # So person x is unhappy
                unhappy_count += 1
                break
    
    return unhappy_count
    # Time: O(n²)
    # Space: O(n²)

# Alternative Solution: https://leetcode.com/problems/count-unhappy-friends/solutions/3766612/python-3-4-lines-w-explanation-ts-97-96-l2v99
# Credit: Capt Spaulding -> https://leetcode.com/u/Spaulding_/
def unhappy_friends_alt(n, preferences, pairs):
    from collections import defaultdict

    sc = defaultdict()

    for u,v in pairs:  
        sc[u],sc[v] = (preferences[u][:preferences[u].index(v)],
                                        preferences[v][:preferences[v].index(u)])
        
    return sum(any(u in sc[v] for v in sc[u]) for u in range(n))
    # Time: O(n³)
    # Space: O(n²)


def main():
    result = unhappy_friends(n = 4, preferences = [[1, 2, 3], [3, 2, 0], [3, 1, 0], [1, 2, 0]], pairs = [[0, 1], [2, 3]])
    print(result) # 2

    result = unhappy_friends(n = 2, preferences = [[1], [0]], pairs = [[1, 0]])
    print(result) # 0

    result = unhappy_friends(n = 4, preferences = [[1, 3, 2], [2, 3, 0], [1, 3, 0], [0, 2, 1]], pairs = [[1, 3], [0, 2]])
    print(result) # 4

if __name__ == "__main__":
    main()
