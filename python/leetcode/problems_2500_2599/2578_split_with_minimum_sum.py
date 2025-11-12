# ----------------------------
# 2578. Split With Minimum Sum
# ----------------------------

# Problem: https://leetcode.com/problems/split-with-minimum-sum
#
# Given a positive integer num, split it into two non-negative integers num1 and
# num2 such that:
#         
#   * The concatenation of num1 and num2 is a permutation of num.
#       * In other words, the sum of the number of occurrences of each digit in 
#         num1 and num2 is equal to the number of occurrences of that digit in num.
#   * num1 and num2 can contain leading zeros.
# 
# Return the minimum possible sum of num1 and num2.
#
# Notes:
#   * It is guaranteed that num does not contain any leading zeros.
#   * The order of occurrence of the digits in num1 and num2 may differ from the 
#     order of occurrence of num.
# 
# Example 1:
# 
# Input: num = 4325
# Output: 59
# 
# Explanation: We can split 4325 so that num1 is 24 and num2 is 35, giving a sum
# of 59. We can prove that 59 is indeed the minimal possible sum.
# 
# Example 2:
# 
# Input: num = 687
# Output: 75
# 
# Explanation: We can split 687 so that num1 is 68 and num2 is 7, which would give
# an optimal sum of 75.
# 
# 
# Constraints:
#         10 <= num <= 10⁹


# Credit: Jaweria Batool -> https://github.com/Jaweria-B
def split_num(num):
    num = str(num)
    sorted_num = sorted(num)
    
    num1 = ""
    num2 = ""
    
    if len(num) % 2 != 0:
        sorted_num = ["0"] + sorted_num
    
    for i in range(len(sorted_num)):
        if i % 2 == 0:
            num1 += sorted_num[i]
        else:
            num2 += sorted_num[i]
    
    return int(num1) + int(num2)
    # Time: O(n * log(n))
    # Space: O(n)
    # n = the number of digits in the input number num


def main():
    result = split_num(4325)
    print(result) # 59

    result = split_num(687)
    print(result) # 75

if __name__ == "__main__":
    main()
