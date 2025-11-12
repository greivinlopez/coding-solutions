# -------------------------------------------
# 1304. Find N Unique Integers Sum up to Zero
# -------------------------------------------

# Problem: https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero
#
# Given an integer n, return any array containing n unique integers such that they
# add up to 0.
# 
# Example 1:
# 
# Input: n = 5
# Output: [-7,-1,1,3,4]
# 
# Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].
# 
# Example 2:
# 
# Input: n = 3
# Output: [-1,0,1]
# 
# Example 3:
# 
# Input: n = 1
# Output: [0]
# 
# 
# Constraints:
#         1 <= n <= 1000


# Solution: https://algo.monster/liteproblems/1304
# Credit: AlgoMonster
def sum_zero(n):
    result = []
    
    # Add pairs of positive and negative integers
    # n >> 1 is equivalent to n // 2 (integer division)
    for i in range(n >> 1):
        # Add positive integer (i+1)
        result.append(i + 1)
        # Add corresponding negative integer -(i+1)
        result.append(-(i + 1))
    
    # If n is odd, add 0 to maintain zero sum
    # n & 1 checks if n is odd (equivalent to n % 2 == 1)
    if n & 1:
        result.append(0)
        
    return result
    # Time: O(n)
    # Space: O(n)

# Alternative Solution: https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/solutions/465585/javacpython-find-the-rule-by-lee215-1iuj
# Credit: Lee -> https://leetcode.com/u/lee215/
def sum_zero_short(n):
    return list(range(1 - n, n, 2))
    # Time: O(n)
    # Space: O(n)


def main():
    result = sum_zero(5)
    print(result) # [1, -1, 2, -2, 0]

    result = sum_zero(3)
    print(result) # [1, -1, 0]

    result = sum_zero(1)
    print(result) # [0]

if __name__ == "__main__":
    main()
