# ----------------------
# 45. Jump Game II
# ----------------------

# Problem: https://leetcode.com/problems/jump-game-ii/
# You are given a 0-indexed array of integers nums of length n. You are initially 
# positioned at index 0.
# 
# Each element nums[i] represents the maximum length of a forward jump from index i.
# In other words, if you are at index i, you can jump to any index (i + j) where:
# 
# *   0 <= j <= nums[i] and
# *   i + j < n
# 
# Return the minimum number of jumps to reach index n - 1. The test cases are generated such that you can reach index n - 1.

# Solution: https://youtu.be/dJ7sWiOoK7g
# Credit: Navdeep Singh founder of NeetCode 
def jump(nums):
    l, r = 0, 0
    res = 0
    while r < (len(nums) - 1):
        maxJump = 0
        for i in range(l, r + 1):
            maxJump = max(maxJump, i + nums[i])
        l = r + 1
        r = maxJump
        res += 1
    return res

# Solution: https://youtu.be/CsDI-yQuGeM
# Credit: Greg Hogg
def jump_alt(nums):
    # Time: O(n)
    # Space: O(1)
    smallest = 0
    n = len(nums)
    end, far = 0, 0

    for i in range(n-1):
        far = max(far, i+nums[i])
        
        if i == end:
            smallest += 1
            end = far
    
    return smallest

def main():
    result = jump([2,3,1,1,4]) # 2
    print(result)
    result = jump([2,3,0,1,4]) # 2
    print(result)

if __name__ == "__main__":
    main()