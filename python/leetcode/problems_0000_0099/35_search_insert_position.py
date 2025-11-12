# ----------------------------
# 35. Search Insert Position
# ----------------------------

# Problem: https://leetcode.com/problems/search-insert-position/
# Given a sorted array of distinct integers and a target value, return the index 
# if the target is found. If not, return the index where it would be if it were 
# inserted in order.
# 
# You must write an algorithm with O(log n) runtime complexity.

# Solution: https://youtu.be/K-RYzDZkzCI
# Credit: Navdeep Singh founder of NeetCode 
def search_insert(nums, target):
    # Time: O(log(n))
    # Space: O(1)
    low, high = 0, len(nums)
    while low<high:
        mid = low +(high - low) // 2
        if target > nums[mid]:
            low = mid + 1
        else:
            high = mid
    return low

# Solution: https://youtu.be/4bluwC4wSlI
# Credit: Greg Hogg
# Almost identical
def search_insert(nums, target):
    # Time: O(log(n))
    # Space: O(1)
    n = len(nums)
    l = 0
    r = n - 1

    while l <= r:
        m = (l + r) // 2
        
        if nums[m] < target:
            l = m + 1
        elif nums[m] > target:
            r = m - 1
        else:
            return m

    if nums[m] < target:
        return m + 1
    else:
        return m

def main():
    result = search_insert(nums = [1,3,5,6], target = 5) # 2
    print(result)
    result = search_insert(nums = [1,3,5,6], target = 2) # 1
    print(result)
    result = search_insert(nums = [1,3,5,6], target = 7) # 4
    print(result)

if __name__ == "__main__":
    main()