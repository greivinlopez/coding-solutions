# -----------------------
# 739. Daily Temperatures
# -----------------------

# Problem: https://leetcode.com/problems/daily-temperatures/
# 
# Given an array of integers temperatures represents the daily temperatures, 
# return an array answer such that answer[i] is the number of days you have to 
# wait after the ith day to get a warmer temperature. If there is no future day 
# for which this is possible, keep answer[i] == 0 instead.
# 
#  
# Example 1:
# 
# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
# 
# Example 2:
# 
# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]
# 
# Example 3:
# 
# Input: temperatures = [30,60,90]
# Output: [1,1,0]
# 
#  
# Constraints:
# 
# 	1 <= temperatures.length <= 10^5
# 	30 <= temperatures[i] <= 100


# Solution: https://youtu.be/cTBiBSnjO3c
# Credit: Navdeep Singh founder of NeetCode
def daily_temperatures(temperatures):
    res = [0] * len(temperatures)
    stack = []  # pair: [temp, index]

    for i, t in enumerate(temperatures):
        while stack and t > stack[-1][0]:
            stackT, stackInd = stack.pop()
            res[stackInd] = i - stackInd
        stack.append((t, i))
    return res
    # Time: O(n)
    # Space: O(n)

# Solution: https://youtu.be/_ZEvmycwXHs
# Credit: Greg Hogg
# Same Solution

def main():
    result = daily_temperatures([73,74,75,71,69,72,76,73])
    print(result) # [1,1,4,2,1,1,0,0]

    result = daily_temperatures([30,40,50,60])
    print(result) # [1,1,1,0]

    result = daily_temperatures([30,60,90])
    print(result) # [1,1,0]

if __name__ == "__main__":
    main()
