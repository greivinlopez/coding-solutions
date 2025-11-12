# ---------------------------------
# 768. Max Chunks To Make Sorted II
# ---------------------------------

# Problem: https://leetcode.com/problems/max-chunks-to-make-sorted-ii
#
# You are given an integer array arr.
# 
# We split arr into some number of chunks (i.e., partitions), and individually
# sort each chunk. After concatenating them, the result should equal the sorted
# array.
# 
# Return the largest number of chunks we can make to sort the array.
# 
# Example 1:
# 
# Input: arr = [5,4,3,2,1]
# Output: 1
# 
# Explanation:
# Splitting into two or more chunks will not return the required result.
# For example, splitting into [5, 4], [3, 2, 1] will result in [4, 5, 1, 2, 3],
# which isn't sorted.
# 
# Example 2:
# 
# Input: arr = [2,1,3,4,4]
# Output: 4
# 
# Explanation:
# We can split into two chunks, such as [2, 1], [3, 4, 4].
# However, splitting into [2, 1], [3], [4], [4] is the highest number of chunks
# possible.
# 
# 
# Constraints:
#         1 <= arr.length <= 2000
#         0 <= arr[i] <= 10⁸

# Solution: https://algo.monster/liteproblems/768
# Credit: AlgoMonster
def max_chunks_to_sorted(arr):
    # Stack to maintain the maximum value of each chunk
    stack = []
    
    for value in arr:
        # If stack is empty or current value is greater than or equal to 
        # the max of the last chunk, start a new chunk
        if not stack or value >= stack[-1]:
            stack.append(value)
        else:
            # Current value is smaller than the max of the last chunk
            # Need to merge chunks
            
            # Save the maximum value of the current chunk being merged
            max_value = stack.pop()
            
            # Pop all chunks whose max value is greater than current value
            # These chunks need to be merged because the current smaller value
            # would need to be sorted before their elements
            while stack and stack[-1] > value:
                stack.pop()
            
            # Push back the maximum value of all merged chunks
            stack.append(max_value)
    
    # The number of elements in stack represents the number of chunks
    return len(stack)
    # Time: O(n)
    # Space: O(n)


def main():
    result = max_chunks_to_sorted(arr = [5,4,3,2,1])
    print(result) # 1

    result = max_chunks_to_sorted(arr = [2,1,3,4,4])
    print(result) # 4

if __name__ == "__main__":
    main()
