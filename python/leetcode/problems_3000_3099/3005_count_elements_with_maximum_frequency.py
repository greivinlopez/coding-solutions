# -------------------------------------------
# 3005. Count Elements With Maximum Frequency
# -------------------------------------------

# Problem: https://leetcode.com/problems/count-elements-with-maximum-frequency
#
# You are given an array nums consisting of positive integers.
# 
# Return the total frequencies of elements in nums such that those elements all
# have the maximum frequency.
# 
# The frequency of an element is the number of occurrences of that element in the
# array.
# 
# Example 1:
# 
# Input: nums = [1,2,2,3,1,4]
# Output: 4
# 
# Explanation: The elements 1 and 2 have a frequency of 2 which is the maximum
# frequency in the array.
# So the number of elements in the array with maximum frequency is 4.
# 
# Example 2:
# 
# Input: nums = [1,2,3,4,5]
# Output: 5
# 
# Explanation: All elements of the array have a frequency of 1 which is the
# maximum.
# So the number of elements in the array with maximum frequency is 5.
# 
# 
# Constraints:
#         1 <= nums.length <= 100
#         1 <= nums[i] <= 100


# Credit: Jaweria Batool -> https://github.com/Jaweria-B
def max_frequency_elements(nums):
    # Find the frequency of each element
    frequencies = {}
    for num in nums:
        if num in frequencies:
            frequencies[num] += 1
        else:
            frequencies[num] = 1

    # Determine the maximum frequency
    max_frequency = 0
    for frequency in frequencies.values():
        max_frequency = max(max_frequency, frequency)

    # Calculate the total frequencies of elements with the maximum frequency
    frequency_of_max_frequency = 0
    for frequency in frequencies.values():
        if frequency == max_frequency:
            frequency_of_max_frequency += 1

    return frequency_of_max_frequency * max_frequency
    # Time: O(n)
    # Space: O(n)


def main():
    result = max_frequency_elements(nums = [1,2,2,3,1,4])
    print(result) # 4

    result = max_frequency_elements(nums = [1,2,3,4,5])
    print(result) # 5

if __name__ == "__main__":
    main()
