# ------------------------------
# 1115. Print FooBar Alternately
# ------------------------------

# Problem: https://leetcode.com/problems/print-foobar-alternately
#
# Suppose you are given the following code:
# 
# class FooBar {
#   public void foo() {
#     for (int i = 0; i < n; i++) {
#       print("foo");
#     }
#   }
#   public void bar() {
#     for (int i = 0; i < n; i++) {
#       print("bar");
#     }
#   }
# }
# 
# The same instance of FooBar will be passed to two different threads:
#         
#   * thread A will call foo(), while
#   * thread B will call bar().
# 
# Modify the given program to output "foobar" n times.
# 
# Example 1:
# 
# Input: n = 1
# Output: "foobar"
# 
# Explanation: There are two threads being fired asynchronously. One of them calls
# foo(), while the other calls bar().
# "foobar" is being output 1 time.
# 
# Example 2:
# 
# Input: n = 2
# Output: "foobarfoobar"
# 
# Explanation: "foobar" is being output 2 times.
# 
# 
# Constraints:
#         1 <= n <= 1000


# Solution: https://algo.monster/liteproblems/1115
# Credit: AlgoMonster
from threading import Semaphore
from typing import Callable

class FooBar:
    """
    A class that coordinates two threads to print "foo" and "bar" alternately.
  
    This implementation uses semaphores to ensure that "foo" and "bar" are printed
    in alternating order, regardless of which thread runs first or how the threads
    are scheduled.
    """
  
    def __init__(self, n: int) -> None:
        """
        Initialize the FooBar synchronization object.
      
        Args:
            n: The number of times each method (foo and bar) should print.
        """
        self.n = n
        # Semaphore for foo method - initially available (value=1)
        # This allows foo to run first
        self.foo_semaphore = Semaphore(1)
      
        # Semaphore for bar method - initially blocked (value=0)
        # This ensures bar waits for foo to complete first
        self.bar_semaphore = Semaphore(0)

    def foo(self, printFoo: Callable[[], None]) -> None:
        """
        Print "foo" n times, alternating with bar method.
      
        Args:
            printFoo: A callable that prints "foo" when invoked.
        """
        for _ in range(self.n):
            # Wait for permission to print foo
            # First iteration: semaphore is available (value=1)
            # Subsequent iterations: wait for bar to release this semaphore
            self.foo_semaphore.acquire()
          
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
          
            # Signal bar method that foo has completed
            # This allows bar to proceed with its print
            self.bar_semaphore.release()

    def bar(self, printBar: Callable[[], None]) -> None:
        """
        Print "bar" n times, alternating with foo method.
      
        Args:
            printBar: A callable that prints "bar" when invoked.
        """
        for _ in range(self.n):
            # Wait for foo to complete before printing bar
            # First iteration: blocked until foo releases this semaphore
            # Subsequent iterations: wait for foo to release this semaphore
            self.bar_semaphore.acquire()
          
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
          
            # Signal foo method that bar has completed
            # This allows foo to proceed with its next iteration
            self.foo_semaphore.release()


def main():
    print("TO DO")

if __name__ == "__main__":
    main()
