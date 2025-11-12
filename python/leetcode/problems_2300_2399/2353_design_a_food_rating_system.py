# ------------------------------------
# 2353. Design a Food Rating System 🍥
# ------------------------------------

# Problem: https://leetcode.com/problems/design-a-food-rating-system
#
# Design a food rating system that can do the following:
#         
#   * Modify the rating of a food item listed in the system.
#   * Return the highest-rated food item for a type of cuisine in the system.
# 
# Implement the FoodRatings class:
# 
#   * FoodRatings(String[] foods, String[] cuisines, int[] ratings)
#     Initializes the system. The food items are described by foods, cuisines and
#     ratings, all of which have a length of n.
# 
#                 foods[i] is the name of the ith food,
#                 cuisines[i] is the type of cuisine of the ith food, and
#                 ratings[i] is the initial rating of the ith food.
#
#    * void changeRating(String food, int newRating) Changes the rating of the
#      food item with the name food.
#    * String highestRated(String cuisine) Returns the name of the food item
#      that has the highest rating for the given type of cuisine. If there is a tie,
#      return the item with the lexicographically smaller name.
# 
# Note that a string x is lexicographically smaller than string y if x comes
# before y in dictionary order, that is, either x is a prefix of y, or if i is the
# first position such that x[i] != y[i], then x[i] comes before y[i] in alphabetic
# order.
# 
# Example 1:
# 
# Input
# ["FoodRatings", "highestRated", "highestRated", "changeRating", "highestRated",
# "changeRating", "highestRated"]
# [[["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"], ["korean",
# "japanese", "japanese", "greek", "japanese", "korean"], [9, 12, 8, 15, 14, 7]],
# ["korean"], ["japanese"], ["sushi", 16], ["japanese"], ["ramen", 16],
# ["japanese"]]
# Output
# [null, "kimchi", "ramen", null, "sushi", null, "ramen"]
# 
# Explanation
# FoodRatings foodRatings = new FoodRatings(["kimchi", "miso", "sushi",
# "moussaka", "ramen", "bulgogi"], ["korean", "japanese", "japanese", "greek",
# "japanese", "korean"], [9, 12, 8, 15, 14, 7]);
# foodRatings.highestRated("korean"); // return "kimchi"
#                                     // "kimchi" is the highest rated korean food
# with a rating of 9.
# foodRatings.highestRated("japanese"); // return "ramen"
#                                       // "ramen" is the highest rated japanese
# food with a rating of 14.
# foodRatings.changeRating("sushi", 16); // "sushi" now has a rating of 16.
# foodRatings.highestRated("japanese"); // return "sushi"
#                                       // "sushi" is the highest rated japanese
# food with a rating of 16.
# foodRatings.changeRating("ramen", 16); // "ramen" now has a rating of 16.
# foodRatings.highestRated("japanese"); // return "ramen"
#                                       // Both "sushi" and "ramen" have a rating
# of 16.
#                                       // However, "ramen" is lexicographically
# smaller than "sushi".
# 
# 
# Constraints:
#         1 <= n <= 2 * 10⁴
#         n == foods.length == cuisines.length == ratings.length
#         1 <= foods[i].length, cuisines[i].length <= 10
#         foods[i], cuisines[i] consist of lowercase English letters.
#         1 <= ratings[i] <= 10⁸
#         All the strings in foods are distinct.
#         food will be the name of a food item in the system across all calls to
# changeRating.
#         cuisine will be a type of cuisine of at least one food item in the
# system across all calls to highestRated.
#         At most 2 * 10⁴ calls in total will be made to changeRating and
# highestRated.

# You must install sortedcontainers library
#   pip install sortedcontainers

from sortedcontainers import SortedSet
from collections import defaultdict

# Solution: https://youtu.be/Ikp8SgbgbEo
# Credit: Navdeep Singh founder of NeetCode
class FoodRatings:
    # O(n log n)
    def __init__(self, foods, cuisines, ratings):
        self.cuisines_food = defaultdict(SortedSet)
        self.cuisines = {}
        self.ratings = {}
        for i in range(len(foods)):
            self.cuisines_food[cuisines[i]].add((-ratings[i], foods[i]))
            self.cuisines[foods[i]] = cuisines[i]
            self.ratings[foods[i]] = ratings[i]

    # O(log n)
    def changeRating(self, food, newRating):
        c = self.cuisines[food]
        r = self.ratings[food]
        self.cuisines_food[c].remove((-r, food))
        self.cuisines_food[c].add((-newRating, food))
        self.ratings[food] = newRating

    # O(1)
    def highestRated(self, cuisine):
        return self.cuisines_food[cuisine][0][1]


def main():
    foodRatings = FoodRatings(["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"], 
                              ["korean", "japanese", "japanese", "greek", "japanese", "korean"], 
                              [9, 12, 8, 15, 14, 7])
    result = foodRatings.highestRated("korean")
    print(result)  # "kimchi"

    result = foodRatings.highestRated("japanese")
    print(result)  # "ramen"

    foodRatings.changeRating("sushi", 16)
    result = foodRatings.highestRated("japanese")
    print(result)  # "sushi"

    foodRatings.changeRating("ramen", 16)
    result = foodRatings.highestRated("japanese")
    print(result)  # "ramen"

if __name__ == "__main__":
    main()
