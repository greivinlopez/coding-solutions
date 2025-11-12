# --------------------------
# 1046. Last Stone Weight 🪨
# --------------------------

# Problem: https://leetcode.com/problems/last-stone-weight
#
# You are given an array of integers stones where stones[i] is the weight of the
# ith stone.
# 
# We are playing a game with the stones. On each turn, we choose the heaviest two
# stones and smash them together. Suppose the heaviest two stones have weights x
# and y with x <= y. The result of this smash is:
# 
#         If x == y, both stones are destroyed, and
#         If x != y, the stone of weight x is destroyed, and the stone of weight y
#         has new weight y - x.
# 
# At the end of the game, there is at most one stone left.
# 
# Return the weight of the last remaining stone. If there are no stones left,
# return 0.
# 
# Example 1:
# 
# Input: stones = [2,7,4,1,8,1]
# Output: 1
# Explanation:
# We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
# we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
# we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
# we combine 1 and 1 to get 0 so the array converts to [1] then that's the value
# of the last stone.
# 
# Example 2:
# 
# Input: stones = [1]
# Output: 1
# 
# 
# Constraints:
#         1 <= stones.length <= 30
#         1 <= stones[i] <= 1000

import heapq

# Solution: https://youtu.be/B-QCq79-Vfw
# Credit: Navdeep Singh founder of NeetCode
def last_stone_weight(stones):
    # Next to lines can be replaced by using heapq._heapify_max(stones)
    stones = [-s for s in stones]
    heapq.heapify(stones)

    while len(stones) > 1:
        first = heapq.heappop(stones)
        second = heapq.heappop(stones)
        if second > first:
            heapq.heappush(stones, first - second)

    stones.append(0)
    return abs(stones[0])
    # Time: O(n log n)
    # Space: O(1)

# Solution: https://youtu.be/B-QCq79-Vfw
# Credit: Greg Hogg
# Optimal Solution Same as Navdeep's
def last_stone_weight_brute(stones):
    def remove_largest():
        index_of_largest = stones.index(max(stones))
        return stones.pop(index_of_largest)

    while len(stones) > 1:
        stone_1 = remove_largest()
        stone_2 = remove_largest()
        if stone_1 != stone_2:
            stones.append(stone_1 - stone_2)

    return stones[0] if stones else 0
    # Time: O(n^2)
    # Space: O(1)

def main():
    result = last_stone_weight([2,7,4,1,8,1])
    print(result) # 1

    result = last_stone_weight([1])
    print(result) # 1

if __name__ == "__main__":
    main()
