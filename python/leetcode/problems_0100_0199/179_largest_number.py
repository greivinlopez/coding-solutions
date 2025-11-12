# -------------------
# 179. Largest Number
# -------------------

# Problem: https://leetcode.com/problems/largest-number/
# 
# Given a list of non-negative integers nums, arrange them such that they form 
# the largest number and return it.
# 
# Since the result may be very large, so you need to return a string instead of 
# an integer.
# 
#  
# Example 1:
# 
# Input: nums = [10,2]
# Output: "210"
# 
# 
# Example 2:
# 
# Input: nums = [3,30,34,5,9]
# Output: "9534330"
# 
#  
# Constraints:
# 
# 	1 <= nums.length <= 100
# 	0 <= nums[i] <= 109

def cmp_to_key(mycmp):
    """Convert a cmp= function into a key= function"""
    class K(object):
        _slots_ = ['obj']
        def __init__(self, obj):
            self.obj = obj
        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0
        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0
        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0
        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0
        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0
        _hash_ = None
    return K

# Solution: https://youtu.be/WDx6Y4i4xJ8
# Credit: Navdeep Singh founder of NeetCode
def largest_number(nums):
    for i, n in enumerate(nums):
        nums[i] = str(n)

    def compare(n1, n2):
        if n1 + n2 > n2 + n1:
            return -1
        else:
            return 1

    nums = sorted(nums, key = cmp_to_key(compare))

    return str(int("".join(nums)))


def main():
    result = largest_number([10,2])
    print(result) # "210"

    result = largest_number([3,30,34,5,9])
    print(result) # "9534330"

if __name__ == "__main__":
    main()
