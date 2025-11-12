# -------------------------------------------------------------
# 1491. Average Salary Excluding the Minimum and Maximum Salary
# -------------------------------------------------------------

# Problem: https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary
#
# You are given an array of unique integers salary where salary[i] is the salary
# of the iᵗʰ employee.
# 
# Return the average salary of employees excluding the minimum and maximum salary.
# Answers within 10⁻⁵ of the actual answer will be accepted.
# 
# Example 1:
# 
# Input: salary = [4000,3000,1000,2000]
# Output: 2500.00000
# 
# Explanation: Minimum salary and maximum salary are 1000 and 4000 respectively.
# Average salary excluding minimum and maximum salary is (2000+3000) / 2 = 2500
# 
# Example 2:
# 
# Input: salary = [1000,2000,3000]
# Output: 2000.00000
# 
# Explanation: Minimum salary and maximum salary are 1000 and 3000 respectively.
# Average salary excluding minimum and maximum salary is (2000) / 1 = 2000
# 
# 
# Constraints:
#         3 <= salary.length <= 100
#         1000 <= salary[i] <= 10⁶
#         All the integers of salary are unique.


# Solution: https://algo.monster/liteproblems/1491
# Credit: AlgoMonster
def average(salary):
    # Calculate the total sum and subtract both the minimum and maximum values
    total_sum = sum(salary) - min(salary) - max(salary)
    
    # Divide by the count of remaining elements (total count minus 2)
    average_salary = total_sum / (len(salary) - 2)
    
    return average_salary
    # Time: O(n)
    # Space: O(1)


def main():
    result = average(salary = [4000,3000,1000,2000])
    print(result) # 2500.0

    result = average(salary = [1000,2000,3000])
    print(result) # 2000.0

if __name__ == "__main__":
    main()
