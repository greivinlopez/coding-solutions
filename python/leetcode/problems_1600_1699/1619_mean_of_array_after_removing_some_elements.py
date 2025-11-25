# ------------------------------------------------
# 1619. Mean of Array After Removing Some Elements
# ------------------------------------------------

# Problem: https://leetcode.com/problems/mean-of-array-after-removing-some-elements
#
# Given an integer array arr, return the mean of the remaining integers after
# removing the smallest 5% and the largest 5% of the elements.
# 
# Answers within 10⁻⁵ of the actual answer will be considered accepted.
# 
# Example 1:
# 
# Input: arr = [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3]
# Output: 2.00000
# 
# Explanation: After erasing the minimum and the maximum values of this array, all
# elements are equal to 2, so the mean is 2.
# 
# Example 2:
# 
# Input: arr = [6,2,7,5,1,2,0,3,10,2,5,0,5,5,0,8,7,6,8,0]
# Output: 4.00000
# 
# Example 3:
# 
# Input: arr = [6,0,7,0,7,5,7,8,3,4,0,7,8,1,6,8,1,1,2,4,8,1,9,5,4,3,8,5,10,8,6,6,1
# ,0,6,10,8,2,3,4]
# Output: 4.77778
# 
# 
# Constraints:
#         20 <= arr.length <= 1000
#         arr.length is a multiple of 20.
#         0 <= arr[i] <= 10⁵


# Solution: https://algo.monster/liteproblems/1619
# Credit: AlgoMonster
def trim_mean(arr) :
    # Get the total number of elements
    n = len(arr)
    
    # Calculate indices for 5% and 95% positions
    # These represent the start and end of our trimmed range
    trim_start_index = int(n * 0.05)
    trim_end_index = int(n * 0.95)
    
    # Sort the array to identify smallest and largest elements
    arr.sort()
    
    # Extract the middle 90% of elements (removing smallest 5% and largest 5%)
    trimmed_array = arr[trim_start_index:trim_end_index]
    
    # Calculate and return the mean of trimmed elements, rounded to 5 decimal places
    trimmed_mean = sum(trimmed_array) / len(trimmed_array)
    return round(trimmed_mean, 5)
    # Time: O(n log n)
    # Space: O(n)


def main():
    result = trim_mean(arr = [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3])
    print(result) # 2.0

    result = trim_mean(arr = [6,2,7,5,1,2,0,3,10,2,5,0,5,5,0,8,7,6,8,0])
    print(result) # 4.0

    result = trim_mean(arr = [6,0,7,0,7,5,7,8,3,4,0,7,8,1,6,8,1,1,2,4,8,1,9,5,4,3,8,5,10,8,6,6,1,0,6,10,8,2,3,4])
    print(result) # 4.77778

if __name__ == "__main__":
    main()
