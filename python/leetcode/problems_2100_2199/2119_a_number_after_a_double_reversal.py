# --------------------------------------
# 2119. A Number After a Double Reversal
# --------------------------------------

# Problem: https://leetcode.com/problems/a-number-after-a-double-reversal
#
# Reversing an integer means to reverse all its digits.
#         
#   * For example, reversing 2021 gives 1202. Reversing 12300 gives 321 as the
#     leading zeros are not retained.
# 
# Given an integer num, reverse num to get reversed1, then reverse reversed1 to
# get reversed2. Return true if reversed2 equals num. Otherwise return false.
# 
# Example 1:
# 
# Input: num = 526
# Output: true
# 
# Explanation: Reverse num to get 625, then reverse 625 to get 526, which equals
# num.
# 
# Example 2:
# 
# Input: num = 1800
# Output: false
# 
# Explanation: Reverse num to get 81, then reverse 81 to get 18, which does not
# equal num.
# 
# Example 3:
# 
# Input: num = 0
# Output: true
# 
# Explanation: Reverse num to get 0, then reverse 0 to get 0, which equals num.
# 
# 
# Constraints:
#         0 <= num <= 10⁶


# Credit: Jaweria Batool -> https://github.com/Jaweria-B
def is_same_after_reversals(num):
    if(len(str(num))==1):
        return True
    
    if(str(num)[-1]==0):
        return False
    
    r_int1 = int(str(num)[::-1])
    r_int2 = int(str(r_int1)[::-1])
    
    if(r_int2==num):
        return True
    return False
    # Time: O(log(n))
    # Space: O(log(n))


def main():
    result = is_same_after_reversals(526)
    print(result) # True

    result = is_same_after_reversals(1800)
    print(result) # False

    result = is_same_after_reversals(0)
    print(result) # True

if __name__ == "__main__":
    main()
