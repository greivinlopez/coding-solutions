# -----------------
# 1340. Jump Game V
# -----------------

# Problem: https://leetcode.com/problems/jump-game-v
#
# Given an array of integers arr and an integer d. In one step you can jump from
# index i to index:
#         
#   * i + x where: i + x < arr.length and  0 < x <= d.
#   * i - x where: i - x >= 0 and  0 < x <= d.
# 
# In addition, you can only jump from index i to index j if arr[i] > arr[j] and
# arr[i] > arr[k] for all indices k between i and j (More formally min(i, j) < k <
# max(i, j)).
# 
# You can choose any index of the array and start jumping. Return the maximum
# number of indices you can visit.
# 
# Notice that you can not jump outside of the array at any time.
# 
# Example 1:
# 
# Input: arr = [6,4,14,6,8,13,9,7,10,6,12], d = 2
# Output: 4
# 
# Explanation: You can start at index 10. You can jump 10 --> 8 --> 6 --> 7 as
# shown.
# Note that if you start at index 6 you can only jump to index 7. You cannot jump
# to index 5 because 13 > 9. You cannot jump to index 4 because index 5 is between
# index 4 and 6 and 13 > 9.
# Similarly You cannot jump from index 3 to index 2 or index 1.
# 
# Example 2:
# 
# Input: arr = [3,3,3,3,3], d = 3
# Output: 1
# 
# Explanation: You can start at any index. You always cannot jump to any index.
# 
# Example 3:
# 
# Input: arr = [7,6,5,4,3,2,1], d = 1
# Output: 7
# 
# Explanation: Start at index 0. You can visit all the indicies.
# 
# 
# Constraints:
#         1 <= arr.length <= 1000
#         1 <= arr[i] <= 10⁵
#         1 <= d <= arr.length


# Solution: https://algo.monster/liteproblems/1340
# Credit: AlgoMonster
def max_jumps(arr, d):
    from functools import cache

    @cache
    def dfs(index):
        # Start with 1 (counting current index)
        max_jumps = 1
        
        # Try jumping to the left (indices before current)
        for next_index in range(index - 1, -1, -1):
            # Stop if distance exceeds d or we hit a taller/equal element
            if index - next_index > d or arr[next_index] >= arr[index]:
                break
            # Update max jumps if jumping to next_index gives better result
            max_jumps = max(max_jumps, 1 + dfs(next_index))
        
        # Try jumping to the right (indices after current)
        for next_index in range(index + 1, array_length):
            # Stop if distance exceeds d or we hit a taller/equal element
            if next_index - index > d or arr[next_index] >= arr[index]:
                break
            # Update max jumps if jumping to next_index gives better result
            max_jumps = max(max_jumps, 1 + dfs(next_index))
        
        return max_jumps
    
    # Store array length for efficiency
    array_length = len(arr)
    
    # Find maximum jumps starting from each index
    return max(dfs(i) for i in range(array_length))
    # Time: O(n * d)
    # Space: O(n)


def main():
    result = max_jumps(arr = [6,4,14,6,8,13,9,7,10,6,12], d = 2)
    print(result) # 4

    result = max_jumps(arr = [3,3,3,3,3], d = 3)
    print(result) # 1

    result = max_jumps(arr = [7,6,5,4,3,2,1], d = 1)
    print(result) # 7

if __name__ == "__main__":
    main()
