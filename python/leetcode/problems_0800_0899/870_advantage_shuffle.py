# ----------------------
# 870. Advantage Shuffle
# ----------------------

# Problem: https://leetcode.com/problems/advantage-shuffle
#
# You are given two integer arrays nums1 and nums2 both of the same length. The
# advantage of nums1 with respect to nums2 is the number of indices i for which
# nums1[i] > nums2[i].
# 
# Return any permutation of nums1 that maximizes its advantage with respect to
# nums2.
# 
# Example 1:
# 
# Input: nums1 = [2,7,11,15], nums2 = [1,10,4,11]
# Output: [2,11,7,15]
# 
# Example 2:
# 
# Input: nums1 = [12,24,8,32], nums2 = [13,25,32,11]
# Output: [24,32,8,12]
# 
# 
# Constraints:
#         1 <= nums1.length <= 10⁵
#         nums2.length == nums1.length
#         0 <= nums1[i], nums2[i] <= 10⁹


# Solution: https://algo.monster/liteproblems/870
# Credit: AlgoMonster
def advantage_count(nums1, nums2):
    # Sort nums1 in ascending order for greedy matching
    nums1.sort()
    
    # Create tuples of (value, original_index) from nums2 and sort by value
    # This allows us to track original positions while working with sorted values
    sorted_nums2_with_indices = sorted((value, index) for index, value in enumerate(nums2))
    
    # Get the length of the arrays
    n = len(nums2)
    
    # Initialize result array with zeros
    result = [0] * n
    
    # Two pointers: left for smallest unmatched in nums2, right for largest unmatched
    left_pointer = 0
    right_pointer = n - 1
    
    # Greedy strategy: iterate through sorted nums1
    for num in nums1:
        # If current number from nums1 cannot beat the smallest unmatched from nums2
        if num <= sorted_nums2_with_indices[left_pointer][0]:
            # Use this number against the largest unmatched element (sacrifice strategy)
            original_index = sorted_nums2_with_indices[right_pointer][1]
            result[original_index] = num
            right_pointer -= 1
        else:
            # Current number can beat the smallest unmatched, so match them
            original_index = sorted_nums2_with_indices[left_pointer][1]
            result[original_index] = num
            left_pointer += 1
    
    return result
    # Time: O(n * log(n))
    # Space: O(n)


def main():
    result = advantage_count(nums1 = [2,7,11,15], nums2 = [1,10,4,11])
    print(result) # [2,11,7,15]

    result = advantage_count(nums1 = [12,24,8,32], nums2 = [13,25,32,11])
    print(result) # [24,32,8,12]

if __name__ == "__main__":
    main()
