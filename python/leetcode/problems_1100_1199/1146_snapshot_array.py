# --------------------
# 1146. Snapshot Array
# --------------------

# Problem: https://leetcode.com/problems/snapshot-array
#
# Implement a SnapshotArray that supports the following interface:
#         
#   * SnapshotArray(int length) initializes an array-like data structure with
#     the given length. Initially, each element equals 0.
#   * void set(index, val) sets the element at the given index to be equal to val.
#   * int snap() takes a snapshot of the array and returns the snap_id: the total 
#     number of times we called snap() minus 1.
#   * int get(index, snap_id) returns the value at the given index, at the
#     time we took the snapshot with the given snap_id
# 
# Example 1:
# 
# Input: ["SnapshotArray","set","snap","set","get"]
# [[3],[0,5],[],[0,6],[0,0]]
# Output: [null,null,0,null,5]
# 
# Explanation:
# SnapshotArray snapshotArr = new SnapshotArray(3); // set the length to be 3
# snapshotArr.set(0,5);  // Set array[0] = 5
# snapshotArr.snap();  // Take a snapshot, return snap_id = 0
# snapshotArr.set(0,6);
# snapshotArr.get(0,0);  // Get the value of array[0] with snap_id = 0, return 5
# 
# 
# Constraints:
#         1 <= length <= 5 * 10⁴
#         0 <= index < length
#         0 <= val <= 10⁹
#         0 <= snap_id < (the total number of times we call snap())
#         At most 5 * 10⁴ calls will be made to set, snap, and get.

from bisect import bisect_left
from typing import List, Tuple
from math import inf

# Solution: https://algo.monster/liteproblems/1146
# Credit: AlgoMonster
class SnapshotArray:
    """
    A data structure that supports taking snapshots of an array.
    Each snapshot preserves the state of the array at that point in time.
    """

    def __init__(self, length: int) -> None:
        """
        Initialize the SnapshotArray with the given length.
      
        Args:
            length: The size of the array to create
        """
        # Each index stores a list of (snapshot_id, value) tuples
        # representing the history of values at that index
        self.array_history: List[List[Tuple[int, int]]] = [[] for _ in range(length)]
      
        # Current snapshot ID (incremented with each snap() call)
        self.current_snap_id: int = 0

    def set(self, index: int, val: int) -> None:
        """
        Set the value at the given index for the current snapshot.
      
        Args:
            index: The index in the array to update
            val: The value to set at the index
        """
        # Append the new value with the current snapshot ID
        self.array_history[index].append((self.current_snap_id, val))

    def snap(self) -> int:
        """
        Take a snapshot of the current array state.
      
        Returns:
            The snapshot ID of the snapshot that was just taken
        """
        # Increment snapshot ID for future operations
        snapshot_id = self.current_snap_id
        self.current_snap_id += 1
        return snapshot_id

    def get(self, index: int, snap_id: int) -> int:
        """
        Get the value at the given index for a specific snapshot.
      
        Args:
            index: The index in the array to retrieve
            snap_id: The snapshot ID to query
          
        Returns:
            The value at the index during the specified snapshot, or 0 if no value was set
        """
        # Binary search for the rightmost entry with snapshot_id <= snap_id
        # We search for (snap_id, inf) and then go one position back
        history = self.array_history[index]
        insertion_point = bisect_left(history, (snap_id, inf)) - 1
      
        # If no value was set before or at snap_id, return default value 0
        if insertion_point < 0:
            return 0
      
        # Return the value from the found entry
        return history[insertion_point][1]


def main():
    print("TO DO")

if __name__ == "__main__":
    main()
