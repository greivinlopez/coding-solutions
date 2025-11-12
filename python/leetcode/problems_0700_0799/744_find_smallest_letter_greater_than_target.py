# ---------------------------------------------
# 744. Find Smallest Letter Greater Than Target
# ---------------------------------------------

# Problem: https://leetcode.com/problems/find-smallest-letter-greater-than-target
#
# You are given an array of characters letters that is sorted in non-decreasing
# order, and a character target. There are at least two different characters in
# letters.
# 
# Return the smallest character in letters that is lexicographically greater than
# target. If such a character does not exist, return the first character in
# letters.
# 
# Example 1:
# 
# Input: letters = ["c","f","j"], target = "a"
# Output: "c"
# 
# Explanation: The smallest character that is lexicographically greater than 'a'
# in letters is 'c'.
# 
# Example 2:
# 
# Input: letters = ["c","f","j"], target = "c"
# Output: "f"
# 
# Explanation: The smallest character that is lexicographically greater than 'c'
# in letters is 'f'.
# 
# Example 3:
# 
# Input: letters = ["x","x","y","y"], target = "z"
# Output: "x"
# 
# Explanation: There are no characters in letters that is lexicographically
# greater than 'z' so we return letters[0].
# 
# 
# Constraints:
#         2 <= letters.length <= 10⁴
#         letters[i] is a lowercase English letter.
#         letters is sorted in non-decreasing order.
#         letters contains at least two different characters.
#         target is a lowercase English letter.

from bisect import bisect_right

# Solution: https://algo.monster/liteproblems/744
# Credit: AlgoMonster
def next_greatest_letter(letters, target):
    # Use binary search to find the insertion point for target
    # bisect_right returns the rightmost position where target can be inserted
    # to maintain sorted order
    insertion_index = bisect_right(letters, target)
    
    # Use modulo to handle wrap-around case:
    # - If insertion_index < len(letters): return letters[insertion_index]
    # - If insertion_index == len(letters): wrap around to letters[0]
    return letters[insertion_index % len(letters)]
    # Time: O(log(n))
    # Space: O(1)

# Alternative Solution: Binary Search
# Solution: https://leetcode.com/problems/find-smallest-letter-greater-than-target/solutions/1568523/python-easy-solution-with-detail-explanation-modified-binary-search
# Credit: Abeni -> https://leetcode.com/u/abeni/
def next_greatest_letter_alt(letters, target):
    # if the number is out of bound
    if target >= letters[-1] or target < letters[0]:
        return letters[0]
    
    low = 0
    high = len(letters)-1
    while low <= high:
        mid = (high+low)//2
        
        if  target >= letters[mid]: # in binary search this would be only greater than
            low = mid+1
        
        if target < letters[mid]:
            high = mid-1
            
    return letters[low]
    # Time: O(n)
    # Space: O(1)


def main():
    result = next_greatest_letter(letters = ["c","f","j"], target = "a")
    print(result) # "c"

    result = next_greatest_letter(letters = ["c","f","j"], target = "c")
    print(result) # "f"

    result = next_greatest_letter(letters = ["x","x","y","y"], target = "z")
    print(result) # "x"

if __name__ == "__main__":
    main()
