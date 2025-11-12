# --------------------------------------------
# 1389. Create Target Array in the Given Order
# --------------------------------------------

# Problem: https://leetcode.com/problems/create-target-array-in-the-given-order
#
# Given two arrays of integers nums and index. Your task is to create target array
# under the following rules:
#         
#   * Initially target array is empty.
#   * From left to right read nums[i] and index[i], insert at index index[i] the 
#     value nums[i] in target array.
#   * Repeat the previous step until there are no elements to read in nums and index.
# 
# Return the target array.
# 
# It is guaranteed that the insertion operations will be valid.
# 
# Example 1:
# 
# Input: nums = [0,1,2,3,4], index = [0,1,2,2,1]
# Output: [0,4,1,3,2]
# 
# Explanation:
# nums       index     target
# 0            0        [0]
# 1            1        [0,1]
# 2            2        [0,1,2]
# 3            2        [0,1,3,2]
# 4            1        [0,4,1,3,2]
# 
# Example 2:
# 
# Input: nums = [1,2,3,4,0], index = [0,1,2,3,0]
# Output: [0,1,2,3,4]
# 
# Explanation:
# nums       index     target
# 1            0        [1]
# 2            1        [1,2]
# 3            2        [1,2,3]
# 4            3        [1,2,3,4]
# 0            0        [0,1,2,3,4]
# 
# Example 3:
# 
# Input: nums = [1], index = [0]
# Output: [1]
# 
# 
# Constraints:
#         1 <= nums.length, index.length <= 100
#         nums.length == index.length
#         0 <= nums[i] <= 100
#         0 <= index[i] <= i


# Solution: https://algo.monster/liteproblems/1389
# Credit: AlgoMonster
def create_target_array(nums, index):
    # Initialize an empty list to store the target array
    target = []
    
    # Iterate through nums and index arrays simultaneously
    # For each pair (num_value, insert_position), insert num_value at insert_position
    for num_value, insert_position in zip(nums, index):
        # Insert the current number at the specified index position
        # If elements exist at or after this position, they shift to the right
        target.insert(insert_position, num_value)
    
    # Return the constructed target array
    return target
    # Time: O(n²)
    # Space: O(n)

# Solution: https://leetcode.com/problems/create-target-array-in-the-given-order/solutions/805009/three-solutions-in-python-3-by-denisrasu-xhgb
# Credit: Denis Rasulev -> https://leetcode.com/u/denisrasulev/
def create_target_array_alt(nums, index):
    lst = []
    for i in range(len(nums)):
        lst = lst[:index[i]] + [nums[i]] + lst[index[i]:]
    return lst
    # Time: O(n²)
    # Space: O(n)


def main():
    result = create_target_array(nums = [0,1,2,3,4], index = [0,1,2,2,1])
    print(result) # [0, 4, 1, 3, 2]

    result = create_target_array(nums = [1,2,3,4,0], index = [0,1,2,3,0])
    print(result) # [0, 1, 2, 3, 4]

    result = create_target_array(nums = [1], index = [0])
    print(result) # [1]

if __name__ == "__main__":
    main()
