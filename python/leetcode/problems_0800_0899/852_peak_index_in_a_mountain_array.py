# -----------------------------------
# 852. Peak Index in a Mountain Array
# -----------------------------------

# Problem: https://leetcode.com/problems/peak-index-in-a-mountain-array
#
# You are given an integer mountain array arr of length n where the values
# increase to a peak element and then decrease.
# 
# Return the index of the peak element.
# 
# Your task is to solve it in O(log(n)) time complexity.
# 
# Example 1:
# 
# Input: arr = [0,1,0]
# Output: 1
# 
# Example 2:
# 
# Input: arr = [0,2,1,0]
# Output: 1
# 
# Example 3:
# 
# Input: arr = [0,10,5,2]
# Output: 1
# 
# 
# Constraints:
#         3 <= arr.length <= 10⁵
#         0 <= arr[i] <= 10⁶
#         arr is guaranteed to be a mountain array.


# Solution: https://algo.monster/liteproblems/852
# Credit: AlgoMonster
def peak_index_in_mountain_array(arr):
    # Initialize binary search boundaries
    # Start from index 1 and end at len(arr) - 2 since the peak cannot be at the edges
    left, right = 1, len(arr) - 2
    
    # Binary search for the peak element
    while left < right:
        # Calculate middle index using bit shift (equivalent to dividing by 2)
        mid = (left + right) >> 1
        
        # Check if we're on the descending slope
        if arr[mid] > arr[mid + 1]:
            # Peak is at mid or to the left of mid
            right = mid
        else:
            # We're on the ascending slope, peak is to the right of mid
            left = mid + 1
    
    # When left == right, we've found the peak index
    return left
    # Time: O(log(n))
    # Space: O(1)


def main():
    result = peak_index_in_mountain_array(arr = [0,1,0])
    print(result) # 1

    result = peak_index_in_mountain_array(arr = [0,2,1,0])
    print(result) # 1

    result = peak_index_in_mountain_array(arr = [0,10,5,2])
    print(result) # 1

if __name__ == "__main__":
    main()
