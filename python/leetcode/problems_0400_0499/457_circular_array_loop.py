# ------------------------
# 457. Circular Array Loop
# ------------------------

# Problem: https://leetcode.com/problems/circular-array-loop
#
# You are playing a game involving a circular array of non-zero integers nums.
# Each nums[i] denotes the number of indices forward/backward you must move if you
# are located at index i:
# 
#         If nums[i] is positive, move nums[i] steps forward, and
#         If nums[i] is negative, move nums[i] steps backward.
# 
# Since the array is circular, you may assume that moving forward from the last
# element puts you on the first element, and moving backwards from the first
# element puts you on the last element.
# 
# A cycle in the array consists of a sequence of indices seq of length k where:
#         
#   * Following the movement rules above results in the repeating index sequence 
#     seq[0] -> seq[1] -> ... -> seq[k - 1] -> seq[0] -> ...
#   * Every nums[seq[j]] is either all positive or all negative.
#   * k > 1
# 
# Return true if there is a cycle in nums, or false otherwise.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2022/09/01/img1.jpg
# 
# Input: nums = [2,-1,1,2,2]
# Output: true
# 
# Explanation: The graph shows how the indices are connected. White nodes are
# jumping forward, while red is jumping backward.
# We can see the cycle 0 --> 2 --> 3 --> 0 --> ..., and all of its nodes are white
# (jumping in the same direction).
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2022/09/01/img2.jpg
# 
# Input: nums = [-1,-2,-3,-4,-5,6]
# Output: false
# 
# Explanation: The graph shows how the indices are connected. White nodes are
# jumping forward, while red is jumping backward.
# The only cycle is of size 1, so we return false.
# 
# Example 3:
# 
# https://assets.leetcode.com/uploads/2022/09/01/img3.jpg
# 
# Input: nums = [1,-1,5,1,4]
# Output: true
# 
# Explanation: The graph shows how the indices are connected. White nodes are
# jumping forward, while red is jumping backward.
# We can see the cycle 0 --> 1 --> 0 --> ..., and while it is of size > 1, it has
# a node jumping forward and a node jumping backward, so it is not a cycle.
# We can see the cycle 3 --> 4 --> 3 --> ..., and all of its nodes are white
# (jumping in the same direction).
# 
# 
# Constraints:
#         1 <= nums.length <= 5000
#         -1000 <= nums[i] <= 1000
#         nums[i] != 0
# 
# 
# Follow up: Could you solve it in O(n) time complexity and O(1) extra space
# complexity?


# Solution: https://algo.monster/liteproblems/457
# Credit: AlgoMonster
def circular_array_loop(nums):
    n = len(nums)
    
    def get_next_index(current_index):
        """Calculate the next index in the circular array."""
        # Handle both positive and negative movements with proper wrapping
        # The '+ n' term handles cases where (current_index + nums[current_index] % n) is negative
        return (current_index + nums[current_index] % n + n) % n
    
    # Try each position as a potential starting point for a cycle
    for start_index in range(n):
        # Skip already visited positions (marked as 0)
        if nums[start_index] == 0:
            continue
        
        # Initialize slow and fast pointers for cycle detection
        slow_pointer = start_index
        fast_pointer = get_next_index(start_index)
        
        # Continue while all movements are in the same direction
        # The condition nums[slow] * nums[fast] > 0 ensures same sign (same direction)
        while (nums[slow_pointer] * nums[fast_pointer] > 0 and 
                nums[slow_pointer] * nums[get_next_index(fast_pointer)] > 0):
            
            # Cycle detected
            if slow_pointer == fast_pointer:
                # Check if cycle length > 1 (not a self-loop: nums[i] % n != 0)
                if slow_pointer != get_next_index(slow_pointer):
                    return True
                break
            
            # Move pointers: slow moves one step, fast moves two steps
            slow_pointer = get_next_index(slow_pointer)
            fast_pointer = get_next_index(get_next_index(fast_pointer))
        
        # Mark all positions in this path as visited (set to 0)
        # This optimization prevents revisiting invalid paths
        current_position = start_index
        
        # Only mark path as visited if the current index is still part of the same-sign path
        # (This avoids marking the entire array as 0 if the path is invalid)
        current_sign = nums[current_position]
        while nums[current_position] * current_sign > 0:
            next_position = get_next_index(current_position)
            nums[current_position] = 0 # Mark as visited/invalid
            current_position = next_position
    
    # No valid cycle found
    return False


def main():
    result = circular_array_loop([2,-1,1,2,2])
    print(result) # True

    result = circular_array_loop([-1,-2,-3,-4,-5,6])
    print(result) # False

    result = circular_array_loop([1,-1,5,1,4])
    print(result) # True

if __name__ == "__main__":
    main()
