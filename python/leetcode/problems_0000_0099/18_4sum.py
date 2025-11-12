# --------
# 18. 4Sum
# --------

# Problem: https://leetcode.com/problems/4sum
#
# Given an array nums of n integers, return an array of all the unique quadruplets
# [nums[a], nums[b], nums[c], nums[d]] such that:
#
#          0 <= a, b, c, d < n
#         a, b, c, and d are distinct.
#         nums[a] + nums[b] + nums[c] + nums[d] == target
# 
# You may return the answer in any order.
# 
# Example 1:
# 
# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
# 
# Example 2:
# 
# Input: nums = [2,2,2,2,2], target = 8
# Output: [[2,2,2,2]]
# 
# 
# Constraints:
#         1 <= nums.length <= 200
#         -10⁹ <= nums[i] <= 10⁹
#         -10⁹ <= target <= 10⁹

# Solution: https://youtu.be/EYeR-_1NRlQ
# Credit: Navdeep Singh founder of NeetCode 
def four_sum(nums, target):
    def findNsum(l, r, target, N, result, results):
        if r-l+1 < N or N < 2 or target < nums[l]*N or target > nums[r]*N:  
            return
        if N == 2: 
            while l < r:
                s = nums[l] + nums[r]
                if s == target:
                    results.append(result + [nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif s < target:
                    l += 1
                else:
                    r -= 1
        else:
            for i in range(l, r+1):
                if i == l or (i > l and nums[i-1] != nums[i]):
                    findNsum(i+1, r, target-nums[i], N-1, result+[nums[i]], results)

    nums.sort()
    results = []
    findNsum(0, len(nums)-1, target, 4, [], results)
    return results
    # Time: O(n³)
    # Space: O(k)
    # k = number of unique quadruplets

# Solution: https://youtu.be/PDawWT9xAsI
# Credit: Greg Hogg
def four_sum_alt(nums, target):
    n = len(nums)
    answer = []
    nums.sort()

    for i in range(n):
        if i > 0 and nums[i] == nums[i-1]:
            continue

        for j in range(i+1, n):
            if j > i + 1 and nums[j] == nums[j-1]:
                continue

            lo, hi = j + 1, n - 1
            while lo < hi:
                summ = nums[i] + nums[j] + nums[lo] + nums[hi]
                if summ == target:
                    answer.append([nums[i], nums[j], nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1
                    while lo < hi and nums[lo] == nums[lo - 1]:
                        lo += 1
                    while lo < hi and nums[hi] == nums[hi + 1]:
                        hi -= 1
                elif summ < target:
                    lo += 1
                else:
                    hi -= 1
    return answer
    # Time: O(n³)
    # Space: O(k)
    # k = number of unique quadruplets


def main():
    result = four_sum(nums = [1,0,-1,0,-2,2], target = 0) # [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
    print(result)
    result = four_sum(nums = [2,2,2,2,2], target = 8) # [[2,2,2,2]]
    print(result)

if __name__ == "__main__":
    main()