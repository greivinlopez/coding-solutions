# ---------------
# 67. Add Binary
# ---------------

# Problem: https://leetcode.com/problems/add-binary/
# 
# Given two binary strings a and b, return their sum as a binary string.

# Solution: https://youtu.be/keuWJ47xG8g
# Credit: Navdeep Singh founder of NeetCode 
def add_binary(a, b):
    res = ""
    carry = 0

    a, b = a[::-1], b[::-1]
    for i in range(max(len(a), len(b))):
        bitA = ord(a[i]) - ord('0') if i < len(a) else 0
        bitB = ord(b[i]) - ord('0') if i < len(b) else 0

        total = bitA + bitB + carry
        char = str(total % 2)
        res = char + res
        carry = total // 2

    if carry:
        res = "1" + res

    return res

# Solution: https://youtu.be/M9foA9gcL98
# Credit: Greg Hogg
def add_binary_alt(a, b):
    a, b = int(a, 2), int(b, 2)
    
    while b:
        without_carry = a ^ b
        carry = (a & b) << 1
        a, b = without_carry, carry
        
    return bin(a)[2:]

def main():
    result = add_binary(a = "11", b = "1") # "100"
    print(result)
    result = add_binary(a = "1010", b = "1011") # "10101"
    print(result)

if __name__ == "__main__":
    main()