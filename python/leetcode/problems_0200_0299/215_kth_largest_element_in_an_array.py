# ------------------------------------
# 215. Kth Largest Element In An Array
# ------------------------------------

# Problem: https://leetcode.com/problems/kth-largest-element-in-an-array/
# 
# Given an integer array nums and an integer k, return the kth largest element 
# in the array.
# 
# Note that it is the kth largest element in the sorted order, not the kth 
# distinct element.
# 
# Can you solve it without sorting?
#  
# Example 1:
# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
# Example 2:
# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4
# 
#  
# Constraints:
# 
# 	1 <= k <= nums.length <= 105
# 	-104 <= nums[i] <= 104

import heapq

# Solution: https://www.youtube.com/watch?v=XEmy13g1Qxc
# Credit: Navdeep Singh founder of NeetCode

# Solution: Sorting
# Time Complexity:
#   - Best Case: O(n*log(k))
#   - Average Case: O(n*log(k))
#   - Worst Case:O(n*log(k))
# Extra Space Complexity: O(k)
def kth_largest_heapify(nums, k):
    heapq.heapify(nums)
    while len(nums) > k:
        heapq.heappop(nums)
    return nums[0]

# Solution: Sorting
# Time Complexity:
#   - Best Case: O(n)
#   - Average Case: O(n*log(n))
#   - Worst Case:O(n*log(n))
# Extra Space Complexity: O(n)
def kth_largest_simple(nums, k):
    nums.sort()
    return nums[len(nums) - k]

# Solution: QuickSelect
# Time Complexity: O(n)
# Extra Space Complexity: O(n)
def kth_largest_quicksort(nums, k):
    pivot = random.choice(nums)
    left = [num for num in nums if num > pivot]
    mid = [num for num in nums if num == pivot]
    right = [num for num in nums if num < pivot]

    length_left = len(left)
    length_right = len(right)
    length_mid = len(mid)
    if k <= length_left:
        return self.findKthLargest(left, k)
    elif k > length_left + length_mid:
        return self.findKthLargest(right, k - length_mid - length_left)
    else:
        return mid[0]

# Solution: https://youtu.be/ZmGk7h8KZLs
# Credit: Greg Hogg
def kth_largest_heap(nums, k):
    for i in range(len(nums)):
        nums[i] = -nums[i] # Max Heap

    heapq.heapify(nums)

    for _ in range(k-1):
        heapq.heappop(nums)

    return -heapq.heappop(nums)
    # Max Heap of size n
    # Time: O(n + k log n)
    # Space: O(1)

def kth_largest_min_heap(nums, k):
    min_heap = []
        
    for num in nums:
        if len(min_heap) < k:
            heapq.heappush(min_heap, num)
        else:
            heapq.heappushpop(min_heap, num)
    
    return min_heap[0]
    # Min heap of size k
    # Time: O(n log k)
    # Space: O(k)


def main():
    result = kth_largest_heapify([3,2,1,5,6,4], 2)
    print(result) # 5

    result = kth_largest_heapify([3,2,3,1,2,4,5,5,6], 4)
    print(result) # 4

if __name__ == "__main__":
    main()
