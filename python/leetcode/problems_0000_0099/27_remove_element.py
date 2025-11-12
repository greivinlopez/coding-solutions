# ------------------
# 27. Remove Element
# ------------------

# Problem: https://leetcode.com/problems/remove-element
#
# Given an integer array nums and an integer val, remove all occurrences of val in
# nums in-place. The order of the elements may be changed. Then return the number
# of elements in nums which are not equal to val.
# 
# Consider the number of elements in nums which are not equal to val be k, to get
# accepted, you need to do the following things:
#        
#   * Change the array nums such that the first k elements of nums contain the
#     elements which are not equal to val. The remaining elements of nums are not
#     important as well as the size of nums.
#   * Return k.
# 
# Custom Judge:
# 
# The judge will test your solution with the following code:
# int[] nums = [...]; // Input array
# int val = ...; // Value to remove
# int[] expectedNums = [...]; // The expected answer with correct length.
#                             // It is sorted with no values equaling val.
# int k = removeElement(nums, val); // Calls your implementation
# assert k == expectedNums.length;
# sort(nums, 0, k); // Sort the first k elements of nums
# for (int i = 0; i < actualLength; i++) {
#     assert nums[i] == expectedNums[i];
# }
# 
# If all assertions pass, then your solution will be accepted.
# 
# Example 1:
# 
# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]
# 
# Explanation: Your function should return k = 2, with the first two elements of
# nums being 2.
# It does not matter what you leave beyond the returned k (hence they are
# underscores).
# 
# Example 2:
# 
# Input: nums = [0,1,2,2,3,0,4,2], val = 2
# Output: 5, nums = [0,1,4,0,3,_,_,_]
# 
# Explanation: Your function should return k = 5, with the first five elements of
# nums containing 0, 0, 1, 3, and 4.
# Note that the five elements can be returned in any order.
# It does not matter what you leave beyond the returned k (hence they are
# underscores).
# 
# 
# Constraints:
#         0 <= nums.length <= 100
#         0 <= nums[i] <= 50
#         0 <= val <= 100


# Solution: https://youtu.be/Pcd1ii9P9ZI
# Credit: Navdeep Singh founder of NeetCode 
def remove_element(nums, val):
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k
    # Time: O(n)
    # Space: O(1)

# Solution: https://youtu.be/opmnMBAEe8E
# Credit: Greg Hog
# Almost identical
def remove_element_alt(nums, val):
    i = 0
    n = len(nums)

    while i < n:
        if nums[i] == val:
            nums[i] = nums[n - 1]
            n -= 1
        else:
            i += 1
    return n
    # Time: O(n)
    # Space: O(1)


def main():
    result = remove_element(nums = [3,2,2,3], val = 3) # 2
    print(result)
    result = remove_element(nums = [0,1,2,2,3,0,4,2], val = 2) # 5
    print(result)

if __name__ == "__main__":
    main()