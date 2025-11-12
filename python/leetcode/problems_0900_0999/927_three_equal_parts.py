# ----------------------
# 927. Three Equal Parts
# ----------------------

# Problem: https://leetcode.com/problems/three-equal-parts
#
# You are given an array arr which consists of only zeros and ones, divide the
# array into three non-empty parts such that all of these parts represent the same
# binary value.
# 
# If it is possible, return any [i, j] with i + 1 < j, such that:
#         
#   * arr[0], arr[1], ..., arr[i] is the first part,
#   * arr[i + 1], arr[i + 2], ..., arr[j - 1] is the second part, and
#   * arr[j], arr[j + 1], ..., arr[arr.length - 1] is the third part.
#   * All three parts have equal binary values.
# 
# If it is not possible, return [-1, -1].
# 
# Note that the entire part is used when considering what binary value it
# represents. For example, [1,1,0] represents 6 in decimal, not 3. Also, leading
# zeros are allowed, so [0,1,1] and [1,1] represent the same value.
# 
# Example 1:
# 
# Input: arr = [1,0,1,0,1]
# Output: [0,3]
# 
# Example 2:
# 
# Input: arr = [1,1,0,1,1]
# Output: [-1,-1]
# 
# Example 3:
# 
# Input: arr = [1,1,0,0,1]
# Output: [0,2]
# 
# 
# Constraints:
#         3 <= arr.length <= 3 * 10⁴
#         arr[i] is 0 or 1


# Solution: https://leetcode.com/problems/three-equal-parts/solutions/1343923/linear-times-o-n-solution-in-python-clean
# Credit: Shantanu Gupta -> https://leetcode.com/u/shantanugupta1118/
def three_equal_parts(arr):
    ans = [-1,-1]
    numsOf1s = 0
    for i in arr:
        numsOf1s += i
    if numsOf1s == 0:
        return [0,2]
    if numsOf1s%3 != 0:
        return ans
    
    eachPart = numsOf1s//3
    index0, index1, index2 = -1, -1, -1
    numsOf1s = 0
    for i in range(len(arr)):
        if arr[i] == 1:
            numsOf1s += 1
            if numsOf1s == eachPart+1:
                index1 = i
            elif numsOf1s == 2*eachPart+1:
                index2 = i
            elif numsOf1s == 1:
                index0 = i
    while index2 < len(arr):
        if arr[index2] == arr[index0] and arr[index2] == arr[index1]:
            index0 += 1
            index1 += 1
            index2 += 1
        else:
            return ans 
    return [index0-1, index1]
    # Time: O(n)
    # Space: O(1)


def main():
    result = three_equal_parts(arr = [1,0,1,0,1])
    print(result) # [0,3]

    result = three_equal_parts(arr = [1,1,0,1,1])
    print(result) # [-1,-1]

    result = three_equal_parts(arr = [1,1,0,0,1])
    print(result) # [0,2]

if __name__ == "__main__":
    main()
