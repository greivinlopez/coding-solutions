# ---------------------------------
# 1539. Kth Missing Positive Number
# ---------------------------------

# Problem: https://leetcode.com/problems/kth-missing-positive-number
#
# Given an array arr of positive integers sorted in a strictly increasing order,
# and an integer k.
# 
# Return the kᵗʰ positive integer that is missing from this array.
# 
# Example 1:
# 
# Input: arr = [2,3,4,7,11], k = 5
# Output: 9
# 
# Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The
# 5th missing positive integer is 9.
# 
# Example 2:
# 
# Input: arr = [1,2,3,4], k = 2
# Output: 6
# 
# Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing
# positive integer is 6.
# 
# 
# Constraints:
#         1 <= arr.length <= 1000
#         1 <= arr[i] <= 1000
#         1 <= k <= 1000
#         arr[i] < arr[j] for 1 <= i < j <= arr.length
# 
# Follow up:
# Could you solve this problem in less than O(n) complexity?


# Solution: https://algo.monster/liteproblems/1539
# Credit: AlgoMonster
def find_kth_positive(arr, k):
    # If the first element is greater than k, then the kth missing number is k itself
    # Example: arr = [5, 6, 7], k = 3 -> missing are 1, 2, 3, 4... so 3rd missing is 3
    if arr[0] > k:
        return k
    
    # Binary search to find the position where we have at least k missing numbers
    left, right = 0, len(arr)
    
    while left < right:
        mid = (left + right) // 2
        
        # Calculate how many positive integers are missing before arr[mid]
        # arr[mid] - mid - 1 gives the count of missing numbers before index mid
        # Example: arr[2] = 7, then 7 - 2 - 1 = 4 missing numbers (1,2,3,4 are missing)
        missing_count = arr[mid] - mid - 1
        
        if missing_count >= k:
            # We have at least k missing numbers before mid, search in left half
            right = mid
        else:
            # We don't have enough missing numbers yet, search in right half
            left = mid + 1
    
    # After binary search, left points to the smallest index where we have >= k missing numbers
    # We need to find the kth missing number based on arr[left - 1]
    # Formula: arr[left - 1] + (k - count of missing numbers before arr[left - 1])
    prev_index = left - 1
    missing_before_prev = arr[prev_index] - prev_index - 1
    return arr[prev_index] + k - missing_before_prev
    # Time: O(log n)
    # Space: O(1)

# One liner solution
# Solution: https://leetcode.com/problems/kth-missing-positive-number/solutions/3262163/c-java-python3-1-line-ologn-by-tojuna-w8qs
# Credit: Anujot Singh -> https://leetcode.com/u/tojuna/
from bisect import bisect_right
def find_kth_positive_alt(arr, k):
    return bisect_right(range(len(arr)), k, key= lambda x: arr[x] - x) + k

def main():
    result = find_kth_positive(arr = [2,3,4,7,11], k = 5)
    print(result) # 9

    result = find_kth_positive(arr = [1,2,3,4], k = 2)
    print(result) # 6

if __name__ == "__main__":
    main()
