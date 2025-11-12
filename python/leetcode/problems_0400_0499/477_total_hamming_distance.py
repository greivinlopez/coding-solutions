# ---------------------------
# 477. Total Hamming Distance
# ---------------------------

# Problem: https://leetcode.com/problems/total-hamming-distance
#
# The Hamming distance between two integers is the number of positions at which
# the corresponding bits are different.
# 
# Given an integer array nums, return the sum of Hamming distances between all the
# pairs of the integers in nums.
# 
# Example 1:
# 
# Input: nums = [4,14,2]
# Output: 6
# 
# Explanation: In binary representation, the 4 is 0100, 14 is 1110, and 2 is 0010
# (just
# showing the four bits relevant in this case).
# The answer will be:
# HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2
# + 2 = 6.
# 
# Example 2:
# 
# Input: nums = [4,14,4]
# Output: 4
# 
# 
# Constraints:
#         1 <= nums.length <= 10⁴
#         0 <= nums[i] <= 10⁹
#         The answer for the given input will fit in a 32-bit integer.


# Solution: https://algo.monster/liteproblems/477
# Credit: AlgoMonster
def total_hamming_distance(nums):
    total_distance = 0
    array_length = len(nums)
    
    # Check each bit position (0 to 31 for 32-bit integers)
    for bit_position in range(32):
        # Count how many numbers have a 1 at this bit position
        ones_count = sum((num >> bit_position) & 1 for num in nums)
        
        # Count how many numbers have a 0 at this bit position
        zeros_count = array_length - ones_count
        
        # For this bit position, the contribution to total Hamming distance
        # is the number of (1, 0) pairs, which equals ones_count * zeros_count
        total_distance += ones_count * zeros_count
    
    return total_distance
    # Time: O(n)
    # Space: O(1)


def main():
    result = total_hamming_distance([4,14,2])
    print(result) # 6

    result = total_hamming_distance([4,14,4])
    print(result) # 4

if __name__ == "__main__":
    main()
