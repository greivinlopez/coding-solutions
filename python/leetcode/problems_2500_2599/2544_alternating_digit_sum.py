# ---------------------------
# 2544. Alternating Digit Sum
# ---------------------------

# Problem: https://leetcode.com/problems/alternating-digit-sum
#
# You are given a positive integer n. Each digit of n has a sign according to the
# following rules:
#         
#   * The most significant digit is assigned a positive sign.
#   * Each other digit has an opposite sign to its adjacent digits.
# 
# Return the sum of all digits with their corresponding sign.
# 
# Example 1:
# 
# Input: n = 521
# Output: 4
# 
# Explanation: (+5) + (-2) + (+1) = 4.
# 
# Example 2:
# 
# Input: n = 111
# Output: 1
# 
# Explanation: (+1) + (-1) + (+1) = 1.
# 
# Example 3:
# 
# Input: n = 886996
# Output: 0
# 
# Explanation: (+8) + (-8) + (+6) + (-9) + (+9) + (-6) = 0.
# 
# 
# Constraints:
#         1 <= n <= 10⁹


# Credit: Jaweria Batool -> https://github.com/Jaweria-B
def alternate_digit_sum(n):
    n = str(n)  
    ans = 0
    
    for i in range(len(n)):
        if i % 2 == 0:
            ans += int(n[i])
        else:
            ans += (-1 * int(n[i]))
        
    return ans
    # Time: O(n)
    # Space: O(1)


def main():
    result = alternate_digit_sum(521)
    print(result) # 4

    result = alternate_digit_sum(111)
    print(result) # 1

    result = alternate_digit_sum(886996)
    print(result) # 0

if __name__ == "__main__":
    main()
