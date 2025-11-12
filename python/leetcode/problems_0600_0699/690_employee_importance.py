# ------------------------
# 690. Employee Importance
# ------------------------

# Problem: https://leetcode.com/problems/employee-importance
#
# You have a data structure of employee information, including the employee's
# unique ID, importance value, and direct subordinates' IDs.
# 
# You are given an array of employees employees where:
# 
#         employees[i].id is the ID of the iᵗʰ employee.
#         employees[i].importance is the importance value of the iᵗʰ employee.
#         employees[i].subordinates is a list of the IDs of the direct
#         subordinates of the iᵗʰ employee.
# 
# Given an integer id that represents an employee's ID, return the total
# importance value of this employee and all their direct and indirect
# subordinates.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2021/05/31/emp1-tree.jpg
# 
# Input: employees = [[1,5,[2,3]],[2,3,[]],[3,3,[]]], id = 1
# Output: 11
# 
# Explanation: Employee 1 has an importance value of 5 and has two direct
# subordinates: employee 2 and employee 3.
# They both have an importance value of 3.
# Thus, the total importance value of employee 1 is 5 + 3 + 3 = 11.
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2021/05/31/emp2-tree.jpg
# 
# Input: employees = [[1,2,[5]],[5,-3,[]]], id = 5
# Output: -3
# 
# Explanation: Employee 5 has an importance value of -3 and has no direct
# subordinates.
# Thus, the total importance value of employee 5 is -3.
# 
# 
# Constraints:
#         1 <= employees.length <= 2000
#         1 <= employees[i].id <= 2000
#         All employees[i].id are unique.
#         -100 <= employees[i].importance <= 100
#         One employee has at most one direct leader and may have several
# subordinates.
#         The IDs in employees[i].subordinates are valid IDs.


# Solution: https://algo.monster/liteproblems/690
# Credit: AlgoMonster
def get_importance(employees, id):

    def calculate_total_importance(employee_id):
        # Get the employee object from the map
        employee = employee_map[employee_id]
        
        # Calculate total: employee's importance + sum of all subordinates' importance
        subordinates_importance = sum(
            calculate_total_importance(subordinate_id) 
            for subordinate_id in employee.subordinates
        )
        
        return employee.importance + subordinates_importance
    
    # Create a map for O(1) employee lookup by ID
    employee_map = {employee.id: employee for employee in employees}
    
    # Start DFS from the given employee ID
    return calculate_total_importance(id)
    # Time: O(n)
    # Space: O(n)


def main():
    print("TO DO")

if __name__ == "__main__":
    main()
