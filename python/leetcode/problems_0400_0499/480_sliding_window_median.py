# -----------------------------
# 480. Sliding Window Median 🪟
# -----------------------------

# Problem: https://leetcode.com/problems/sliding-window-median
#
# The median is the middle value in an ordered integer list. If the size of the
# list is even, there is no middle value. So the median is the mean of the two
# middle values.
#         
#   * For examples, if arr = [2,3,4], the median is 3.
#   * For examples, if arr = [1,2,3,4], the median is (2 + 3) / 2 = 2.5.
# 
# You are given an integer array nums and an integer k. There is a sliding window
# of size k which is moving from the very left of the array to the very right. You
# can only see the k numbers in the window. Each time the sliding window moves
# right by one position.
# 
# Return the median array for each window in the original array. Answers within
# 10⁻⁵ of the actual value will be accepted.
# 
# Example 1:
# 
# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [1.00000,-1.00000,-1.00000,3.00000,5.00000,6.00000]
# 
# Explanation:
# Window position                Median
# ---------------                -----
# [1  3  -1] -3  5  3  6  7        1
#  1 [3  -1  -3] 5  3  6  7       -1
#  1  3 [-1  -3  5] 3  6  7       -1
#  1  3  -1 [-3  5  3] 6  7        3
#  1  3  -1  -3 [5  3  6] 7        5
#  1  3  -1  -3  5 [3  6  7]       6
# 
# Example 2:
# 
# Input: nums = [1,2,3,4,2,3,1,4,2], k = 3
# Output: [2.00000,3.00000,3.00000,3.00000,2.00000,3.00000,2.00000]
# 
# 
# Constraints:
#         1 <= k <= nums.length <= 10⁵
#         -2³¹ <= nums[i] <= 2³¹ - 1

from collections import defaultdict
from heapq import heappush, heappop

# Solution: https://leetcode.com/problems/sliding-window-median/solutions/1942580/easiest-python-o-n-log-k-two-heaps-lazy-removal-96-23
# Credit: Anton Belski -> https://leetcode.com/u/AntonBelski/
def median_sliding_window_alt(nums, k):

    def find_median(max_heap, min_heap, heap_size):
        if heap_size % 2 == 1:
            return -max_heap[0]
        else:
            return (-max_heap[0] + min_heap[0]) / 2

    max_heap = []
    min_heap = []
    heap_dict = defaultdict(int)
    result = []
    
    for i in range(k):
        heappush(max_heap, -nums[i])
        heappush(min_heap, -heappop(max_heap))
        if len(min_heap) > len(max_heap):
            heappush(max_heap, -heappop(min_heap))
    
    median = find_median(max_heap, min_heap, k)
    result.append(median)
    
    for i in range(k, len(nums)):
        prev_num = nums[i - k]
        heap_dict[prev_num] += 1

        balance = -1 if prev_num <= median else 1
        
        if nums[i] <= median:
            balance += 1
            heappush(max_heap, -nums[i])
        else:
            balance -= 1
            heappush(min_heap, nums[i])
        
        if balance < 0:
            heappush(max_heap, -heappop(min_heap))
        elif balance > 0:
            heappush(min_heap, -heappop(max_heap))

        while max_heap and heap_dict[-max_heap[0]] > 0:
            heap_dict[-max_heap[0]] -= 1
            heappop(max_heap)
        
        while min_heap and heap_dict[min_heap[0]] > 0:
            heap_dict[min_heap[0]] -= 1
            heappop(min_heap)

        median = find_median(max_heap, min_heap, k)
        result.append(median)
    
    return result
    # Time: O(n * k) worst case, O(n * log(k)) amortized/average case
    # Space: O(n)


# My Solution
# Pros: Better time complexity and cleaner
# Cons: Requires external library: sortedcontainers
# ---------------------------------------------
#  pip install sortedcontainers
# ---------------------------------------------
def median_sliding_window(nums, k):
    from sortedcontainers import SortedList
    
    window = SortedList()
    result = []
    
    # Add first k elements
    for i in range(k):
        window.add(nums[i])
    
    # Calculate first median
    if k % 2 == 1:
        result.append(float(window[k // 2]))
    else:
        result.append((window[k // 2 - 1] + window[k // 2]) / 2.0)
    
    # Slide the window
    for i in range(k, len(nums)):
        # Remove leftmost element
        window.remove(nums[i - k])
        
        # Add new element
        window.add(nums[i])
        
        # Calculate median
        if k % 2 == 1:
            result.append(float(window[k // 2]))
        else:
            result.append((window[k // 2 - 1] + window[k // 2]) / 2.0)
    
    return result
    # Time: O(n * log(k))
    # Space: O(k)


def main():
    result = median_sliding_window(nums = [1,3,-1,-3,5,3,6,7], k = 3)
    print(result) # [1, -1, -1, 3, 5, 6]

    result = median_sliding_window(nums = [1,2,3,4,2,3,1,4,2], k = 3)
    print(result) # [2, 3, 3, 3, 2, 3, 2]

if __name__ == "__main__":
    main()
