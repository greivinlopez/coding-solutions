# ------------------
# 52. N-Queens II ♟️
# ------------------

# Problem: https://leetcode.com/problems/n-queens-ii/
# The n-queens puzzle is the problem of placing n queens on an n x n chessboard 
# such that no two queens attack each other.
# 
# Given an integer n, return the number of distinct solutions to the n-queens puzzle.

# Solution: https://youtu.be/nalYyLZgvCY
# Credit: Navdeep Singh founder of NeetCode 
def total_n_queens(n):
    # Time: O(n * n!)
    answer = 0

    cols = set()
    posdiag = set()
    negdiag = set()

    def backtrack(i):
        if i == n:
            nonlocal answer
            answer += 1
            return
        
        for j in range(n):
            if j in cols or (i+j) in posdiag or (i-j) in negdiag:
                continue

            cols.add(j)
            posdiag.add(i+j)
            negdiag.add(i-j)

            backtrack(i+1)
            
            cols.remove(j)
            posdiag.remove(i+j)
            negdiag.remove(i-j)
    
    backtrack(0)
    return answer

def main():
    result = total_n_queens(4)
    # Expected Output: 2
    print(result)
    result = total_n_queens(1)
    # Expected Output: 1
    print(result)

if __name__ == "__main__":
    main()