# ---------------------------------
# 374. Guess Number Higher Or Lower
# ---------------------------------

# Problem: https://leetcode.com/problems/guess-number-higher-or-lower/
# 
# We are playing the Guess Game. The game is as follows:
# 
# I pick a number from 1 to n. You have to guess which number I picked 
# (the number I picked stays the same throughout the game).
# 
# Every time you guess wrong, I will tell you whether the number I picked is 
# higher or lower than your guess.
# 
# You call a pre-defined API int guess(int num), which returns three possible 
# results:
# 
# 	-1: Your guess is higher than the number I picked (i.e. num > pick).
# 	1: Your guess is lower than the number I picked (i.e. num < pick).
# 	0: your guess is equal to the number I picked (i.e. num == pick).
# 
# Return the number that I picked.
# 
# 
# Example 1:
# 
# Input: n = 10, pick = 6
# Output: 6
# 
# 
# Example 2:
# 
# Input: n = 1, pick = 1
# Output: 1
# 
# 
# Example 3:
# 
# Input: n = 2, pick = 1
# Output: 1
# 
# 
# Constraints:
# 
# 	1 <= n <= 2^31 - 1
# 	1 <= pick <= n

# Global variable used for testing
pick = 6
def guess(n):
    if n > pick:
        return -1
    elif pick == n:
        return 0
    else:  # n < pick
        return 1

# Solution: https://youtu.be/xW4QsTtaCa4
# Credit: Navdeep Singh founder of NeetCode
def guess_number(n):
    # return a num btw 1,..,n
    low = 1
    high = n
    
    while True:
        mid = low + (high - low) // 2
        myGuess = guess(mid)
        if myGuess == 1:
            low = mid + 1
        elif myGuess == -1:
            high = mid - 1
        else:
            return mid


def main():
    pick = 6
    result = guess_number(10)
    print(result) # 6

    # WARNING: Infinite loop here?
    pick = 1
    result = guess_number(1)
    print(result) # 1

    pick = 1
    result = guess_number(2)
    print(result) # 1

if __name__ == "__main__":
    main()
