# --------------------------
# 118. Pascal's Triangle 🔺
# --------------------------

# Problem: https://leetcode.com/problems/pascals-triangle/
# 
# Given an integer numRows, return the first numRows of Pascal's triangle.
# 
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
#       1
#      1 1
#     1 2 1
#    1 3 3 1

# Solution: https://youtu.be/nPVEaB3AjUM
# Credit: Navdeep Singh founder of NeetCode
def generate(rowIndex):
    if rowIndex == 0:
        return [[1]]
    else:
        return get_all_row(rowIndex - 1)

def get_all_row(rowIndex):
    if rowIndex == 0:
        return [[1]]
    ListPrec = get_all_row(rowIndex - 1)
    Len = len(ListPrec[-1])
    ListPrec.append([1])
    for i in range(0, Len - 1):
        ListPrec[-1].append(ListPrec[-2][i] + ListPrec[-2][i + 1])
    ListPrec[-1].append(1)
    return ListPrec


def main():
    result = generate(5)
    print(result) # 3

    result = generate(1)
    print(result) # 5

if __name__ == "__main__":
    main()