# -----------------------
# 1051. Height Checker 📏
# -----------------------

# Problem: https://leetcode.com/problems/height-checker
#
# A school is trying to take an annual photo of all the students. The students are
# asked to stand in a single file line in non-decreasing order by height. Let this
# ordering be represented by the integer array expected where expected[i] is the
# expected height of the i^th student in line.
# 
# You are given an integer array heights representing the current order that the
# students are standing in. Each heights[i] is the height of the i^th student in
# line (0-indexed).
# 
# Return the number of indices where heights[i] != expected[i].
# 
# Example 1:
# 
# Input: heights = [1,1,4,2,1,3]
# Output: 3
# 
# Explanation:
# heights:  [1,1,4,2,1,3]
# expected: [1,1,1,2,3,4]
# Indices 2, 4, and 5 do not match.
# 
# Example 2:
# 
# Input: heights = [5,1,2,3,4]
# Output: 5
# 
# Explanation:
# heights:  [5,1,2,3,4]
# expected: [1,2,3,4,5]
# All indices do not match.
# 
# Example 3:
# 
# Input: heights = [1,2,3,4,5]
# Output: 0
# 
# Explanation:
# heights:  [1,2,3,4,5]
# expected: [1,2,3,4,5]
# All indices match.
# 
# 
# Constraints:
#         1 <= heights.length <= 100
#         1 <= heights[i] <= 100


# Solution: https://youtu.be/mQAoeYaE3Xk
# Credit: Navdeep Singh founder of NeetCode
def height_checker(heights):
    count = [0] * 101
    for h in heights:
        count[h] += 1
        
    expected = []
    for h in range(1, 101):
        c = count[h]
        for _ in range(c):
            expected.append(h)
            
    res = 0
    for i in range(len(heights)):
        if heights[i] != expected[i]:
            res += 1
    
    return res
    # Time: O(n)
    # Space: O(n)
    # n = number of elements in heights


def main():
    result = height_checker(heights = [1,1,4,2,1,3])
    print(result) # 3

    result = height_checker(heights = [5,1,2,3,4])
    print(result) # 5

    result = height_checker(heights = [1,2,3,4,5])
    print(result) # 0

if __name__ == "__main__":
    main()
