# ----------------------------
# 347. Top K Frequent Elements
# ----------------------------

# Problem: https://leetcode.com/problems/top-k-frequent-elements/
# 
# Given an integer array nums and an integer k, return the k most frequent 
# elements. You may return the answer in any order.
# 
#  
# Example 1:
# 
# Input: nums = [1,1,1,2,2,3], k = 2
# 
# Output: [1,2]
# 
# 
# Example 2:
# 
# Input: nums = [1], k = 1
# 
# Output: [1]
# 
# 
# Example 3:
# 
# Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2
# 
# Output: [1,2]
# 
# 
# Constraints:
# 
# 	1 <= nums.length <= 10^5
# 	-10^4 <= nums[i] <= 10^4
# 	k is in the range [1, the number of unique elements in the array].
# 	It is guaranteed that the answer is unique.
# 
# Follow up: Your algorithm's time complexity must be better than O(n log n), 
# where n is the array's size.


# Solution: https://youtu.be/YPTqKIgVk-k
# Credit: Navdeep Singh founder of NeetCode
def top_k_frequent(nums, k):
    count = {}
    freq = [[] for i in range(len(nums) + 1)]

    for n in nums:
        count[n] = 1 + count.get(n, 0)
    for n, c in count.items():
        freq[c].append(n)

    res = []
    for i in range(len(freq) - 1, 0, -1):
        res += freq[i]
        if len(res) == k:
            return res
    # Time: O(n)
    # Space: O(n)

# Solution: https://youtu.be/phNDYf1xzco
# Credit: Greg Hogg
# Buckets Solution
from collections import Counter
def top_k_frequent_buckets(nums, k):
    n = len(nums)
    counter = Counter(nums)
    buckets = [0] * (n + 1)

    for num, freq in counter.items():
        if buckets[freq] == 0:
            buckets[freq] = [num]
        else:
            buckets[freq].append(num)
    
    ret = []
    for i in range(n, -1, -1):
        if buckets[i] != 0:
            ret.extend(buckets[i])
        if len(ret) == k:
            break
    
    return ret
    # Time: O(n)
    # Space: O(n)

# Heap Solution:
from collections import Counter
import heapq
def top_k_frequent_heap(nums, k):
    counter = Counter(nums)
    heap = []

    for key, val in counter.items():
        if len(heap) < k:
            heapq.heappush(heap, (val, key))
        else:
            heapq.heappushpop(heap, (val, key))
    
    return [h[1] for h in heap]
    # Time: O(n log k)
    # Space: O(k)

# Heap Solution 2:
import heapq
from collections import Counter

def top_k_frequent_heap_2(nums, k):
    # Step 1: Count frequency
    freq_map = Counter(nums)

    # Step 2: Use max heap (invert frequency to simulate max heap)
    max_heap = [(-freq, num) for num, freq in freq_map.items()]
    heapq.heapify(max_heap)  # Convert list into a heap in O(n)

    # Step 3: Extract k most frequent elements
    result = [heapq.heappop(max_heap)[1] for _ in range(k)]
    return result
    # Max Heap


def main():
    result = top_k_frequent([1,1,1,2,2,3], 2)
    print(result) # [1, 2]

    result = top_k_frequent([1], 1)
    print(result) # [1]

    result = top_k_frequent([1,2,1,2,1,2,3,1,3,2], 2)
    print(result) # [1, 2]

if __name__ == "__main__":
    main()
