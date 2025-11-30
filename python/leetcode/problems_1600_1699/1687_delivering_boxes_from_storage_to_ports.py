# -----------------------------------------------
# 1687. Delivering Boxes from Storage to Ports 📦
# -----------------------------------------------

# Problem: https://leetcode.com/problems/delivering-boxes-from-storage-to-ports
#
# You have the task of delivering some boxes from storage to their ports using
# only one ship. However, this ship has a limit on the number of boxes and the
# total weight that it can carry.
# 
# You are given an array boxes, where boxes[i] = [ports​​i​, weighti], and three
# integers portsCount, maxBoxes, and maxWeight.
#         
#   * ports​​i is the port where you need to deliver the iᵗʰ box and weightsi
#     is the weight of the iᵗʰ box.
#   * portsCount is the number of ports.
#   * maxBoxes and maxWeight are the respective box and weight limits of the ship.
# 
# The boxes need to be delivered in the order they are given. The ship will follow
# these steps:
#         
#   * The ship will take some number of boxes from the boxes queue, not violating 
#     the maxBoxes and maxWeight constraints.
#   * For each loaded box in order, the ship will make a trip to the port the
#     box needs to be delivered to and deliver it. If the ship is already at the
#     correct port, no trip is needed, and the box can immediately be delivered.
#   * The ship then makes a return trip to storage to take more boxes from the queue.
# 
# The ship must end at storage after all the boxes have been delivered.
# 
# Return the minimum number of trips the ship needs to make to deliver all boxes
# to their respective ports.
# 
# Example 1:
# 
# Input: boxes = [[1,1],[2,1],[1,1]], portsCount = 2, maxBoxes = 3, maxWeight = 3
# Output: 4
# 
# Explanation: The optimal strategy is as follows:
# - The ship takes all the boxes in the queue, goes to port 1, then port 2, then
# port 1 again, then returns to storage. 4 trips.
# So the total number of trips is 4.
# Note that the first and third boxes cannot be delivered together because the
# boxes need to be delivered in order (i.e. the second box needs to be delivered
# at port 2 before the third box).
# 
# Example 2:
# 
# Input: boxes = [[1,2],[3,3],[3,1],[3,1],[2,4]], portsCount = 3, maxBoxes = 3,
# maxWeight = 6
# Output: 6
# 
# Explanation: The optimal strategy is as follows:
# - The ship takes the first box, goes to port 1, then returns to storage. 2
# trips.
# - The ship takes the second, third and fourth boxes, goes to port 3, then
# returns to storage. 2 trips.
# - The ship takes the fifth box, goes to port 2, then returns to storage. 2
# trips.
# So the total number of trips is 2 + 2 + 2 = 6.
# 
# Example 3:
# 
# Input: boxes = [[1,4],[1,2],[2,1],[2,1],[3,2],[3,4]], portsCount = 3, maxBoxes =
# 6, maxWeight = 7
# Output: 6
# 
# Explanation: The optimal strategy is as follows:
# - The ship takes the first and second boxes, goes to port 1, then returns to
# storage. 2 trips.
# - The ship takes the third and fourth boxes, goes to port 2, then returns to
# storage. 2 trips.
# - The ship takes the fifth and sixth boxes, goes to port 3, then returns to
# storage. 2 trips.
# So the total number of trips is 2 + 2 + 2 = 6.
# 
# 
# Constraints:
#         1 <= boxes.length <= 10⁵
#         1 <= portsCount, maxBoxes, maxWeight <= 10⁵
#         1 <= ports​​i <= portsCount
#         1 <= weightsi <= maxWeight


# Note: The use of pairwise limits this solution to Python 3.10+
# Solution: https://algo.monster/liteproblems/1687
# Credit: AlgoMonster
def box_delivering(boxes, portsCount, maxBoxes, maxWeight):
    from collections import deque
    from itertools import accumulate, pairwise

    n = len(boxes)
    
    # Prefix sum of weights for quick range sum calculation
    weight_prefix_sum = list(accumulate((box[1] for box in boxes), initial=0))
    
    # Count transitions between different ports (1 if port changes, 0 otherwise)
    port_changes = [int(a != b) for a, b in pairwise(box[0] for box in boxes)]
    
    # Prefix sum of port changes for quick range calculation
    changes_prefix_sum = list(accumulate(port_changes, initial=0))
    
    # dp[i] represents minimum trips needed to deliver first i boxes
    dp = [0] * (n + 1)
    
    # Monotonic deque to maintain optimal starting points for current batch
    deque_indices = deque([0])
    
    for i in range(1, n + 1):
        # Remove indices that violate constraints (too many boxes or too heavy)
        while deque_indices and (
            i - deque_indices[0] > maxBoxes or 
            weight_prefix_sum[i] - weight_prefix_sum[deque_indices[0]] > maxWeight
        ):
            deque_indices.popleft()
        
        # Calculate minimum trips if we have valid starting points
        if deque_indices:
            # Trips = previous trips + port changes in current batch + 2 (pickup and delivery)
            start_idx = deque_indices[0]
            dp[i] = (changes_prefix_sum[i - 1] + dp[start_idx] - 
                    changes_prefix_sum[start_idx] + 2)
        
        # Prepare for next iteration (only if not at last box)
        if i < n:
            # Maintain monotonic property: remove suboptimal starting points
            while deque_indices and (
                dp[deque_indices[-1]] - changes_prefix_sum[deque_indices[-1]] >= 
                dp[i] - changes_prefix_sum[i]
            ):
                deque_indices.pop()
            deque_indices.append(i)
    
    return dp[n]
    # Time: O(n)
    # Space: O(n)


def main():
    result = box_delivering(boxes = [[1,1],[2,1],[1,1]], portsCount = 2, maxBoxes = 3, maxWeight = 3)
    print(result) # 4

    result = box_delivering(boxes = [[1,2],[3,3],[3,1],[3,1],[2,4]], portsCount = 3, maxBoxes = 3, maxWeight = 6)
    print(result) # 6

    result = box_delivering(boxes = [[1,4],[1,2],[2,1],[2,1],[3,2],[3,4]], portsCount = 3, maxBoxes = 6, maxWeight = 7)
    print(result) # 6

if __name__ == "__main__":
    main()
