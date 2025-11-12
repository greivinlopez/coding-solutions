# --------------------------------------
# 599. Minimum Index Sum of Two Lists 🍗
# --------------------------------------

# Problem: https://leetcode.com/problems/minimum-index-sum-of-two-lists
#
# Given two arrays of strings list1 and list2, find the common strings with the
# least index sum.
# 
# A common string is a string that appeared in both list1 and list2.
# 
# A common string with the least index sum is a common string such that if it
# appeared at list1[i] and list2[j] then i + j should be the minimum value among
# all the other common strings.
# 
# Return all the common strings with the least index sum. Return the answer in any
# order.
# 
# Example 1:
# 
# Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 =
# ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
# Output: ["Shogun"]
# 
# Explanation: The only common string is "Shogun".
# 
# Example 2:
# 
# Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 =
# ["KFC","Shogun","Burger King"]
# Output: ["Shogun"]
# 
# Explanation: The common string with the least index sum is "Shogun" with index
# sum = (0 + 1) = 1.
# 
# Example 3:
# 
# Input: list1 = ["happy","sad","good"], list2 = ["sad","happy","good"]
# Output: ["sad","happy"]
# 
# Explanation: There are three common strings:
# "happy" with index sum = (0 + 1) = 1.
# "sad" with index sum = (1 + 0) = 1.
# "good" with index sum = (2 + 2) = 4.
# The strings with the least index sum are "sad" and "happy".
# 
# 
# Constraints:
#         1 <= list1.length, list2.length <= 1000
#         1 <= list1[i].length, list2[i].length <= 30
#         list1[i] and list2[i] consist of spaces ' ' and English letters.
#         All the strings of list1 are unique.
#         All the strings of list2 are unique.
#         There is at least a common string between list1 and list2.


# Solution: https://algo.monster/liteproblems/599
# Credit: AlgoMonster
def find_restaurant(list1, list2):
    # Create a dictionary mapping restaurant names to their indices in list2
    restaurant_to_index = {restaurant: index for index, restaurant in enumerate(list2)}
    
    # Initialize result list to store restaurants with minimum index sum
    result = []
    
    # Initialize minimum index sum to infinity
    min_index_sum = float('inf')
    
    # Iterate through list1 with index
    for index1, restaurant in enumerate(list1):
        # Check if current restaurant exists in list2
        if restaurant in restaurant_to_index:
            # Get the index of restaurant in list2
            index2 = restaurant_to_index[restaurant]
            
            # Calculate the sum of indices
            current_sum = index1 + index2
            
            # If current sum is less than minimum, update minimum and reset result
            if current_sum < min_index_sum:
                min_index_sum = current_sum
                result = [restaurant]
            # If current sum equals minimum, add restaurant to result
            elif current_sum == min_index_sum:
                result.append(restaurant)
    
    return result
    # Time: O(n + m)
    # Space: O(m)
    # n = the length of list1
    # m = the length of list


def main():
    list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
    list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
    result = find_restaurant(list1, list2)
    print(result) # ["Shogun"]

    list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
    list2 = ["KFC","Shogun","Burger King"]
    result = find_restaurant(list1, list2)
    print(result) # ["Shogun"]

    list1 = ["happy","sad","good"]
    list2 = ["sad","happy","good"]
    result = find_restaurant(list1, list2)
    print(result) # ["sad", "happy"]

if __name__ == "__main__":
    main()
