# ------------------------
# 1116. Print Zero Even Odd
# ------------------------

# Problem: https://leetcode.com/problems/print-zero-even-odd
#
# You have a function printNumber that can be called with an integer parameter and
# prints it to the console.
#         
#   * For example, calling printNumber(7) prints 7 to the console.
# 
# You are given an instance of the class ZeroEvenOdd that has three functions:
# zero, even, and odd. The same instance of ZeroEvenOdd will be passed to three
# different threads:
# 
#         Thread A: calls zero() that should only output 0's.
#         Thread B: calls even() that should only output even numbers.
#         Thread C: calls odd() that should only output odd numbers.
# 
# Modify the given class to output the series "010203040506..." where the length
# of the series must be 2n.
# 
# Implement the ZeroEvenOdd class:
#         
#   * ZeroEvenOdd(int n) Initializes the object with the number n that
#     represents the numbers that should be printed.
#   * void zero(printNumber) Calls printNumber to output one zero.
#   * void even(printNumber) Calls printNumber to output one even number.
#   * void odd(printNumber) Calls printNumber to output one odd number.
# 
# Example 1:
# 
# Input: n = 2
# Output: "0102"
# 
# Explanation: There are three threads being fired asynchronously.
# One of them calls zero(), the other calls even(), and the last one calls odd().
# "0102" is the correct output.
# 
# Example 2:
# 
# Input: n = 5
# Output: "0102030405"
# 
# 
# Constraints:
#         1 <= n <= 1000


# Solution: https://algo.monster/liteproblems/1116
# Credit: AlgoMonster
from threading import Semaphore
from typing import Callable

class ZeroEvenOdd:
    """
    A class that coordinates three threads to print numbers in the pattern:
    0, 1, 0, 2, 0, 3, 0, 4, ... up to n
    where zero() prints 0s, odd() prints odd numbers, and even() prints even numbers.
    """
  
    def __init__(self, n: int) -> None:
        """
        Initialize the synchronization mechanism for n numbers.
      
        Args:
            n: The maximum number to print (inclusive)
        """
        self.n = n
        # Semaphore for zero thread - starts with 1 permit (zero goes first)
        self.zero_semaphore = Semaphore(1)
        # Semaphore for even thread - starts with 0 permits
        self.even_semaphore = Semaphore(0)
        # Semaphore for odd thread - starts with 0 permits
        self.odd_semaphore = Semaphore(0)

    def zero(self, printNumber: Callable[[int], None]) -> None:
        """
        Thread function that prints zeros.
        Alternates releasing permits to odd and even threads.
      
        Args:
            printNumber: Function to call to print a number
        """
        for i in range(self.n):
            # Wait for permission to print zero
            self.zero_semaphore.acquire()
          
            # Print zero
            printNumber(0)
          
            # Determine which thread should go next based on iteration
            # i=0 -> release odd (for printing 1)
            # i=1 -> release even (for printing 2)
            # i=2 -> release odd (for printing 3)
            # and so on...
            if i % 2 == 0:
                # Release odd thread for odd numbers (1, 3, 5, ...)
                self.odd_semaphore.release()
            else:
                # Release even thread for even numbers (2, 4, 6, ...)
                self.even_semaphore.release()

    def even(self, printNumber: Callable[[int], None]) -> None:
        """
        Thread function that prints even numbers.
        Prints 2, 4, 6, ... up to n (if n is even) or n-1 (if n is odd).
      
        Args:
            printNumber: Function to call to print a number
        """
        # Iterate through even numbers from 2 to n
        for number in range(2, self.n + 1, 2):
            # Wait for permission to print even number
            self.even_semaphore.acquire()
          
            # Print the even number
            printNumber(number)
          
            # Release zero thread to print next zero
            self.zero_semaphore.release()

    def odd(self, printNumber: Callable[[int], None]) -> None:
        """
        Thread function that prints odd numbers.
        Prints 1, 3, 5, ... up to n (if n is odd) or n-1 (if n is even).
      
        Args:
            printNumber: Function to call to print a number
        """
        # Iterate through odd numbers from 1 to n
        for number in range(1, self.n + 1, 2):
            # Wait for permission to print odd number
            self.odd_semaphore.acquire()
          
            # Print the odd number
            printNumber(number)
          
            # Release zero thread to print next zero
            self.zero_semaphore.release()


def main():
    print("TO DO")

if __name__ == "__main__":
    main()
