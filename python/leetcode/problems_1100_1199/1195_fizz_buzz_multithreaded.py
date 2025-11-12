# -----------------------------
# 1195. Fizz Buzz Multithreaded
# -----------------------------

# Problem: https://leetcode.com/problems/fizz-buzz-multithreaded
#
# You have the four functions:
#         printFizz that prints the word "fizz" to the console,
#         printBuzz that prints the word "buzz" to the console,
#         printFizzBuzz that prints the word "fizzbuzz" to the console, and
#         printNumber that prints a given integer to the console.
# 
# You are given an instance of the class FizzBuzz that has four functions: fizz,
# buzz, fizzbuzz and number. The same instance of FizzBuzz will be passed to four
# different threads:
#         Thread A: calls fizz() that should output the word "fizz".
#         Thread B: calls buzz() that should output the word "buzz".
#         Thread C: calls fizzbuzz() that should output the word "fizzbuzz".
#         Thread D: calls number() that should only output the integers.
# 
# Modify the given class to output the series [1, 2, "fizz", 4, "buzz", ...] where
# the ith token (1-indexed) of the series is:
#         "fizzbuzz" if i is divisible by 3 and 5,
#         "fizz" if i is divisible by 3 and not 5,
#         "buzz" if i is divisible by 5 and not 3, or
#         i if i is not divisible by 3 or 5.
# 
# Implement the FizzBuzz class:
#         FizzBuzz(int n) Initializes the object with the number n that represents
# the length of the sequence that should be printed.
#         void fizz(printFizz) Calls printFizz to output "fizz".
#         void buzz(printBuzz) Calls printBuzz to output "buzz".
#         void fizzbuzz(printFizzBuzz) Calls printFizzBuzz to output "fizzbuzz".
#         void number(printNumber) Calls printnumber to output the numbers.
# 
# Example 1:
# 
# Input: n = 15
# Output:
# [1,2,"fizz",4,"buzz","fizz",7,8,"fizz","buzz",11,"fizz",13,14,"fizzbuzz"]
# 
# Example 2:
# 
# Input: n = 5
# Output: [1,2,"fizz",4,"buzz"]
# 
# 
# Constraints:
#         1 <= n <= 50


# Solution: https://algo.monster/liteproblems/1195
# Credit: AlgoMonster
import threading

class FizzBuzz:
    def __init__(self, n: int):
        """
        Initialize FizzBuzz with upper limit n.
      
        Args:
            n: Upper limit of the sequence (inclusive)
        """
        self.n = n                              # Upper limit of the sequence
        self.index = 1                          # Current number being processed
        self.lock = threading.Lock()            # Mutex for thread synchronization
  
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        """
        Print "Fizz" for numbers divisible by 3 but not 5.
      
        Args:
            printFizz: Callback function to print "Fizz"
        """
        while self.index <= self.n:
            # Acquire lock to ensure thread-safe access to shared index
            with self.lock:
                # Check if current index is divisible by 3 but not 5
                # Additional index <= n check ensures we don't exceed limit after acquiring lock
                if self.index % 3 == 0 and self.index % 5 != 0 and self.index <= self.n:
                    printFizz()
                    self.index += 1
  
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        """
        Print "Buzz" for numbers divisible by 5 but not 3.
      
        Args:
            printBuzz: Callback function to print "Buzz"
        """
        while self.index <= self.n:
            # Acquire lock to ensure thread-safe access to shared index
            with self.lock:
                # Check if current index is divisible by 5 but not 3
                if self.index % 5 == 0 and self.index % 3 != 0 and self.index <= self.n:
                    printBuzz()
                    self.index += 1
  
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        """
        Print "FizzBuzz" for numbers divisible by both 3 and 5 (i.e., divisible by 15).
      
        Args:
            printFizzBuzz: Callback function to print "FizzBuzz"
        """
        while self.index <= self.n:
            # Acquire lock to ensure thread-safe access to shared index
            with self.lock:
                # Check if current index is divisible by 15 (both 3 and 5)
                if self.index % 15 == 0 and self.index <= self.n:
                    printFizzBuzz()
                    self.index += 1
  
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        """
        Print the actual number for numbers not divisible by 3 or 5.
      
        Args:
            printNumber: Callback function to print the number
        """
        while self.index <= self.n:
            # Acquire lock to ensure thread-safe access to shared index
            with self.lock:
                # Check if current index is not divisible by either 3 or 5
                if self.index % 3 != 0 and self.index % 5 != 0 and self.index <= self.n:
                    printNumber(self.index)
                    self.index += 1


def main():
    print("TO DO")

if __name__ == "__main__":
    main()
