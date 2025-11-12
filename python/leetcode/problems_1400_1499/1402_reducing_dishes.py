# ------------------------
# 1402. Reducing Dishes 🍱
# ------------------------

# Problem: https://leetcode.com/problems/reducing-dishes
#
# A chef has collected data on the satisfaction level of his n dishes. Chef can
# cook any dish in 1 unit of time.
# 
# Like-time coefficient of a dish is defined as the time taken to cook that dish
# including previous dishes multiplied by its satisfaction level i.e. 
# time[i] * satisfaction[i].
# 
# Return the maximum sum of like-time coefficient that the chef can obtain after
# preparing some amount of dishes.
# 
# Dishes can be prepared in any order and the chef can discard some dishes to get
# this maximum value.
# 
# Example 1:
# 
# Input: satisfaction = [-1,-8,0,5,-9]
# Output: 14
# 
# Explanation: After Removing the second and last dish, the maximum total like-
# time coefficient will be equal to (-1*1 + 0*2 + 5*3 = 14).
# Each dish is prepared in one unit of time.
# 
# Example 2:
# 
# Input: satisfaction = [4,3,2]
# Output: 20
# 
# Explanation: Dishes can be prepared in any order, (2*1 + 3*2 + 4*3 = 20)
# 
# Example 3:
# 
# Input: satisfaction = [-1,-4,-5]
# Output: 0
# 
# Explanation: People do not like the dishes. No dish is prepared.
# 
# 
# Constraints:
#         n == satisfaction.length
#         1 <= n <= 500
#         -1000 <= satisfaction[i] <= 1000


# Solution: https://algo.monster/liteproblems/1402
# Credit: AlgoMonster
def max_satisfaction(satisfaction):
    # Sort dishes by satisfaction in descending order (highest satisfaction first)
    satisfaction.sort(reverse=True)
    
    # Initialize result and cumulative sum
    max_like_time_coefficient = 0
    cumulative_sum = 0
    
    # Iterate through dishes from highest to lowest satisfaction
    for dish_satisfaction in satisfaction:
        # Add current dish to cumulative sum
        cumulative_sum += dish_satisfaction
        
        # If adding this dish (and all previous dishes) would decrease total satisfaction, stop
        if cumulative_sum <= 0:
            break
        
        # Add cumulative sum to result
        # This effectively adds each dish's satisfaction multiplied by its position
        # when dishes are served in ascending order of satisfaction
        max_like_time_coefficient += cumulative_sum
    
    return max_like_time_coefficient
    # Time: O(n * log n)
    # Space: O(log n)


def main():
    result = max_satisfaction(satisfaction = [-1,-8,0,5,-9])
    print(result) # 14

    result = max_satisfaction(satisfaction = [4,3,2])
    print(result) # 20

    result = max_satisfaction(satisfaction = [-1,-4,-5])
    print(result) # 0

if __name__ == "__main__":
    main()
