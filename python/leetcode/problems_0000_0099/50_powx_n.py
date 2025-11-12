# --------------
# 50. Pow(x, n)
# --------------

# Problem: https://leetcode.com/problems/powx-n/
# Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).

# Solution: https://youtu.be/g9YQyYi4IQQ
# Credit: Navdeep Singh founder of NeetCode 
def my_pow(x, n):
    def helper(x, n):
        if x == 0:
            return 0
        if n == 0:
            return 1

        res = helper(x * x, n // 2)
        return x * res if n % 2 else res

    res = helper(x, abs(n))
    return res if n >= 0 else 1 / res

def main():
    result = my_pow(x = 2.00000, n = 10) # 1024.0
    print(result)
    result = my_pow(x = 2.10000, n = 3) # 9.26100
    print(result)
    result = my_pow(x = 2.00000, n = -2) # 0.25
    print(result)

if __name__ == "__main__":
    main()