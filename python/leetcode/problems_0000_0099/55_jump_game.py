# --------------
# 55. Jump Game
# --------------

# Problem: https://leetcode.com/problems/jump-game/
# You are given an integer array nums. You are initially positioned at the 
# array's first index, and each element in the array represents your maximum
# jump length at that position.
# 
# Return true if you can reach the last index, or false otherwise.

# Solution: https://youtu.be/Yan0cv2cLy8
# Credit: Navdeep Singh founder of NeetCode 
def can_jump(nums):
    # Greedy
    # Time: O(n)
	# Space: O(1)
    goal = len(nums) - 1

    for i in range(len(nums) - 2, -1, -1):
        if i + nums[i] >= goal:
            goal = i
    return goal == 0

# Alternative solution
def can_jump_alt(nums):
    # Top Down DP (Memoization)
    # Time: O(n^2)
    # Space: O(n)
    n = len(nums)
    memo = {n-1: True}

    def can_reach(i):
        if i in memo:
            return memo[i]
        
        for jump in range(1, nums[i]+1):
            if can_reach(i+jump):
                memo[i] = True
                return True
        
        memo[i] = False
        return False
    
    return can_reach(0)

# Same Solution Different Video: https://youtu.be/PfGypLRcoVA
# Credit: Greg Hogg

def main():
    result = can_jump([2,3,1,1,4])
    # Expected Output: True
    print(result)
    result = can_jump([3,2,1,0,4])
    # Expected Output: False
    print(result)

if __name__ == "__main__":
    main()