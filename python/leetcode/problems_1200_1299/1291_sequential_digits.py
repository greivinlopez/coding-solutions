# ----------------------
# 1291. Sequential Digits
# ----------------------

# Problem: https://leetcode.com/problems/sequential-digits
#
# An integer has sequential digits if and only if each digit in the number is one
# more than the previous digit.
# 
# Return a sorted list of all the integers in the range [low, high] inclusive that
# have sequential digits.
# 
# Example 1:
# 
# Input: low = 100, high = 300
# Output: [123,234]
# 
# Example 2:
# 
# Input: low = 1000, high = 13000
# Output: [1234,2345,3456,4567,5678,6789,12345]
# 
# 
# Constraints:
#         10 <= low <= high <= 10^9

from collections import deque

# Solution: https://youtu.be/Q-ca65wRJyI
# Credit: Navdeep Singh founder of NeetCode
def sequential_digits_alt(low, high):
    res = []
    low_digit = len(str(low))
    high_digit = len(str(high))

    for digits in range(low_digit, high_digit + 1):
        for start in range(1, 9):
            if start + digits > 10:
                break
            num = start
            prev = start

            for _ in range(digits - 1):
                prev += 1
                num = num * 10 + prev
            
            if low <= num <= high:
                res.append(num)

    return res
    # Time: O(n) 

def sequential_digits(low, high):
    res = []
    queue = deque(range(1, 10))
    while queue:
        n = queue.popleft()
        if n > high:
            continue
        if low <= n <= high:
            res.append(n)
        
        ones = n % 10
        if ones < 9:
            new_num = n * 10 + (ones + 1)
            queue.append(new_num)
            
    return res
    # Time: O(1)

def main():
    result = sequential_digits(low = 100, high = 300)
    print(result) # [123,234]

    result = sequential_digits(low = 1000, high = 13000)
    print(result) # [1234,2345,3456,4567,5678,6789,12345]

if __name__ == "__main__":
    main()
