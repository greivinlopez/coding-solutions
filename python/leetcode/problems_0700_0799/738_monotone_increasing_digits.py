# -------------------------------
# 738. Monotone Increasing Digits
# -------------------------------

# Problem: https://leetcode.com/problems/monotone-increasing-digits
#
# An integer has monotone increasing digits if and only if each pair of adjacent
# digits x and y satisfy x <= y.
# 
# Given an integer n, return the largest number that is less than or equal to n
# with monotone increasing digits.
# 
# Example 1:
# 
# Input: n = 10
# Output: 9
# 
# Example 2:
# 
# Input: n = 1234
# Output: 1234
# 
# Example 3:
# 
# Input: n = 332
# Output: 299
# 
# 
# Constraints:
#         0 <= n <= 10⁹


# Solution: https://algo.monster/liteproblems/738
# Credit: AlgoMonster
def monotone_increasing_digits_alt(n):
    # Convert number to list of digit characters for easier manipulation
    digits = list(str(n))
    length = len(digits)
    
    # Find the first position where monotone property breaks (digit decreases)
    break_point = 1
    while break_point < length and digits[break_point - 1] <= digits[break_point]:
        break_point += 1
    
    # If we found a break in monotone property
    if break_point < length:
        # Backtrack to find the position where we need to decrease the digit
        # This handles cases where we have repeated digits before the break
        while break_point > 0 and digits[break_point - 1] > digits[break_point]:
            digits[break_point - 1] = str(int(digits[break_point - 1]) - 1)
            break_point -= 1
        
        # Move forward one position after the decreased digit
        break_point += 1
        
        # Set all remaining digits to '9' to get the largest possible number
        while break_point < length:
            digits[break_point] = '9'
            break_point += 1
    
    # Convert the list of digit characters back to an integer
    return int(''.join(digits))
    # Time: O(d)    -> O(d * 5), as d = log(n) then O(log(n))
    # Space: O(d)
    # d = the number of digits in n


# Alternative:
# Solution: https://leetcode.com/problems/monotone-increasing-digits/solutions/2602170/python3-7-lines-w-explanation-t-s-82-87
# Credit: Capt Spaulding -> https://leetcode.com/u/Spaulding_/
def monotone_increasing_digits(n):
    n = str(n)                                        # For example: n = 246621 --> "246621"
    N = len(n)

    for i in range(N-1):                              # find the first break in monotonicity
        if n[i] > n[i+1]: break                       #       Ex: "2466 21"
                                                      #                ^
        else: return int(n)                           # if no break, then n is a mono non-decr seq
    
    while i>0 and n[i]==n[i-1]: i-=1                  # back up to the last digit in the mono incr seq 
                                                        #       Ex: "246 621"
                                                        #               ^
    return int(str(int(n[:i+1])-1)+'9'*(N-i-1))       # borrow a 1 from the mono incr portion and pad with 9s
                                                        #       Ex: ("246"-"1")+ '9'*4 = "245999"--> 245999
    # Time: O(n)
    # Space: O(n)


def main():
    result = monotone_increasing_digits(10)
    print(result) # 9

    result = monotone_increasing_digits(1234)
    print(result) # 1234

    result = monotone_increasing_digits(332)
    print(result) # 299

if __name__ == "__main__":
    main()
