# -----------------------------------------------------
# 1013. Partition Array Into Three Parts With Equal Sum
# -----------------------------------------------------

# Problem: https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum
#
# Given an array of integers arr, return true if we can partition the array into
# three non-empty parts with equal sums.
# 
# Formally, we can partition the array if we can find indexes i + 1 < j with
# (arr[0] + arr[1] + ... + arr[i] == arr[i + 1] + arr[i + 2] + ... + arr[j - 1] ==
# arr[j] + arr[j + 1] + ... + arr[arr.length - 1])
# 
# Example 1:
# 
# Input: arr = [0,2,1,-6,6,-7,9,1,2,0,1]
# Output: true
# 
# Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
# 
# Example 2:
# 
# Input: arr = [0,2,1,-6,6,7,9,-1,2,0,1]
# Output: false
# 
# Example 3:
# 
# Input: arr = [3,3,6,5,-2,2,5,1,-9,4]
# Output: true
# 
# Explanation: 3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4
# 
# 
# Constraints:
#         3 <= arr.length <= 5 * 10⁴
#         -10⁴ <= arr[i] <= 10⁴


# Solution: https://algo.monster/liteproblems/1013
# Credit: AlgoMonster
def can_three_parts_equal_sum(arr):
    # Calculate the total sum and check if it's divisible by 3
    target_sum, remainder = divmod(sum(arr), 3)
    
    # If the total sum is not divisible by 3, we can't partition into 3 equal parts
    if remainder != 0:
        return False
    
    # Count how many partitions with the target sum we can find
    partition_count = 0
    current_sum = 0
    
    # Iterate through the array to find partitions
    for num in arr:
        current_sum += num
        
        # When we reach the target sum, we found a valid partition
        if current_sum == target_sum:
            partition_count += 1
            current_sum = 0  # Reset for the next partition
    
    # We need at least 3 partitions (the last partition is implicit)
    # If we found at least 2 partitions explicitly, the remaining elements
    # automatically form the third partition with the same sum
    return partition_count >= 3
    # Time: O(n)
    # Space: O(1)


def main():
    result = can_three_parts_equal_sum(arr = [0,2,1,-6,6,-7,9,1,2,0,1])
    print(result) # True

    result = can_three_parts_equal_sum(arr = [0,2,1,-6,6,7,9,-1,2,0,1])
    print(result) # False

    result = can_three_parts_equal_sum(arr = [3,3,6,5,-2,2,5,1,-9,4])
    print(result) # True

if __name__ == "__main__":
    main()
