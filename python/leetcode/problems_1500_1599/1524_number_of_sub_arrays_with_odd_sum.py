# ---------------------------------------
# 1524. Number of Sub-arrays With Odd Sum
# ---------------------------------------

# Problem: https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum
#
# Given an array of integers arr, return the number of subarrays with an odd sum.
# 
# Since the answer can be very large, return it modulo 10⁹ + 7.
# 
# Example 1:
# 
# Input: arr = [1,3,5]
# Output: 4
# 
# Explanation: All subarrays are [[1],[1,3],[1,3,5],[3],[3,5],[5]]
# All sub-arrays sum are [1,4,9,3,8,5].
# Odd sums are [1,9,3,5] so the answer is 4.
# 
# Example 2:
# 
# Input: arr = [2,4,6]
# Output: 0
# 
# Explanation: All subarrays are [[2],[2,4],[2,4,6],[4],[4,6],[6]]
# All sub-arrays sum are [2,6,12,4,10,6].
# All sub-arrays have even sum and the answer is 0.
# 
# Example 3:
# 
# Input: arr = [1,2,3,4,5,6,7]
# Output: 16
# 
# 
# Constraints:
#         1 <= arr.length <= 10⁵
#         1 <= arr[i] <= 100


# Solution: https://youtu.be/AIlI-24oC6Q
# Credit: Navdeep Singh founder of NeetCode
def num_of_subarrays(arr):
    cur_sum = 0
    odd_cnt = 0
    even_cnt = 0
    res = 0
    MOD = 10**9 + 7
    
    for n in arr:
        cur_sum += n
        
        if cur_sum % 2:  # odd
            res = (res + 1 + even_cnt) % MOD
            odd_cnt += 1
        else:  # even
            res = (res + odd_cnt) % MOD
            even_cnt += 1
    
    return res
    # Time: O(n)
    # Space: O(1)


def main():
    result = num_of_subarrays([1,3,5])
    print(result) # 4

    result = num_of_subarrays([2,4,6])
    print(result) # 0

    result = num_of_subarrays([1,2,3,4,5,6,7])
    print(result) # 16

if __name__ == "__main__":
    main()
