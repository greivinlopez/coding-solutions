# -----------------------------
# 282. Expression Add Operators
# -----------------------------

# Problem: https://leetcode.com/problems/expression-add-operators
#
# Given a string num that contains only digits and an integer target, return all
# possibilities to insert the binary operators '+', '-', and/or '*' between the
# digits of num so that the resultant expression evaluates to the target value.
# 
# Note that operands in the returned expressions should not contain leading zeros.
# 
# Note that a number can contain multiple digits.
# 
# Example 1:
# 
# Input: num = "123", target = 6
# Output: ["1*2*3","1+2+3"]
# 
# Explanation: Both "1*2*3" and "1+2+3" evaluate to 6.
# 
# Example 2:
# 
# Input: num = "232", target = 8
# Output: ["2*3+2","2+3*2"]
# 
# Explanation: Both "2*3+2" and "2+3*2" evaluate to 8.
# 
# Example 3:
# 
# Input: num = "3456237490", target = 9191
# Output: []
# 
# Explanation: There are no expressions that can be created from "3456237490" to
# evaluate to 9191.
# 
# 
# Constraints:
#         1 <= num.length <= 10
#         num consists of only digits.
#         -2³¹ <= target <= 2³¹ - 1


# Solution: https://leetcode.com/problems/expression-add-operators/solutions/3330455/well-explained-python-code
# Credit: https://leetcode.com/u/tryingall/
def add_operators(num, target):
    res = []

    def dfs(i, path, cur_num, prevNum):
        if i == len(num):
            if cur_num == target:
                res.append(path)
            return
        
        for j in range(i, len(num)):
            # starting with zero?
            if j > i and num[i] == '0':
                break
            n = int(num[i:j+1])

            # if cur index is 0 then simple add that number
            if i == 0:
                dfs(j + 1, path + str(n), cur_num + n, n)
            else:
                dfs(j + 1, path + "+" + str(n), cur_num + n, n)
                dfs(j + 1, path + "-" + str(n), cur_num - n, -n)
                dfs(j + 1, path + "*" + str(n), cur_num - prevNum + prevNum * n, prevNum * n)
    
    dfs(0, "", 0, 0)
    return res


def main():
    result = add_operators(num = "123", target = 6)
    print(result) # ['1+2+3', '1*2*3']

    result = add_operators(num = "232", target = 8)
    print(result) # ['2+3*2', '2*3+2']

    result = add_operators(num = "3456237490", target = 9191)
    print(result) # []

if __name__ == "__main__":
    main()
