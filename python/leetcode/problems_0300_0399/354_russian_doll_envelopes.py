# ---------------------------
# 354. Russian Doll Envelopes
# ---------------------------

# Problem: https://leetcode.com/problems/russian-doll-envelopes
#
# You are given a 2D array of integers envelopes where envelopes[i] = [wᵢ, hᵢ]
# represents the width and the height of an envelope.
# 
# One envelope can fit into another if and only if both the width and height of
# one envelope are greater than the other envelope's width and height.
# 
# Return the maximum number of envelopes you can Russian doll (i.e., put one
# inside the other).
# 
# Note: You cannot rotate an envelope.
# 
# Example 1:
# 
# Input: envelopes = [[5,4],[6,4],[6,7],[2,3]]
# Output: 3
# 
# Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] =>
# [5,4] => [6,7]).
# 
# Example 2:
# 
# Input: envelopes = [[1,1],[1,1],[1,1]]
# Output: 1
# 
# 
# Constraints:
#         1 <= envelopes.length <= 10⁵
#         envelopes[i].length == 2
#         1 <= wᵢ, hᵢ <= 10⁵

from bisect import bisect_left

# Solution: https://leetcode.com/problems/russian-doll-envelopes/solutions/699268/python-simple-dp-nlogn-solution
def max_envelopes(envelopes): 
    def lis(nums):
        dp = []
        for i in range(len(nums)):
            idx = bisect_left(dp, nums[i])
            if idx == len(dp):
                dp.append(nums[i])
            else:
                dp[idx] = nums[i]
        return len(dp)
    
    envelopes.sort(key=lambda x: (x[0], -x[1]))
    
    return lis([envelope[1] for envelope in envelopes])
    # Time: O(n * log(n))
    # Space: O(n)


def main():
    result = max_envelopes(envelopes = [[5,4],[6,4],[6,7],[2,3]])
    print(result) # 3

    result = max_envelopes(envelopes = [[1,1],[1,1],[1,1]])
    print(result) # 1

if __name__ == "__main__":
    main()
