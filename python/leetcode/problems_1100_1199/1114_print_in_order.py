# --------------------
# 1114. Print in Order
# --------------------

# Problem: https://leetcode.com/problems/print-in-order
#
# Suppose we have a class:
# 
# public class Foo {
#   public void first() { print("first"); }
#   public void second() { print("second"); }
#   public void third() { print("third"); }
# }
# 
# The same instance of Foo will be passed to three different threads. Thread A
# will call first(), thread B will call second(), and thread C will call third().
# Design a mechanism and modify the program to ensure that second() is executed
# after first(), and third() is executed after second().
# 
# Note:
# 
# We do not know how the threads will be scheduled in the operating system, even
# though the numbers in the input seem to imply the ordering. The input format you
# see is mainly to ensure our tests' comprehensiveness.
# 
# Example 1:
# 
# Input: nums = [1,2,3]
# Output: "firstsecondthird"
# 
# Explanation: There are three threads being fired asynchronously. The input
# [1,2,3] means thread A calls first(), thread B calls second(), and thread C
# calls third(). "firstsecondthird" is the correct output.
# 
# Example 2:
# 
# Input: nums = [1,3,2]
# Output: "firstsecondthird"
# 
# Explanation: The input [1,3,2] means thread A calls first(), thread B calls
# third(), and thread C calls second(). "firstsecondthird" is the correct output.
# 
# 
# Constraints:
#         nums is a permutation of [1, 2, 3].


# Solution: https://algo.monster/liteproblems/1114
# Credit: AlgoMonster
import threading
from typing import Callable

class Foo:
    def __init__(self):
        # Initialize two locks to control the execution order
        # Lock for controlling when second() can execute
        self.lock_for_second = threading.Lock()
        # Lock for controlling when third() can execute
        self.lock_for_third = threading.Lock()
      
        # Pre-acquire both locks to block second() and third() initially
        # This ensures first() must complete before second() can run
        self.lock_for_second.acquire()
        # This ensures second() must complete before third() can run
        self.lock_for_third.acquire()

    def first(self, printFirst: Callable[[], None]) -> None:
        # First method can execute immediately without waiting
        # Execute the first print function
        printFirst()
      
        # Release the lock to allow second() to proceed
        self.lock_for_second.release()

    def second(self, printSecond: Callable[[], None]) -> None:
        # Wait until first() releases the lock
        self.lock_for_second.acquire()
      
        # Execute the second print function
        printSecond()
      
        # Release the lock to allow third() to proceed
        self.lock_for_third.release()

    def third(self, printThird: Callable[[], None]) -> None:
        # Wait until second() releases the lock
        self.lock_for_third.acquire()
      
        # Execute the third print function
        printThird()
      
        # No need to release as this is the final method


def main():
    print("TO DO")

if __name__ == "__main__":
    main()
