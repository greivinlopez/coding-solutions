# ---------------------
# 202. Happy Number 1️⃣😉
# ---------------------

# Problem: https://leetcode.com/problems/happy-number/
# 
# Write an algorithm to determine if a number n is happy.
# 
# A happy number is a number defined by the following process:
# 
# 	- Starting with any positive integer, replace the number by the sum of the 
#   squares of its digits.
# 	- Repeat the process until the number equals 1 (where it will stay), or it 
#   loops endlessly in a cycle which does not include 1.
# 	- Those numbers for which this process ends in 1 are happy.
# 
# Return true if n is a happy number, and false if not.
# 
# Example 1:
# 
# Input: n = 19
# Output: true
# Explanation:
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1
# 
# 
# Example 2:
# 
# Input: n = 2
# Output: false
# 
#  
# Constraints:
# 
# 	1 <= n <= 231 - 1


# Solution: https://youtu.be/ljz85bxOYJ0
# Credit: Navdeep Singh founder of NeetCode
def is_happy(n):
    def sumSquareDigits(n):
        output = 0
        while n:
            output += (n % 10) ** 2
            n = n // 10
        return output
    slow, fast = n, sumSquareDigits(n)

    while slow != fast:
        fast = sumSquareDigits(fast)
        fast = sumSquareDigits(fast)
        slow = sumSquareDigits(slow)

    return True if fast == 1 else False

# Solution: https://www.youtube.com/shorts/wHJxgkITbBc?feature=share
# Credit: Greg Hogg
def is_happy_alt(n):
    seen = set()
    cur = str(n)
    while cur not in seen:
        seen.add(cur)
        s = 0
        for d in cur:
            s += int(d)**2
        if s == 1: return True
        cur = str(s)
    return False

def main():
    result = is_happy_alt(19)
    print(result) # True

    result = is_happy_alt(2)
    print(result) # False

if __name__ == "__main__":
    main()
