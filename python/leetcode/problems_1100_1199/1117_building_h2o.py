# -----------------
# 1117. Building H2O
# -----------------

# Problem: https://leetcode.com/problems/building-h2o
#
# There are two kinds of threads: oxygen and hydrogen. Your goal is to group these
# threads to form water molecules.
# 
# There is a barrier where each thread has to wait until a complete molecule can
# be formed. Hydrogen and oxygen threads will be given releaseHydrogen and
# releaseOxygen methods respectively, which will allow them to pass the barrier.
# These threads should pass the barrier in groups of three, and they must
# immediately bond with each other to form a water molecule. You must guarantee
# that all the threads from one molecule bond before any other threads from the
# next molecule do.
# 
# In other words:
#         
#   * If an oxygen thread arrives at the barrier when no hydrogen threads are
#     present, it must wait for two hydrogen threads.
#   * If a hydrogen thread arrives at the barrier when no other threads are
#     present, it must wait for an oxygen thread and another hydrogen thread.
# 
# We do not have to worry about matching the threads up explicitly; the threads do
# not necessarily know which other threads they are paired up with. The key is
# that threads pass the barriers in complete sets; thus, if we examine the
# sequence of threads that bind and divide them into groups of three, each group
# should contain one oxygen and two hydrogen threads.
# 
# Write synchronization code for oxygen and hydrogen molecules that enforces these
# constraints.
# 
# Example 1:
# 
# Input: water = "HOH"
# Output: "HHO"
# 
# Explanation: "HOH" and "OHH" are also valid answers.
# 
# Example 2:
# 
# Input: water = "OOHHHH"
# Output: "HHOHHO"
# 
# Explanation: "HOHHHO", "OHHHHO", "HHOHOH", "HOHHOH", "OHHHOH", "HHOOHH",
# "HOHOHH" and "OHHOHH" are also valid answers.
# 
# 
# Constraints:
#         3 * n == water.length
#         1 <= n <= 20
#         water[i] is either 'H' or 'O'.
#         There will be exactly 2 * n 'H' in water.
#         There will be exactly n 'O' in water.


# Solution: https://algo.monster/liteproblems/1117
# Credit: AlgoMonster
from threading import Semaphore
from typing import Callable

class H2O:
    def __init__(self):
        # Semaphore to control hydrogen threads (initially allows 2 hydrogens)
        self.hydrogen_semaphore = Semaphore(2)
        # Semaphore to control oxygen threads (initially blocks oxygen)
        self.oxygen_semaphore = Semaphore(0)
        # Counter to track how many hydrogen atoms have been released
        self.hydrogen_count = 0

    def hydrogen(self, releaseHydrogen: Callable[[], None]) -> None:
        """
        Method called by hydrogen threads.
        Two hydrogen threads must combine with one oxygen thread to form H2O.
        """
        # Wait for permission to release a hydrogen atom
        self.hydrogen_semaphore.acquire()
      
        # releaseHydrogen() outputs "H". Do not change or remove this line.
        releaseHydrogen()
      
        # Increment the hydrogen counter
        self.hydrogen_count += 1
      
        # If two hydrogens have been released, signal oxygen to proceed
        if self.hydrogen_count == 2:
            self.hydrogen_count = 0  # Reset counter for next molecule
            self.oxygen_semaphore.release()

    def oxygen(self, releaseOxygen: Callable[[], None]) -> None:
        """
        Method called by oxygen threads.
        One oxygen thread must wait for two hydrogen threads before forming H2O.
        """
        # Wait for two hydrogen atoms to be available
        self.oxygen_semaphore.acquire()
      
        # releaseOxygen() outputs "O". Do not change or remove this line.
        releaseOxygen()
      
        # Allow two more hydrogen atoms to be released for the next molecule
        self.hydrogen_semaphore.release()
        self.hydrogen_semaphore.release()


def main():
    print("TO DO")

if __name__ == "__main__":
    main()
