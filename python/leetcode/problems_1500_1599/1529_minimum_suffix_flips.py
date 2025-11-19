# --------------------------
# 1529. Minimum Suffix Flips
# --------------------------

# Problem: https://leetcode.com/problems/minimum-suffix-flips
#
# You are given a 0-indexed binary string target of length n. You have another
# binary string s of length n that is initially set to all zeros. You want to make
# s equal to target.
# 
# In one operation, you can pick an index i where 0 <= i < n and flip all bits in
# the inclusive range [i, n - 1]. Flip means changing '0' to '1' and '1' to '0'.
# 
# Return the minimum number of operations needed to make s equal to target.
# 
# Example 1:
# 
# Input: target = "10111"
# Output: 3
# 
# Explanation: Initially, s = "00000".
# Choose index i = 2: "00000" -> "00111"
# Choose index i = 0: "00111" -> "11000"
# Choose index i = 1: "11000" -> "10111"
# We need at least 3 flip operations to form target.
# 
# Example 2:
# 
# Input: target = "101"
# Output: 3
# 
# Explanation: Initially, s = "000".
# Choose index i = 0: "000" -> "111"
# Choose index i = 1: "111" -> "100"
# Choose index i = 2: "100" -> "101"
# We need at least 3 flip operations to form target.
# 
# Example 3:
# 
# Input: target = "00000"
# Output: 0
# 
# Explanation: We do not need any operations since the initial s already equals
# target.
# 
# 
# Constraints:
#         n == target.length
#         1 <= n <= 10⁵
#         target[i] is either '0' or '1'.


# Solution: https://algo.monster/liteproblems/1529
# Credit: AlgoMonster
def min_flips(target):
    # Track the total number of flips performed
    flip_count = 0
    
    # Iterate through each character in the target string
    for char in target:
        # Check if current position needs a flip
        # (flip_count & 1) gives the current state: 0 if even flips, 1 if odd flips
        # XOR with target bit to check if they differ
        if (flip_count & 1) ^ int(char):
            # If current state doesn't match target, we need to flip
            flip_count += 1
    
    return flip_count
    # Time: O(n)
    # Space: O(1)


def main():
    result = min_flips(target = "10111")
    print(result) # 3

    result = min_flips(target = "101")
    print(result) # 3

    result = min_flips(target = "00000")
    print(result) # 0

if __name__ == "__main__":
    main()
