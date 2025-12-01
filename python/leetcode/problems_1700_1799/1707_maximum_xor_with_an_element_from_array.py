# --------------------------------------------
# 1707. Maximum XOR With an Element From Array
# --------------------------------------------

# Problem: https://leetcode.com/problems/maximum-xor-with-an-element-from-array
#
# You are given an array nums consisting of non-negative integers. You are also
# given a queries array, where queries[i] = [xᵢ, mᵢ].
# 
# The answer to the iᵗʰ query is the maximum bitwise XOR value of xᵢ and any
# element of nums that does not exceed mᵢ. In other words, the answer is
# max(nums[j] XOR xᵢ) for all j such that nums[j] <= mᵢ. If all elements in nums
# are larger than mᵢ, then the answer is -1.
# 
# Return an integer array answer where answer.length == queries.length and
# answer[i] is the answer to the iᵗʰ query.
# 
# Example 1:
# 
# Input: nums = [0,1,2,3,4], queries = [[3,1],[1,3],[5,6]]
# Output: [3,3,7]
# 
# Explanation:
# 1) 0 and 1 are the only two integers not greater than 1. 0 XOR 3 = 3 and 1 XOR 3
# = 2. The larger of the two is 3.
# 2) 1 XOR 2 = 3.
# 3) 5 XOR 2 = 7.
# 
# Example 2:
# 
# Input: nums = [5,2,4,6,6,3], queries = [[12,4],[8,1],[6,3]]
# Output: [15,-1,5]
# 
# 
# Constraints:
#         1 <= nums.length, queries.length <= 10⁵
#         queries[i].length == 2
#         0 <= nums[j], xi, mi <= 10⁹


# Solution: https://algo.monster/liteproblems/1707
# Credit: AlgoMonster
def maximize_xor(nums, queries):
    trie = Trie()
    nums.sort()  # Sort nums to process them in ascending order
    
    num_index = 0
    num_queries = len(queries)
    result = [-1] * num_queries
    
    # Process queries in ascending order of their limits (mi)
    # Enumerate queries with their original indices to maintain result order
    sorted_queries = sorted(enumerate(queries), key=lambda item: item[1][1])
    
    for original_index, (xi, mi) in sorted_queries:
        # Insert all numbers <= mi into the trie
        while num_index < len(nums) and nums[num_index] <= mi:
            trie.insert(nums[num_index])
            num_index += 1
        
        # Find maximum XOR with xi among inserted numbers
        result[original_index] = trie.search(xi)
        
    return result
    # Time: O(n * log n + q * log q)
    # Space: O(n + q)
    # n = the length of nums array
    # q = the length of queries array.


class Trie:
    """Binary trie to store numbers and find maximum XOR"""
    __slots__ = ["children"]

    def __init__(self):
        # Each node has two children: 0 and 1
        self.children = [None] * 2

    def insert(self, x: int) -> None:
        """Insert a number into the trie by its binary representation"""
        node = self
        # Process bits from most significant to least significant (30th to 0th bit)
        for i in range(30, -1, -1):
            # Extract the i-th bit of x
            bit = (x >> i) & 1
            # Create new node if path doesn't exist
            if node.children[bit] is None:
                node.children[bit] = Trie()
            # Move to the next node
            node = node.children[bit]

    def search(self, x: int) -> int:
        """Find the maximum XOR value with x among all inserted numbers"""
        node = self
        max_xor = 0
      
        # Process bits from most significant to least significant
        for i in range(30, -1, -1):
            # Extract the i-th bit of x
            bit = (x >> i) & 1
            # Try to go opposite direction for maximum XOR
            toggled_bit = bit ^ 1
          
            if node.children[toggled_bit]:
                # If opposite bit exists, add this bit position to result
                max_xor |= (1 << i)
                node = node.children[toggled_bit]
            elif node.children[bit]:
                # If only same bit exists, follow that path
                node = node.children[bit]
            else:
                # No valid path exists (trie is empty at this point)
                return -1
              
        return max_xor


def main():
    result = maximize_xor(nums = [0,1,2,3,4], queries = [[3,1],[1,3],[5,6]])
    print(result) # [3, 3, 7]

    result = maximize_xor(nums = [5,2,4,6,6,3], queries = [[12,4],[8,1],[6,3]])
    print(result) # [15, -1, 5]

if __name__ == "__main__":
    main()
