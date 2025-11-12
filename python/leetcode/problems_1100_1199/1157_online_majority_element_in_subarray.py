# -----------------------------------------
# 1157. Online Majority Element In Subarray
# -----------------------------------------

# Problem: https://leetcode.com/problems/online-majority-element-in-subarray
#
# Design a data structure that efficiently finds the majority element of a given
# subarray.
# 
# The majority element of a subarray is an element that occurs threshold times or
# more in the subarray.
# 
# Implementing the MajorityChecker class:
#         
#   * MajorityChecker(int[] arr) Initializes the instance of the class with
#     the given array arr.
#   * int query(int left, int right, int threshold) returns the element in the
#     subarray arr[left...right] that occurs at least threshold times, or -1 if no
#     such element exists.
# 
# Example 1:
# 
# Input
# ["MajorityChecker", "query", "query", "query"]
# [[[1, 1, 2, 2, 1, 1]], [0, 5, 4], [0, 3, 3], [2, 3, 2]]
# Output
# [null, 1, -1, 2]
# 
# Explanation
# MajorityChecker majorityChecker = new MajorityChecker([1, 1, 2, 2, 1, 1]);
# majorityChecker.query(0, 5, 4); // return 1
# majorityChecker.query(0, 3, 3); // return -1
# majorityChecker.query(2, 3, 2); // return 2
# 
# 
# Constraints:
#         1 <= arr.length <= 2 * 10⁴
#         1 <= arr[i] <= 2 * 10⁴
#         0 <= left <= right < arr.length
#         threshold <= right - left + 1
#         2 * threshold > right - left + 1
#         At most 10⁴ calls will be made to query.

from typing import List
from collections import defaultdict
from bisect import bisect_left

# Solution: https://algo.monster/liteproblems/1157
# Credit: AlgoMonster
class Node:
    """Node for segment tree storing potential majority element and its count."""
    __slots__ = ("left", "right", "candidate", "count")
  
    def __init__(self):
        self.left = 0          # Left boundary of segment
        self.right = 0         # Right boundary of segment  
        self.candidate = 0     # Potential majority element in this segment
        self.count = 0         # Net count of candidate (using Boyer-Moore logic)


class SegmentTree:
    """
    Segment tree that maintains potential majority elements using Boyer-Moore voting.
    Each node stores a candidate element and its net count after cancellation.
    """
  
    def __init__(self, nums: List[int]):
        self.nums = nums
        n = len(nums)
        # Allocate 4n nodes for the segment tree (standard practice)
        self.nodes = [Node() for _ in range(n << 2)]
        self.build(1, 1, n)
  
    def build(self, node_idx: int, left: int, right: int) -> None:
        """Build the segment tree recursively."""
        self.nodes[node_idx].left = left
        self.nodes[node_idx].right = right
      
        # Base case: leaf node
        if left == right:
            self.nodes[node_idx].candidate = self.nums[left - 1]  # 1-indexed to 0-indexed
            self.nodes[node_idx].count = 1
            return
      
        # Recursive case: build left and right children
        mid = (left + right) >> 1
        left_child = node_idx << 1
        right_child = (node_idx << 1) | 1
      
        self.build(left_child, left, mid)
        self.build(right_child, mid + 1, right)
      
        # Update current node based on children
        self._push_up(node_idx)
  
    def query(self, node_idx: int, query_left: int, query_right: int) -> tuple[int, int]:
        """
        Query the potential majority element in range [query_left, query_right].
        Returns (candidate, net_count) using Boyer-Moore voting logic.
        """
        current_node = self.nodes[node_idx]
      
        # Case 1: Current segment is fully within query range
        if current_node.left >= query_left and current_node.right <= query_right:
            return current_node.candidate, current_node.count
      
        mid = (current_node.left + current_node.right) >> 1
        left_child = node_idx << 1
        right_child = (node_idx << 1) | 1
      
        # Case 2: Query range is entirely in left subtree
        if query_right <= mid:
            return self.query(left_child, query_left, query_right)
      
        # Case 3: Query range is entirely in right subtree
        if query_left > mid:
            return self.query(right_child, query_left, query_right)
      
        # Case 4: Query range spans both subtrees - merge results
        left_candidate, left_count = self.query(left_child, query_left, query_right)
        right_candidate, right_count = self.query(right_child, query_left, query_right)
      
        # Apply Boyer-Moore voting logic to merge
        if left_candidate == right_candidate:
            return left_candidate, left_count + right_count
        elif left_count >= right_count:
            return left_candidate, left_count - right_count
        else:
            return right_candidate, right_count - left_count
  
    def _push_up(self, node_idx: int) -> None:
        """
        Update parent node based on its children using Boyer-Moore voting.
        This merges two segments' majority candidates.
        """
        left_child = node_idx << 1
        right_child = (node_idx << 1) | 1
      
        left_node = self.nodes[left_child]
        right_node = self.nodes[right_child]
        current_node = self.nodes[node_idx]
      
        # If both children have same candidate, add their counts
        if left_node.candidate == right_node.candidate:
            current_node.candidate = left_node.candidate
            current_node.count = left_node.count + right_node.count
        # Otherwise, the one with higher count survives (with reduced count)
        elif left_node.count >= right_node.count:
            current_node.candidate = left_node.candidate
            current_node.count = left_node.count - right_node.count
        else:
            current_node.candidate = right_node.candidate
            current_node.count = right_node.count - left_node.count


class MajorityChecker:
    """
    Data structure to efficiently check if an element appears >= threshold times
    in any subarray. Uses segment tree to find potential majority candidates.
    """
  
    def __init__(self, arr: List[int]):
        # Build segment tree for finding potential majority elements
        self.tree = SegmentTree(arr)
      
        # Store positions of each element for verification
        self.element_positions = defaultdict(list)
        for index, value in enumerate(arr):
            self.element_positions[value].append(index)
  
    def query(self, left: int, right: int, threshold: int) -> int:
        """
        Check if any element appears >= threshold times in arr[left:right+1].
        Returns the element if found, otherwise -1.
        """
        # Get potential majority candidate from segment tree (1-indexed query)
        candidate, _ = self.tree.query(1, left + 1, right + 1)
      
        # Verify if candidate actually appears >= threshold times
        # Binary search to count occurrences of candidate in range
        positions = self.element_positions[candidate]
        left_bound = bisect_left(positions, left)
        right_bound = bisect_left(positions, right + 1)
      
        actual_count = right_bound - left_bound
        return candidate if actual_count >= threshold else -1


def main():
    print("TO DO")

if __name__ == "__main__":
    main()
