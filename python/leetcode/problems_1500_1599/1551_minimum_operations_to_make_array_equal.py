# --------------------------------------------
# 1551. Minimum Operations to Make Array Equal
# --------------------------------------------

# Problem: https://leetcode.com/problems/minimum-operations-to-make-array-equal
#
# You have an array arr of length n where arr[i] = (2 * i) + 1 for all valid
# values of i (i.e., 0 <= i < n).
# 
# In one operation, you can select two indices x and y where 0 <= x, y < n and
# subtract 1 from arr[x] and add 1 to arr[y] (i.e., perform arr[x] -=1 and arr[y]
# += 1). The goal is to make all the elements of the array equal. It is guaranteed
# that all the elements of the array can be made equal using some operations.
# 
# Given an integer n, the length of the array, return the minimum number of
# operations needed to make all the elements of arr equal.
# 
# Example 1:
# 
# Input: n = 3
# Output: 2
# 
# Explanation: arr = [1, 3, 5]
# First operation choose x = 2 and y = 0, this leads arr to be [2, 3, 4]
# In the second operation choose x = 2 and y = 0 again, thus arr = [3, 3, 3].
# 
# Example 2:
# 
# Input: n = 6
# Output: 9
# 
# 
# Constraints:
#         1 <= n <= 10⁴


# Solution: https://algo.monster/liteproblems/1551
# Credit: AlgoMonster
def min_operations(n):
    # For the first half of elements (those less than n),
    # calculate how many operations needed to bring them up to n
    half_n = n // 2
    total_operations = 0
    
    for i in range(half_n):
        # Calculate the i-th element value: 2*i + 1
        element_value = 2 * i + 1
        # Add the difference between target (n) and current element
        total_operations += n - element_value
        
    return total_operations
    # Time: O(n)
    # Space: O(1)


def main():
    result = min_operations(n = 3)
    print(result) # 2

    result = min_operations(n = 6)
    print(result) # 9

if __name__ == "__main__":
    main()
