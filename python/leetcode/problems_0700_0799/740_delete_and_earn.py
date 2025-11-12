# --------------------
# 740. Delete And Earn
# --------------------

# Problem: https://leetcode.com/problems/delete-and-earn/
# 
# You are given an integer array nums. You want to maximize the number of 
# points you get by performing the following operation any number of times:
# 
# 	Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must 
# delete every element equal to nums[i] - 1 and every element equal to 
# nums[i] + 1.
# 
# Return the maximum number of points you can earn by applying the above 
# operation some number of times.
# 
#  
# Example 1:
# 
# Input: nums = [3,4,2]
# Output: 6
# Explanation: You can perform the following operations:
# - Delete 4 to earn 4 points. Consequently, 3 is also deleted. nums = [2].
# - Delete 2 to earn 2 points. nums = [].
# You earn a total of 6 points.
# 
# 
# Example 2:
# 
# Input: nums = [2,2,3,3,3,4]
# Output: 9
# Explanation: You can perform the following operations:
# - Delete a 3 to earn 3 points. All 2's and 4's are also deleted. nums = [3,3].
# - Delete a 3 again to earn 3 points. nums = [3].
# - Delete a 3 once more to earn 3 points. nums = [].
# You earn a total of 9 points.
# 
#  
# Constraints:
# 
# 	1 <= nums.length <= 2 * 10^4
# 	1 <= nums[i] <= 10^4


# Solution: https://youtu.be/7FCemBxvGw0
# Credit: Navdeep Singh founder of NeetCode
def delete_and_earn(nums):
    upperLimit = max(nums) + 1 
    store = [0] * upperLimit

    for num in nums:
        store[num] += num

    dp = [0] * upperLimit

    dp[1] = 1 * store[1]
    for i in range(2, upperLimit):
        dp[i] = max(dp[i - 2] + store[i], dp[i - 1])

    return dp[-1]


def main():
    result = delete_and_earn([3,4,2])
    print(result) # 6

    result = delete_and_earn([2,2,3,3,3,4])
    print(result) # 9

if __name__ == "__main__":
    main()
