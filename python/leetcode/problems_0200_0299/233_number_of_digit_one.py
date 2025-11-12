# ------------------------
# 233. Number of Digit One
# ------------------------

# Problem: https://leetcode.com/problems/number-of-digit-one
#
# Given an integer n, count the total number of digit 1 appearing in all non-
# negative integers less than or equal to n.
# 
# Example 1:
# 
# Input: n = 13
# Output: 6
# 
# Example 2:
# 
# Input: n = 0
# Output: 0
# 
# 
# Constraints:
#         0 <= n <= 10⁹


# Solution: https://leetcode.com/problems/number-of-digit-one/solutions/4295427/python-3-solution-100-working
def count_digit_one(n):
    n = str(n) # converting it to string
    c=0        # initializing count variable
    l=len(n)

    for i in range(l-1,0,-1):
        first_dig=int(n[0])   #taking the first digit
        if first_dig==1:
            c+=(int(str(i)+'0'*(i-1))+1)
            c+=int(n[1:])
        elif first_dig==0:
            pass
        else:
            c+=(int(str(i)+'0'*(i-1))+1)
            c+=(int('9'*i))
            c+=((first_dig-1)*(int(str(i)+'0'*(i-1))))
        n=n[1::]     #removing the first digit.

    if n=='0':
        return c     #if 0 return c
    else:
        return c+1   #else return c+1 because the digit 1 would have occurred once.


def main():
    result = count_digit_one(13)
    print(result) # 6

    result = count_digit_one(0)
    print(result) # 0

if __name__ == "__main__":
    main()
