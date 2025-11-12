# ----------------------------------------
# 1313. Decompress Run-Length Encoded List
# ----------------------------------------

# Problem: https://leetcode.com/problems/decompress-run-length-encoded-list
#
# We are given a list nums of integers representing a list compressed with run-
# length encoding.
# 
# Consider each adjacent pair of elements [freq, val] = [nums[2*i],
# nums[2*i+1]] (with i >= 0).  For each such pair, there are freq elements with
# value val concatenated in a sublist. Concatenate all the sublists from left to
# right to generate the decompressed list.
# 
# Return the decompressed list.
# 
# Example 1:
# 
# Input: nums = [1,2,3,4]
# Output: [2,4,4,4]
# 
# Explanation: The first pair [1,2] means we have freq = 1 and val = 2 so we
# generate the array [2].
# The second pair [3,4] means we have freq = 3 and val = 4 so we generate [4,4,4].
# At the end the concatenation [2] + [4,4,4] is [2,4,4,4].
# 
# Example 2:
# 
# Input: nums = [1,1,2,3]
# Output: [1,3,3]
# 
# 
# Constraints:
#         2 <= nums.length <= 100
#         nums.length % 2 == 0
#         1 <= nums[i] <= 100


# Solution: https://algo.monster/liteproblems/1313
# Credit: AlgoMonster
def decompress_RLE_list(nums):
    # Initialize result list
    result = []
    
    # Iterate through the list in steps of 2 to process each (frequency, value) pair
    for i in range(0, len(nums), 2):
        frequency = nums[i]      # Extract frequency at even index
        value = nums[i + 1]      # Extract value at odd index
        
        # Append the value 'frequency' times to the result
        for _ in range(frequency):
            result.append(value)
    
    return result
    # Time: O(m)
    # Space: O(1)
    # m = the total number of elements in the decompressed output.

# Solution: https://leetcode.com/problems/decompress-run-length-encoded-list/solutions/478426/python-3-one-line-beats-100-by-junaidman-fjfv
# Credit: Junaid Mansuri -> https://leetcode.com/u/junaidmansuri/
def decompress_RLE_list_short(nums):
    return sum([nums[i] * [nums[i+1]] for i in range(0, len(nums), 2)], [])
    # Time: O(l * n)
    # Space: O(l)
    # l = the length of the resulting decompressed list, which is the sum of all frequencies.


def main():
    result = decompress_RLE_list(nums = [1,2,3,4])
    print(result) # [2, 4, 4, 4]

    result = decompress_RLE_list(nums = [1,1,2,3])
    print(result) # [1, 3, 3]

if __name__ == "__main__":
    main()
