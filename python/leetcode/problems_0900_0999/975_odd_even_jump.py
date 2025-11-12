# ------------------
# 975. Odd Even Jump
# ------------------

# Problem: https://leetcode.com/problems/odd-even-jump
#
# You are given an integer array arr. From some starting index, you can make a
# series of jumps. The (1ˢᵗ, 3ʳᵈ, 5ᵗʰ, ...) jumps in the series are called odd-
# numbered jumps, and the (2ⁿᵈ, 4ᵗʰ, 6ᵗʰ, ...) jumps in the series are called
# even-numbered jumps. Note that the jumps are numbered, not the indices.
# 
# You may jump forward from index i to index j (with i < j) in the following way:
#         
#   * During odd-numbered jumps (i.e., jumps 1, 3, 5, ...), you jump to the
#     index j such that arr[i] <= arr[j] and arr[j] is the smallest possible value. If
#     there are multiple such indices j, you can only jump to the smallest such index
#     j.
#   * During even-numbered jumps (i.e., jumps 2, 4, 6, ...), you jump to the
#     index j such that arr[i] >= arr[j] and arr[j] is the largest possible value. If
#     there are multiple such indices j, you can only jump to the smallest such index
#     j.
#   * It may be the case that for some index i, there are no legal jumps.
# 
# A starting index is good if, starting from that index, you can reach the end of
# the array (index arr.length - 1) by jumping some number of times (possibly 0 or
# more than once).
# 
# Return the number of good starting indices.
# 
# Example 1:
# 
# Input: arr = [10,13,12,14,15]
# Output: 2
# 
# Explanation:
# From starting index i = 0, we can make our 1st jump to i = 2 (since arr[2] is
# the smallest among arr[1], arr[2], arr[3], arr[4] that is greater or equal to
# arr[0]), then we cannot jump any more.
# From starting index i = 1 and i = 2, we can make our 1st jump to i = 3, then we
# cannot jump any more.
# From starting index i = 3, we can make our 1st jump to i = 4, so we have reached
# the end.
# From starting index i = 4, we have reached the end already.
# In total, there are 2 different starting indices i = 3 and i = 4, where we can
# reach the end with some number of
# jumps.
# 
# Example 2:
# 
# Input: arr = [2,3,1,1,4]
# Output: 3
# 
# Explanation:
# From starting index i = 0, we make jumps to i = 1, i = 2, i = 3:
# During our 1st jump (odd-numbered), we first jump to i = 1 because arr[1] is the
# smallest value in [arr[1], arr[2], arr[3], arr[4]] that is greater than or equal
# to arr[0].
# During our 2nd jump (even-numbered), we jump from i = 1 to i = 2 because arr[2]
# is the largest value in [arr[2], arr[3], arr[4]] that is less than or equal to
# arr[1]. arr[3] is also the largest value, but 2 is a smaller index, so we can
# only jump to i = 2 and not i = 3
# During our 3rd jump (odd-numbered), we jump from i = 2 to i = 3 because arr[3]
# is the smallest value in [arr[3], arr[4]] that is greater than or equal to
# arr[2].
# We can't jump from i = 3 to i = 4, so the starting index i = 0 is not good.
# In a similar manner, we can deduce that:
# From starting index i = 1, we jump to i = 4, so we reach the end.
# From starting index i = 2, we jump to i = 3, and then we can't jump anymore.
# From starting index i = 3, we jump to i = 4, so we reach the end.
# From starting index i = 4, we are already at the end.
# In total, there are 3 different starting indices i = 1, i = 3, and i = 4, where
# we can reach the end with some
# number of jumps.
# 
# Example 3:
# 
# Input: arr = [5,1,3,4,2]
# Output: 3
# 
# Explanation: We can reach the end from starting indices 1, 2, and 4.
# 
# 
# Constraints:
#         1 <= arr.length <= 2 * 10⁴
#         0 <= arr[i] < 10⁵


# Solution: https://algo.monster/liteproblems/975
# Credit: AlgoMonster
def odd_even_jumps(arr):
    from sortedcontainers import SortedDict
    from functools import cache
    
    @cache
    def can_reach_end(index, jump_type):
        # Base case: already at the last index
        if index == array_length - 1:
            return True
        
        # No valid next jump exists
        if next_jump_indices[index][jump_type] == -1:
            return False
        
        # Recursively check from next position with alternating jump type
        return can_reach_end(next_jump_indices[index][jump_type], jump_type ^ 1)
    
    array_length = len(arr)
    
    # Build next jump indices table
    # next_jump_indices[i][0] = next index for even jump from i
    # next_jump_indices[i][1] = next index for odd jump from i
    next_jump_indices = [[0] * 2 for _ in range(array_length)]
    
    # SortedDict to maintain sorted order of values and their indices
    sorted_dict = SortedDict()
    
    # Process array from right to left to build jump table
    for current_index in range(array_length - 1, -1, -1):
        current_value = arr[current_index]
        
        # Find next index for odd jump (smallest value >= current_value)
        position = sorted_dict.bisect_left(current_value)
        if position < len(sorted_dict):
            next_jump_indices[current_index][1] = sorted_dict.values()[position]
        else:
            next_jump_indices[current_index][1] = -1
        
        # Find next index for even jump (largest value <= current_value)
        position = sorted_dict.bisect_right(current_value) - 1
        if position >= 0:
            next_jump_indices[current_index][0] = sorted_dict.values()[position]
        else:
            next_jump_indices[current_index][0] = -1
        
        # Add current value and index to sorted dict
        sorted_dict[current_value] = current_index
    
    # Count how many starting indices can reach the end
    # All jumps start with odd jump (jump_type = 1)
    return sum(can_reach_end(start_index, 1) for start_index in range(array_length))
    # Time: O(n * log(n))
    # Space: O(n)


def main():
    result = odd_even_jumps([10,13,12,14,15])
    print(result) # 2

    result = odd_even_jumps([2,3,1,1,4])
    print(result) # 3

    result = odd_even_jumps([5,1,3,4,2])
    print(result) # 3

if __name__ == "__main__":
    main()
