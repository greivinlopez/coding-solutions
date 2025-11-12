# ------------------------------------------------------------
# 2275. Largest Combination With Bitwise AND Greater Than Zero
# ------------------------------------------------------------

# Problem: https://leetcode.com/problems/largest-combination-with-bitwise-and-greater-than-zero
#
# The bitwise AND of an array nums is the bitwise AND of all integers in nums.
# 
#   * For example, for nums = [1, 5, 3], the bitwise AND is equal to 1 & 5 & 3 = 1.
#   * Also, for nums = [7], the bitwise AND is 7.
# 
# You are given an array of positive integers candidates. Compute the bitwise AND
# for all possible combinations of elements in the candidates array.
# 
# Return the size of the largest combination of candidates with a bitwise AND
# greater than 0.
# 
# Example 1:
# 
# Input: candidates = [16,17,71,62,12,24,14]
# Output: 4
# 
# Explanation: The combination [16,17,62,24] has a bitwise AND of 16 & 17 & 62 &
# 24 = 16 > 0.
# The size of the combination is 4.
# It can be shown that no combination with a size greater than 4 has a bitwise AND
# greater than 0.
# Note that more than one combination may have the largest size.
# For example, the combination [62,12,24,14] has a bitwise AND of 62 & 12 & 24 &
# 14 = 8 > 0.
# 
# Example 2:
# 
# Input: candidates = [8,8]
# Output: 2
# 
# Explanation: The largest combination [8,8] has a bitwise AND of 8 & 8 = 8 > 0.
# The size of the combination is 2, so we return 2.
# 
# 
# Constraints:
#         1 <= candidates.length <= 10^5
#         1 <= candidates[i] <= 10^7


# Solution: https://youtu.be/rUYfBldVqLY
# Credit: Navdeep Singh founder of NeetCode
def largest_combination(candidates):
    count = [0] * 32

    for n in candidates:
        i = 0
        while n > 0:
            count[i] += 1 & n
            i += 1
            n = n >> 1

    return max(count)


def largest_combination_alt(candidates):
    res = 0

    for i in range(32):
        cnt = 0

        for n in candidates:
            cnt += 1 if (1 << i) & n else 0
        res = max(res, cnt)

    return res

def main():
    result = largest_combination(candidates = [16,17,71,62,12,24,14])
    print(result) # 4

    result = largest_combination(candidates = [8,8])
    print(result) # 2

if __name__ == "__main__":
    main()
