# -----------------------------
# 532. K-diff Pairs in an Array
# -----------------------------

# Problem: https://leetcode.com/problems/k-diff-pairs-in-an-array
#
# Given an array of integers nums and an integer k, return the number of unique
# k-diff pairs in the array.
# 
# A k-diff pair is an integer pair (nums[i], nums[j]), where the following are
# true:
# 
#         0 <= i, j < nums.length
#         i != j
#         |nums[i] - nums[j]| == k
# 
# Notice that |val| denotes the absolute value of val.
# 
# Example 1:
# 
# Input: nums = [3,1,4,1,5], k = 2
# Output: 2
# 
# Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
# Although we have two 1s in the input, we should only return the number of unique
# pairs.
# 
# Example 2:
# 
# Input: nums = [1,2,3,4,5], k = 1
# Output: 4
# 
# Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4)
# and (4, 5).
# 
# Example 3:
# 
# Input: nums = [1,3,1,5,4], k = 0
# Output: 1
# 
# Explanation: There is one 0-diff pair in the array, (1, 1).
# 
# 
# Constraints:
#         1 <= nums.length <= 10⁴
#         -10⁷ <= nums[i] <= 10⁷
#         0 <= k <= 10⁷


# Solution: https://algo.monster/liteproblems/532
# Credit: AlgoMonster
def find_pairs(nums, k):
    # Set to store unique pairs (represented by the smaller value in each pair)
    unique_pairs = set()
    
    # Set to track numbers we've already seen
    seen_numbers = set()
    
    # Iterate through each number in the array
    for current_num in nums:
        # Check if (current_num - k, current_num) forms a valid pair
        # If current_num - k was seen before, we found a pair
        if current_num - k in seen_numbers:
            unique_pairs.add(current_num - k)
        
        # Check if (current_num, current_num + k) forms a valid pair
        # If current_num + k was seen before, we found a pair
        if current_num + k in seen_numbers:
            unique_pairs.add(current_num)
        
        # Add current number to the set of seen numbers
        seen_numbers.add(current_num)
    
    # Return the count of unique k-diff pairs
    return len(unique_pairs)
    # Time: O(n)
    # Space: O(n)


def main():
    result = find_pairs(nums = [3,1,4,1,5], k = 2)
    print(result) # 2

    result = find_pairs(nums = [1,2,3,4,5], k = 1)
    print(result) # 4

    result = find_pairs(nums = [1,3,1,5,4], k = 0)
    print(result) # 1

if __name__ == "__main__":
    main()
