# ----------------------------------------------
# 1649. Create Sorted Array through Instructions
# ----------------------------------------------

# Problem: https://leetcode.com/problems/create-sorted-array-through-instructions
#
# Given an integer array instructions, you are asked to create a sorted array from
# the elements in instructions. You start with an empty container nums. For each
# element from left to right in instructions, insert it into nums. The cost of
# each insertion is the minimum of the following:
#         
#   * The number of elements currently in nums that are strictly less than
#     instructions[i].
#   * The number of elements currently in nums that are strictly greater than
#     instructions[i].
# 
# For example, if inserting element 3 into nums = [1,2,3,5], the cost of insertion
# is min(2, 1) (elements 1 and 2 are less than 3, element 5 is greater than 3) and
# nums will become [1,2,3,3,5].
# 
# Return the total cost to insert all elements from instructions into nums. Since
# the answer may be large, return it modulo 109 + 7
# 
# Example 1:
# 
# Input: instructions = [1,5,6,2]
# Output: 1
# 
# Explanation: Begin with nums = [].
# Insert 1 with cost min(0, 0) = 0, now nums = [1].
# Insert 5 with cost min(1, 0) = 0, now nums = [1,5].
# Insert 6 with cost min(2, 0) = 0, now nums = [1,5,6].
# Insert 2 with cost min(1, 2) = 1, now nums = [1,2,5,6].
# The total cost is 0 + 0 + 0 + 1 = 1.
# 
# Example 2:
# 
# Input: instructions = [1,2,3,6,5,4]
# Output: 3
# 
# Explanation: Begin with nums = [].
# Insert 1 with cost min(0, 0) = 0, now nums = [1].
# Insert 2 with cost min(1, 0) = 0, now nums = [1,2].
# Insert 3 with cost min(2, 0) = 0, now nums = [1,2,3].
# Insert 6 with cost min(3, 0) = 0, now nums = [1,2,3,6].
# Insert 5 with cost min(3, 1) = 1, now nums = [1,2,3,5,6].
# Insert 4 with cost min(3, 2) = 2, now nums = [1,2,3,4,5,6].
# The total cost is 0 + 0 + 0 + 0 + 1 + 2 = 3.
# 
# Example 3:
# 
# Input: instructions = [1,3,3,3,2,4,2,1,2]
# Output: 4
# 
# Explanation: Begin with nums = [].
# Insert 1 with cost min(0, 0) = 0, now nums = [1].
# Insert 3 with cost min(1, 0) = 0, now nums = [1,3].
# Insert 3 with cost min(1, 0) = 0, now nums = [1,3,3].
# Insert 3 with cost min(1, 0) = 0, now nums = [1,3,3,3].
# Insert 2 with cost min(1, 3) = 1, now nums = [1,2,3,3,3].
# Insert 4 with cost min(5, 0) = 0, now nums = [1,2,3,3,3,4].
# ​​​​​​​Insert 2 with cost min(1, 4) = 1, now nums = [1,2,2,3,3,3,4].
# ​​​​​​​Insert 1 with cost min(0, 6) = 0, now nums = [1,1,2,2,3,3,3,4].
# ​​​​​​​Insert 2 with cost min(2, 4) = 2, now nums = [1,1,2,2,2,3,3,3,4].
# The total cost is 0 + 0 + 0 + 0 + 1 + 0 + 1 + 0 + 2 = 4.
# 
# 
# Constraints:
#         1 <= instructions.length <= 10⁵
#         1 <= instructions[i] <= 10⁵


# Solution: https://algo.monster/liteproblems/1649
# Credit: AlgoMonster
def create_sorted_array(instructions):
    # Find maximum value to determine BIT size
    max_value = max(instructions)

    # Initialize Binary Indexed Tree to track element frequencies
    bit = BinaryIndexedTree(max_value)

    total_cost = 0
    MOD = 10**9 + 7

    for position, value in enumerate(instructions):
        # Count elements strictly less than current value
        smaller_count = bit.query(value - 1)

        # Count elements strictly greater than current value
        # Total elements so far minus elements less than or equal to current
        greater_count = position - bit.query(value)

        # Add minimum cost for this insertion
        cost = min(smaller_count, greater_count)
        total_cost += cost

        # Update BIT to include current element
        bit.update(value, 1)

    return total_cost % MOD
    # Time: O(n * log m)
    # Space: O(m)
    # m = the maximum value in the instructions array.

class BinaryIndexedTree:
    """Fenwick Tree (Binary Indexed Tree) for efficient prefix sum queries and updates."""

    def __init__(self, n: int) -> None:
        """
        Initialize a Binary Indexed Tree with size n.

        Args:
            n: The maximum value that can be indexed (1-indexed)
        """
        self.size = n
        self.tree = [0] * (n + 1)  # 1-indexed array for BIT

    def update(self, index: int, delta: int) -> None:
        """
        Add delta to the value at index and update the tree accordingly.

        Args:
            index: The position to update (1-indexed)
            delta: The value to add at the position
        """
        while index <= self.size:
            self.tree[index] += delta
            # Move to next index by adding the lowest set bit
            index += index & (-index)

    def query(self, index: int) -> int:
        """
        Get the prefix sum from 1 to index (inclusive).

        Args:
            index: The end position for prefix sum (1-indexed)

        Returns:
            The sum of elements from position 1 to index
        """
        prefix_sum = 0
        while index > 0:
            prefix_sum += self.tree[index]
            # Move to parent by removing the lowest set bit
            index -= index & (-index)
        return prefix_sum


def main():
    result = create_sorted_array(instructions = [1,5,6,2])
    print(result) # 1

    result = create_sorted_array(instructions = [1,2,3,6,5,4])
    print(result) # 3

    result = create_sorted_array(instructions = [1,3,3,3,2,4,2,1,2])
    print(result) # 4

if __name__ == "__main__":
    main()
