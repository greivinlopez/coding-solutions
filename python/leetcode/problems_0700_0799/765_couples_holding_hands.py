# --------------------------
# 765. Couples Holding Hands
# --------------------------

# Problem: https://leetcode.com/problems/couples-holding-hands
#
# There are n couples sitting in 2n seats arranged in a row and want to hold
# hands.
# 
# The people and seats are represented by an integer array row where row[i] is the
# ID of the person sitting in the iᵗʰ seat. The couples are numbered in order, the
# first couple being (0, 1), the second couple being (2, 3), and so on with the
# last couple being (2n - 2, 2n - 1).
# 
# Return the minimum number of swaps so that every couple is sitting side by side.
# A swap consists of choosing any two people, then they stand up and switch seats.
# 
# Example 1:
# 
# Input: row = [0,2,1,3]
# Output: 1
# 
# Explanation: We only need to swap the second (row[1]) and third (row[2]) person.
# 
# Example 2:
# 
# Input: row = [3,2,0,1]
# Output: 0
# 
# Explanation: All couples are already seated side by side.
# 
# 
# Constraints:
#         2n == row.length
#         2 <= n <= 30
#         n is even.
#         0 <= row[i] < 2n
#         All the elements of row are unique.


# Solution: https://algo.monster/liteproblems/765
# Credit: AlgoMonster
def min_swaps_couples(row):
    def find_root(node):
        if parent[node] != node:
            # Path compression: make every node point directly to root
            parent[node] = find_root(parent[node])
        return parent[node]
    
    # Calculate number of couples (each couple consists of 2 people)
    num_couples = len(row) // 2
    
    # Initialize parent array for Union-Find
    # Each couple initially forms its own set
    parent = list(range(num_couples))
    
    # Process each seat pair (positions 0-1, 2-3, 4-5, etc.)
    for seat_index in range(0, len(row), 2):
        # Get couple IDs for the two people sitting together
        # Person i belongs to couple i//2
        couple_a = row[seat_index] // 2
        couple_b = row[seat_index + 1] // 2
        
        # Union: Connect the two couples in the same component
        # If they're from different couples, they need to be swapped
        root_a = find_root(couple_a)
        root_b = find_root(couple_b)
        parent[root_a] = root_b
    
    # Count number of connected components
    # Each component requires (size - 1) swaps to fix
    num_components = sum(1 for couple_id in range(num_couples) 
                        if couple_id == find_root(couple_id))
    
    # Total swaps = total couples - number of components
    return num_couples - num_components
    # Time: O(n × α(n))
    # Space: O(n)
    # α(n) is the inverse Ackermann function used in the find operation


def main():
    result = min_swaps_couples(row = [0,2,1,3])
    print(result) # 1

    result = min_swaps_couples(row = [3,2,0,1])
    print(result) # 0

if __name__ == "__main__":
    main()
