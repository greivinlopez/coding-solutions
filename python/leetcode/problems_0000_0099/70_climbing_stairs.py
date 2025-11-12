# --------------------
# 70. Climbing Stairs
# --------------------

# Problem: https://leetcode.com/problems/climbing-stairs/
# 
# You are climbing a staircase. It takes n steps to reach the top.
# 
# Each time you can either climb 1 or 2 steps. In how many distinct ways can 
# you climb to the top?

# Solution: https://youtu.be/Y0lT9Fck7qI
# Credit: Navdeep Singh founder of NeetCode 
def climb_stairs(n):
    if n <= 3:
        return n
    n1, n2 = 2, 3

    for _ in range(4, n + 1):
        temp = n1 + n2
        n1 = n2
        n2 = temp
    return n2

# Solution: https://youtu.be/I-R1XsECJu8
# Credit: Greg Hogg
def climb_stairs_alt(n):
    # Time: O(n)
    # Space: O(1)
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    two_back = 1
    one_back = 2
    for i in range(2, n):
        next_num = two_back + one_back
        two_back = one_back
        one_back = next_num
    
    return one_back

# Credit: Greg Hogg
def climb_stairs_bottom_up(n):
    # Time: O(n)
    # Space: O(n)
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    dp = [0] * n
    dp[0] = 1
    dp[1] = 2

    for i in range(2, n):
        dp[i] = dp[i-2] + dp[i-1]
    
    return dp[n-1]

# Credit: Greg Hogg
def climb_stairs_memo(n):
    # Time: O(n)
    # Space: O(n)
    memo = {1:1, 2:2}
    def f(n):
        if n in memo:
            return memo[n]
        else:
            memo[n] = f(n-2) + f(n-1)
            return memo[n]
    
    return f(n)

def main():
    result = climb_stairs(2) 
    # Expected Output: 2
    print(result)
    result = climb_stairs(3)
    # Expected Output: 3
    print(result)

if __name__ == "__main__":
    main()