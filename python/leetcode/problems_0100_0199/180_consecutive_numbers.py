# ------------------------
# 180. Consecutive Numbers
# ------------------------

# Problem: https://leetcode.com/problems/consecutive-numbers
#
# Table: Logs
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | id          | int     |
# | num         | varchar |
# +-------------+---------+
# In SQL, id is the primary key for this table.
# id is an autoincrement column starting from 1.
# Find all numbers that appear at least three times consecutively.
# Return the result table in any order.
# The result format is in the following example.
# Example 1:
# Input:
# Logs table:
# +----+-----+
# | id | num |
# +----+-----+
# | 1  | 1   |
# | 2  | 1   |
# | 3  | 1   |
# | 4  | 2   |
# | 5  | 1   |
# | 6  | 2   |
# | 7  | 2   |
# +----+-----+
# Output:
# +-----------------+
# | ConsecutiveNums |
# +-----------------+
# | 1               |
# +-----------------+
# Explanation: 1 is the only number that appears consecutively for at least three
# times.


# Solution: 
# Credit: Navdeep Singh founder of NeetCode


# Solution: 
# Credit: Greg Hogg


def main():
    result = word_break(params)
    print(result) # True

    result = word_break(params)
    print(result) # True

    result = word_break(params)
    print(result) # False

if __name__ == "__main__":
    main()
