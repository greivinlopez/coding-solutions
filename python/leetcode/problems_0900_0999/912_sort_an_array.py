# ------------------
# 912. Sort An Array
# ------------------

# Problem: https://leetcode.com/problems/sort-an-array/
# 
# Given an array of integers nums, sort the array in ascending order and return 
# it.
# 
# You must solve the problem without using any built-in functions in O(nlog(n)) 
# time complexity and with the smallest space complexity possible.
# 
#  
# Example 1:
# 
# Input: nums = [5,2,3,1]
# Output: [1,2,3,5]
# Explanation: After sorting the array, the positions of some numbers are not 
# changed (for example, 2 and 3), while the positions of other numbers are 
# changed (for example, 1 and 5).
# 
# Example 2:
# 
# Input: nums = [5,1,1,2,0,0]
# Output: [0,0,1,1,2,5]
# Explanation: Note that the values of nums are not necessarily unique.
#  
# 
# Constraints:
# 
#   1 <= nums.length <= 5 * 10^4
#   -5 * 10^4 <= nums[i] <= 5 * 10^4

# Solution: 
# Credit: Navdeep Singh founder of NeetCode
def sort_array(nums):
    def merge(arr, L, M, R):
        left, right = arr[L:M+1], arr[M+1:R+1]
        i, j, k = L, 0, 0
        while j < len(left) and k < len(right):
            if left[j] <= right[k]:
                arr[i] = left[j]
                j += 1
            else:
                arr[i] = right[k]
                k += 1
            i += 1
        while j < len(left):
            nums[i] = left[j]
            j += 1
            i += 1
        while k < len(right):
            nums[i] = right[k]
            k += 1
            i += 1

    def mergeSort(arr, l, r):
        if l == r:
            return arr
        m = (l + r) // 2
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)
        return arr
    
    return mergeSort(nums, 0, len(nums) - 1)


def main():
    result = sort_array([5,2,3,1])
    print(result) # [1,2,3,5]

    result = sort_array([5,1,1,2,0,0])
    print(result) # [0,0,1,1,2,5]

if __name__ == "__main__":
    main()
