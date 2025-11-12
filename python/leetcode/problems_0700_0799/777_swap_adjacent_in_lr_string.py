# -------------------------------
# 777. Swap Adjacent in LR String
# -------------------------------

# Problem: https://leetcode.com/problems/swap-adjacent-in-lr-string
#
# In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL", a move
# consists of either replacing one occurrence of "XL" with "LX", or replacing one
# occurrence of "RX" with "XR". Given the starting string start and the ending
# string result, return True if and only if there exists a sequence of moves to
# transform start to result.
# 
# Example 1:
# 
# Input: start = "RXXLRXRXL", result = "XRLXXRRLX"
# Output: true
# 
# Explanation: We can transform start to result following these steps:
# RXXLRXRXL ->
# XRXLRXRXL ->
# XRLXRXRXL ->
# XRLXXRRXL ->
# XRLXXRRLX
# 
# Example 2:
# 
# Input: start = "X", result = "L"
# Output: false
# 
# 
# Constraints:
#       1 <= start.length <= 10⁴
#       start.length == result.length
#       Both start and result will only consist of characters in 'L', 'R', and 'X'.


# Solution: https://algo.monster/liteproblems/777
# Credit: AlgoMonster
def can_transform(start, result):
    n = len(start)
    i = 0  # Pointer for start string
    j = 0  # Pointer for end string
    
    while True:
        # Skip all 'X' characters in start string
        while i < n and start[i] == 'X':
            i += 1
        
        # Skip all 'X' characters in end string
        while j < n and result[j] == 'X':
            j += 1
        
        # Both pointers reached the end - transformation successful
        if i >= n and j >= n:
            return True
        
        # One pointer reached the end but not the other - transformation impossible
        # Or the non-X characters don't match
        if i >= n or j >= n or start[i] != result[j]:
            return False
        
        # 'L' can only move left, so its position in start must be >= its position in end
        if start[i] == 'L' and i < j:
            return False
        
        # 'R' can only move right, so its position in start must be <= its position in end
        if start[i] == 'R' and i > j:
            return False
        
        # Move both pointers forward
        i += 1
        j += 1
    # Time: O(n)
    # Space: O(1)


def main():
    result = can_transform(start = "RXXLRXRXL", result = "XRLXXRRLX")
    print(result) # True

    result = can_transform(start = "X", result = "L")
    print(result) # False

if __name__ == "__main__":
    main()
