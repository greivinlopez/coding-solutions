# -------------------------------------------------
# 1359. Count All Valid Pickup and Delivery Options
# -------------------------------------------------

# Problem: https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options
#
# Given n orders, each order consists of a pickup and a delivery service.
# 
# Count all valid pickup/delivery possible sequences such that delivery(i) is
# always after of pickup(i). 
# 
# Since the answer may be too large, return it modulo 10^9 + 7.
# 
# Example 1:
# 
# Input: n = 1
# Output: 1
# 
# Explanation: Unique order (P1, D1), Delivery 1 always is after of Pickup 1.
# 
# Example 2:
# 
# Input: n = 2
# Output: 6
# 
# Explanation: All possible orders:
# (P1,P2,D1,D2), (P1,P2,D2,D1), (P1,D1,P2,D2), (P2,P1,D1,D2), (P2,P1,D2,D1) and
# (P2,D2,P1,D1).
# This is an invalid order (P1,D2,P2,D1) because Pickup 2 is after of Delivery 2.
# 
# Example 3:
# 
# Input: n = 3
# Output: 90
# 
# 
# Constraints:
#         1 <= n <= 500


# Solution: https://youtu.be/OpgslsirW8s
# Credit: Navdeep Singh founder of NeetCode
def count_orders(n):
    slots = 2 * n
    output = 1
    while slots > 0:
        valid_choices = slots * (slots - 1) // 2
        output *= valid_choices
        slots -= 2
    return output % (10**9 + 7)


def main():
    result = count_orders(1)
    print(result) # 1

    result = count_orders(2)
    print(result) # 6

    result = count_orders(3)
    print(result) # 90

if __name__ == "__main__":
    main()
