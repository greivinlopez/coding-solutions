# ---------------------------------------------------
# 2115. Find All Possible Recipes from Given Supplies
# ---------------------------------------------------

# Problem: https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies
#
# You have information about n different recipes. You are given a string array
# recipes and a 2D string array ingredients. The ith recipe has the name
# recipes[i], and you can create it if you have all the needed ingredients from
# ingredients[i]. A recipe can also be an ingredient for other recipes, i.e.,
# ingredients[i] may contain a string that is in recipes.
# 
# You are also given a string array supplies containing all the ingredients that
# you initially have, and you have an infinite supply of all of them.
# 
# Return a list of all the recipes that you can create. You may return the answer
# in any order.
# 
# Note that two recipes may contain each other in their ingredients.
# 
# Example 1:
# 
# Input: recipes = ["bread"], ingredients = [["yeast","flour"]], supplies =
# ["yeast","flour","corn"]
# Output: ["bread"]
# 
# Explanation:
# We can create "bread" since we have the ingredients "yeast" and "flour".
# 
# Example 2:
# 
# Input: recipes = ["bread","sandwich"], ingredients =
# [["yeast","flour"],["bread","meat"]], supplies = ["yeast","flour","meat"]
# Output: ["bread","sandwich"]
# 
# Explanation:
# We can create "bread" since we have the ingredients "yeast" and "flour".
# We can create "sandwich" since we have the ingredient "meat" and can create the
# ingredient "bread".
# 
# Example 3:
# 
# Input: recipes = ["bread","sandwich","burger"], ingredients =
# [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]], supplies =
# ["yeast","flour","meat"]
# Output: ["bread","sandwich","burger"]
# 
# Explanation:
# We can create "bread" since we have the ingredients "yeast" and "flour".
# We can create "sandwich" since we have the ingredient "meat" and can create the
# ingredient "bread".
# We can create "burger" since we have the ingredient "meat" and can create the
# ingredients "bread" and "sandwich".
# 
# 
# Constraints:
#         n == recipes.length == ingredients.length
#         1 <= n <= 100
#         1 <= ingredients[i].length, supplies.length <= 100
#         1 <= recipes[i].length, ingredients[i][j].length, supplies[k].length <=
# 10
#         recipes[i], ingredients[i][j], and supplies[k] consist only of lowercase
# English letters.
#         All the values of recipes and supplies combined are unique.
#         Each ingredients[i] does not contain any duplicate values.


# Solution: https://youtu.be/AQrsAc3EcyQ
# Credit: Navdeep Singh founder of NeetCode
def find_all_recipes(recipes, ingredients, supplies):
    can_cook = {s: True for s in supplies}
    recipe_index = {r: i for i, r in enumerate(recipes)}

    def dfs(r):
        if r in can_cook:
            return can_cook[r]
        if r not in recipe_index:
            return False

        can_cook[r] = False  # circular dependency check

        for nei in ingredients[recipe_index[r]]:
            if not dfs(nei):
                return False

        can_cook[r] = True
        return can_cook[r]

    return [r for r in recipes if dfs(r)]
    # Time: O(v + e)    v = recipies + ingredients + supplies, e = number of dependencies
    # Space: O(v + e)


def main():
    recipes = ["bread"]
    ingredients = [["yeast","flour"]]
    supplies = ["yeast","flour","corn"]
    result = find_all_recipes(recipes, ingredients, supplies)
    print(result) # ["bread"]

    recipes = ["bread","sandwich"]
    ingredients = [["yeast","flour"],["bread","meat"]]
    supplies = ["yeast","flour","meat"]
    result = find_all_recipes(recipes, ingredients, supplies)
    print(result) # ["bread","sandwich"]

    recipes = ["bread","sandwich","burger"]
    ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]]
    supplies = ["yeast","flour","meat"]
    result = find_all_recipes(recipes, ingredients, supplies)
    print(result) # ["bread","sandwich","burger"]

if __name__ == "__main__":
    main()
