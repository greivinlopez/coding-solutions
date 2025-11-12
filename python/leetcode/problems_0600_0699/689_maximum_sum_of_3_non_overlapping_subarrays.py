# -----------------------------------------------
# 689. Maximum Sum of 3 Non-Overlapping Subarrays
# -----------------------------------------------

# Problem: https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays
#
# Given an integer array nums and an integer k, find three non-overlapping
# subarrays of length k with maximum sum and return them.
# 
# Return the result as a list of indices representing the starting position of
# each interval (0-indexed). If there are multiple answers, return the
# lexicographically smallest one.
# 
# Example 1:
# 
# Input: nums = [1,2,1,2,6,7,5,1], k = 2
# Output: [0,3,5]
# 
# Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices
# [0, 3, 5].
# We could have also taken [2, 1], but an answer of [1, 3, 5] would be
# lexicographically larger.
# 
# Example 2:
# 
# Input: nums = [1,2,1,2,1,2,1,2,1], k = 2
# Output: [0,2,4]
# 
# 
# Constraints:
#         1 <= nums.length <= 2 * 10^4
#         1 <= nums[i] < 2^16
#         1 <= k <= floor(nums.length / 3)


# Solution: https://youtu.be/SfjeJ1qyCVg
# Credit: Navdeep Singh founder of NeetCode
def max_sum_of_three_subarrays(nums, k):
    # Brute force solution
    max_sum, res = 0, []

    def backtrack(i, choosen):
        if len(choosen) == 3 or i >= len(nums) - 1:
            nonlocal max_sum, res
            cur_sum = 0
            for j in choosen:
                cur_sum += sum(nums[j:j+k])
            if cur_sum > max_sum:
                max_sum = cur_sum
                res = choosen[:]
            return

        # Choose i
        choosen.append(i)
        backtrack(i + k, choosen)
        choosen.pop()

        # Skip i
        backtrack(i + 1, choosen)

    backtrack(0, [])
    return res

def max_sum_of_three_subarrays_memo(nums, k):
    # Memoization solution

    # preprocessing
    k_sums = [sum(nums[:k])]
    for i in range(k, len(nums)):
        k_sums.append(k_sums[-1] + nums[i] - nums[i - k])

    dp = {}
    def get_max_sum(i, cnt):
        if cnt == 3 or i > len(nums) - k:
            return 0
        if (i, cnt) in dp:
            return dp[(i, cnt)]
        
         # Include
        include = k_sums[i] + get_max_sum(i + k, cnt + 1)
        # Skip
        skip = get_max_sum(i + 1, cnt)
        dp[(i, cnt)] = max(include, skip)
        return dp[(i, cnt)]
    
    def get_indices():
        i = 0
        indices = []

        while i <= len(nums) - k and len(indices) < 3:
            include = k_sums[i] + get_max_sum(i + k, len(indices) + 1)
            skip = get_max_sum(i + 1, len(indices))

            if include >= skip:
                indices.append(i)
                i += k
            else:
                i += 1
        return indices
    return get_indices()

def main():
    result = max_sum_of_three_subarrays(nums = [1,2,1,2,6,7,5,1], k = 2)
    print(result) # True

    result = max_sum_of_three_subarrays([1,2,1,2,1,2,1,2,1], k = 2)
    print(result) # True

if __name__ == "__main__":
    main()
