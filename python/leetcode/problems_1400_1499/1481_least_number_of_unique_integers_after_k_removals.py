# ------------------------------------------------------
# 1481. Least Number Of Unique Integers After K Removals
# ------------------------------------------------------

# Problem: https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals
#
# Given an array of integers arr and an integer k. Find the least number of unique
# integers after removing exactly k elements.
# 
# Example 1:
# 
# Input: arr = [5,5,4], k = 1
# Output: 1
# Explanation: Remove the single 4, only 5 is left.
# 
# Example 2:
# 
# Input: arr = [4,3,1,1,3,3,2], k = 3
# Output: 2
# Explanation: Remove 4, 2 and either one of the two 1s or three 3s. 1 and 3 will
# be left.
# 
# 
# Constraints:
#         1 <= arr.length <= 10^5
#         1 <= arr[i] <= 10^9
#         0 <= k <= arr.length

from collections import Counter
import heapq

# Solution: https://youtu.be/Nsp_ta7SlEk
# Credit: Navdeep Singh founder of NeetCode
def find_least_num_of_unique_ints(arr, k): 
    # Use a heap
    freq = Counter(arr)
    heap = list(freq.values())
    heapq.heapify(heap)

    res = len(heap)
    while k > 0 and heap:
        f = heapq.heappop(heap)
        if k >= f:
            k -= f
            res -= 1
    return res

def find_least_num_of_unique_ints_buckets(arr, k):
    # Use buckets
    freq = Counter(arr)
    freqList = [0] * (len(arr) + 1)

    for n, f in freq.items():
        freqList[f] += 1

    res = len(freq)
    for f in range(1, len(freqList)):
        remove = freqList[f]
        if k >= f * remove:
            k -= f * remove
            res -= remove
        else:
            remove = k // f
            res -= remove
            break
    return res


def main():
    result = find_least_num_of_unique_ints(arr = [5,5,4], k = 1)
    print(result) # 1

    result = find_least_num_of_unique_ints(arr = [4,3,1,1,3,3,2], k = 3)
    print(result) # 2

if __name__ == "__main__":
    main()
