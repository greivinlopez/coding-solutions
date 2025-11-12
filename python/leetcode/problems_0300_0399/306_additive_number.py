# --------------------
# 306. Additive Number
# --------------------

# Problem: https://leetcode.com/problems/additive-number
#
# An additive number is a string whose digits can form an additive sequence.
# 
# A valid additive sequence should contain at least three numbers. Except for the
# first two numbers, each subsequent number in the sequence must be the sum of the
# preceding two.
# 
# Given a string containing only digits, return true if it is an additive number
# or false otherwise.
# 
# Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1,
# 2, 03 or 1, 02, 3 is invalid.
# 
# Example 1:
# 
# Input: "112358"
# Output: true
# 
# Explanation:
# The digits can form an additive sequence: 1, 1, 2, 3, 5, 8.
# 1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
# 
# Example 2:
# 
# Input: "199100199"
# Output: true
# 
# Explanation:
# The additive sequence is: 1, 99, 100, 199. 
# 1 + 99 = 100, 99 + 100 = 199
# 
# 
# Constraints:
#         1 <= num.length <= 35
#         num consists only of digits.
# 
# Follow up: How would you handle overflow for very large input integers?


# Solution: https://leetcode.com/problems/additive-number/solutions/913506/easyway-explanation-every-step
def is_additive_number(num):
    def dfs(s, seq):
        if not s:  
            if len(seq) > 2: 
                return True
            else: 
                return False
    
        for i in range(len(s)):
            if s[0] == '0' and i > 0: 
                break                
            cur = int(s[:i+1]) 
            
            if len(seq) > 1 and cur != seq[-2] + seq[-1]:    
                continue
            
            if dfs(s[i+1:], seq+[cur]): return True           
        return False

    return dfs(num, [])
    # Time: O(n³)
    # Space: O(n²)


def main():
    result = is_additive_number("112358")
    print(result) # True

    result = is_additive_number("199100199")
    print(result) # True

if __name__ == "__main__":
    main()
