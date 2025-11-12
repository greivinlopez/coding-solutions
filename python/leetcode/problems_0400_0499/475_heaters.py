# ------------
# 475. Heaters
# ------------

# Problem: https://leetcode.com/problems/heaters
#
# Winter is coming! During the contest, your first job is to design a standard
# heater with a fixed warm radius to warm all the houses.
# 
# Every house can be warmed, as long as the house is within the heater's warm
# radius range. 
# 
# Given the positions of houses and heaters on a horizontal line, return the
# minimum radius standard of heaters so that those heaters could cover all houses.
# 
# Notice that all the heaters follow your radius standard, and the warm radius
# will be the same.
# 
# Example 1:
# 
# Input: houses = [1,2,3], heaters = [2]
# Output: 1
# 
# Explanation: The only heater was placed in the position 2, and if we use the
# radius 1 standard, then all the houses can be warmed.
# 
# Example 2:
# 
# Input: houses = [1,2,3,4], heaters = [1,4]
# Output: 1
# 
# Explanation: The two heaters were placed at positions 1 and 4. We need to use a
# radius 1 standard, then all the houses can be warmed.
# 
# Example 3:
# 
# Input: houses = [1,5], heaters = [2]
# Output: 3
# 
# 
# Constraints:
#         1 <= houses.length, heaters.length <= 3 * 10⁴
#         1 <= houses[i], heaters[i] <= 10⁹


# Solution: https://leetcode.com/problems/heaters/solutions/554748/python-3-simple-solution
# Credit: nbismoi -> https://leetcode.com/u/nbismoi/
def find_radius(houses, heaters):
    """
    Finds the minimum radius R such that all houses are within R distance
    of a heater.
    """
    houses.sort()
    heaters.sort()
    ans = 0
    pos = 0
    
    # Pad heaters list with infinite values for simplified boundary checks
    heaters = [float('-inf')] + heaters + [float('inf')]
    
    for house in houses:
        # Move 'pos' until heaters[pos] is the first heater position strictly
        # greater than the current house position. This means heaters[pos - 1] 
        # is the heater immediately to the left.
        while house >= heaters[pos]:
            pos += 1
            
        # Calculate the distance to the two nearest heaters:
        # 1. heaters[pos - 1]: The heater immediately to the left (or at) the house
        # 2. heaters[pos]: The heater immediately to the right of the house
        r = min(house - heaters[pos - 1], heaters[pos] - house)
        
        # The required radius must cover the farthest house
        ans = max(ans, r)
        
    return ans
    # Time: O(n * log(n) + m * log(m))
    # Space: O(m) <- considering the padding heater list
    # n = number of houses
    # m = number of heaters


def main():
    result = find_radius(houses = [1,2,3], heaters = [2])
    print(result) # 1

    result = find_radius(houses = [1,2,3,4], heaters = [1,4])
    print(result) # 1

    result = find_radius(houses = [1,5], heaters = [2])
    print(result) # 3

if __name__ == "__main__":
    main()
