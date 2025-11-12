# -------------------
# 134. Gas Station ⛽
# -------------------

# Problem: https://leetcode.com/problems/gas-station/
# 
# There are n gas stations along a circular route, where the amount of gas at 
# the ith station is gas[i].
# 
# You have a car with an unlimited gas tank and it costs cost[i] of gas to 
# travel from the ith station to its next (i + 1)th station. You begin the 
# journey with an empty tank at one of the gas stations.
# 
# Given two integer arrays gas and cost, return the starting gas station's 
# index if you can travel around the circuit once in the clockwise direction, 
# otherwise return -1. If there exists a solution, it is guaranteed to be unique.

# Solution: https://youtu.be/lJwbPZGo05A
# Credit: Navdeep Singh founder of NeetCode
def can_complete_circuit(gas, cost):
    start, end = len(gas) - 1, 0
    total = gas[start] - cost[start]

    while start >= end:
        while total < 0 and start >= end:
            start -= 1
            total += gas[start] - cost[start]
        if start == end:
            return start
        total += gas[end] - cost[end]
        end += 1
    return -1


def main():
    result = can_complete_circuit(gas = [1,2,3,4,5], cost = [3,4,5,1,2])
    print(result) # 3

    result = can_complete_circuit(gas = [2,3,4], cost = [3,4,3])
    print(result) # -1

if __name__ == "__main__":
    main()