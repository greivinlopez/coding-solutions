# ------------------------------------
# 1187. Make Array Strictly Increasing
# ------------------------------------

# Problem: https://leetcode.com/problems/make-array-strictly-increasing
#
# Given two integer arrays arr1 and arr2, return the minimum number of operations
# (possibly zero) needed to make arr1 strictly increasing.
# 
# In one operation, you can choose two indices 0 <= i < arr1.length and 0 <= j <
# arr2.length and do the assignment arr1[i] = arr2[j].
# 
# If there is no way to make arr1 strictly increasing, return -1.
# 
# Example 1:
# 
# Input: arr1 = [1,5,3,6,7], arr2 = [1,3,2,4]
# Output: 1
# 
# Explanation: Replace 5 with 2, then arr1 = [1, 2, 3, 6, 7].
# 
# Example 2:
# 
# Input: arr1 = [1,5,3,6,7], arr2 = [4,3,1]
# Output: 2
# 
# Explanation: Replace 5 with 3 and then replace 3 with 4. arr1 = [1, 3, 4, 6, 7].
# 
# Example 3:
# 
# Input: arr1 = [1,5,3,6,7], arr2 = [1,6,3,3]
# Output: -1
# 
# Explanation: You can't make arr1 strictly increasing.
# 
# 
# Constraints:
#         1 <= arr1.length, arr2.length <= 2000
#         0 <= arr1[i], arr2[i] <= 10^9

from bisect import bisect_left

# Solution: https://algo.monster/liteproblems/1187
# Credit: AlgoMonster
def make_array_increasing(arr1, arr2):
    # Sort arr2 and remove duplicates
    arr2.sort()
    unique_count = 0
    for value in arr2:
        # Keep only unique values from arr2
        if unique_count == 0 or value != arr2[unique_count - 1]:
            arr2[unique_count] = value
            unique_count += 1
    arr2 = arr2[:unique_count]
    
    # Add sentinels to arr1 to simplify boundary conditions
    # -inf at start ensures we can always start, inf at end ensures we can always end
    extended_arr = [float('-inf')] + arr1 + [float('inf')]
    n = len(extended_arr)
    
    # dp[i] = minimum operations needed to make extended_arr[0..i] strictly increasing
    dp = [float('inf')] * n
    dp[0] = 0  # No operations needed for the first sentinel
    
    # Process each position in the extended array
    for i in range(1, n):
        # Option 1: Keep current element if it's already greater than previous
        if extended_arr[i - 1] < extended_arr[i]:
            dp[i] = dp[i - 1]
        
        # Option 2: Try replacing previous k elements with values from arr2
        # Find the position in arr2 where we could insert extended_arr[i]
        max_replacement_idx = bisect_left(arr2, extended_arr[i])
        
        # Try replacing k consecutive elements before position i
        for k in range(1, min(i - 1, max_replacement_idx) + 1):
            # Check if we can replace elements [i-k, i-1] with arr2[max_replacement_idx-k:max_replacement_idx]
            # This works if extended_arr[i-k-1] < arr2[max_replacement_idx-k] (maintains strict increasing)
            if extended_arr[i - k - 1] < arr2[max_replacement_idx - k]:
                dp[i] = min(dp[i], dp[i - k - 1] + k)
    
    # Return -1 if impossible, otherwise return the minimum operations
    return -1 if dp[n - 1] >= float('inf') else dp[n - 1]
    # Time: O(n * (log m + min(m, n)))
    # Space: O(n)


def main():
    result = make_array_increasing(arr1 = [1,5,3,6,7], arr2 = [1,3,2,4])
    print(result) # 1

    result = make_array_increasing(arr1 = [1,5,3,6,7], arr2 = [4,3,1])
    print(result) # 2

    result = make_array_increasing(arr1 = [1,5,3,6,7], arr2 = [1,6,3,3])
    print(result) # -1

if __name__ == "__main__":
    main()
