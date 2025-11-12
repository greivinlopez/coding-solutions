# ------------------
# 493. Reverse Pairs
# ------------------

# Problem: https://leetcode.com/problems/reverse-pairs
#
# Given an integer array nums, return the number of reverse pairs in the array.
# 
# A reverse pair is a pair (i, j) where:
# 
#         0 <= i < j < nums.length and
#         nums[i] > 2 * nums[j].
# 
# Example 1:
# 
# Input: nums = [1,3,2,3,1]
# Output: 2
# 
# Explanation: The reverse pairs are:
# (1, 4) --> nums[1] = 3, nums[4] = 1, 3 > 2 * 1
# (3, 4) --> nums[3] = 3, nums[4] = 1, 3 > 2 * 1
# 
# Example 2:
# 
# Input: nums = [2,4,3,5,1]
# Output: 3
# 
# Explanation: The reverse pairs are:
# (1, 4) --> nums[1] = 4, nums[4] = 1, 4 > 2 * 1
# (2, 4) --> nums[2] = 3, nums[4] = 1, 3 > 2 * 1
# (3, 4) --> nums[3] = 5, nums[4] = 1, 5 > 2 * 1
# 
# 
# Constraints:
#         1 <= nums.length <= 5 * 10⁴
#         -2³¹ <= nums[i] <= 2³¹ - 1


# Solution: https://algo.monster/liteproblems/493
# Credit: AlgoMonster
def reverse_pairs(nums): 
    def merge_sort_and_count(left, right):
        # Base case: single element or invalid range
        if left >= right:
            return 0
        
        # Divide the array into two halves
        mid = (left + right) // 2
        
        # Recursively count pairs in left half, right half, and across halves
        count = merge_sort_and_count(left, mid) + merge_sort_and_count(mid + 1, right)
        
        # Count reverse pairs across the two sorted halves
        # For each element in left half, count elements in right half
        # where nums[i] > 2 * nums[j]
        i, j = left, mid + 1
        while i <= mid and j <= right:
            if nums[i] <= 2 * nums[j]:
                i += 1
            else:
                # All elements from i to mid satisfy the condition
                # with current nums[j]
                count += mid - i + 1
                j += 1
        
        # Merge the two sorted halves
        temp = []
        i, j = left, mid + 1
        
        # Merge elements in sorted order
        while i <= mid and j <= right:
            if nums[i] <= nums[j]:
                temp.append(nums[i])
                i += 1
            else:
                temp.append(nums[j])
                j += 1
        
        # Add remaining elements from left half
        temp.extend(nums[i:mid + 1])
        
        # Add remaining elements from right half
        temp.extend(nums[j:right + 1])
        
        # Copy sorted elements back to original array
        nums[left:right + 1] = temp
        
        return count
    
    # Start merge sort from entire array
    return merge_sort_and_count(0, len(nums) - 1)
    # Time: O(n * log(n))
    # Space: O(n)


def main():
    result = reverse_pairs([1,3,2,3,1])
    print(result) # 2

    result = reverse_pairs([2,4,3,5,1])
    print(result) # 3

if __name__ == "__main__":
    main()
