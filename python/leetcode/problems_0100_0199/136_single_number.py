# -------------------
# 136. Single Number
# -------------------

# Problem: https://leetcode.com/problems/single-number/
# 
# Given a non-empty array of integers nums, every element appears twice except 
# for one. Find that single one.
# 
# You must implement a solution with a linear runtime complexity and use only 
# constant extra space.

# Solution: https://youtu.be/qMPX1AOa83k
# Credit: Navdeep Singh founder of NeetCode
def single_number(nums):
    # Time: O(n)
    # Space: O(1)
    res = 0
    for n in nums:
        res = n ^ res
    return res

# Same Solution: https://youtu.be/mriHA5vEh0A
# Credit: Greg Hogg

def main():
    result = single_number([2,2,1])
    print(result) # 1

    result = single_number([4,1,2,1,2])
    print(result) # 4

    result = single_number([1])
    print(result) # 1

if __name__ == "__main__":
    main()