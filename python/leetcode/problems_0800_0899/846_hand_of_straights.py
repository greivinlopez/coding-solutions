# -------------------------
# 846. Hand of Straights ♠️
# -------------------------

# Problem: https://leetcode.com/problems/hand-of-straights/
# 
# Alice has some number of cards and she wants to rearrange the cards into 
# groups so that each group is of size groupSize, and consists of groupSize 
# consecutive cards.
# 
# Given an integer array hand where hand[i] is the value written on the ith 
# card and an integer groupSize, return true if she can rearrange the cards, 
# or false otherwise.
# 
#  
# Example 1:
# 
# Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
# Output: true
# Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]
# 
# 
# Example 2:
# 
# Input: hand = [1,2,3,4,5], groupSize = 4
# Output: false
# Explanation: Alice's hand can not be rearranged into groups of 4.
# 
# 
# Constraints:
# 
#   1 <= hand.length <= 10^4
#   0 <= hand[i] <= 10^9
#   1 <= groupSize <= hand.length
# 
# Note: This question is the same as 1296: 
# https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/

import heapq

# Solution: https://youtu.be/amnrMCVd2YI
# Credit: Navdeep Singh founder of NeetCode
def is_n_straight_hand(hand, groupSize):
    if len(hand) % groupSize:
        return False

    count = {}
    for n in hand:
        count[n] = 1 + count.get(n, 0)

    minH = list(count.keys())
    heapq.heapify(minH)
    while minH:
        first = minH[0]
        for i in range(first, first + groupSize):
            if i not in count:
                return False
            count[i] -= 1
            if count[i] == 0:
                if i != minH[0]:
                    return False
                heapq.heappop(minH)
    return True

def main():
    result = is_n_straight_hand(hand = [1,2,3,6,2,3,4,7,8], groupSize = 3)
    print(result) # True

    result = is_n_straight_hand(hand = [1,2,3,4,5], groupSize = 4)
    print(result) # False

if __name__ == "__main__":
    main()
