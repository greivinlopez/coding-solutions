# ----------------------------------------------
# 967. Numbers With Same Consecutive Differences
# ----------------------------------------------

# Problem: https://leetcode.com/problems/numbers-with-same-consecutive-differences
#
# Given two integers n and k, return an array of all the integers of length n
# where the difference between every two consecutive digits is k. You may return
# the answer in any order.
# 
# Note that the integers should not have leading zeros. Integers as 02 and 043 are
# not allowed.
# 
# Example 1:
# 
# Input: n = 3, k = 7
# Output: [181,292,707,818,929]
# 
# Explanation: Note that 070 is not a valid number, because it has leading zeroes.
# 
# Example 2:
# 
# Input: n = 2, k = 1
# Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
# 
# 
# Constraints:
#         2 <= n <= 9
#         0 <= k <= 9


# Solution: https://algo.monster/liteproblems/967
# Credit: AlgoMonster
def nums_same_consec_diff(n, k):
    
    def dfs(current_number):
        # If we've reached n digits, add to result
        if current_number >= min_n_digit_value:
            result.append(current_number)
            return
        
        # Get the last digit of current number
        last_digit = current_number % 10
        
        # Try adding a digit that is k more than the last digit
        if last_digit + k <= 9:
            dfs(current_number * 10 + last_digit + k)
        
        # Try adding a digit that is k less than the last digit
        # Avoid duplicates when k=0
        if last_digit - k >= 0 and k != 0:
            dfs(current_number * 10 + last_digit - k)
    
    # Initialize result list
    result = []
    
    # Calculate the minimum n-digit number (e.g., 100 for n=3)
    min_n_digit_value = 10 ** (n - 1)
    
    # Start DFS from each digit 1-9 (no leading zeros)
    for starting_digit in range(1, 10):
        dfs(starting_digit)
    
    return result
    # Time: O(n * 2ⁿ)
    # Space: O(2ⁿ)

# Alternative Solution
# Solution: https://leetcodethehardway.com/solutions/0900-0999/numbers-with-same-consecutive-differences-medium
# Credit: LeetCode The Hard Way -> https://leetcodethehardway.com/
def nums_same_consec_diff_alt(n, k):
    from collections import deque

    # init ans
    ans = []
    # push all numbers with single digit to a deque
    # (1, d) : (current position, number)
    d = deque((1, d) for d in range(1, 10))

    # while the queue is not empty
    while d:
        # pop the first element from the deque
        pos, num = d.pop()
        # if the current position is n,
        if pos == n:
            # then we can append num to ans
            ans.append(num)
        else:
            # otherwise, we can iterate 0 to 9
            for j in range(10):
                # and use num % 10 to get the last digit of num
                # then get the difference with j
                # since (num % 10) - j can be negative and positive
                # we use abs to cover both case
                if abs(num % 10 - j) == k:
                    # if the difference is equal to k
                    # we can include digit j
                    # so multiply the current number by 10 and add j
                    d.append((pos + 1, num * 10 + j))
    # return the final ans
    return ans
    # Time: O(2ⁿ)
    # Space: O(2ⁿ)


def main():
    result = nums_same_consec_diff(n = 3, k = 7)
    print(result) # [181, 292, 707, 818, 929]

    result = nums_same_consec_diff(n = 2, k = 1)
    print(result) # [12, 10, 23, 21, 34, 32, 45, 43, 56, 54, 67, 65, 78, 76, 89, 87, 98]

if __name__ == "__main__":
    main()
