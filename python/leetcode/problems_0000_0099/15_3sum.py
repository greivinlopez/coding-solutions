# -----------
# 15. 3Sum 3️⃣
# -----------

# Problem: https://leetcode.com/problems/3sum
#
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# 
# Notice that the solution set must not contain duplicate triplets.
# 
# Example 1:
# 
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# 
# Explanation:
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not
# matter.
# 
# Example 2:
# 
# Input: nums = [0,1,1]
# Output: []
# 
# Explanation: The only possible triplet does not sum up to 0.
# 
# Example 3:
# 
# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# 
# Explanation: The only possible triplet sums up to 0.
# 
# 
# Constraints:
#         3 <= nums.length <= 3000
#         -10⁵ <= nums[i] <= 10⁵

# Solution: https://www.youtube.com/watch?v=jzZsG8n2R9A
# Credit: Navdeep Singh founder of NeetCode 
def three_sum(nums):
    res = []
    nums.sort()

    for i, n in enumerate(nums):
        # avoid duplicates
        if i > 0 and n == nums[i - 1]:
            continue
        l, r = i + 1, len(nums) - 1

        while l < r:
            s = n + nums[l] + nums[r]
            if s > 0:
                r -= 1
            elif s < 0:
                l += 1
            else:
                res.append([n, nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
    return res
    # Time: O(n²)
    # Space: O(n)

# Solution: https://youtu.be/TBePcj8DgxM
# Credit: Greg Hogg
def three_sum_alt(nums):
    h = {}
    n = len(nums)
    s = set()

    for i, num in enumerate(nums):
        h[num] = i

    for i in range(n):
        for j in range(i + 1, n):
            desired = -nums[i] - nums[j]
            if desired in h and h[desired] != i and h[desired] != j:
                s.add(tuple(sorted([nums[i], nums[j], desired])))

    return s
    # Time: O(n²)
    # Space: O(n)

# Solution: https://leetcode.com/problems/3sum/solutions/3523898/beats-99-48-44-145-top-interview-question/
# Credit: rahulbnair -> https://leetcode.com/u/rahulbnair/
from collections import defaultdict
def three_sum_alt_2(nums):
    negative = defaultdict(int)
    positive = defaultdict(int)
    zeros = 0
    for num in nums:
        if num < 0:
            negative[num] += 1
        elif num > 0:
            positive[num] += 1
        else:
            zeros += 1
    
    result = []
    if zeros:
        for n in negative:
            if -n in positive:
                result.append((0, n, -n))       
        if zeros > 2:
            result.append((0,0,0))

    for set1, set2 in ((negative, positive), (positive, negative)):
        set1Items = list(set1.items())
        for i, (j, k) in enumerate(set1Items):
            for j2, k2 in set1Items[i:]:
                if j != j2 or (j == j2 and k > 1):
                    if -j-j2 in set2:
                        result.append((j, j2, -j-j2))
    return result
    # Time: O(n²)
    # Space: O(n)

# Credit: Jeel Gajera -> https://github.com/JeelGajera
def three_sum_alt_3(nums):
    n = len(nums)
    res = set()
    nums.sort()
    for i in range(n-2):
        left,right = i+1, n-1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            if current_sum == 0:
                triplet = [nums[i], nums[left], nums[right]]
                res.add(tuple(triplet))

                left += 1
                right -= 1
            elif current_sum < 0:
                left += 1
            else:
                right -= 1

    return [list(triplet) for triplet in res]
    # Time: O(n²)
    # Space: O(n²)


def main():
    result = three_sum([-1,0,1,2,-1,-4]) # [[-1,-1,2],[-1,0,1]]
    print(result)
    result = three_sum([0,1,1]) # []
    print(result)
    result = three_sum([0,0,0]) # [[0,0,0]]
    print(result)

if __name__ == "__main__":
    main()