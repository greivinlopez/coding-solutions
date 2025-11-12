# --------------------------------------------
# 1298. Maximum Candies You Can Get from Boxes
# --------------------------------------------

# Problem: https://leetcode.com/problems/maximum-candies-you-can-get-from-boxes
#
# You have n boxes labeled from 0 to n - 1. You are given four arrays: status,
# candies, keys, and containedBoxes where:
#         
#   * status[i] is 1 if the ith box is open and 0 if the ith box is closed,
#   * candies[i] is the number of candies in the ith box,
#   * keys[i] is a list of the labels of the boxes you can open after opening
#     the ith box.
#   * containedBoxes[i] is a list of the boxes you found inside the ith box.
# 
# You are given an integer array initialBoxes that contains the labels of the
# boxes you initially have. You can take all the candies in any open box and you
# can use the keys in it to open new boxes and you also can use the boxes you find
# in it.
# 
# Return the maximum number of candies you can get following the rules above.
# 
# Example 1:
# 
# Input: status = [1,0,1,0], candies = [7,5,4,100], keys = [[],[],[1],[]],
# containedBoxes = [[1,2],[3],[],[]], initialBoxes = [0]
# Output: 16
# 
# Explanation: You will be initially given box 0. You will find 7 candies in it
# and boxes 1 and 2.
# Box 1 is closed and you do not have a key for it so you will open box 2. You
# will find 4 candies and a key to box 1 in box 2.
# In box 1, you will find 5 candies and box 3 but you will not find a key to box 3
# so box 3 will remain closed.
# Total number of candies collected = 7 + 4 + 5 = 16 candy.
# 
# Example 2:
# 
# Input: status = [1,0,0,0,0,0], candies = [1,1,1,1,1,1], keys =
# [[1,2,3,4,5],[],[],[],[],[]], containedBoxes = [[1,2,3,4,5],[],[],[],[],[]],
# initialBoxes = [0]
# Output: 6
# 
# Explanation: You have initially box 0. Opening it you can find boxes 1,2,3,4 and
# 5 and their keys.
# The total number of candies will be 6.
# 
# 
# Constraints:
#         n == status.length == candies.length == keys.length == containedBoxes.length
#         1 <= n <= 1000
#         status[i] is either 0 or 1.
#         1 <= candies[i] <= 1000
#         0 <= keys[i].length <= n
#         0 <= keys[i][j] < n
#         All values of keys[i] are unique.
#         0 <= containedBoxes[i].length <= n
#         0 <= containedBoxes[i][j] < n
#         All values of containedBoxes[i] are unique.
#         Each box is contained in one box at most.
#         0 <= initialBoxes.length <= n
#         0 <= initialBoxes[i] < n

from collections import deque

# Solution: https://algo.monster/liteproblems/1298
# Credit: AlgoMonster
def max_candies(
    status,
    candies,
    keys,
    containedBoxes,
    initialBoxes,
):
    # Initialize queue for BFS traversal
    queue = deque()
    
    # Track boxes we have and boxes we've already opened
    boxes_owned = set(initialBoxes)
    boxes_opened = set()
    
    # Total candies collected
    total_candies = 0
    
    # Process initial boxes - open any that are already unlocked
    for box in initialBoxes:
        if status[box] == 1:  # Box is open/unlocked
            queue.append(box)
            boxes_opened.add(box)
            total_candies += candies[box]
    
    # BFS to process all reachable boxes
    while queue:
        current_box = queue.popleft()
        
        # Process keys found in current box
        for key in keys[current_box]:
            if status[key] == 0:  # Box was locked
                status[key] = 1  # Unlock the box
                
                # If we own this box and haven't opened it yet, open it now
                if key in boxes_owned and key not in boxes_opened:
                    queue.append(key)
                    boxes_opened.add(key)
                    total_candies += candies[key]
        
        # Process boxes found inside current box
        for contained_box in containedBoxes[current_box]:
            boxes_owned.add(contained_box)
            
            # If this box is unlocked and we haven't opened it yet, open it
            if status[contained_box] == 1 and contained_box not in boxes_opened:
                queue.append(contained_box)
                boxes_opened.add(contained_box)
                total_candies += candies[contained_box]
    
    return total_candies
    # Time: O(n)
    # Space: O(n)


def main():
    result = max_candies(status = [1,0,1,0], 
                         candies = [7,5,4,100], 
                         keys = [[],[],[1],[]], 
                         containedBoxes = [[1,2],[3],[],[]], 
                         initialBoxes = [0])
    print(result) # 16

    result = max_candies(status = [1,0,0,0,0,0], 
                         candies = [1,1,1,1,1,1], 
                         keys = [[1,2,3,4,5],[],[],[],[],[]], 
                         containedBoxes = [[1,2,3,4,5],[],[],[],[],[]], 
                         initialBoxes = [0])
    print(result) # 6

if __name__ == "__main__":
    main()
