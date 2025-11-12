# ---------------------------------------
# 1394. Find Lucky Integer in an Array 🍀
# ---------------------------------------

# Problem: https://leetcode.com/problems/find-lucky-integer-in-an-array
#
# Given an array of integers arr, a lucky integer is an integer that has a
# frequency in the array equal to its value.
# 
# Return the largest lucky integer in the array. If there is no lucky integer
# return -1.
# 
# Example 1:
# 
# Input: arr = [2,2,3,4]
# Output: 2
# 
# Explanation: The only lucky number in the array is 2 because frequency[2] == 2.
# 
# Example 2:
# 
# Input: arr = [1,2,2,3,3,3]
# Output: 3
# 
# Explanation: 1, 2 and 3 are all lucky numbers, return the largest of them.
# 
# Example 3:
# 
# Input: arr = [2,2,2,3,3]
# Output: -1
# 
# Explanation: There are no lucky numbers in the array.
# 
# 
# Constraints:
#         1 <= arr.length <= 500
#         1 <= arr[i] <= 500

from collections import Counter

# Solution: https://algo.monster/liteproblems/1394
# Credit: AlgoMonster
def find_lucky(arr):
    # Count the frequency of each number in the array
    frequency_map = Counter(arr)
    
    # Find all lucky numbers (numbers where value equals its frequency)
    # and return the maximum, or -1 if no lucky number exists
    return max((num for num, freq in frequency_map.items() if num == freq), default=-1)
    # Time: O(n)
    # Space: O(n)

# Solution: https://leetcode.com/problems/find-lucky-integer-in-an-array/solutions/6920514/beginner-freindlyjavacpythonjs-by-ashokv-ufmp
# Credit: Ashok Varma -> https://leetcode.com/u/ashokvarma5247/
def find_lucky_alt(arr):
    freq = Counter(arr)
    lucky = -1

    for num, count in freq.items():
        if num == count:
            lucky = max(lucky, num)

    return lucky
    # Time: O(n)
    # Space: O(n)

# Solution: https://leetcode.com/problems/find-lucky-integer-in-an-array/solutions/6921019/python3-filter-then-max-ts-99-96-by-spau-2gfn
# Credit: Capt Spaulding -> https://leetcode.com/u/Spaulding_/
def find_lucky_alt_2(arr):
    freq = Counter(arr)
    lucky = -1

    for num, count in freq.items():
        if num == count:
            lucky = max(lucky, num)

    return lucky
    # Time: O(n)
    # Space: O(n)


def main():
    result = find_lucky([2,2,3,4])
    print(result) # 2

    result = find_lucky([1,2,2,3,3,3])
    print(result) # 3

    result = find_lucky([2,2,2,3,3])
    print(result) # -1

if __name__ == "__main__":
    main()
