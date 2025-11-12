# ------------------------------
# 957. Prison Cells After N Days
# ------------------------------

# Problem: https://leetcode.com/problems/prison-cells-after-n-days
#
# There are 8 prison cells in a row and each cell is either occupied or vacant.
# 
# Each day, whether the cell is occupied or vacant changes according to the
# following rules:
#         
#   * If a cell has two adjacent neighbors that are both occupied or both
#     vacant, then the cell becomes occupied.
#   * Otherwise, it becomes vacant.
# 
# Note that because the prison is a row, the first and the last cells in the row
# can't have two adjacent neighbors.
# 
# You are given an integer array cells where cells[i] == 1 if the iᵗʰ cell is
# occupied and cells[i] == 0 if the iᵗʰ cell is vacant, and you are given an
# integer n.
# 
# Return the state of the prison after n days (i.e., n such changes described
# above).
# 
# Example 1:
# 
# Input: cells = [0,1,0,1,1,0,0,1], n = 7
# Output: [0,0,1,1,0,0,0,0]
# 
# Explanation: The following table summarizes the state of the prison on each day:
# Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
# Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
# Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
# Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
# Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
# Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
# Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
# Day 7: [0, 0, 1, 1, 0, 0, 0, 0]
# 
# Example 2:
# 
# Input: cells = [1,0,0,1,0,0,1,0], n = 1000000000
# Output: [0,0,1,1,1,1,1,0]
# 
# 
# Constraints:
#         cells.length == 8
#         cells[i] is either 0 or 1.
#         1 <= n <= 10⁹


# Solution: https://leetcode.com/problems/prison-cells-after-n-days/solutions/411559/python-general-solution-beats-83-26-w-commentary
# Credit: 宇祥 黃 -> https://leetcode.com/u/jadore801120/
def prison_after_n_days(cells, n):
    cells = tuple(cells)  # For hash-able
    c2d = {}              # Cells to date mapping
    states = []           # Sequentially record the cell states everyday
    day = 0               # Day counter
    
    while cells not in c2d:
        if day == n:
            return cells
            
        states += [cells]
        c2d[cells] = day
        
        # Calculate the next state of cells 
        cells = tuple([0]+[1 if cells[i-1] == cells[i+1] else 0 for i in range(1,len(cells)-1)]+[0])
        day += 1
    
    loopStartDate = c2d[cells]          # Get the offset to repeating part
    loopLength = day - loopStartDate    # Get the cycle length
    return states[loopStartDate + (n - loopStartDate) % loopLength]
    # Time: O(2ᵐ)
    # Space: O(2ᵐ * m)
    # m = the length of the cells array.


def main():
    result = prison_after_n_days(cells = [0,1,0,1,1,0,0,1], n = 7)
    print(result) # (0, 0, 1, 1, 0, 0, 0, 0)

    result = prison_after_n_days(cells = [1,0,0,1,0,0,1,0], n = 1000000000)
    print(result) # (0, 0, 1, 1, 1, 1, 1, 0)

if __name__ == "__main__":
    main()
