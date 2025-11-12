# ---------------------------------
# 1675. Minimize Deviation in Array
# ---------------------------------

# Problem: https://leetcode.com/problems/minimize-deviation-in-array
#
# You are given an array nums of n positive integers.
# 
# You can perform two types of operations on any element of the array any number
# of times:
# 
#   * If the element is even, divide it by 2.
#     For example, if the array is [1,2,3,4], then you can do this
#     operation on the last element, and the array will be [1,2,3,2].
# 
#   * If the element is odd, multiply it by 2.
#     For example, if the array is [1,2,3,4], then you can do this
#     operation on the first element, and the array will be [2,2,3,4].
# 
# The deviation of the array is the maximum difference between any two elements in
# the array.
# 
# Return the minimum deviation the array can have after performing some number of
# operations.
# 
# Example 1:
# 
# Input: nums = [1,2,3,4]
# Output: 1
# 
# Explanation: You can transform the array to [1,2,3,2], then to [2,2,3,2], then
# the deviation will be 3 - 2 = 1.
# 
# Example 2:
# 
# Input: nums = [4,1,5,20,3]
# Output: 3
# 
# Explanation: You can transform the array after two operations to [4,2,5,5,3],
# then the deviation will be 5 - 2 = 3.
# 
# Example 3:
# 
# Input: nums = [2,10,8]
# Output: 3
# 
# 
# Constraints:
#         n == nums.length
#         2 <= n <= 5 * 10^4
#         1 <= nums[i] <= 10^9

import heapq

# Solution: https://youtu.be/boHNFptxo2A
# Credit: Navdeep Singh founder of NeetCode
def minimum_deviation(nums):
    min_heap, heap_max = [], 0
    
    for n in nums:
        tmp = n
        while n % 2 == 0:
            n //= 2
        min_heap.append((n, max(tmp, 2 * n)))
        heap_max = max(heap_max, n)

    res = float("inf")
    heapq.heapify(min_heap)
    
    while len(min_heap) == len(nums):
        n, n_max = heapq.heappop(min_heap)
        res = min(res, heap_max - n)

        if n < n_max:
            heapq.heappush(min_heap, (n * 2, n_max))
            heap_max = max(heap_max, n * 2)

    return res
    # Time: O(n * log(m) + n * log(n))
    # Space: O(n)


def main():
    result = minimum_deviation([1,2,3,4])
    print(result) # 1

    result = minimum_deviation([4,1,5,20,3])
    print(result) # 3

    result = minimum_deviation([2,10,8])
    print(result) # 3

if __name__ == "__main__":
    main()
