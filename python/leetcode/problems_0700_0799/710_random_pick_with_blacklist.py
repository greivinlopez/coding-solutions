# -------------------------------
# 710. Random Pick with Blacklist
# -------------------------------

# Problem: https://leetcode.com/problems/random-pick-with-blacklist
#
# You are given an integer n and an array of unique integers blacklist. Design an
# algorithm to pick a random integer in the range [0, n - 1] that is not in
# blacklist. Any integer that is in the mentioned range and not in blacklist
# should be equally likely to be returned.
# 
# Optimize your algorithm such that it minimizes the number of calls to the built-
# in random function of your language.
# 
# Implement the Solution class:
#         
#   * Solution(int n, int[] blacklist) Initializes the object with the integer
#     n and the blacklisted integers blacklist.
#   * int pick() Returns a random integer in the range [0, n - 1] and not in
#     blacklist.
# 
# Example 1:
# 
# Input
# ["Solution", "pick", "pick", "pick", "pick", "pick", "pick", "pick"]
# [[7, [2, 3, 5]], [], [], [], [], [], [], []]
# Output
# [null, 0, 4, 1, 6, 1, 0, 4]
# 
# Explanation
# Solution solution = new Solution(7, [2, 3, 5]);
# solution.pick(); // return 0, any integer from [0,1,4,6] should be ok. Note that
# for every call of pick,
#                  // 0, 1, 4, and 6 must be equally likely to be returned (i.e.,
# with probability 1/4).
# solution.pick(); // return 4
# solution.pick(); // return 1
# solution.pick(); // return 6
# solution.pick(); // return 1
# solution.pick(); // return 0
# solution.pick(); // return 4
# 
# 
# Constraints:
#         1 <= n <= 10⁹
#         0 <= blacklist.length <= min(10⁵, n - 1)
#         0 <= blacklist[i] < n
#         All the values of blacklist are unique.
#         At most 2 * 10⁴ calls will be made to pick.

from typing import List
from random import randrange

# Solution: https://algo.monster/liteproblems/710
# Credit: AlgoMonster
class Solution:
    def __init__(self, n: int, blacklist: List[int]):
        # Calculate the size of the valid range [0, k) where we'll pick from
        # All blacklisted numbers will be remapped if they fall in this range
        self.valid_range_size = n - len(blacklist)
      
        # Dictionary to remap blacklisted numbers in [0, k) to valid numbers in [k, n)
        self.remap_dict = {}
      
        # Start searching for replacement values from position k
        replacement_index = self.valid_range_size
      
        # Convert blacklist to set for O(1) lookup
        blacklist_set = set(blacklist)
      
        # Process each blacklisted number
        for blacklisted_num in blacklist:
            # Only remap if the blacklisted number is in our picking range [0, k)
            if blacklisted_num < self.valid_range_size:
                # Find the next non-blacklisted number in range [k, n)
                while replacement_index in blacklist_set:
                    replacement_index += 1
              
                # Map the blacklisted number to a valid replacement
                self.remap_dict[blacklisted_num] = replacement_index
                replacement_index += 1

    def pick(self) -> int:
        # Pick a random number from [0, k)
        random_num = randrange(self.valid_range_size)
      
        # If it's a blacklisted number (exists in remap dict), return its replacement
        # Otherwise, return the number itself
        return self.remap_dict.get(random_num, random_num)


def main():
    print("TO DO")

if __name__ == "__main__":
    main()
