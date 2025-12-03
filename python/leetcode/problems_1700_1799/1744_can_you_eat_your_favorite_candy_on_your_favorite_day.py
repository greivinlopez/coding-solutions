# --------------------------------------------------------------
# 1744. Can You Eat Your Favorite Candy on Your Favorite Day? 🍫
# --------------------------------------------------------------

# Problem: https://leetcode.com/problems/can-you-eat-your-favorite-candy-on-your-favorite-day
#
# You are given a (0-indexed) array of positive integers candiesCount where
# candiesCount[i] represents the number of candies of the iᵗʰ type you have. You
# are also given a 2D array queries where queries[i] = [favoriteTypeᵢ,
# favoriteDayᵢ, dailyCapᵢ].
# 
# You play a game with the following rules:
#         
#   * You start eating candies on day 0.
#   * You cannot eat any candy of type i unless you have eaten all candies of
#     type i - 1.
#   * You must eat at least one candy per day until you have eaten all the
#     candies.
# 
# Construct a boolean array answer such that answer.length == queries.length and
# answer[i] is true if you can eat a candy of type favoriteTypeᵢ on day
# favoriteDayᵢ without eating more than dailyCapᵢ candies on any day, and false
# otherwise. Note that you can eat different types of candy on the same day,
# provided that you follow rule 2.
# 
# Return the constructed array answer.
# 
# Example 1:
# 
# Input: candiesCount = [7,4,5,3,8], queries = [[0,2,2],[4,2,4],[2,13,1000000000]]
# Output: [true,false,true]
# 
# Explanation:
# 1- If you eat 2 candies (type 0) on day 0 and 2 candies (type 0) on day 1, you
# will eat a candy of type 0 on day 2.
# 2- You can eat at most 4 candies each day.
#    If you eat 4 candies every day, you will eat 4 candies (type 0) on day 0 and
# 4 candies (type 0 and type 1) on day 1.
#    On day 2, you can only eat 4 candies (type 1 and type 2), so you cannot eat a
# candy of type 4 on day 2.
# 3- If you eat 1 candy each day, you will eat a candy of type 2 on day 13.
# 
# Example 2:
# 
# Input: candiesCount = [5,2,6,4,1], queries =
# [[3,1,2],[4,10,3],[3,10,100],[4,100,30],[1,3,1]]
# Output: [false,true,true,false,false]
# 
# 
# Constraints:
#         1 <= candiesCount.length <= 10⁵
#         1 <= candiesCount[i] <= 10⁵
#         1 <= queries.length <= 10⁵
#         queries[i].length == 3
#         0 <= favoriteTypei < candiesCount.length
#         0 <= favoriteDayi <= 10⁹
#         1 <= dailyCapi <= 10⁹


# Solution: https://algo.monster/liteproblems/1744
# Credit: AlgoMonster
def can_eat(candiesCount, queries):
    from itertools import accumulate
    
    # Calculate prefix sum of candies (cumulative sum)
    # prefix_sum[i] represents total candies from type 0 to type i-1
    prefix_sum = list(accumulate(candiesCount, initial=0))
    
    result = []
    
    for favorite_type, favorite_day, daily_cap in queries:
        # Minimum candies eaten: eat 1 candy per day until favorite_day
        min_candies_eaten = favorite_day
        
        # Maximum candies eaten: eat daily_cap candies per day through favorite_day
        max_candies_eaten = (favorite_day + 1) * daily_cap
        
        # Check if we can eat favorite_type candy on favorite_day
        # We need to have eaten enough to reach favorite_type candies (> prefix_sum[favorite_type])
        # But not so many that we've already consumed all of them (< prefix_sum[favorite_type + 1])
        can_eat_favorite = (min_candies_eaten < prefix_sum[favorite_type + 1] and 
                            max_candies_eaten > prefix_sum[favorite_type])
        
        result.append(can_eat_favorite)
    
    return result
    # Time: O(n + q)
    # Space: O(n)
    # q = the length of queries.


def main():
    result = can_eat(candiesCount = [7,4,5,3,8], queries = [[0,2,2],[4,2,4],[2,13,1000000000]])
    print(result) # [True, False, True]

    result = can_eat(candiesCount = [5,2,6,4,1], queries = [[3,1,2],[4,10,3],[3,10,100],[4,100,30],[1,3,1]])
    print(result) # [False, True, True, False, False]

if __name__ == "__main__":
    main()
