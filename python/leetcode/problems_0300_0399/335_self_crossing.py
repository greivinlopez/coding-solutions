# ------------------
# 335. Self Crossing
# ------------------

# Problem: https://leetcode.com/problems/self-crossing
#
# You are given an array of integers distance.
# 
# You start at the point (0, 0) on an X-Y plane, and you move distance[0] meters
# to the north, then distance[1] meters to the west, distance[2] meters to the
# south, distance[3] meters to the east, and so on. In other words, after each
# move, your direction changes counter-clockwise.
# 
# Return true if your path crosses itself or false if it does not.
# 
# Example 1:
# 
# Input: distance = [2,1,1,2]
# Output: true
# 
# Explanation: The path crosses itself at the point (0, 1).
# 
# Example 2:
# 
# Input: distance = [1,2,3,4]
# Output: false
# 
# Explanation: The path does not cross itself at any point.
# 
# Example 3:
# 
# Input: distance = [1,1,1,2,1]
# Output: true
# 
# Explanation: The path crosses itself at the point (0, 0).
# 
# 
# Constraints:
#         1 <= distance.length <= 10⁵
#         1 <= distance[i] <= 10⁵


# Solution: https://leetcode.com/problems/self-crossing/solutions/993157/python-93-5-very-concise-and-understandable-solution-10-lines-of-code
# Credit: Dhruv Vavliya -> https://leetcode.com/u/risky_coder/
def is_self_crossing(distance):
    x = distance

    for i in range(3,len(x)):

        if x[i-3]>=x[i-1] and x[i]>=x[i-2]:
            return True
        
        if i>=4:
            if x[i-3] == x[i-1] and x[i-2]<=(x[i-4]+x[i]):
                return True

        if i>=5:
            if x[i-2]>=x[i-4] and x[i-3]>=x[i-1] and (x[i-5]+x[i-1])>=x[i-3] and (x[i-4]+x[i])>=x[i-2]:
                return True

    return False
    # Time: O(n)
    # Space: O(1)


def main():
    result = is_self_crossing(distance = [2,1,1,2])
    print(result) # True

    result = is_self_crossing(distance = [1,2,3,4])
    print(result) # False

    result = is_self_crossing(distance = [1,1,1,2,1])
    print(result) # True

if __name__ == "__main__":
    main()
