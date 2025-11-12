# -----------------------------------
# 1338. Reduce Array Size to The Half
# -----------------------------------

# Problem: https://leetcode.com/problems/reduce-array-size-to-the-half
#
# You are given an integer array arr. You can choose a set of integers and remove
# all the occurrences of these integers in the array.
# 
# Return the minimum size of the set so that at least half of the integers of the
# array are removed.
# 
# Example 1:
# 
# Input: arr = [3,3,3,3,5,5,5,2,2,7]
# Output: 2
# 
# Explanation: Choosing {3,7} will make the new array [5,5,5,2,2] which has size 5
# (i.e equal to half of the size of the old array).
# Possible sets of size 2 are {3,5},{3,2},{5,2}.
# Choosing set {2,7} is not possible as it will make the new array [3,3,3,3,5,5,5]
# which has a size greater than half of the size of the old array.
# 
# Example 2:
# 
# Input: arr = [7,7,7,7,7,7]
# Output: 1
# 
# Explanation: The only possible set you can choose is {7}. This will make the new
# array empty.
# 
# 
# Constraints:
#         2 <= arr.length <= 10⁵
#         arr.length is even.
#         1 <= arr[i] <= 10⁵

from collections import Counter

# Solution: https://algo.monster/liteproblems/1338
# Credit: AlgoMonster
def min_set_size(arr):
    # Count frequency of each element in the array
    frequency_counter = Counter(arr)
    
    # Initialize variables to track the answer and removed elements count
    result = 0
    removed_count = 0
    
    # Iterate through elements sorted by frequency in descending order
    for element, frequency in frequency_counter.most_common():
        # Add current element's frequency to the removed count
        removed_count += frequency
        # Increment the size of our removal set
        result += 1
        
        # Check if we've removed at least half of the array elements
        if removed_count * 2 >= len(arr):
            break
    
    return result
    # Time: O(n log n)
    # Space: O(n)


# Alternative Solution: https://leetcode.com/problems/reduce-array-size-to-the-half/solutions/2441786/python-100-runtime-simple-fast-please-up-xceg
# Credit: Steve Shin -> https://leetcode.com/u/SteveShin_/
def min_set_size_alt(arr):
    d = {}
    for x in arr:
        if x not in d:
            d[x] = 1
        else:
            d[x] += 1
                
    l = sorted(d.values())
    N = len(arr) // 2
    idx = 0
    
    while N > 0:
        N -= l[-idx-1]
        idx += 1
        
    return idx
    # Time: O(n log n)
    # Space: O(n)


def main():
    result = min_set_size(arr = [3,3,3,3,5,5,5,2,2,7])
    print(result) # 2

    result = min_set_size(arr = [7,7,7,7,7,7])
    print(result) # 1

if __name__ == "__main__":
    main()
