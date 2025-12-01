# ---------------------------------
# 1710. Maximum Units on a Truck 🚛
# ---------------------------------

# Problem: https://leetcode.com/problems/maximum-units-on-a-truck
#
# You are assigned to put some amount of boxes onto one truck. You are given a 2D
# array boxTypes, where boxTypes[i] = [numberOfBoxesᵢ, numberOfUnitsPerBoxᵢ]:
#         
#   * numberOfBoxesᵢ is the number of boxes of type i.
#   * numberOfUnitsPerBoxᵢ is the number of units in each box of the type i.
# 
# You are also given an integer truckSize, which is the maximum number of boxes
# that can be put on the truck. You can choose any boxes to put on the truck as
# long as the number of boxes does not exceed truckSize.
# 
# Return the maximum total number of units that can be put on the truck.
# 
# Example 1:
# 
# Input: boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4
# Output: 8
# 
# Explanation: There are:
# - 1 box of the first type that contains 3 units.
# - 2 boxes of the second type that contain 2 units each.
# - 3 boxes of the third type that contain 1 unit each.
# You can take all the boxes of the first and second types, and one box of the
# third type.
# The total number of units will be = (1 * 3) + (2 * 2) + (1 * 1) = 8.
# 
# Example 2:
# 
# Input: boxTypes = [[5,10],[2,5],[4,7],[3,9]], truckSize = 10
# Output: 91
# 
# 
# Constraints:
#         1 <= boxTypes.length <= 1000
#         1 <= numberOfBoxesᵢ, numberOfUnitsPerBoxᵢ <= 1000
#         1 <= truckSize <= 10⁶


# Solution: https://algo.monster/liteproblems/1710
# Credit: AlgoMonster
def maximum_units(boxTypes, truckSize):
    # Initialize total units counter
    total_units = 0
    
    # Sort boxes by units per box in descending order (greedy approach)
    # Each element is [number_of_boxes, units_per_box]
    sorted_boxes = sorted(boxTypes, key=lambda box: -box[1])
    
    # Iterate through sorted boxes, taking boxes with most units first
    for num_boxes, units_per_box in sorted_boxes:
        # Take as many boxes as possible (limited by available boxes or remaining truck capacity)
        boxes_to_take = min(truckSize, num_boxes)
        
        # Add units from these boxes to total
        total_units += units_per_box * boxes_to_take
        
        # Reduce remaining truck capacity
        truckSize -= boxes_to_take
        
        # If truck is full, stop loading
        if truckSize <= 0:
            break
    
    return total_units
    # Time: O(n * log n)
    # Space: O(n)


def main():
    result = maximum_units(boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4)
    print(result) # 8

    result = maximum_units(boxTypes = [[5,10],[2,5],[4,7],[3,9]], truckSize = 10)
    print(result) # 91

if __name__ == "__main__":
    main()
