# ----------------------------------------
# 2251. Number of Flowers in Full Bloom 🌷
# ----------------------------------------

# Problem: https://leetcode.com/problems/number-of-flowers-in-full-bloom
#
# You are given a 0-indexed 2D integer array flowers, where flowers[i] = [startᵢ, endᵢ] 
# means the ith flower will be in full bloom from startᵢ to endᵢ
# (inclusive). You are also given a 0-indexed integer array people of size n,
# where people[i] is the time that the ith person will arrive to see the flowers.
# 
# Return an integer array answer of size n, where answer[i] is the number of
# flowers that are in full bloom when the i^th person arrives.
# 
# Example 1:
# 
# Input: flowers = [[1,6],[3,7],[9,12],[4,13]], people = [2,3,7,11]
# Output: [1,2,2,2]
# 
# Explanation: The figure above shows the times when the flowers are in full bloom
# and when the people arrive.
# For each person, we return the number of flowers in full bloom during their
# arrival.
# 
# Example 2:
# 
# Input: flowers = [[1,10],[3,3]], people = [3,3,2]
# Output: [2,2,1]
# 
# Explanation: The figure above shows the times when the flowers are in full bloom
# and when the people arrive.
# For each person, we return the number of flowers in full bloom during their
# arrival.
# 
# 
# Constraints:
#         1 <= flowers.length <= 5 * 10⁴
#         flowers[i].length == 2
#         1 <= startᵢ <= endᵢ <= 10⁹
#         1 <= people.length <= 5 * 10⁴
#         1 <= people[i] <= 10⁹

import heapq

# Solution: https://youtu.be/zY3Uty9IwvY
# Credit: Navdeep Singh founder of NeetCode
def full_bloom_flowers(flowers, people):
    people = [(p, i) for i, p in enumerate(people)]
    res = [0] * len(people)
    flowers.sort()
    end = []
    
    j = 0
    for p, i in sorted(people):
        while j < len(flowers) and flowers[j][0] <= p:
            heapq.heappush(end, flowers[j][1])
            j += 1
        
        while end and end[0] < p:
            heapq.heappop(end)
        
        res[i] = len(end)
    
    return res
    # Time: O(n * log(n) + m * log(m))
    # Space: O(n + m)
    # n = number of people
    # m = number of flowers


def main():
    result = full_bloom_flowers(flowers = [[1,6],[3,7],[9,12],[4,13]], people = [2,3,7,11])
    print(result) # [1,2,2,2]

    result = full_bloom_flowers(flowers = [[1,10],[3,3]], people = [3,3,2])
    print(result) # [2,2,1]

if __name__ == "__main__":
    main()
