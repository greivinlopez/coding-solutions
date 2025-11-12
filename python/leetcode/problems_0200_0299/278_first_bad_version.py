# ----------------------
# 278. First Bad Version
# ----------------------

# Problem: https://leetcode.com/problems/first-bad-version/
# 
# You are a product manager and currently leading a team to develop a new product. 
# Unfortunately, the latest version of your product fails the quality check. 
# Since each version is developed based on the previous version, all the versions 
# after a bad version are also bad.
# 
# Suppose you have n versions [1, 2, ..., n] and you want to find out the first 
# bad one, which causes all the following ones to be bad.
# 
# You are given an API bool isBadVersion(version) which returns whether version 
# is bad. Implement a function to find the first bad version. 
# You should minimize the number of calls to the API.
# 
#  
# Example 1:
# 
# Input: n = 5, bad = 4
# Output: 4
# Explanation:
# call isBadVersion(3) -> false
# call isBadVersion(5) -> true
# call isBadVersion(4) -> true
# Then 4 is the first bad version.
# 
# 
# Example 2:
# 
# Input: n = 1, bad = 1
# Output: 1
# 
# 
# Constraints:
# 
# 	1 <= bad <= n <= 231 - 1


# Solution: https://youtu.be/SiDMFIMldgg
# Credit: Navdeep Singh founder of NeetCode
def first_bad_version(n):
    l, r = 1, n
    while l < r:
        v = (l + r) // 2
        if isBadVersion(v):
            r = v
        else:
            l = v + 1
    return l
    # Time: O(Log n)
    # Space: O(1)

# Solution: https://youtu.be/vnfGi-ucwTE
# Credit: Greg Hogg
# Brute Force Solution
def first_bad_version_brute(n):
    for version in range(1, n+1):
        if isBadVersion(version):
            return version
    # Time: O(n)
    # Space: O(1)

# Optimal Solution
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
def first_bad_version_optimal(n):
    L = 1
    R = n

    while L < R:
        M = (L+R) // 2
        if isBadVersion(M):
            R = M
        else:
            L = M + 1
    
    return L 
    # Time: O(Log n)
    # Space: O(1)

def main():
    print("TO DO")

if __name__ == "__main__":
    main()
