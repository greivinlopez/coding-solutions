# ----------------------------------
# 128. Longest Consecutive Sequence
# ----------------------------------

# Problem: https://leetcode.com/problems/longest-consecutive-sequence/
# 
# Given an unsorted array of integers nums, return the length of the longest 
# consecutive elements sequence.
# 
# You must write an algorithm that runs in O(n) time.

# Solution: https://youtu.be/P6RZZMu_maU
# Credit: Navdeep Singh founder of NeetCode
def longest_consecutive(nums):
    # Time: O(n)
    # Space: O(n)
    numSet = set(nums)
    longest = 0

    for n in numSet:
        # check if its the start of a sequence
        if (n - 1) not in numSet:
            length = 1
            while (n + length) in numSet:
                length += 1
            longest = max(length, longest)
    return longest

# Same Solution: https://youtu.be/joIEdeOGqjQ
# Credit: Greg Hogg

def main():
    result = longest_consecutive([100,4,200,1,3,2])
    print(result) # 4

    result = longest_consecutive([0,3,7,2,5,8,4,6,0,1])
    print(result) # 9

    result = longest_consecutive([1,0,1,2])
    print(result) # 3

if __name__ == "__main__":
    main()