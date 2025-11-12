# --------------------
# 699. Falling Squares
# --------------------

# Problem: https://leetcode.com/problems/falling-squares
#
# There are several squares being dropped onto the X-axis of a 2D plane.
# 
# You are given a 2D integer array positions where positions[i] = [leftᵢ,
# sideLengthᵢ] represents the iᵗʰ square with a side length of sideLengthi that is
# dropped with its left edge aligned with X-coordinate leftᵢ.
# 
# Each square is dropped one at a time from a height above any landed squares. It
# then falls downward (negative Y direction) until it either lands on the top side
# of another square or on the X-axis. A square brushing the left/right side of
# another square does not count as landing on it. Once it lands, it freezes in
# place and cannot be moved.
# 
# After each square is dropped, you must record the height of the current tallest
# stack of squares.
# 
# Return an integer array ans where ans[i] represents the height described above
# after dropping the iᵗʰ square.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2021/04/28/fallingsq1-plane.jpg
# 
# Input: positions = [[1,2],[2,3],[6,1]]
# Output: [2,5,5]
# 
# Explanation:
# After the first drop, the tallest stack is square 1 with a height of 2.
# After the second drop, the tallest stack is squares 1 and 2 with a height of 5.
# After the third drop, the tallest stack is still squares 1 and 2 with a height
# of 5.
# Thus, we return an answer of [2, 5, 5].
# 
# Example 2:
# 
# Input: positions = [[100,100],[200,100]]
# Output: [100,100]
# 
# Explanation:
# After the first drop, the tallest stack is square 1 with a height of 100.
# After the second drop, the tallest stack is either square 1 or square 2, both
# with heights of 100.
# Thus, we return an answer of [100, 100].
# Note that square 2 only brushes the right side of square 1, which does not count
# as landing on it.
# 
# 
# Constraints:
#         1 <= positions.length <= 1000
#         1 <= lefti <= 10⁸
#         1 <= sideLengthi <= 10⁶


# Solution: https://algo.monster/liteproblems/699
# Credit: AlgoMonster
from typing import List

class Node:
    """Node for dynamic segment tree."""
    def __init__(self, left: int, right: int):
        self.left_child = None  # Left child node
        self.right_child = None  # Right child node
        self.left_bound = left  # Left boundary of the interval
        self.right_bound = right  # Right boundary of the interval
        self.mid = (left + right) >> 1  # Midpoint of the interval
        self.max_value = 0  # Maximum value in this interval
        self.lazy_tag = 0  # Lazy propagation tag for range updates

class SegmentTree:
    """Dynamic segment tree for range maximum query and range update."""
  
    def __init__(self):
        # Initialize root node covering range [1, 10^9]
        self.root = Node(1, int(1e9))
  
    def modify(self, left: int, right: int, value: int, node: Node = None) -> None:
        """
        Update all elements in range [left, right] to value.
      
        Args:
            left: Left boundary of update range
            right: Right boundary of update range
            value: Value to set for the range
            node: Current node in recursion (defaults to root)
        """
        if left > right:
            return
      
        if node is None:
            node = self.root
      
        # If current node's interval is completely within update range
        if node.left_bound >= left and node.right_bound <= right:
            node.max_value = value
            node.lazy_tag = value
            return
      
        # Push down lazy tag before going to children
        self._push_down(node)
      
        # Recursively update left child if needed
        if left <= node.mid:
            self.modify(left, right, value, node.left_child)
      
        # Recursively update right child if needed
        if right > node.mid:
            self.modify(left, right, value, node.right_child)
      
        # Update current node's value based on children
        self._push_up(node)
  
    def query(self, left: int, right: int, node: Node = None) -> int:
        """
        Query maximum value in range [left, right].
      
        Args:
            left: Left boundary of query range
            right: Right boundary of query range
            node: Current node in recursion (defaults to root)
      
        Returns:
            Maximum value in the specified range
        """
        if left > right:
            return 0
      
        if node is None:
            node = self.root
      
        # If current node's interval is completely within query range
        if node.left_bound >= left and node.right_bound <= right:
            return node.max_value
      
        # Push down lazy tag before querying children
        self._push_down(node)
      
        max_val = 0
      
        # Query left child if needed
        if left <= node.mid:
            max_val = max(max_val, self.query(left, right, node.left_child))
      
        # Query right child if needed
        if right > node.mid:
            max_val = max(max_val, self.query(left, right, node.right_child))
      
        return max_val
  
    def _push_up(self, node: Node) -> None:
        """
        Update parent node's value based on children's values.
      
        Args:
            node: Node to update
        """
        node.max_value = max(node.left_child.max_value, node.right_child.max_value)
  
    def _push_down(self, node: Node) -> None:
        """
        Push lazy tag down to children and create children if they don't exist.
      
        Args:
            node: Node whose lazy tag needs to be pushed down
        """
        # Create left child if it doesn't exist
        if node.left_child is None:
            node.left_child = Node(node.left_bound, node.mid)
      
        # Create right child if it doesn't exist
        if node.right_child is None:
            node.right_child = Node(node.mid + 1, node.right_bound)
      
        # If there's a lazy tag, propagate it to children
        if node.lazy_tag:
            node.left_child.max_value = node.lazy_tag
            node.right_child.max_value = node.lazy_tag
            node.left_child.lazy_tag = node.lazy_tag
            node.right_child.lazy_tag = node.lazy_tag
            node.lazy_tag = 0  # Clear the lazy tag after propagation

class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        """
        Simulate falling squares and return maximum height after each square falls.
      
        Args:
            positions: List of [left, side_length] pairs representing squares
      
        Returns:
            List of maximum heights after each square falls
        """
        result = []
        max_height = 0
        tree = SegmentTree()
      
        for left_pos, side_length in positions:
            # Calculate right boundary of the square
            right_pos = left_pos + side_length - 1
          
            # Find current maximum height in the range where square will land
            current_height = tree.query(left_pos, right_pos)
          
            # New height after this square lands
            new_height = current_height + side_length
          
            # Update global maximum height
            max_height = max(max_height, new_height)
            result.append(max_height)
          
            # Update the height in the range covered by this square
            tree.modify(left_pos, right_pos, new_height)
      
        return result


def main():
    print("TO DO")

if __name__ == "__main__":
    main()
