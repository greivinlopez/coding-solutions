# --------------
# 855. Exam Room
# --------------

# Problem: https://leetcode.com/problems/exam-room
#
# There is an exam room with n seats in a single row labeled from 0 to n - 1.
# 
# When a student enters the room, they must sit in the seat that maximizes the
# distance to the closest person. If there are multiple such seats, they sit in
# the seat with the lowest number. If no one is in the room, then the student sits
# at seat number 0.
# 
# Design a class that simulates the mentioned exam room.
# 
# Implement the ExamRoom class:
#         
#   * ExamRoom(int n) Initializes the object of the exam room with the number
#     of the seats n.
#   * int seat() Returns the label of the seat at which the next student will set.
#   * void leave(int p) Indicates that the student sitting at seat p will leave 
#     the room. It is guaranteed that there will be a student sitting at seat p.
# 
# Example 1:
# 
# Input
# ["ExamRoom", "seat", "seat", "seat", "seat", "leave", "seat"]
# [[10], [], [], [], [], [4], []]
# Output
# [null, 0, 9, 4, 2, null, 5]
# 
# Explanation
# ExamRoom examRoom = new ExamRoom(10);
# examRoom.seat(); // return 0, no one is in the room, then the student sits at
# seat number 0.
# examRoom.seat(); // return 9, the student sits at the last seat number 9.
# examRoom.seat(); // return 4, the student sits at the last seat number 4.
# examRoom.seat(); // return 2, the student sits at the last seat number 2.
# examRoom.leave(4);
# examRoom.seat(); // return 5, the student sits at the last seat number 5.
# 
# 
# Constraints:
#         1 <= n <= 10⁹
#         It is guaranteed that there is a student sitting at seat p.
#         At most 104 calls will be made to seat and leave.


# Solution: https://algo.monster/liteproblems/855
# Credit: AlgoMonster
from sortedcontainers import SortedList

class ExamRoom:
    def __init__(self, n: int):
        """
        Initialize the exam room with n seats numbered from 0 to n-1.
      
        Args:
            n: Total number of seats in the exam room
        """
        def calculate_distance(segment):
            """
            Calculate the maximum distance a student can sit from others in a segment.
          
            For segments at the boundaries (starting at -1 or ending at n),
            the distance is the full length minus 1.
            For internal segments, the distance is half the segment length (sitting in middle).
            """
            left, right = segment
            if left == -1 or right == n:
                # Boundary segment: student sits at edge (0 or n-1)
                return right - left - 1
            else:
                # Internal segment: student sits in the middle
                return (right - left) >> 1
      
        self.n = n
        # SortedList maintains segments sorted by:
        # 1. Maximum distance (descending, hence negative)
        # 2. Left boundary (ascending, for tie-breaking)
        self.sorted_segments = SortedList(key=lambda segment: (-calculate_distance(segment), segment[0]))
      
        # Maps to track segment boundaries
        self.left_boundary = {}   # Maps right boundary -> left boundary
        self.right_boundary = {}  # Maps left boundary -> right boundary
      
        # Initially, the entire room is one empty segment from -1 to n
        self._add_segment((-1, n))
  
    def seat(self) -> int:
        """
        Assign a seat to a student maximizing distance from others.
      
        Returns:
            The seat position assigned to the student
        """
        # Get the segment with maximum available distance
        best_segment = self.sorted_segments[0]
      
        # Calculate where to place the student
        position = (best_segment[0] + best_segment[1]) >> 1  # Default: middle of segment
      
        # Handle boundary cases
        if best_segment[0] == -1:
            # Left boundary: sit at position 0
            position = 0
        elif best_segment[1] == self.n:
            # Right boundary: sit at position n-1
            position = self.n - 1
      
        # Remove the original segment
        self._delete_segment(best_segment)
      
        # Add two new segments created by placing the student
        self._add_segment((best_segment[0], position))
        self._add_segment((position, best_segment[1]))
      
        return position
  
    def leave(self, p: int) -> None:
        """
        Remove a student from seat p and merge the adjacent segments.
      
        Args:
            p: The seat position being vacated
        """
        # Find the segments on both sides of position p
        left_neighbor = self.left_boundary[p]
        right_neighbor = self.right_boundary[p]
      
        # Remove the two segments adjacent to position p
        self._delete_segment((left_neighbor, p))
        self._delete_segment((p, right_neighbor))
      
        # Add the merged segment
        self._add_segment((left_neighbor, right_neighbor))
  
    def _add_segment(self, segment):
        """
        Add a segment to the data structures.
      
        Args:
            segment: Tuple (left, right) representing an empty segment
        """
        self.sorted_segments.add(segment)
        self.left_boundary[segment[1]] = segment[0]
        self.right_boundary[segment[0]] = segment[1]
  
    def _delete_segment(self, segment):
        """
        Remove a segment from the data structures.
      
        Args:
            segment: Tuple (left, right) representing an empty segment
        """
        self.sorted_segments.remove(segment)
        self.left_boundary.pop(segment[1])
        self.right_boundary.pop(segment[0])


def main():
    print("TO DO")

if __name__ == "__main__":
    main()
