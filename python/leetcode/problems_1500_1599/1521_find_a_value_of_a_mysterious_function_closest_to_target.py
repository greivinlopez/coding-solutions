# -------------------------------------------------------------
# 1521. Find a Value of a Mysterious Function Closest to Target
# -------------------------------------------------------------

# Problem: https://leetcode.com/problems/find-a-value-of-a-mysterious-function-closest-to-target
#
# https://assets.leetcode.com/uploads/2020/07/09/change.png
# 
# Winston was given the above mysterious function func. He has an integer array
# arr and an integer target and he wants to find the values l and r that make the
# value |func(arr, l, r) - target| minimum possible.
# 
# Return the minimum possible value of |func(arr, l, r) - target|.
# 
# Notice that func should be called with the values l and r where 0 <= l, 
# r < arr.length.
# 
# Example 1:
# 
# Input: arr = [9,12,3,7,15], target = 5
# Output: 2
# 
# Explanation: Calling func with all the pairs of [l,r] = [[0,0],[1,1],[2,2],[3,3]
# ,[4,4],[0,1],[1,2],[2,3],[3,4],[0,2],[1,3],[2,4],[0,3],[1,4],[0,4]], Winston got
# the following results [9,12,3,7,15,8,0,3,7,0,0,3,0,0,0]. The value closest to 5
# is 7 and 3, thus the minimum difference is 2.
# 
# Example 2:
# 
# Input: arr = [1000000,1000000,1000000], target = 1
# Output: 999999
# 
# Explanation: Winston called the func with all possible values of [l,r] and he
# always got 1000000, thus the min difference is 999999.
# 
# Example 3:
# 
# Input: arr = [1,2,4,8,16], target = 0
# Output: 0
# 
# 
# Constraints:
#         1 <= arr.length <= 10⁵
#         1 <= arr[i] <= 10⁶
#         0 <= target <= 10⁷


# Solution: https://algo.monster/liteproblems/1521
# Credit: AlgoMonster
def closest_to_target(arr, target):
    # Initialize the minimum difference with the first element
    min_difference = abs(arr[0] - target)
    
    # Set to store all possible AND values ending at current position
    current_and_values = {arr[0]}
    
    # Iterate through each element in the array
    for num in arr:
        # Create new set of AND values by:
        # 1. AND-ing current number with all previous AND values
        # 2. Including the current number itself as a new subsequence start
        current_and_values = {num & prev_value for prev_value in current_and_values} | {num}
        
        # Update minimum difference by checking all current AND values
        min_difference = min(min_difference, min(abs(and_value - target) for and_value in current_and_values))
    
    return min_difference
    # Time: O(n * log(max(arr)))
    # Space: O(log(max(arr)))


def main():
    result = closest_to_target(arr = [9,12,3,7,15], target = 5)
    print(result) # 2

    result = closest_to_target(arr = [1000000,1000000,1000000], target = 1)
    print(result) # 999999

    result = closest_to_target(arr = [1,2,4,8,16], target = 0)
    print(result) # 0

if __name__ == "__main__":
    main()
