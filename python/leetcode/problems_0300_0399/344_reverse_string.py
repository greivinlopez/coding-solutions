# -------------------
# 344. Reverse String
# -------------------

# Problem: https://leetcode.com/problems/reverse-string/
# 
# Write a function that reverses a string. The input string is given as an 
# array of characters s.
# 
# You must do this by modifying the input array in-place with O(1) extra 
# memory.
# 
#  
# Example 1:
# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# Example 2:
# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]
# 
#  
# Constraints:
# 
# 	1 <= s.length <= 10^5
# 	s[i] is a printable ascii character.


# Solution: https://youtu.be/_d0T_2Lk2qA
# Credit: Navdeep Singh founder of NeetCode
def reverse_string(s):
    """
    Do not return anything, modify s in-place instead.
    """
    l = 0
    r = len(s) - 1
    while l < r:
        s[l],s[r] = s[r],s[l]
        l += 1
        r -= 1
    # Time: O(n)
    # Space: O(1)

# Solution: https://youtu.be/OD9PjLapAOQ
# Credit: Greg Hogg
# Brute Force Solution
def reverse_string_brute(s):
    """
    Do not return anything, modify s in-place instead.
    """
    n = len(s)
    T = []
    for i in range(n-1, -1, -1):
        T.append(s[i])
    
    for i in range(n):
        s[i] = T[i]
    
    # Time: O(n)
    # Space: O(n)

# Two Pointers (Optimal) Solution
# Same as Navdeep's


def main():
    l1 = ["h","e","l","l","o"]
    reverse_string(l1)
    print(l1) # ["o","l","l","e","h"]

    l2 = ["H","a","n","n","a","h"]
    result = reverse_string(l2)
    print(l2) # ["h","a","n","n","a","H"]


if __name__ == "__main__":
    main()
