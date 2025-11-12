# -------------------------
# 605. Can Place Flowers 🌷
# -------------------------

# Problem: https://leetcode.com/problems/can-place-flowers/
# 
# You have a long flowerbed in which some of the plots are planted, and some 
# are not. However, flowers cannot be planted in adjacent plots.
# 
# Given an integer array flowerbed containing 0's and 1's, where 0 means empty 
# and 1 means not empty, and an integer n, return true if n new flowers can be 
# planted in the flowerbed without violating the no-adjacent-flowers rule and 
# false otherwise.
# 
#  
# Example 1:
# 
# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true
# 
# Example 2:
# 
# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: false
# 
#  
# Constraints:
# 
# 	1 <= flowerbed.length <= 2 * 10^4
# 	flowerbed[i] is 0 or 1.
# 	There are no two adjacent flowers in flowerbed.
# 	0 <= n <= flowerbed.length


# Solution: https://youtu.be/ZGxqqjljpUI
# Credit: Navdeep Singh founder of NeetCode
def can_place_flowers(flowerbed, n):
    # Solution with O(1) space complexity
    empty = 0 if flowerbed[0] else 1

    for f in flowerbed:
        if f:
            n -= int((empty - 1) / 2)  # int division, round toward zero
            empty = 0
        else:
            empty += 1

    n -= (empty) // 2
    return n <= 0
        

def can_place_flowers(flowerbed, n):
    # Another solution with O(1) space complexity
    for i in range(len(flowerbed)):
        if n == 0:
            return True
        if ((i == 0 or flowerbed[i - 1] == 0)   # If at the first element or the previous element equals to 0
            and (flowerbed[i] == 0)             # If current element equals to 0
            and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)): # If at the last element or the next element equals to 0
            # Place flower at the current position
            flowerbed[i] = 1
            n -= 1

    return n == 0
       
def can_place_flowers(flowerbed, n):
    # Solution with O(n) space complexity
    f = [0] + flowerbed + [0]
    
    for i in range(1, len(f) - 1):  # skip first & last
        if f[i - 1] == 0 and f[i] == 0 and f[i + 1] == 0:
            f[i] = 1
            n -= 1
    return n <= 0


def main():
    result = can_place_flowers(flowerbed = [1,0,0,0,1], n = 1)
    print(result) # True

    result = can_place_flowers(flowerbed = [1,0,0,0,1], n = 2)
    print(result) # False

if __name__ == "__main__":
    main()
