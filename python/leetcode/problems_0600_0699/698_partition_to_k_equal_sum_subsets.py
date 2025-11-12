# -------------------------------------
# 698. Partition To K Equal Sum Subsets
# -------------------------------------

# Problem: https://leetcode.com/problems/partition-to-k-equal-sum-subsets/
# 
# Given an integer array nums and an integer k, return true if it is possible 
# to divide this array into k non-empty subsets whose sums are all equal.
# 
#  
# Example 1:
# 
# 
# Input: nums = [4,3,2,3,5,2,1], k = 4
# Output: true
# Explanation: It is possible to divide it into 4 subsets (5), (1, 4), 
# (2,3), (2,3) with equal sums.
# 
# 
# Example 2:
# 
# Input: nums = [1,2,3,4], k = 3
# Output: false
# 
#  
# Constraints:
# 
# 	1 <= k <= nums.length <= 16
# 	1 <= nums[i] <= 10^4
# 	The frequency of each element is in the range [1, 4].


# Solution: https://youtu.be/mBk4I0X46oI
# Credit: Navdeep Singh founder of NeetCode
def can_partition_k_subsets(nums, k):
    if sum(nums) % k != 0:
        return False

    nums.sort(reverse = True)
    target = sum(nums) / k
    visited= set()

    def backtrack(idx, count, currSum):
        if count == k:
            return True

        if target == currSum:
            return backtrack(0, count + 1, 0)

        for i in range(idx, len(nums)):
            
            # skip duplicates if last same number was skipped
            if i > 0 and (i - 1) not in visited and nums[i] == nums[i - 1]:
                continue

            if i in visited or currSum + nums[i] > target:
                continue

            visited.add(i)

            if backtrack(i + 1, count, currSum + nums[i]):
                return True
            
            visited.remove(i)
        return False

    return backtrack(0, 0, 0)


def main():
    result = can_partition_k_subsets(nums = [4,3,2,3,5,2,1], k = 4)
    print(result) # True

    result = can_partition_k_subsets(nums = [1,2,3,4], k = 3)
    print(result) # False

if __name__ == "__main__":
    main()
