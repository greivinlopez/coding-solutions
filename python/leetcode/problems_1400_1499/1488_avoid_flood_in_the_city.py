# -----------------------------
# 1488. Avoid Flood in The City
# -----------------------------

# Problem: https://leetcode.com/problems/avoid-flood-in-the-city
#
# Your country has 10⁹ lakes. Initially, all the lakes are empty, but when it
# rains over the nth lake, the nth lake becomes full of water. If it rains over a
# lake that is full of water, there will be a flood. Your goal is to avoid floods
# in any lake.
# 
# Given an integer array rains where:
#         
#   * rains[i] > 0 means there will be rains over the rains[i] lake.
#   * rains[i] == 0 means there are no rains this day and you must choose one
#     lake this day and dry it.
# 
# Return an array ans where:
#         
#   * ans.length == rains.length
#   * ans[i] == -1 if rains[i] > 0.
#   * ans[i] is the lake you choose to dry in the ith day if rains[i] == 0.
# 
# If there are multiple valid answers return any of them. If it is impossible to
# avoid flood return an empty array.
# 
# Notice that if you chose to dry a full lake, it becomes empty, but if you chose
# to dry an empty lake, nothing changes.
# 
# Example 1:
# 
# Input: rains = [1,2,3,4]
# Output: [-1,-1,-1,-1]
# 
# Explanation: After the first day full lakes are [1]
# After the second day full lakes are [1,2]
# After the third day full lakes are [1,2,3]
# After the fourth day full lakes are [1,2,3,4]
# There's no day to dry any lake and there is no flood in any lake.
# 
# Example 2:
# 
# Input: rains = [1,2,0,0,2,1]
# Output: [-1,-1,2,1,-1,-1]
# 
# Explanation: After the first day full lakes are [1]
# After the second day full lakes are [1,2]
# After the third day, we dry lake 2. Full lakes are [1]
# After the fourth day, we dry lake 1. There is no full lakes.
# After the fifth day, full lakes are [2].
# After the sixth day, full lakes are [1,2].
# It is easy that this scenario is flood-free. [-1,-1,1,2,-1,-1] is another
# acceptable scenario.
# 
# Example 3:
# 
# Input: rains = [1,2,0,1,2]
# Output: []
# 
# Explanation: After the second day, full lakes are  [1,2]. We have to dry one
# lake in the third day.
# After that, it will rain over lakes [1,2]. It's easy to prove that no matter
# which lake you choose to dry in the 3rd day, the other one will flood.
# 
# 
# Constraints:
#         1 <= rains.length <= 10⁵
#         0 <= rains[i] <= 10⁹

# ----------------------------
# pip install sortedcontainers
# ----------------------------
from sortedcontainers import SortedList

# Solution: 
# Credit: Navdeep Singh founder of NeetCode
def avoid_flood(rains):
    n = len(rains)
    # Initialize result array with -1 (default for rainy days)
    result = [-1] * n
    
    # Keep track of sunny days (when we can dry a lake)
    sunny_days = SortedList()
    
    # Dictionary to store the last day each lake was filled
    # Key: lake number, Value: day index when it rained on this lake
    last_rain_day = {}
    
    for day, lake in enumerate(rains):
        if lake > 0:  # Rainy day (lake > 0 means it rains on this lake)
            # Check if this lake was already full
            if lake in last_rain_day:
                # Find the first sunny day after the last rain on this lake
                # We need to dry this lake before it rains again
                sunny_day_idx = sunny_days.bisect_right(last_rain_day[lake])
                
                # If no sunny day available after last rain, flood is inevitable
                if sunny_day_idx == len(sunny_days):
                    return []
                
                # Use this sunny day to dry the current lake
                dry_day = sunny_days[sunny_day_idx]
                result[dry_day] = lake
                
                # Remove the used sunny day from available days
                sunny_days.discard(dry_day)
            
            # Update the last rain day for this lake
            last_rain_day[lake] = day
        else:  # Sunny day (lake == 0)
            # Add this day to available sunny days
            sunny_days.add(day)
            # Default: dry lake 1 (can be any valid lake number)
            result[day] = 1
    
    return result
    # O(n * log n)
    # O(n)


def main():
    result = avoid_flood(rains = [1,2,3,4])
    print(result) # [-1, -1, -1, -1]

    result = avoid_flood(rains = [1,2,0,0,2,1])
    print(result) # [-1, -1, 2, 1, -1, -1]

    result = avoid_flood(rains = [1,2,0,1,2])
    print(result) # []

if __name__ == "__main__":
    main()
