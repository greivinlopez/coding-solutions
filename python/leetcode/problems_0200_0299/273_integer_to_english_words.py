# -----------------------------
# 273. Integer to English Words
# -----------------------------

# Problem: https://leetcode.com/problems/integer-to-english-words
#
# Convert a non-negative integer num to its English words representation.
# 
# Example 1:
# 
# Input: num = 123
# Output: "One Hundred Twenty Three"
# 
# Example 2:
# 
# Input: num = 12345
# Output: "Twelve Thousand Three Hundred Forty Five"
# 
# Example 3:
# 
# Input: num = 1234567
# Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
# 
# 
# Constraints:
#         0 <= num <= 2^31 - 1


# Solution: https://youtu.be/SCtIlKd3mDM
# Credit: Navdeep Singh founder of NeetCode
def number_to_words(num):
    if num == 0:
        return "Zero"
    
    ones_map = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
        10: "Ten",
        11: "Eleven",
        12: "Twelve",
        13: "Thirteen",
        14: "Fourteen",
        15: "Fifteen",
        16: "Sixteen",
        17: "Seventeen",
        18: "Eighteen",
        19: "Nineteen",
    }
    
    tens_map = {
        20: "Twenty",
        30: "Thirty",
        40: "Forty",
        50: "Fifty",
        60: "Sixty",
        70: "Seventy",
        80: "Eighty",
        90: "Ninety",
    }

    def get_string(n):
        # 123, 120, 102, 012, 100
        res = []
        hundreds = n // 100
        if hundreds:
            res.append(ones_map[hundreds] + " Hundred")
        last_2 = n % 100
        if last_2 >= 20:
            # Handle tens and ones
            tens = (last_2 // 10) * 10
            ones = last_2 % 10
            if ones:
                res.append(tens_map[tens] + " " + ones_map[ones])
            else:
                res.append(tens_map[tens])
        elif last_2:
            res.append(ones_map[last_2])
        
        return " ".join(res)
    
    postfix = ["", " Thousand", " Million", " Billion"]
    i = 0
    res = []
    while num:
        digits = num % 1000
        s = get_string(digits) + postfix[i]  # 1,000,000
        if s:
            res.append(s)
        num = num // 1000
        i += 1
    res.reverse()
    return " ".join(res)
    # Time: O(log(n))
    # Space: O(1)


def main():
    result = number_to_words(num = 123)
    print(result) # "One Hundred Twenty Three"

    result = number_to_words(num = 12345)
    print(result) # "Twelve Thousand Three Hundred Forty Five"

    result = number_to_words(num = 1234567)
    print(result) # "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

if __name__ == "__main__":
    main()
