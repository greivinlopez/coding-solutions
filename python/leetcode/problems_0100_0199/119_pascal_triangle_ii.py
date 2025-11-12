# ----------------------------
# 119. Pascal's Triangle II 🔺
# ----------------------------

# Problem: https://leetcode.com/problems/pascals-triangle/
# 
# Given an integer rowIndex, return the rowIndexth (0-indexed) row of 
# the Pascal's triangle.
# 
# In Pascal's triangle, each number is the sum of the two numbers 
# directly above it as shown:
#       1
#      1 1
#     1 2 1
#    1 3 3 1

# Solution: https://youtu.be/k1DNTyal77I
# Credit: Navdeep Singh founder of NeetCode
def get_row(rowIndex):
    return get_row_rec(rowIndex, {})

def get_row_rec(rowIndex, memo):
    if rowIndex in memo:
        return memo[rowIndex]
    if rowIndex == 0:
        return [1]
    ListPrec = get_row_rec(rowIndex - 1, memo)
    Result = [1]
    for i in range(0, len(ListPrec) - 1):
        Result.append(ListPrec[i] + ListPrec[i + 1])
    Result.append(1)
    memo[rowIndex] = Result
    return Result


def main():
    result = get_row(3)
    print(result) # [1,3,3,1]

    result = get_row(0)
    print(result) # [1]

    result = get_row(1)
    print(result) # [1,1]

if __name__ == "__main__":
    main()