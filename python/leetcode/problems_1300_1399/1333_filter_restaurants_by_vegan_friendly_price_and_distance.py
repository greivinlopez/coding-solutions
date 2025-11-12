# --------------------------------------------------------------
# 1333. Filter Restaurants by Vegan-Friendly, Price and Distance
# --------------------------------------------------------------

# Problem: https://leetcode.com/problems/filter-restaurants-by-vegan-friendly-price-and-distance
#
# Given the array restaurants where  restaurants[i] = [idᵢ, ratingᵢ,
# veganFriendlyᵢ, priceᵢ, distanceᵢ]. You have to filter the restaurants using
# three filters.
# 
# The veganFriendly filter will be either true (meaning you should only include
# restaurants with veganFriendlyᵢ set to true) or false (meaning you can include
# any restaurant). In addition, you have the filters maxPrice and
# maxDistance which are the maximum value for price and distance of restaurants
# you should consider respectively.
# 
# Return the array of restaurant IDs after filtering, ordered by rating from
# highest to lowest. For restaurants with the same rating, order them by id from
# highest to lowest. For simplicity veganFriendlyᵢ and veganFriendly take value 1
# when it is true, and 0 when it is false.
# 
# Example 1:
# 
# Input: restaurants =
# [[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]],
# veganFriendly = 1, maxPrice = 50, maxDistance = 10
# Output: [3,1,5]
# 
# Explanation:
# The restaurants are:
# Restaurant 1 [id=1, rating=4, veganFriendly=1, price=40, distance=10]
# Restaurant 2 [id=2, rating=8, veganFriendly=0, price=50, distance=5]
# Restaurant 3 [id=3, rating=8, veganFriendly=1, price=30, distance=4]
# Restaurant 4 [id=4, rating=10, veganFriendly=0, price=10, distance=3]
# Restaurant 5 [id=5, rating=1, veganFriendly=1, price=15, distance=1]
# After filter restaurants with veganFriendly = 1, maxPrice = 50 and maxDistance =
# 10 we have restaurant 3, restaurant 1 and restaurant 5 (ordered by rating from
# highest to lowest).
# 
# Example 2:
# 
# Input: restaurants =
# [[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]],
# veganFriendly = 0, maxPrice = 50, maxDistance = 10
# Output: [4,3,2,1,5]
# 
# Explanation: The restaurants are the same as in example 1, but in this case the
# filter veganFriendly = 0, therefore all restaurants are considered.
# 
# Example 3:
# 
# Input: restaurants =
# [[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]],
# veganFriendly = 0, maxPrice = 30, maxDistance = 3
# Output: [4,5]
# 
# 
# Constraints:
#         1 <= restaurants.length <= 10^4
#         restaurants[i].length == 5
#         1 <= idᵢ, ratingᵢ, priceᵢ, distanceᵢ <= 10^5
#         1 <= maxPrice, maxDistance <= 10^5
#         veganFriendlyᵢ and veganFriendly are 0 or 1.
#         All idᵢ are distinct.


# Solution: https://algo.monster/liteproblems/1333
# Credit: AlgoMonster
def filter_restaurants(
    restaurants,
    veganFriendly,
    maxPrice,
    maxDistance,
):
    # Sort restaurants by rating (descending) and then by ID (descending)
    # x[1] is rating, x[0] is restaurant ID
    restaurants.sort(key=lambda restaurant: (-restaurant[1], -restaurant[0]))
    
    # Store filtered restaurant IDs
    filtered_ids = []
    
    # Iterate through sorted restaurants and apply filters
    for restaurant_id, rating, is_vegan, price, distance in restaurants:
        # Check if restaurant meets all criteria:
        # - Vegan requirement: restaurant's vegan status >= required vegan status
        # - Price constraint: restaurant's price <= maximum price
        # - Distance constraint: restaurant's distance <= maximum distance
        if (is_vegan >= veganFriendly and 
            price <= maxPrice and 
            distance <= maxDistance):
            filtered_ids.append(restaurant_id)
    
    return filtered_ids
    # Time: O(n log n)
    # Space: O(n)


def main():
    result = filter_restaurants(restaurants = [[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]], 
                                veganFriendly = 1, 
                                maxPrice = 50, 
                                maxDistance = 10)
    print(result) # [3, 1, 5]

    result = filter_restaurants(restaurants = [[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]], 
                                veganFriendly = 0, 
                                maxPrice = 50, 
                                maxDistance = 10)
    print(result) # [4, 3, 2, 1, 5]

    result = filter_restaurants(restaurants = [[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]], 
                                veganFriendly = 0, 
                                maxPrice = 30, 
                                maxDistance = 3)
    print(result) # [4, 5]

if __name__ == "__main__":
    main()
