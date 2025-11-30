# -----------------------------------------------
# 1665. Minimum Initial Energy to Finish Tasks 🔋
# -----------------------------------------------

# Problem: https://leetcode.com/problems/minimum-initial-energy-to-finish-tasks
#
# You are given an array tasks where tasks[i] = [actualᵢ, minimumᵢ]:
#         
#   * actualᵢ is the actual amount of energy you spend to finish the iᵗʰ task.
#   * minimumᵢ is the minimum amount of energy you require to begin the iᵗʰ task.
# 
# For example, if the task is [10, 12] and your current energy is 11, you cannot
# start this task. However, if your current energy is 13, you can complete this
# task, and your energy will be 3 after finishing it.
# 
# You can finish the tasks in any order you like.
# 
# Return the minimum initial amount of energy you will need to finish all the
# tasks.
# 
# Example 1:
# 
# Input: tasks = [[1,2],[2,4],[4,8]]
# Output: 8
# 
# Explanation:
# Starting with 8 energy, we finish the tasks in the following order:
#     - 3rd task. Now energy = 8 - 4 = 4.
#     - 2nd task. Now energy = 4 - 2 = 2.
#     - 1st task. Now energy = 2 - 1 = 1.
# Notice that even though we have leftover energy, starting with 7 energy does not
# work because we cannot do the 3rd task.
# 
# Example 2:
# 
# Input: tasks = [[1,3],[2,4],[10,11],[10,12],[8,9]]
# Output: 32
# 
# Explanation:
# Starting with 32 energy, we finish the tasks in the following order:
#     - 1st task. Now energy = 32 - 1 = 31.
#     - 2nd task. Now energy = 31 - 2 = 29.
#     - 3rd task. Now energy = 29 - 10 = 19.
#     - 4th task. Now energy = 19 - 10 = 9.
#     - 5th task. Now energy = 9 - 8 = 1.
# 
# Example 3:
# 
# Input: tasks = [[1,7],[2,8],[3,9],[4,10],[5,11],[6,12]]
# Output: 27
# 
# Explanation:
# Starting with 27 energy, we finish the tasks in the following order:
#     - 5th task. Now energy = 27 - 5 = 22.
#     - 2nd task. Now energy = 22 - 2 = 20.
#     - 3rd task. Now energy = 20 - 3 = 17.
#     - 1st task. Now energy = 17 - 1 = 16.
#     - 4th task. Now energy = 16 - 4 = 12.
#     - 6th task. Now energy = 12 - 6 = 6.
# 
# 
# Constraints:
#         1 <= tasks.length <= 10⁵
#         1 <= actual​ᵢ <= minimumᵢ <= 10⁴


# Solution: https://algo.monster/liteproblems/1665
# Credit: AlgoMonster
def minimum_effort(tasks):
    # Sort tasks by the difference (actual - minimum) in ascending order
    # This ensures we handle tasks with larger "extra" requirements first
    sorted_tasks = sorted(tasks, key=lambda task: task[0] - task[1])
    
    total_initial_effort = 0  # Total initial effort needed
    current_energy = 0  # Current available energy
    
    # Process each task in the sorted order
    for actual_effort, minimum_effort in sorted_tasks:
        # If current energy is less than minimum required to start this task
        if current_energy < minimum_effort:
            # Add the deficit to our total initial effort
            effort_deficit = minimum_effort - current_energy
            total_initial_effort += effort_deficit
            # Update current energy to the minimum required
            current_energy = minimum_effort
        
        # Consume the actual effort for this task
        current_energy -= actual_effort
    
    return total_initial_effort
    # Time: O(n × log n)
    # Space: O(n)


def main():
    result = minimum_effort(tasks = [[1,2],[2,4],[4,8]])
    print(result) # 8

    result = minimum_effort(tasks = [[1,3],[2,4],[10,11],[10,12],[8,9]])
    print(result) # 32

    result = minimum_effort(tasks = [[1,7],[2,8],[3,9],[4,10],[5,11],[6,12]])
    print(result) # 27

if __name__ == "__main__":
    main()
