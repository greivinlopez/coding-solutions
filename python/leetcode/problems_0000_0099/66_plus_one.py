# -------------
# 66. Plus One
# -------------

# Problem: https://leetcode.com/problems/plus-one/
# 
# You are given a large integer represented as an integer array digits, where each 
# digits[i] is the ith digit of the integer. The digits are ordered from most 
# significant to least significant in left-to-right order. 
# The large integer does not contain any leading 0's.
# 
# Increment the large integer by one and return the resulting array of digits.

# Solution: https://youtu.be/jIaA8boiG1s
# Credit: Navdeep Singh founder of NeetCode 
def plus_one(digits):
    one = 1
    i = 0
    digits = digits[::-1]

    while one:
        if i < len(digits):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                one = 0
        else:
            digits.append(one)
            one = 0
        i += 1
    return digits[::-1]

def main():
    result = plus_one([1,2,3]) # [1,2,4]
    print(result)
    result = plus_one([4,3,2,1]) # [4,3,2,2]
    print(result)
    result = plus_one([9]) # [1,0]
    print(result)

if __name__ == "__main__":
    main()