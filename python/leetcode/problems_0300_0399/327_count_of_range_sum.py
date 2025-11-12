# -----------------------
# 327. Count of Range Sum
# -----------------------

# Problem: https://leetcode.com/problems/count-of-range-sum
#
# Given an integer array nums and two integers lower and upper, return the number
# of range sums that lie in [lower, upper] inclusive.
# 
# Range sum S(i, j) is defined as the sum of the elements in nums between indices
# i and j inclusive, where i <= j.
# 
# Example 1:
# 
# Input: nums = [-2,5,-1], lower = -2, upper = 2
# Output: 3
# 
# Explanation: The three ranges are: [0,0], [2,2], and [0,2] and their respective
# sums are: -2, -1, 2.
# 
# Example 2:
# 
# Input: nums = [0], lower = 0, upper = 0
# Output: 1
# 
# 
# Constraints:
#         1 <= nums.length <= 10⁵
#         -2³¹ <= nums[i] <= 2³¹ - 1
#         -10⁵ <= lower <= upper <= 10⁵
#         The answer is guaranteed to fit in a 32-bit integer.


# Solution: https://leetcode.com/problems/count-of-range-sum/solutions/407655/python-different-concise-solutions
# Credit: Yumho -> https://leetcode.com/u/gyh75520/
def count_range_sum(nums, lower, upper):
    cumsum = [0]
    for n in nums:
        cumsum.append(cumsum[-1]+n)
    
    import collections
    record = collections.defaultdict(int)
    
    res = 0
    for csum in cumsum:
        for target in range(lower,upper+1):
            if csum - target in record:
                res += record[csum - target]
        record[csum] +=1
    return res
    # Time: O(n * (upper - lower + 1))
    # Space: O(n)


def main():
    result = count_range_sum(nums = [-2,5,-1], lower = -2, upper = 2)
    print(result) # 3

    result = count_range_sum(nums = [0], lower = 0, upper = 0)
    print(result) # 1

if __name__ == "__main__":
    main()
