# ----------------------
# 753. Cracking the Safe
# ----------------------

# Problem: https://leetcode.com/problems/cracking-the-safe
#
# There is a safe protected by a password. The password is a sequence of n digits
# where each digit can be in the range [0, k - 1].
# 
# The safe has a peculiar way of checking the password. When you enter in a
# sequence, it checks the most recent n digits that were entered each time you
# type a digit.
#         
#   * For example, the correct password is "345" and you enter in "012345":        
#       * After typing 0, the most recent 3 digits is "0", which is incorrect.
#       * After typing 1, the most recent 3 digits is "01", which is incorrect.
#       * After typing 2, the most recent 3 digits is "012", which is incorrect.
#       * After typing 3, the most recent 3 digits is "123", which is incorrect.
#       * After typing 4, the most recent 3 digits is "234", which is incorrect.
#       * After typing 5, the most recent 3 digits is "345", which is correct 
#         and the safe unlocks.
# 
# Return any string of minimum length that will unlock the safe at some point of
# entering it.
# 
# Example 1:
# 
# Input: n = 1, k = 2
# Output: "10"
# 
# Explanation: The password is a single digit, so enter each digit. "01" would
# also unlock the safe.
# 
# Example 2:
# 
# Input: n = 2, k = 2
# Output: "01100"
# 
# Explanation: For each possible password:
# - "00" is typed in starting from the 4th digit.
# - "01" is typed in starting from the 1st digit.
# - "10" is typed in starting from the 3rd digit.
# - "11" is typed in starting from the 2nd digit.
# Thus "01100" will unlock the safe. "10011", and "11001" would also unlock the
# safe.
# 
# 
# Constraints:
#         1 <= n <= 4
#         1 <= k <= 10
#         1 <= kⁿ <= 4096


# Solution: https://algo.monster/liteproblems/753
# Credit: AlgoMonster
def crack_safe(n, k):
    def dfs(current_node: int) -> None:
        # Try all possible digits to append
        for digit in range(k):
            # Create an edge by appending the digit to current node
            # Edge represents an n-digit combination
            edge = current_node * 10 + digit
            
            # Check if this edge has been visited
            if edge not in visited_edges:
                visited_edges.add(edge)
                
                # Calculate the next node by removing the leftmost digit
                # This creates an (n-1)-digit node for the next iteration
                next_node = edge % modulo
                
                # Recursively visit the next node
                dfs(next_node)
                
                # Append the digit to result after visiting all edges from next_node
                # (Hierholzer's algorithm: build path in reverse)
                result.append(str(digit))
    
    # Calculate modulo for extracting last (n-1) digits
    modulo = 10 ** (n - 1)
    
    # Set to track visited edges (n-digit combinations)
    visited_edges = set()
    
    # List to store the result digits in reverse order
    result = []
    
    # Start DFS from node 0 (representing "00...0" with n-1 zeros)
    dfs(0)
    
    # Append the initial (n-1) zeros for the starting node
    result.append("0" * (n - 1))
    
    # Join the result list to form the final string
    return "".join(result)
    # Time: O(nᵏ)
    # Space: O(nᵏ)


def main():
    result = crack_safe(n = 1, k = 2)
    print(result) # "10"

    result = crack_safe(n = 2, k = 2)
    print(result) # "01100"

if __name__ == "__main__":
    main()
