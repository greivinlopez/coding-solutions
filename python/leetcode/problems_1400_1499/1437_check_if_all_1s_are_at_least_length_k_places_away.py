# --------------------------------------------------------
# 1437. Check If All 1's Are at Least Length K Places Away
# --------------------------------------------------------

# Problem: https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away
#
# Given an binary array nums and an integer k, return true if all 1's are at least
# k places away from each other, otherwise return false.
# 
# Example 1:
# 
# Input: nums = [1,0,0,0,1,0,0,1], k = 2
# Output: true
# 
# Explanation: Each of the 1s are at least 2 places away from each other.
# 
# Example 2:
# 
# Input: nums = [1,0,0,1,0,1], k = 2
# Output: false
# 
# Explanation: The second 1 and third 1 are only one apart from each other.
# 
# 
# Constraints:
#         1 <= nums.length <= 10⁵
#         0 <= k <= nums.length
#         nums[i] is 0 or 1


# Solution: https://algo.monster/liteproblems/1437
# Credit: AlgoMonster
def k_length_apart(nums, k):
    # Initialize the position of the last seen 1 to negative infinity
    # This ensures the first 1 doesn't fail the distance check
    last_one_position = float('-inf')
    
    # Iterate through the array with indices
    for current_index, value in enumerate(nums):
        # Check if current element is 1
        if value == 1:
            # Calculate distance between current 1 and previous 1
            # Subtract 1 because we count only the elements between them
            distance_between_ones = current_index - last_one_position - 1
            
            # If distance is less than k, the condition is violated
            if distance_between_ones < k:
                return False
            
            # Update the position of the last seen 1
            last_one_position = current_index
    
    # All 1s satisfy the distance requirement
    return True
    # Time: O(n)
    # Space: O(1)


def main():
    result = k_length_apart(nums = [1,0,0,0,1,0,0,1], k = 2)
    print(result) # True

    result = k_length_apart(nums = [1,0,0,1,0,1], k = 2)
    print(result) # False

if __name__ == "__main__":
    main()
