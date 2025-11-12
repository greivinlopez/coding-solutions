# ------------------
# 851. Loud and Rich
# ------------------

# Problem: https://leetcode.com/problems/loud-and-rich
#
# There is a group of n people labeled from 0 to n - 1 where each person has a
# different amount of money and a different level of quietness.
# 
# You are given an array richer where richer[i] = [aᵢ, bᵢ] indicates that aᵢ has
# more money than bᵢ and an integer array quiet where quiet[i] is the quietness of
# the iᵗʰ person. All the given data in richer are logically correct (i.e., the
# data will not lead you to a situation where x is richer than y and y is richer
# than x at the same time).
# 
# Return an integer array answer where answer[x] = y if y is the least quiet
# person (that is, the person y with the smallest value of quiet[y]) among all
# people who definitely have equal to or more money than the person x.
# 
# Example 1:
# 
# Input: richer = [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]], quiet =
# [3,2,5,4,6,1,7,0]
# Output: [5,5,2,5,4,5,6,7]
# 
# Explanation:
# answer[0] = 5.
# Person 5 has more money than 3, which has more money than 1, which has more
# money than 0.
# The only person who is quieter (has lower quiet[x]) is person 7, but it is not
# clear if they have more money than person 0.
# answer[7] = 7.
# Among all people that definitely have equal to or more money than person 7
# (which could be persons 3, 4, 5, 6, or 7), the person who is the quietest (has
# lower quiet[x]) is person 7.
# The other answers can be filled out with similar reasoning.
# 
# Example 2:
# 
# Input: richer = [], quiet = [0]
# Output: [0]
# 
# Constraints:
#         n == quiet.length
#         1 <= n <= 500
#         0 <= quiet[i] < n
#         All the values of quiet are unique.
#         0 <= richer.length <= n * (n - 1) / 2
#         0 <= aᵢ, bᵢ < n
#         aᵢ != bᵢ
#         All the pairs of richer are unique.
#         The observations in richer are all logically consistent.

from collections import defaultdict

# Solution: https://algo.monster/liteproblems/851
# Credit: AlgoMonster
def loud_and_rich(richer, quiet):  
    def dfs(person):
        # If already computed, return early (memoization)
        if result[person] != -1:
            return
        
        # Initially, the person themselves is the quietest they know
        result[person] = person
        
        # Check all people who are richer than the current person
        for richer_person in graph[person]:
            # Recursively compute the answer for the richer person
            dfs(richer_person)
            
            # Update if we found someone quieter through the richer person's connections
            if quiet[result[richer_person]] < quiet[result[person]]:
                result[person] = result[richer_person]
    
    # Build adjacency list: graph[person] contains all people richer than person
    graph = defaultdict(list)
    for richer_person, poorer_person in richer:
        graph[poorer_person].append(richer_person)
    
    # Initialize result array with -1 (unprocessed marker)
    num_people = len(quiet)
    result = [-1] * num_people
    
    # Process each person to find their quietest richer person
    for person in range(num_people):
        dfs(person)
    
    return result
    # Time: O(n + m)
    # Space: O(n + m)
    # n = the number of people
    # m = is the number of relationships in the richer array.


def main():
    result = loud_and_rich(richer = [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]], quiet = [3,2,5,4,6,1,7,0])
    print(result) # [5,5,2,5,4,5,6,7]

    result = loud_and_rich(richer = [], quiet = [0])
    print(result) # [0]

if __name__ == "__main__":
    main()
