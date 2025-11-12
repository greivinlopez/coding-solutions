# ------------------------------------
# 2101. Detonate The Maximum Bombs 💣💥
# ------------------------------------

# Problem: https://leetcode.com/problems/detonate-the-maximum-bombs
#
# You are given a list of bombs. The range of a bomb is defined as the area where
# its effect can be felt. This area is in the shape of a circle with the center as
# the location of the bomb.
# 
# The bombs are represented by a 0-indexed 2D integer array bombs where bombs[i] =
# [xi, yi, ri]. xi and yi denote the X-coordinate and Y-coordinate of the location
# of the ith bomb, whereas ri denotes the radius of its range.
# 
# You may choose to detonate a single bomb. When a bomb is detonated, it will
# detonate all bombs that lie in its range. These bombs will further detonate the
# bombs that lie in their ranges.
# 
# Given the list of bombs, return the maximum number of bombs that can be
# detonated if you are allowed to detonate only one bomb.
# 
# Example 1:
# 
# Input: bombs = [[2,1,3],[6,1,4]]
# Output: 2
# Explanation:
# The above figure shows the positions and ranges of the 2 bombs.
# If we detonate the left bomb, the right bomb will not be affected.
# But if we detonate the right bomb, both bombs will be detonated.
# So the maximum bombs that can be detonated is max(1, 2) = 2.
# 
# Example 2:
# 
# Input: bombs = [[1,1,5],[10,10,5]]
# Output: 1
# Explanation:
# Detonating either bomb will not detonate the other bomb, so the maximum number
# of bombs that can be detonated is 1.
# 
# Example 3:
# 
# Input: bombs = [[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]
# Output: 5
# Explanation:
# The best bomb to detonate is bomb 0 because:
# - Bomb 0 detonates bombs 1 and 2. The red circle denotes the range of bomb 0.
# - Bomb 2 detonates bomb 3. The blue circle denotes the range of bomb 2.
# - Bomb 3 detonates bomb 4. The green circle denotes the range of bomb 3.
# Thus all 5 bombs are detonated.
# 
# 
# Constraints:
#         1 <= bombs.length <= 100
#         bombs[i].length == 3
#         1 <= xi, yi, ri <= 10^5

from math import sqrt

# Solution: https://youtu.be/8NPbAvVXKR4
# Credit: Navdeep Singh founder of NeetCode
def maximum_detonation(bombs):
    n = len(bombs)
    graph = [[] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i != j:
                x1, y1, r1 = bombs[i]
                x2, y2, _ = bombs[j]

                dst = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

                if dst <= r1:
                    graph[i].append(j)

    def dfs(node, vis):
        vis[node] = True
        count = 1

        for nbh in graph[node]:
            if not vis[nbh]:
                count += dfs(nbh, vis)
                
        return count

    detonated = 0

    for i in range(n):
        visited = [False] * n
        detonated = max(detonated, dfs(i, visited))
    
    return detonated


def main():
    result = maximum_detonation([[2,1,3],[6,1,4]])
    print(result) # 2

    result = maximum_detonation([[1,1,5],[10,10,5]])
    print(result) # 1

    result = maximum_detonation([[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]])
    print(result) # 5

if __name__ == "__main__":
    main()
