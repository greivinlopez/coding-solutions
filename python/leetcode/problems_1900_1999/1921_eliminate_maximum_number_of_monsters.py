# ---------------------------------------------
# 1921. Eliminate Maximum Number of Monsters 👾
# ---------------------------------------------

# Problem: https://leetcode.com/problems/eliminate-maximum-number-of-monsters
#
# You are playing a video game where you are defending your city from a group of n
# monsters. You are given a 0-indexed integer array dist of size n, where dist[i]
# is the initial distance in kilometers of the ith monster from the city.
# 
# The monsters walk toward the city at a constant speed. The speed of each monster
# is given to you in an integer array speed of size n, where speed[i] is the speed
# of the ith monster in kilometers per minute.
# 
# You have a weapon that, once fully charged, can eliminate a single monster.
# 
# However, the weapon takes one minute to charge. The weapon is fully charged at
# the very start.
# 
# You lose when any monster reaches your city. If a monster reaches the city at
# the exact moment the weapon is fully charged, it counts as a loss, and the game
# ends before you can use your weapon.
# 
# Return the maximum number of monsters that you can eliminate before you lose, or
# n if you can eliminate all the monsters before they reach the city.
# 
# Example 1:
# 
# Input: dist = [1,3,4], speed = [1,1,1]
# Output: 3
# 
# Explanation:
# In the beginning, the distances of the monsters are [1,3,4]. You eliminate the
# first monster.
# After a minute, the distances of the monsters are [X,2,3]. You eliminate the
# second monster.
# After a minute, the distances of the monsters are [X,X,2]. You eliminate the
# third monster.
# All 3 monsters can be eliminated.
# 
# Example 2:
# 
# Input: dist = [1,1,2,3], speed = [1,1,1,1]
# Output: 1
# 
# Explanation:
# In the beginning, the distances of the monsters are [1,1,2,3]. You eliminate the
# first monster.
# After a minute, the distances of the monsters are [X,0,1,2], so you lose.
# You can only eliminate 1 monster.
# 
# Example 3:
# 
# Input: dist = [3,2,4], speed = [5,3,2]
# Output: 1
# 
# Explanation:
# In the beginning, the distances of the monsters are [3,2,4]. You eliminate the
# first monster.
# After a minute, the distances of the monsters are [X,0,2], so you lose.
# You can only eliminate 1 monster.
# 
# 
# Constraints:
#         n == dist.length == speed.length
#         1 <= n <= 10⁵
#         1 <= dist[i], speed[i] <= 10⁵

import math

# Solution: https://youtu.be/6QQRayzOTD4
# Credit: Navdeep Singh founder of NeetCode
def eliminate_maximum(dist, speed):
    min_reach = []
    for d, s in zip(dist, speed):
        minute = math.ceil(d / s)
        min_reach.append(minute)

    min_reach.sort()
    res = 0
    for minute in range(len(min_reach)):
        if minute >= min_reach[minute]:
            return res
        res += 1
    return res
    # Time: O(n * log(n))
    # Space: O(n)


def main():
    result = eliminate_maximum(dist = [1,3,4], speed = [1,1,1])
    print(result) # 3

    result = eliminate_maximum(dist = [1,1,2,3], speed = [1,1,1,1])
    print(result) # 1

    result = eliminate_maximum(dist = [3,2,4], speed = [5,3,2])
    print(result) # 1

if __name__ == "__main__":
    main()
