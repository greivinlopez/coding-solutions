# -------------------------
# 771. Jewels and Stones
# -------------------------

# Problem: https://leetcode.com/problems/jewels-and-stones/
# 
# You're given strings jewels representing the types of stones that are jewels,
# and stones representing the stones you have. Each character in stones is a 
# type of stone you have. You want to know how many of the stones you have are 
# also jewels.
# 
# Letters are case sensitive, so "a" is considered a different type of stone 
# from "A".
# 
# 
# Example 1:
# 
# Input: jewels = "aA", stones = "aAAbbbb"
# Output: 3
# 
#  
# Example 2:
# 
# Input: jewels = "z", stones = "ZZ"
# Output: 0
# 
# 
# Constraints:
# 
#   1 <= jewels.length, stones.length <= 50
#   jewels and stones consist of only English letters.
#   All the characters of jewels are unique.


# Solution: https://youtu.be/IOt4dS1IWWU
# Credit: Greg Hogg
def num_jewels_in_stones_brute(jewels, stones):
    # Brute Force Solution
    count = 0
    for stone in stones:
        if stone in jewels:
            count += 1
    return count
    # Time: O(n * m)
    # Space: O(1)

def num_jewels_in_stones(jewels, stones):
    # Optimal Solution
    s = set(jewels)
    count = 0
    for stone in stones:
        if stone in s:
            count += 1
    return count
    # Time: O(n + m)
    # Space: O(n)

def main():
    result = num_jewels_in_stones(jewels = "aA", stones = "aAAbbbb")
    print(result) # 3

    result = num_jewels_in_stones(jewels = "z", stones = "ZZ")
    print(result) # 0

if __name__ == "__main__":
    main()
