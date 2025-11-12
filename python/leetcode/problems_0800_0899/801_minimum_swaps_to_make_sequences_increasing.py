# -----------------------------------------------
# 801. Minimum Swaps To Make Sequences Increasing
# -----------------------------------------------

# Problem: https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing
#
# You are given two integer arrays of the same length nums1 and nums2. In one
# operation, you are allowed to swap nums1[i] with nums2[i].
#         
#   * For example, if nums1 = [1,2,3,8], and nums2 = [5,6,7,4], you can swap
#     the element at i = 3 to obtain nums1 = [1,2,3,4] and nums2 = [5,6,7,8].
# 
# Return the minimum number of needed operations to make nums1 and nums2 strictly
# increasing. The test cases are generated so that the given input always makes it
# possible.
# 
# An array arr is strictly increasing if and only if arr[0] < arr[1] < arr[2] <
# ... < arr[arr.length - 1].
# 
# Example 1:
# 
# Input: nums1 = [1,3,5,4], nums2 = [1,2,3,7]
# Output: 1
# 
# Explanation:
# Swap nums1[3] and nums2[3]. Then the sequences are:
# nums1 = [1, 3, 5, 7] and nums2 = [1, 2, 3, 4]
# which are both strictly increasing.
# 
# Example 2:
# 
# Input: nums1 = [0,3,5,8,9], nums2 = [2,1,4,6,9]
# Output: 1
# 
# 
# Constraints:
#         2 <= nums1.length <= 10⁵
#         nums2.length == nums1.length
#         0 <= nums1[i], nums2[i] <= 2 * 10⁵


# Solution: https://algo.monster/liteproblems/801
# Credit: AlgoMonster
def min_swap(nums1, nums2):
    # Dynamic Programming approach to find minimum swaps
    # keep: minimum swaps needed if we DON'T swap at current position
    # swap: minimum swaps needed if we DO swap at current position
    keep = 0  # No swap needed at position 0 to keep arrays valid
    swap = 1  # One swap needed if we swap at position 0
    
    # Iterate through arrays starting from index 1
    for i in range(1, len(nums1)):
        # Store previous state values
        prev_keep = keep
        prev_swap = swap
        
        # Check if arrays are NOT naturally increasing without any swap
        if nums1[i - 1] >= nums1[i] or nums2[i - 1] >= nums2[i]:
            # Arrays are not naturally increasing
            # Must swap at exactly one position (either previous or current)
            keep = prev_swap  # Don't swap current, so must have swapped previous
            swap = prev_keep + 1  # Swap current, so previous must not be swapped
        else:
            # Arrays are naturally increasing without swap
            # Default: continue the same state as previous
            swap = prev_swap + 1  # If we swapped previous, swap current too
            
            # Check if cross-comparison also works
            # (previous nums1 with current nums2, and previous nums2 with current nums1)
            if nums1[i - 1] < nums2[i] and nums2[i - 1] < nums1[i]:
                # Cross-swap is also valid
                # We can choose to swap or not swap independently
                keep = min(keep, prev_swap)  # Can keep current regardless of previous
                swap = min(swap, prev_keep + 1)  # Can swap current regardless of previous
    
    # Return minimum of both final states
    return min(keep, swap)
    # Time: O(n)
    # Space: O(1)


def main():
    result = min_swap(nums1 = [1,3,5,4], nums2 = [1,2,3,7])
    print(result) # 1

    result = min_swap(nums1 = [0,3,5,8,9], nums2 = [2,1,4,6,9])
    print(result) # 1

if __name__ == "__main__":
    main()
