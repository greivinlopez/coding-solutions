# -----------------
# 670. Maximum Swap
# -----------------

# Problem: https://leetcode.com/problems/maximum-swap
#
# You are given an integer num. You can swap two digits at most once to get the
# maximum valued number.
# 
# Return the maximum valued number you can get.
# 
# Example 1:
# 
# Input: num = 2736
# Output: 7236
# 
# Explanation: Swap the number 2 and the number 7.
# 
# Example 2:
# 
# Input: num = 9973
# Output: 9973
# 
# Explanation: No swap.
# 
# 
# Constraints:
#         0 <= num <= 10^8


# Solution: https://youtu.be/4FZtJ8420m8
# Credit: Navdeep Singh founder of NeetCode
def maximum_swap(num):
    num = list(str(num))
    max_digit = "0"
    max_i = -1
    swap_i = -1
    swap_j = -1

    for i in reversed(range(len(num))):
        if num[i] > max_digit:
            max_digit = num[i]
            max_i = i
        
        if num[i] < max_digit:
            swap_i, swap_j = i, max_i
    
    if swap_i != -1:
        num[swap_i], num[swap_j] = num[swap_j], num[swap_i]
    
    return int("".join(num))
    # Time: O(log(n))
    # Space: O(log(n))


def main():
    result = maximum_swap(num = 2736)
    print(result) # 7236

    result = maximum_swap(num = 9973)
    print(result) # 9973

if __name__ == "__main__":
    main()
