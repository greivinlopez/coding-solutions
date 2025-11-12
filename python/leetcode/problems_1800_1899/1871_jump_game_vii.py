# -------------------
# 1871. Jump Game VII
# -------------------

# Problem: https://leetcode.com/problems/jump-game-vii
#
# You are given a 0-indexed binary string s and two integers minJump and maxJump.
# In the beginning, you are standing at index 0, which is equal to '0'. You can
# move from index i to index j if the following conditions are fulfilled:
#         
#   * i + minJump <= j <= min(i + maxJump, s.length - 1), and
#   * s[j] == '0'.
# 
# Return true if you can reach index s.length - 1 in s, or false otherwise.
# 
# Example 1:
# 
# Input: s = "011010", minJump = 2, maxJump = 3
# Output: true
# 
# Explanation:
# In the first step, move from index 0 to index 3.
# In the second step, move from index 3 to index 5.
# 
# Example 2:
# 
# Input: s = "01101110", minJump = 2, maxJump = 3
# Output: false
# 
# 
# Constraints:
#         2 <= s.length <= 10^5
#         s[i] is either '0' or '1'.
#         s[0] == '0'
#         1 <= minJump <= maxJump < s.length

from collections import deque

# Solution: https://youtu.be/v1HpZUnQ4Yo
# Credit: Navdeep Singh founder of NeetCode
def can_reach(s, minJump, maxJump):
    # If the last character is '1', it's impossible to land there.
    if s[-1] == '1':
        return False

    # The queue stores indices of '0's that we can jump from.
    q = deque([0])
    
    # 'farthest' tracks the farthest index we have already processed.
    # This prevents re-visiting indices in the inner loop.
    farthest = 0

    while q:
        i = q.popleft()

        # Determine the range of the next possible jumps.
        # We start from max(i + min_jump, farthest + 1) to avoid redundant checks.
        start = max(i + minJump, farthest + 1)
        end = min(i + maxJump + 1, len(s))

        # Explore all valid '0' positions in the jump range.
        for j in range(start, end):
            if s[j] == '0':
                # If we've reached the end, success!
                if j == len(s) - 1:
                    return True
                # Otherwise, add this new position to the queue to explore from later.
                q.append(j)
        
        # Update the farthest index we've processed up to.
        farthest = i + maxJump

    # If the queue is empty and we haven't reached the end, it's not possible.
    return False
    # Time: O(n)
    # Space: O(n)


def main():
    result = can_reach(s = "011010", minJump = 2, maxJump = 3)
    print(result) # True

    result = can_reach(s = "01101110", minJump = 2, maxJump = 3)
    print(result) # False

if __name__ == "__main__":
    main()
