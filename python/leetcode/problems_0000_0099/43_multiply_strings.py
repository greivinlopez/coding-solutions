# ---------------------
# 43. Multiply Strings
# ---------------------

# Problem: https://leetcode.com/problems/multiply-strings/
# Given two non-negative integers num1 and num2 represented as strings, 
# return the product of num1 and num2, also represented as a string.
#  
# Note: You must not use any built-in BigInteger library or convert the 
# inputs to integer directly.

# Solution: https://youtu.be/1vZswirL8Y8
# Credit: Navdeep Singh founder of NeetCode 
def multiply(num1, num2):
    # Time: O(n * m)
    # Space: O(n + m)
    if "0" in [num1, num2]:
        return "0"

    res = [0] * (len(num1) + len(num2))
    num1, num2 = num1[::-1], num2[::-1]
    for i1 in range(len(num1)):
        for i2 in range(len(num2)):
            digit = int(num1[i1]) * int(num2[i2])
            res[i1 + i2] += digit
            res[i1 + i2 + 1] += res[i1 + i2] // 10
            res[i1 + i2] = res[i1 + i2] % 10

    res, beg = res[::-1], 0
    while beg < len(res) and res[beg] == 0:
        beg += 1
    res = map(str, res[beg:])
    return "".join(res)

# Solution: https://leetcode.com/problems/multiply-strings/solutions/6928502/with-out-using-built-in-integer-functions-beats-100-runtime-0-ms/
# Credit: mahidhar05 -> https://leetcode.com/u/mahidhar05/
def multiply_alt(num1, num2):
    l1=list(num1)
    l2=list(num2)
    n1=0
    n2=0
    a=1
    for i in range(len(num1)-1,-1,-1):
        n1=n1+((ord(l1[i])-48)*a)
        a=a*10
    a=1
    for i in range(len(num2)-1,-1,-1):
        n2=n2+((ord(l2[i])-48)*a)
        a=a*10
    return str(n1*n2)

def main():
    result = multiply(num1 = "2", num2 = "3") # "6"
    print(result)
    result = multiply(num1 = "123", num2 = "456") # "56088"
    print(result)

if __name__ == "__main__":
    main()