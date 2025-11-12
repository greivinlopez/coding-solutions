# ---------------
# 275. H-Index II
# ---------------

# Problem: https://leetcode.com/problems/h-index-ii
#
# Given an array of integers citations where citations[i] is the number of
# citations a researcher received for their iᵗʰ paper and citations is sorted in
# non-descending order, return the researcher's h-index.
# 
# According to the definition of h-index on Wikipedia: The h-index is defined as
# the maximum value of h such that the given researcher has published at least h
# papers that have each been cited at least h times.
# 
# You must write an algorithm that runs in logarithmic time.
# 
# Example 1:
# 
# Input: citations = [0,1,3,5,6]
# Output: 3
# 
# Explanation: [0,1,3,5,6] means the researcher has 5 papers in total and each of
# them had received 0, 1, 3, 5, 6 citations respectively.
# Since the researcher has 3 papers with at least 3 citations each and the
# remaining two with no more than 3 citations each, their h-index is 3.
# 
# Example 2:
# 
# Input: citations = [1,2,100]
# Output: 2
# 
# Constraints:
#         n == citations.length
#         1 <= n <= 10⁵
#         0 <= citations[i] <= 1000
#         citations is sorted in ascending order.


# Solution: https://leetcode.com/problems/h-index-ii/solutions/3235216/275-time-98-1-solution-with-step-by-step-explanation
# Credit: Marlen Kanatbekov -> https://leetcode.com/u/Marlen09/
def h_index(citations):
    n = len(citations)
    left, right = 0, n - 1
    while left <= right:
        mid = (left + right) // 2
        if citations[mid] == n - mid:
            return n - mid
        elif citations[mid] < n - mid:
            left = mid + 1
        else:
            right = mid - 1
    return n - left
    # Time: O(log(n))
    # Space: O(1)


def main():
    result = h_index([0,1,3,5,6])
    print(result) # 3

    result = h_index([1,2,100])
    print(result) # 2

if __name__ == "__main__":
    main()
