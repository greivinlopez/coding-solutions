# -------------------------------------------
# 1515. Best Position for a Service Centre ⛽
# -------------------------------------------

# Problem: https://leetcode.com/problems/best-position-for-a-service-centre
#
# A delivery company wants to build a new service center in a new city. The
# company knows the positions of all the customers in this city on a 2D-Map and
# wants to build the new center in a position such that the sum of the euclidean
# distances to all customers is minimum.
# 
# Given an array positions where positions[i] = [xᵢ, yᵢ] is the position of the
# ith customer on the map, return the minimum sum of the euclidean distances to
# all customers.
# 
# In other words, you need to choose the position of the service center [xcentre,
# ycentre] such that the following formula is minimized:
# 
# https://assets.leetcode.com/uploads/2020/06/25/q4_edited.jpg
# 
# Answers within 10⁻⁵ of the actual value will be accepted.
# 
# Example 1:
# 
# Input: positions = [[0,1],[1,0],[1,2],[2,1]]
# Output: 4.00000
# 
# Explanation: As shown, you can see that choosing [xcentre, ycentre] = [1, 1]
# will make the distance to each customer = 1, the sum of all distances is 4 which
# is the minimum possible we can achieve.
# 
# Example 2:
# 
# Input: positions = [[1,1],[3,3]]
# Output: 2.82843
# 
# Explanation: The minimum possible sum of distances = sqrt(2) + sqrt(2) = 2.82843
# 
# 
# Constraints:
#         1 <= positions.length <= 50
#         positions[i].length == 2
#         0 <= xᵢ, yᵢ <= 100

from math import sqrt

# Solution: https://algo.monster/liteproblems/1515
# Credit: AlgoMonster
def get_min_dist_sum(positions):
    # Calculate the centroid as initial guess for the optimal point
    num_positions = len(positions)
    center_x = sum(pos[0] for pos in positions) / num_positions
    center_y = sum(pos[1] for pos in positions) / num_positions
    
    # Gradient descent parameters
    learning_rate = 0.5  # Initial step size for gradient descent
    decay_factor = 0.999  # Decay factor to reduce learning rate over iterations
    convergence_threshold = 1e-6  # Threshold for convergence detection
    epsilon = 1e-8  # Small value to avoid division by zero
    
    # Iterative gradient descent optimization
    while True:
        # Calculate gradients and total distance
        gradient_x = 0.0
        gradient_y = 0.0
        total_distance = 0.0
        
        for position_x, position_y in positions:
            # Calculate distance components
            delta_x = center_x - position_x
            delta_y = center_y - position_y
            distance = sqrt(delta_x * delta_x + delta_y * delta_y)
            
            # Accumulate partial derivatives (gradient components)
            # Adding epsilon to avoid division by zero when point coincides with a position
            gradient_x += delta_x / (distance + epsilon)
            gradient_y += delta_y / (distance + epsilon)
            
            # Accumulate total distance
            total_distance += distance
        
        # Calculate step sizes based on gradients and learning rate
        step_x = gradient_x * learning_rate
        step_y = gradient_y * learning_rate
        
        # Update center point by moving against gradient direction
        center_x -= step_x
        center_y -= step_y
        
        # Decay the learning rate for finer adjustments
        learning_rate *= decay_factor
        
        # Check convergence: if steps are smaller than threshold, we've converged
        if abs(step_x) <= convergence_threshold and abs(step_y) <= convergence_threshold:
            return total_distance
    # Time: O(n * k)
    # Space: O(1)


def main():
    result = get_min_dist_sum(positions = [[0,1],[1,0],[1,2],[2,1]])
    print(result) # 4.0

    result = get_min_dist_sum(positions = [[1,1],[3,3]])
    print(result) # 2.82843

if __name__ == "__main__":
    main()
