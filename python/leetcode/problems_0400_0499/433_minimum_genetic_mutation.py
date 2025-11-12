# -----------------------------
# 433. Minimum Genetic Mutation
# -----------------------------

# Problem: https://leetcode.com/problems/minimum-genetic-mutation
#
# A gene string can be represented by an 8-character long string, with choices
# from 'A', 'C', 'G', and 'T'.
# 
# Suppose we need to investigate a mutation from a gene string startGene to a gene
# string endGene where one mutation is defined as one single character changed in
# the gene string.
# 
#   * For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
# 
# There is also a gene bank bank that records all the valid gene mutations. A gene
# must be in bank to make it a valid gene string.
# 
# Given the two gene strings startGene and endGene and the gene bank bank, return
# the minimum number of mutations needed to mutate from startGene to endGene. If
# there is no such a mutation, return -1.
# 
# Note that the starting point is assumed to be valid, so it might not be included
# in the bank.
# 
# Example 1:
# 
# Input: startGene = "AACCGGTT", endGene = "AACCGGTA", bank = ["AACCGGTA"]
# Output: 1
# 
# Example 2:
# 
# Input: startGene = "AACCGGTT", endGene = "AAACGGTA", bank =
# ["AACCGGTA","AACCGCTA","AAACGGTA"]
# Output: 2
# 
# Constraints:
#   0 <= bank.length <= 10
#   startGene.length == endGene.length == bank[i].length == 8
#   startGene, endGene, and bank[i] consist of only the characters ['A','C','G','T'].

from collections import deque

# Solution: https://algo.monster/liteproblems/433
# Credit: AlgoMonster
def min_mutation(startGene, endGene, bank):
    # Initialize BFS queue with starting gene and depth 0
    queue = deque([(startGene, 0)])
    
    # Keep track of visited genes to avoid cycles
    visited = {startGene}
    
    # Perform BFS to find shortest path
    while queue:
        current_gene, current_depth = queue.popleft()
        
        # Check if we've reached the target gene
        if current_gene == endGene:
            return current_depth
        
        # Try all possible next mutations from the bank
        for next_gene in bank:
            # Count the number of character differences
            difference_count = sum(
                char1 != char2 
                for char1, char2 in zip(current_gene, next_gene)
            )
            
            # If exactly one character differs and we haven't visited this gene
            if difference_count == 1 and next_gene not in visited:
                queue.append((next_gene, current_depth + 1))
                visited.add(next_gene)
    
    # No valid mutation path found
    return -1


def main():
    result = min_mutation(startGene = "AACCGGTT", endGene = "AACCGGTA", bank = ["AACCGGTA"])
    print(result) # 1

    result = min_mutation(startGene = "AACCGGTT", endGene = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"])
    print(result) # 2

if __name__ == "__main__":
    main()
