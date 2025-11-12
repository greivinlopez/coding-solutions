# -----------------------------------------------------
# 1287. Element Appearing More Than 25% In Sorted Array
# -----------------------------------------------------

# Problem: https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array
#
# Given an integer array sorted in non-decreasing order, there is exactly one
# integer in the array that occurs more than 25% of the time, return that integer.
# 
# Example 1:
# 
# Input: arr = [1,2,2,6,6,6,6,7,10]
# Output: 6
# 
# Example 2:
# 
# Input: arr = [1,1]
# Output: 1
# 
# 
# Constraints:
#         1 <= arr.length <= 10⁴
#         0 <= arr[i] <= 10⁵


# Credit: Jaweria Batool -> https://github.com/Jaweria-B
def find_special_integer(arr):
    size = len(arr) // 4
    
    for i in range(len(arr) - size):
        if arr[i] == arr[i + size]:
            return arr[i]
    
    return -1
    # Time: O(n)
    # Space: O(1)


def main():
    result = find_special_integer(arr = [1,2,2,6,6,6,6,7,10])
    print(result) # 6

    result = find_special_integer(arr = [1,1])
    print(result) # 1

if __name__ == "__main__":
    main()
