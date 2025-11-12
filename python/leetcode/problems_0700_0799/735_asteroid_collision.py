# -----------------------
# 735. Asteroid Collision
# -----------------------

# Problem: https://leetcode.com/problems/asteroid-collision/
# 
# We are given an array asteroids of integers representing asteroids in a row. 
# The indices of the asteriod in the array represent their relative position 
# in space.
# 
# For each asteroid, the absolute value represents its size, and the sign 
# represents its direction (positive meaning right, negative meaning left). 
# Each asteroid moves at the same speed.
# 
# Find out the state of the asteroids after all collisions. If two asteroids 
# meet, the smaller one will explode. If both are the same size, both will 
# explode. Two asteroids moving in the same direction will never meet.
# 
#  
# Example 1:
# 
# Input: asteroids = [5,10,-5]
# Output: [5,10]
# Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
# 
# 
# Example 2:
# 
# Input: asteroids = [8,-8]
# Output: []
# Explanation: The 8 and -8 collide exploding each other.
# 
# 
# Example 3:
# 
# Input: asteroids = [10,2,-5]
# Output: [10]
# Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
# 
# 
# Constraints:
# 
# 	2 <= asteroids.length <= 10^4
# 	-1000 <= asteroids[i] <= 1000
# 	asteroids[i] != 0


# Solution: https://youtu.be/LN7KjRszjk4
# Credit: Navdeep Singh founder of NeetCode
def asteroid_collision(asteroids):
    stack = []

    for a in asteroids:
        while stack and a < 0 and stack[-1] > 0:
            diff = a + stack[-1]
            if diff > 0:
                a = 0
            elif diff < 0:
                stack.pop()
            else:
                a = 0
                stack.pop()
        if a:
            stack.append(a)

    return stack


def main():
    result = asteroid_collision([5,10,-5])
    print(result) # [5,10]

    result = asteroid_collision([8,-8])
    print(result) # []

    result = asteroid_collision([10,2,-5])
    print(result) # [10]

if __name__ == "__main__":
    main()
