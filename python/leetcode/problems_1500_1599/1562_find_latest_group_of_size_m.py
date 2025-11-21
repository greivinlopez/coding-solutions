# ---------------------------------
# 1562. Find Latest Group of Size M
# ---------------------------------

# Problem: https://leetcode.com/problems/find-latest-group-of-size-m
#
# Given an array arr that represents a permutation of numbers from 1 to n.
# 
# You have a binary string of size n that initially has all its bits set to zero.
# At each step i (assuming both the binary string and arr are 1-indexed) from 1 to
# n, the bit at position arr[i] is set to 1.
# 
# You are also given an integer m. Find the latest step at which there exists a
# group of ones of length m. A group of ones is a contiguous substring of 1's such
# that it cannot be extended in either direction.
# 
# Return the latest step at which there exists a group of ones of length exactly
# m. If no such group exists, return -1.
# 
# Example 1:
# 
# Input: arr = [3,5,1,2,4], m = 1
# Output: 4
# 
# Explanation:
# Step 1: "00100", groups: ["1"]
# Step 2: "00101", groups: ["1", "1"]
# Step 3: "10101", groups: ["1", "1", "1"]
# Step 4: "11101", groups: ["111", "1"]
# Step 5: "11111", groups: ["11111"]
# The latest step at which there exists a group of size 1 is step 4.
# 
# Example 2:
# 
# Input: arr = [3,1,5,4,2], m = 2
# Output: -1
# 
# Explanation:
# Step 1: "00100", groups: ["1"]
# Step 2: "10100", groups: ["1", "1"]
# Step 3: "10101", groups: ["1", "1", "1"]
# Step 4: "10111", groups: ["1", "111"]
# Step 5: "11111", groups: ["11111"]
# No group of size 2 exists during any step.
# 
# 
# Constraints:
#         n == arr.length
#         1 <= m <= n <= 10⁵
#         1 <= arr[i] <= n
#         All integers in arr are distinct.


# Solution: https://algo.monster/liteproblems/1562
# Credit: AlgoMonster
def find_latest_step(arr, m):
    
    def find_root(node):
        if parent[node] != node:
            # Path compression: make every node point directly to root
            parent[node] = find_root(parent[node])
        return parent[node]
    
    def union_sets(node_a, node_b):
        root_a = find_root(node_a)
        root_b = find_root(node_b)
        
        # Already in the same set
        if root_a == root_b:
            return
        
        # Connect root_a to root_b and update size
        parent[root_a] = root_b
        component_size[root_b] += component_size[root_a]
    
    n = len(arr)
    
    # Special case: if m equals n, the last step creates the only group of size n
    if m == n:
        return n
    
    # Initialize data structures
    is_flipped = [False] * n  # Track which positions have been flipped to 1
    parent = list(range(n))   # Parent array for Union-Find (each node is its own parent initially)
    component_size = [1] * n   # Size of component rooted at each node
    latest_step = -1          # Answer: latest step where size m group exists
    
    # Process each step
    for step_index, position in enumerate(arr):
        # Convert to 0-indexed position
        current_pos = position - 1
        
        # Check left neighbor
        if current_pos > 0 and is_flipped[current_pos - 1]:
            # Before merging, check if left component has size m
            if component_size[find_root(current_pos - 1)] == m:
                latest_step = step_index
            # Merge with left neighbor
            union_sets(current_pos, current_pos - 1)
        
        # Check right neighbor
        if current_pos < n - 1 and is_flipped[current_pos + 1]:
            # Before merging, check if right component has size m
            if component_size[find_root(current_pos + 1)] == m:
                latest_step = step_index
            # Merge with right neighbor
            union_sets(current_pos, current_pos + 1)
        
        # Mark current position as flipped
        is_flipped[current_pos] = True
    
    return latest_step
    # Time: O(n)
    # Space: O(n)


def main():
    result = find_latest_step(arr = [3,5,1,2,4], m = 1)
    print(result) # 4

    result = find_latest_step(arr = [3,1,5,4,2], m = 2)
    print(result) # -1

if __name__ == "__main__":
    main()
