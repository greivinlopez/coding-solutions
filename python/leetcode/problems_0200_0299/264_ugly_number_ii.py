# -------------------
# 264. Ugly Number II
# -------------------

# Problem: https://leetcode.com/problems/ugly-number-ii
#
# An ugly number is a positive integer whose prime factors are limited to 2, 3,
# and 5.
# 
# Given an integer n, return the n^th ugly number.
# 
# Example 1:
# 
# Input: n = 10
# Output: 12
# 
# Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10
# ugly numbers.
# 
# Example 2:
# 
# Input: n = 1
# Output: 1
# 
# Explanation: 1 has no prime factors, therefore all of its prime factors are
# limited to 2, 3, and 5.
# 
# 
# Constraints:
#         1 <= n <= 1690

import heapq

# Solution: https://youtu.be/1pj2a5bmziY
# Credit: Navdeep Singh founder of NeetCode
def nth_ugly_number(n):
    # Heap Solution
    minHeap = [1]
    visit = set()
    factors = [2, 3, 5]
    for i in range(n):
        num = heapq.heappop(minHeap)
        if i == n - 1:
            return num
        
        for f in factors:
            if num * f not in visit:
                visit.add(num * f)
                heapq.heappush(minHeap, num * f)
    # Time: O(n * log(n)) 
    # Space: O(n)

def nth_ugly_number_alt(n):
    # More optimized dp solution
    nums = [1]
    i2, i3, i5 = 0, 0, 0
    
    for i in range(1, n):
        next_num = min(
            nums[i2] * 2, nums[i3] * 3, nums[i5] * 5
        )
        nums.append(next_num)
        if next_num == nums[i2] * 2:
            i2 += 1
        if next_num == nums[i3] * 3:
            i3 += 1
        if next_num == nums[i5] * 5:
            i5 += 1
    
    return nums[n - 1]
    # Time: O(n) 
    # Space: O(n)


def main():
    result = nth_ugly_number(n = 10)
    print(result) # True

    result = nth_ugly_number(n = 1)
    print(result) # True

if __name__ == "__main__":
    main()
