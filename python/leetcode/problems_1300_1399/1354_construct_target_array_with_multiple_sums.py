# -----------------------------------------------
# 1354. Construct Target Array With Multiple Sums
# -----------------------------------------------

# Problem: https://leetcode.com/problems/construct-target-array-with-multiple-sums
#
# You are given an array target of n integers. From a starting array arr
# consisting of n 1's, you may perform the following procedure :
#         
#   * let x be the sum of all elements currently in your array.
#   * choose index i, such that 0 <= i < n and set the value of arr at index i to x.
#   * You may repeat this procedure as many times as needed.
# 
# Return true if it is possible to construct the target array from arr, otherwise,
# return false.
# 
# Example 1:
# 
# Input: target = [9,3,5]
# Output: true
# 
# Explanation: Start with arr = [1, 1, 1]
# [1, 1, 1], sum = 3 choose index 1
# [1, 3, 1], sum = 5 choose index 2
# [1, 3, 5], sum = 9 choose index 0
# [9, 3, 5] Done
# 
# Example 2:
# 
# Input: target = [1,1,1,2]
# Output: false
# 
# Explanation: Impossible to create target array from [1,1,1,1].
# 
# Example 3:
# 
# Input: target = [8,5]
# Output: true
# 
# 
# Constraints:
#         n == target.length
#         1 <= n <= 5 * 10⁴
#         1 <= target[i] <= 10⁹

from heapq import heapify, heappop, heappush

# Solution: https://algo.monster/liteproblems/1354
# Credit: AlgoMonster
def is_possible(target):
    # Calculate total sum of all elements
    total_sum = sum(target)
    
    # Create max heap (negate values since Python has min heap by default)
    max_heap = [-num for num in target]
    heapify(max_heap)
    
    # Keep reducing the largest element until all elements become 1
    while -max_heap[0] > 1:
        # Get the current maximum element
        current_max = -heappop(max_heap)
        
        # Calculate sum of all other elements
        sum_of_others = total_sum - current_max
        
        # Edge cases where transformation is impossible
        if sum_of_others == 0 or current_max - sum_of_others < 1:
            return False
        
        # Calculate the previous value before this element became current_max
        # Use modulo for optimization when current_max >> sum_of_others
        # If remainder is 0, the previous value was sum_of_others
        previous_value = (current_max % sum_of_others) or sum_of_others
        
        # Push the previous value back to heap
        heappush(max_heap, -previous_value)
        
        # Update total sum
        total_sum = total_sum - current_max + previous_value
    
    # All elements are now 1, transformation is possible
    return True
    # Time: O(n log n + k log n)
    # Space: O(n)
    # n = the length of the array target
    # k = the number of operations needed to reduce all elements to 1.


def main():
    result = is_possible(target = [9,3,5])
    print(result) # True

    result = is_possible(target = [1,1,1,2])
    print(result) # False

    result = is_possible(target = [8,5])
    print(result) # True

if __name__ == "__main__":
    main()
