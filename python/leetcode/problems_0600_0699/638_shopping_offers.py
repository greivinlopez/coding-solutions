# --------------------
# 638. Shopping Offers
# --------------------

# Problem: https://leetcode.com/problems/shopping-offers
#
# In LeetCode Store, there are n items to sell. Each item has a price. However,
# there are some special offers, and a special offer consists of one or more
# different kinds of items with a sale price.
# 
# You are given an integer array price where price[i] is the price of the iᵗʰ
# item, and an integer array needs where needs[i] is the number of pieces of the
# iᵗʰ item you want to buy.
# 
# You are also given an array special where special[i] is of size n + 1 where
# special[i][j] is the number of pieces of the jᵗʰ item in the iᵗʰ offer and
# special[i][n] (i.e., the last integer in the array) is the price of the iᵗʰ
# offer.
# 
# Return the lowest price you have to pay for exactly certain items as given,
# where you could make optimal use of the special offers. You are not allowed to
# buy more items than you want, even if that would lower the overall price. You
# could use any of the special offers as many times as you want.
# 
# Example 1:
# 
# Input: price = [2,5], special = [[3,0,5],[1,2,10]], needs = [3,2]
# Output: 14
# 
# Explanation: There are two kinds of items, A and B. Their prices are $2 and $5
# respectively.
# In special offer 1, you can pay $5 for 3A and 0B
# In special offer 2, you can pay $10 for 1A and 2B.
# You need to buy 3A and 2B, so you may pay $10 for 1A and 2B (special offer #2),
# and $4 for 2A.
# 
# Example 2:
# 
# Input: price = [2,3,4], special = [[1,1,0,4],[2,2,1,9]], needs = [1,2,1]
# Output: 11
# 
# Explanation: The price of A is $2, and $3 for B, $4 for C.
# You may pay $4 for 1A and 1B, and $9 for 2A ,2B and 1C.
# You need to buy 1A ,2B and 1C, so you may pay $4 for 1A and 1B (special offer
# #1), and $3 for 1B, $4 for 1C.
# You cannot add more items, though only $9 for 2A ,2B and 1C.
# 
# 
# Constraints:
#   n == price.length == needs.length
#   1 <= n <= 6
#   0 <= price[i], needs[i] <= 10
#   1 <= special.length <= 100
#   special[i].length == n + 1
#   0 <= special[i][j] <= 50
#   The input is generated that at least one of special[i][j] is non-zero 
#   for 0 <= j <= n - 1.

from functools import cache

# Solution: https://algo.monster/liteproblems/638
# Credit: AlgoMonster
def shopping_offers(price, special, needs):
    @cache
    def calculate_min_cost(current_state):
        # Calculate the cost of buying remaining items individually
        individual_cost = 0
        for item_idx, item_price in enumerate(price):
            # Extract quantity needed for this item from the bit-packed state
            quantity_needed = (current_state >> (item_idx * BITS_PER_ITEM)) & 0xF
            individual_cost += item_price * quantity_needed
        
        min_cost = individual_cost
        
        # Try applying each special offer
        for offer in special:
            next_state = current_state
            can_apply_offer = True
            
            # Check if we can apply this offer (enough items needed)
            for item_idx in range(len(needs)):
                current_need = (current_state >> (item_idx * BITS_PER_ITEM)) & 0xF
                
                # If we need fewer items than the offer provides, skip this offer
                if current_need < offer[item_idx]:
                    can_apply_offer = False
                    break
                
                # Subtract the offer quantities from the next state
                next_state -= offer[item_idx] << (item_idx * BITS_PER_ITEM)
            
            # If offer is applicable, calculate cost with this offer
            if can_apply_offer:
                offer_price = offer[-1]  # Last element is the offer's price
                min_cost = min(min_cost, offer_price + calculate_min_cost(next_state))
        
        return min_cost
    
    # Pack the needs into a single integer using 4 bits per item
    BITS_PER_ITEM = 4
    initial_state = 0
    for item_idx, quantity_needed in enumerate(needs):
        initial_state |= quantity_needed << (item_idx * BITS_PER_ITEM)
    
    return calculate_min_cost(initial_state)
    # Time: O(n * k * mⁿ)
    # Space: O(n * mⁿ)


def main():
    result = shopping_offers(price = [2,5], special = [[3,0,5],[1,2,10]], needs = [3,2])
    print(result) # 14

    result = shopping_offers(price = [2,3,4], special = [[1,1,0,4],[2,2,1,9]], needs = [1,2,1])
    print(result) # 11

if __name__ == "__main__":
    main()
