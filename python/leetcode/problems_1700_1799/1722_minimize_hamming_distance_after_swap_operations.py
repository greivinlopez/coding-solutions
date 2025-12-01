# -----------------------------------------------------
# 1722. Minimize Hamming Distance After Swap Operations
# -----------------------------------------------------

# Problem: https://leetcode.com/problems/minimize-hamming-distance-after-swap-operations
#
# You are given two integer arrays, source and target, both of length n. You are
# also given an array allowedSwaps where each allowedSwaps[i] = [aᵢ, bᵢ] indicates
# that you are allowed to swap the elements at index aᵢ and index bᵢ (0-indexed)
# of array source. Note that you can swap elements at a specific pair of indices
# multiple times and in any order.
# 
# The Hamming distance of two arrays of the same length, source and target, is the
# number of positions where the elements are different. Formally, it is the number
# of indices i for 0 <= i <= n-1 where source[i] != target[i] (0-indexed).
# 
# Return the minimum Hamming distance of source and target after performing any
# amount of swap operations on array source.
# 
# Example 1:
# 
# Input: source = [1,2,3,4], target = [2,1,4,5], allowedSwaps = [[0,1],[2,3]]
# Output: 1
# 
# Explanation: source can be transformed the following way:
# - Swap indices 0 and 1: source = [2,1,3,4]
# - Swap indices 2 and 3: source = [2,1,4,3]
# The Hamming distance of source and target is 1 as they differ in 1 position:
# index 3.
# 
# Example 2:
# 
# Input: source = [1,2,3,4], target = [1,3,2,4], allowedSwaps = []
# Output: 2
# 
# Explanation: There are no allowed swaps.
# The Hamming distance of source and target is 2 as they differ in 2 positions:
# index 1 and index 2.
# 
# Example 3:
# 
# Input: source = [5,1,2,4,3], target = [1,5,4,2,3], allowedSwaps =
# [[0,4],[4,2],[1,3],[1,4]]
# Output: 0
# 
# 
# Constraints:
#         n == source.length == target.length
#         1 <= n <= 105
#         1 <= source[i], target[i] <= 105
#         0 <= allowedSwaps.length <= 105
#         allowedSwaps[i].length == 2
#         0 <= aᵢ, bᵢ <= n - 1
#         aᵢ != bᵢ


# Solution: https://algo.monster/liteproblems/1722
# Credit: AlgoMonster
def minimum_hamming_distance(source, target, allowedSwaps):
    from collections import defaultdict, Counter

    def find_root(index):
        if parent[index] != index:
            # Path compression: directly connect to root
            parent[index] = find_root(parent[index])
        return parent[index]
    
    # Initialize Union-Find structure
    array_length = len(source)
    parent = list(range(array_length))  # Each element is initially its own parent
    
    # Union operation: Connect all swappable indices into groups
    for index_a, index_b in allowedSwaps:
        # Connect the two indices by making them share the same root
        parent[find_root(index_a)] = find_root(index_b)
    
    # Count frequency of values in each connected component for source array
    component_value_counts = defaultdict(Counter)
    for index, value in enumerate(source):
        root = find_root(index)
        component_value_counts[root][value] += 1
    
    # Calculate minimum Hamming distance
    hamming_distance = 0
    for index, value in enumerate(target):
        root = find_root(index)
        # Decrement the count of this value in its component
        component_value_counts[root][value] -= 1
        # If count goes negative, this position contributes to Hamming distance
        if component_value_counts[root][value] < 0:
            hamming_distance += 1
    
    return hamming_distance
    # Time: O(n × α(n))
    # Space: O(n)


def main():
    result = minimum_hamming_distance(source = [1,2,3,4], target = [2,1,4,5], allowedSwaps = [[0,1],[2,3]])
    print(result) # 1

    result = minimum_hamming_distance(source = [1,2,3,4], target = [1,3,2,4], allowedSwaps = [])
    print(result) # 2

    result = minimum_hamming_distance(source = [5,1,2,4,3], target = [1,5,4,2,3], allowedSwaps = [[0,4],[4,2],[1,3],[1,4]])
    print(result) # 0

if __name__ == "__main__":
    main()
