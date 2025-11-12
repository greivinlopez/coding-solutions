# ----------------------------------
# 1207. Unique Number of Occurrences
# ----------------------------------

# Problem: https://leetcode.com/problems/unique-number-of-occurrences
#
# Given an array of integers arr, return true if the number of occurrences of each
# value in the array is unique or false otherwise.
# 
# Example 1:
# 
# Input: arr = [1,2,2,1,1,3]
# Output: true
# 
# Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values
# have the same number of occurrences.
# 
# Example 2:
# 
# Input: arr = [1,2]
# Output: false
# 
# Example 3:
# 
# Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
# Output: true
# 
# 
# Constraints:
#         1 <= arr.length <= 1000
#         -1000 <= arr[i] <= 1000

from collections import defaultdict, Counter

# Credit: Jeel Gajera -> https://github.com/JeelGajera
def unique_occurrences_alt(arr):
    freq = Counter(arr)

    for i in freq.values():
        if list(freq.values()).count(i) > 1:
            return False

    return True
    # Time: O(n²)
    # Space: O(n)

# Credit: Jaweria Batool -> https://github.com/Jaweria-B
def unique_occurrences(arr):
    occurence = defaultdict(int)
    
    for i in arr:
        occurence[i] += 1
        
    return len(set(occurence.values())) == len(occurence)
    # Time: O(n)
    # Space: O(n)


def main():
    result = unique_occurrences(arr = [1,2,2,1,1,3])
    print(result) # True

    result = unique_occurrences(arr = [1,2])
    print(result) # False

    result = unique_occurrences(arr = [-3,0,1,-3,1,1,1,-3,10,0])
    print(result) # True

if __name__ == "__main__":
    main()
