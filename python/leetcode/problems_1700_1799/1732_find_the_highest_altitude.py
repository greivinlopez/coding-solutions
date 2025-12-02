# -------------------------------
# 1732. Find the Highest Altitude
# -------------------------------

# Problem: https://leetcode.com/problems/find-the-highest-altitude
#
# There is a biker going on a road trip. The road trip consists of n + 1 points at
# different altitudes. The biker starts his trip on point 0 with altitude equal 0.
# 
# You are given an integer array gain of length n where gain[i] is the net gain in
# altitude between points i​​​​​​ and i + 1 for all (0 <= i < n). Return the
# highest altitude of a point.
# 
# Example 1:
# 
# Input: gain = [-5,1,5,0,-7]
# Output: 1
# 
# Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.
# 
# Example 2:
# 
# Input: gain = [-4,-3,-2,-1,4,3,2]
# Output: 0
# 
# Explanation: The altitudes are [0,-4,-7,-9,-10,-6,-3,-1]. The highest is 0.
# 
# 
# Constraints:
#         n == gain.length
#         1 <= n <= 100
#         -100 <= gain[i] <= 100


# Solution: https://algo.monster/liteproblems/1732
# Credit: AlgoMonster
def largest_altitude(gain):
    from itertools import accumulate
    
    # Calculate cumulative sum of gains starting from altitude 0
    # accumulate() generates running totals: initial altitude (0) + cumulative gains
    # Example: gain = [−5, 1, 5, 0, −7] → altitudes = [0, −5, −4, 1, 1, −6]
    altitudes = accumulate(gain, initial=0)
    
    # Return the maximum altitude from all points in the journey
    return max(altitudes)
    # Time: O(n)
    # Space: O(1)


def main():
    result = largest_altitude(gain = [-5,1,5,0,-7])
    print(result) # 1

    result = largest_altitude(gain = [-4,-3,-2,-1,4,3,2])
    print(result) # 0

if __name__ == "__main__":
    main()
