# -----------------
# 77. Combinations
# -----------------

# Problem: https://leetcode.com/problems/combinations/
# 
# Given two integers n and k, return all possible combinations of k numbers 
# chosen from the range [1, n].
# 
# You may return the answer in any order.

# Solution: https://youtu.be/q0s6m7AiM7o
# Credit: Navdeep Singh founder of NeetCode
def combine(n, k):
    res = []
    def helper(start, comb):
        if len(comb) == k:
            res.append(comb.copy())
            return
        for i in range(start, n+1):
            comb.append(i)
            helper(i+1, comb)
            comb.pop()
    helper(1, [])
    return res

# Solution: https://youtu.be/v1hg8rDIryg
# Credit: Greg Hogg
def combine_alt(n, k):
    ans, sol = [], []

    def backtrack(x):
        if len(sol) == k:
            ans.append(sol[:])
            return

        left = x
        still_need = k - len(sol)

        if left > still_need:
            backtrack(x - 1)

        sol.append(x)
        backtrack(x - 1)
        sol.pop()

    backtrack(n)
    return ans

def main():
    result = combine(n = 4, k = 2) # [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
    print(result)
    result = combine(n = 1, k = 1) # [[1]]
    print(result)

if __name__ == "__main__":
    main()