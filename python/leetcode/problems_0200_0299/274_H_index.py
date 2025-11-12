# ------------
# 274. H Index
# ------------

# Problem: https://leetcode.com/problems/h-index/
# 
# Given an array of integers citations where citations[i] is the number of 
# citations a researcher received for their ith paper, return the researcher's 
# h-index.
# 
# According to the definition of h-index on Wikipedia: The h-index is defined 
# as the maximum value of h such that the given researcher has published at 
# least h papers that have each been cited at least h times.
# 
#  
# Example 1:
# 
# Input: citations = [3,0,6,1,5]
# Output: 3
# Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
# Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.
# 
# 
# Example 2:
# 
# Input: citations = [1,3,1]
# Output: 1
# 
# 
# Constraints:
# 
# 	n == citations.length
# 	1 <= n <= 5000
# 	0 <= citations[i] <= 1000


# Solution: Not Video Found
# Credit: Navdeep Singh founder of NeetCode
def h_index(citations):
    length = len(citations)
    citations.sort()
    for i in range(length):
        if citations[i] >= length - i:
            return length - i
    return 0

# Solution: https://youtu.be/mgG5KFTvfPw
# Credit: Greg Hogg
def h_index_alt(citations):
    n = len(citations)
    paper_counts = [0] * (n+1)

    for c in citations:
        paper_counts[min(n, c)] += 1
    
    h = n
    papers = paper_counts[n]
    
    while papers < h:
        h -= 1
        papers += paper_counts[h]
    
    return h
        # Time: O(n), Space: O(n)

def main():
    result = h_index([3,0,6,1,5])
    print(result) # 3

    result = h_index([1,3,1])
    print(result) # 1

if __name__ == "__main__":
    main()
