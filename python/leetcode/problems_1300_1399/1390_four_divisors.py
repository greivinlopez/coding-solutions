# -------------------
# 1390. Four Divisors
# -------------------

# Problem: https://leetcode.com/problems/four-divisors
#
# Given an integer array nums, return the sum of divisors of the integers in that
# array that have exactly four divisors. If there is no such integer in the array,
# return 0.
# 
# Example 1:
# 
# Input: nums = [21,4,7]
# Output: 32
# 
# Explanation:
# 21 has 4 divisors: 1, 3, 7, 21
# 4 has 3 divisors: 1, 2, 4
# 7 has 2 divisors: 1, 7
# The answer is the sum of divisors of 21 only.
# 
# Example 2:
# 
# Input: nums = [21,21]
# Output: 64
# 
# Example 3:
# 
# Input: nums = [1,2,3,4,5]
# Output: 0
# 
# 
# Constraints:
#         1 <= nums.length <= 10⁴
#         1 <= nums[i] <= 10⁵


# Solution: https://algo.monster/liteproblems/1390
# Credit: AlgoMonster
def sum_four_divisors(nums):
 
    def get_divisor_sum_if_four(number):
        # Start with divisor 2 (we'll count 1 and number separately)
        divisor = 2
        
        # Initialize with 1 and the number itself as divisors
        divisor_count = 2
        divisor_sum = number + 1
        
        # Check divisors up to sqrt(number)
        while divisor <= number // divisor:
            if number % divisor == 0:
                # Found a divisor
                divisor_count += 1
                divisor_sum += divisor
                
                # Check if the complementary divisor is different
                if divisor * divisor != number:
                    # Add the complementary divisor (number // divisor)
                    divisor_count += 1
                    divisor_sum += number // divisor
            
            divisor += 1
        
        # Return sum only if exactly 4 divisors found
        return divisor_sum if divisor_count == 4 else 0
    
    # Apply the function to all numbers and sum the results
    return sum(get_divisor_sum_if_four(number) for number in nums)
    # Time: O(n × √m)
    # Space: O(1)


def main():
    result = sum_four_divisors(nums = [21,4,7])
    print(result) # 32

    result = sum_four_divisors(nums = [21,21])
    print(result) # 64

    result = sum_four_divisors(nums = [1,2,3,4,5])
    print(result) # 0

if __name__ == "__main__":
    main()
