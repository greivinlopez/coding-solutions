# ------------------------------------
# 405. Convert a Number to Hexadecimal
# ------------------------------------

# Problem: https://leetcode.com/problems/convert-a-number-to-hexadecimal
#
# Given a 32-bit integer num, return a string representing its hexadecimal
# representation. For negative integers, two’s complement method is used.
# 
# All the letters in the answer string should be lowercase characters, and there
# should not be any leading zeros in the answer except for the zero itself.
# 
# Note: You are not allowed to use any built-in library method to directly solve
# this problem.
# 
# Example 1:
# 
# Input: num = 26
# Output: "1a"
# 
# Example 2:
# 
# Input: num = -1
# Output: "ffffffff"
# 
# 
# Constraints:
#         -2³¹ <= num <= 2³¹ - 1


# Credit: Jaweria Batool -> https://github.com/Jaweria-B
def to_hex(num):
    dic = {10 : "a", 11 : "b", 12 : "c", 13 :"d", 14 : "e", 15: "f"}
    
    def conversion(num):
        ans = ""
        while num >= 16:
            rem = num%16
            if rem >= 10:
                ans = str(dic[rem]) + ans
            else:
                ans = str(rem) + ans
            
            num = num//16
        
        if num > 0:
            if num >= 10:
                ans = str(dic[num])+ ans
            else:
                ans = str(num)+ ans
                
        return ans
    
    if num == 0:
        return "0"
    
    if num < 0:
        temp = 0xffffffff
        num = (temp^abs(num)) + 1
        
    return conversion(num)
    # Time: O(log₁₆(n))
    # Space: O(log₁₆(n))


def main():
    result = to_hex(num = 26)
    print(result) # "1a"

    result = to_hex(num = -1)
    print(result) # "ffffffff"

if __name__ == "__main__":
    main()
