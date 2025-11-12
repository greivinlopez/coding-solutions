# ---------------------------------------
# 1344. Angle Between Hands of a Clock 🕰️
# ---------------------------------------

# Problem: https://leetcode.com/problems/angle-between-hands-of-a-clock
#
# Given two numbers, hour and minutes, return the smaller angle (in degrees)
# formed between the hour and the minute hand.
# 
# Answers within 10⁻⁵ of the actual value will be accepted as correct.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2019/12/26/sample_1_1673.png
# 
# Input: hour = 12, minutes = 30
# Output: 165
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2019/12/26/sample_2_1673.png
# 
# Input: hour = 3, minutes = 30
# Output: 75
# 
# Example 3:
# 
# https://assets.leetcode.com/uploads/2019/12/26/sample_3_1673.png
# 
# Input: hour = 3, minutes = 15
# Output: 7.5
# 
# 
# Constraints:
#         1 <= hour <= 12
#         0 <= minutes <= 59


# Solution: https://algo.monster/liteproblems/1344
# Credit: AlgoMonster
def angle_clock(hour, minutes):
    # Calculate hour hand position in degrees
    # Hour hand moves 30 degrees per hour (360/12 = 30)
    # Hour hand also moves 0.5 degrees per minute (30/60 = 0.5)
    hour_angle = 30 * hour + 0.5 * minutes
    
    # Calculate minute hand position in degrees
    # Minute hand moves 6 degrees per minute (360/60 = 6)
    minute_angle = 6 * minutes
    
    # Calculate the absolute difference between the two hands
    angle_difference = abs(hour_angle - minute_angle)
    
    # Return the smaller angle between the two possible angles
    # (the direct angle or the reflex angle)
    return min(angle_difference, 360 - angle_difference)
    # Time: O(1)
    # Space: O(1)


def main():
    result = angle_clock(hour = 12, minutes = 30)
    print(result) # 165

    result = angle_clock(hour = 3, minutes = 30)
    print(result) # 75

    result = angle_clock(hour = 3, minutes = 15)
    print(result) # 7.5

if __name__ == "__main__":
    main()
