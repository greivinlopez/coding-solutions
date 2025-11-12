# ---------------------------
# 517. Super Washing Machines
# ---------------------------

# Problem: https://leetcode.com/problems/super-washing-machines
#
# You have n super washing machines on a line. Initially, each washing machine has
# some dresses or is empty.
# 
# For each move, you could choose any m (1 <= m <= n) washing machines, and pass
# one dress of each washing machine to one of its adjacent washing machines at the
# same time.
# 
# Given an integer array machines representing the number of dresses in each
# washing machine from left to right on the line, return the minimum number of
# moves to make all the washing machines have the same number of dresses. If it is
# not possible to do it, return -1.
# 
# Example 1:
# 
# Input: machines = [1,0,5]
# Output: 3
# 
# Explanation:
# 1st move:    1     0 <-- 5    =>    1     1     4
# 2nd move:    1 <-- 1 <-- 4    =>    2     1     3
# 3rd move:    2     1 <-- 3    =>    2     2     2
# 
# Example 2:
# 
# Input: machines = [0,3,0]
# Output: 2
# 
# Explanation:
# 1st move:    0 <-- 3     0    =>    1     2     0
# 2nd move:    1     2 --> 0    =>    1     1     1
# 
# Example 3:
# 
# Input: machines = [0,2,0]
# Output: -1
# 
# Explanation:
# It's impossible to make all three washing machines have the same number of
# dresses.
# 
# 
# Constraints:
#         n == machines.length
#         1 <= n <= 10⁴
#         0 <= machines[i] <= 10⁵


# Solution: https://algo.monster/liteproblems/517
# Credit: AlgoMonster
def find_min_moves(machines):
    # Get the number of machines
    n = len(machines)
    
    # Calculate the target number of dresses per machine
    total_dresses = sum(machines)
    target_per_machine, remainder = divmod(total_dresses, n)
    
    # If dresses cannot be evenly distributed, return -1
    if remainder:
        return -1
    
    # Track the maximum moves needed
    max_moves = 0
    # Track the cumulative excess/deficit as we traverse machines
    cumulative_balance = 0
    
    # Process each machine
    for current_dresses in machines:
        # Calculate excess/deficit for this machine
        excess = current_dresses - target_per_machine
        
        # Update cumulative balance (net flow through boundaries)
        cumulative_balance += excess
        
        # The answer is the maximum of:
        # 1. abs(cumulative_balance): max flow through any boundary
        # 2. excess: max dresses a single machine needs to give away
        max_moves = max(max_moves, abs(cumulative_balance), excess)
    
    return max_moves
    # Time: O(n)
    # Space: O(1)


def main():
    result = find_min_moves(machines = [1,0,5])
    print(result) # 3

    result = find_min_moves(machines = [0,3,0])
    print(result) # 2

    result = find_min_moves(machines = [0,2,0])
    print(result) # -1

if __name__ == "__main__":
    main()
