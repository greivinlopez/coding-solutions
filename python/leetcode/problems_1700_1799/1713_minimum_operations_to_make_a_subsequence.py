# ----------------------------------------------
# 1713. Minimum Operations to Make a Subsequence
# ----------------------------------------------

# Problem: https://leetcode.com/problems/minimum-operations-to-make-a-subsequence
#
# You are given an array target that consists of distinct integers and another
# integer array arr that can have duplicates.
# 
# In one operation, you can insert any integer at any position in arr. For
# example, if arr = [1,4,1,2], you can add 3 in the middle and make it
# [1,4,3,1,2]. Note that you can insert the integer at the very beginning or end
# of the array.
# 
# Return the minimum number of operations needed to make target a subsequence of
# arr.
# 
# A subsequence of an array is a new array generated from the original array by
# deleting some elements (possibly none) without changing the remaining elements'
# relative order. For example, [2,7,4] is a subsequence of [4,2,3,7,2,1,4] (the
# underlined elements), while [2,4,2] is not.
# 
# Example 1:
# 
# Input: target = [5,1,3], arr = [9,4,2,3,4]
# Output: 2
# 
# Explanation: You can add 5 and 1 in such a way that makes arr = [5,9,4,1,2,3,4],
# then target will be a subsequence of arr.
# 
# Example 2:
# 
# Input: target = [6,4,8,1,3,2], arr = [4,7,6,2,3,8,6,1]
# Output: 3
# 
# 
# Constraints:
#         1 <= target.length, arr.length <= 10⁵
#         1 <= target[i], arr[i] <= 10⁹
#         target contains no duplicates.


# Solution: https://algo.monster/liteproblems/1713
# Credit: AlgoMonster
def min_operations(target, arr):
    position_map = {value: index for index, value in enumerate(target, 1)}

    # Convert arr elements to their positions in target
    # Filter out elements not in target
    mapped_positions = [position_map[value] for value in arr if value in position_map]

    # Initialize BIT with size of target
    target_length = len(target)
    fenwick_tree = BinaryIndexedTree(target_length)

    # Find longest increasing subsequence in mapped positions
    # This corresponds to finding the longest common subsequence
    longest_subsequence = 0

    for position in mapped_positions:
        # Query maximum length ending before current position
        prev_max_length = fenwick_tree.query(position - 1)
        # Current subsequence length including this element
        current_length = prev_max_length + 1
        # Update global maximum
        longest_subsequence = max(longest_subsequence, current_length)
        # Update tree with new length at this position
        fenwick_tree.update(position, current_length)

    # Return minimum operations: elements to insert
    return target_length - longest_subsequence
    # Time: O(n * log m)
    # Space: O(m)


class BinaryIndexedTree:
    """
    Binary Indexed Tree (Fenwick Tree) for range maximum queries.
    This implementation supports point updates and prefix maximum queries.
    """
    __slots__ = "size", "tree"

    def __init__(self, n: int):
        """
        Initialize a Binary Indexed Tree with size n.

        Args:
            n: The size of the tree (1-indexed)
        """
        self.size = n
        self.tree = [0] * (n + 1)  # 1-indexed array for BIT

    def update(self, index: int, value: int):
        """
        Update the tree by setting the maximum value at position index.

        Args:
            index: The position to update (1-indexed)
            value: The value to compare with existing maximum
        """
        while index <= self.size:
            # Update current position with maximum value
            self.tree[index] = max(self.tree[index], value)
            # Move to next index affected by this update
            # index & -index gives the lowest set bit
            index += index & -index

    def query(self, index: int) -> int:
        """
        Query the maximum value in range [1, index].

        Args:
            index: The right boundary of the query range (1-indexed)

        Returns:
            Maximum value in the range [1, index]
        """
        max_value = 0
        while index > 0:
            # Take maximum of current position
            max_value = max(max_value, self.tree[index])
            # Move to parent node by removing lowest set bit
            index -= index & -index
        return max_value


def main():
    result = min_operations(target = [5,1,3], arr = [9,4,2,3,4])
    print(result) # 2

    result = min_operations(target = [6,4,8,1,3,2], arr = [4,7,6,2,3,8,6,1])
    print(result) # 3

if __name__ == "__main__":
    main()
