# --------------------------------------
# 1552. Magnetic Force Between Two Balls
# --------------------------------------

# Problem: https://leetcode.com/problems/magnetic-force-between-two-balls
#
# In the universe Earth C-137, Rick discovered a special form of magnetic force
# between two balls if they are put in his new invented basket. Rick has n empty
# baskets, the iᵗʰ basket is at position[i], Morty has m balls and needs to
# distribute the balls into the baskets such that the minimum magnetic force
# between any two balls is maximum.
# 
# Rick stated that magnetic force between two different balls at positions x and y
# is |x - y|.
# 
# Given the integer array position and the integer m. Return the required force.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2020/08/11/q3v1.jpg
# 
# Input: position = [1,2,3,4,7], m = 3
# Output: 3
# 
# Explanation: Distributing the 3 balls into baskets 1, 4 and 7 will make the
# magnetic force between ball pairs [3, 3, 6]. The minimum magnetic force is 3. We
# cannot achieve a larger minimum magnetic force than 3.
# 
# Example 2:
# 
# Input: position = [5,4,3,2,1,1000000000], m = 2
# Output: 999999999
# 
# Explanation: We can use baskets 1 and 1000000000.
# 
# Constraints:
#         n == position.length
#         2 <= n <= 10⁵
#         1 <= position[i] <= 10⁹
#         All integers in position are distinct.
#         2 <= m <= position.length


# Credit: Jaweria Batool -> https://github.com/Jaweria-B
def can_place_balls(x, position, m):
    # Check if we can place 'm' balls at 'position'
    # with each ball having at least 'x' gap.

    # Place the first ball at the first position.
    prev_ball_pos = position[0]
    balls_placed = 1

    # Iterate on each 'position' and place a ball there if we can place it.
    for i in range(1, len(position)):
        curr_pos = position[i]
        # Check if we can place the ball at the current position.
        if curr_pos - prev_ball_pos >= x:
            balls_placed += 1
            prev_ball_pos = curr_pos
        # If all 'm' balls are placed, return 'True'.
        if balls_placed == m:
            return True
    return False

def max_distance(position, m):
    answer = 0
    n = len(position)
    position.sort()

    # Initial search space.
    low = 1
    high = int(position[-1] / (m - 1.0)) + 1
    while low <= high:
        mid = low + (high - low) // 2
        # If we can place all balls having a gap at least 'mid',
        if can_place_balls(mid, position, m):
            # then 'mid' can be our answer,
            answer = mid
            # and discard the left half search space.
            low = mid + 1
        else:
            # Discard the right half search space.
            high = mid - 1
    return answer
    # Time: O(n * log(n) + n * log(r))
    # Space: O(1)
    # r = maximum value in position


def main():
    result = max_distance(position = [1,2,3,4,7], m = 3)
    print(result) # 3

    result = max_distance(position = [5,4,3,2,1,1000000000], m = 2)
    print(result) # 999999999

if __name__ == "__main__":
    main()
