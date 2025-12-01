# -------------------------
# 1711. Count Good Meals 🍽️
# -------------------------

# Problem: https://leetcode.com/problems/count-good-meals
#
# A good meal is a meal that contains exactly two different food items with a sum
# of deliciousness equal to a power of two.
# 
# You can pick any two different foods to make a good meal.
# 
# Given an array of integers deliciousness where deliciousness[i] is the
# deliciousness of the i​​​​​​th​​​​​​​​ item of food, return the number of
# different good meals you can make from this list modulo 10⁹ + 7.
# 
# Note that items with different indices are considered different even if they
# have the same deliciousness value.
# 
# Example 1:
# 
# Input: deliciousness = [1,3,5,7,9]
# Output: 4
# 
# Explanation: The good meals are (1,3), (1,7), (3,5) and, (7,9).
# Their respective sums are 4, 8, 8, and 16, all of which are powers of 2.
# 
# Example 2:
# 
# Input: deliciousness = [1,1,1,3,3,3,7]
# Output: 15
# 
# Explanation: The good meals are (1,1) with 3 ways, (1,3) with 9 ways, and (1,7)
# with 3 ways.
# 
# 
# Constraints:
#         1 <= deliciousness.length <= 10⁵
#         0 <= deliciousness[i] <= 2²⁰


# Solution: https://leetcode.com/problems/count-good-meals/solutions/2957239/clean-code-on-by-dawit-melka-73sl
# Credit: Dawit Melka -> https://leetcode.com/u/Dawit-Melka/
def count_pairs(deliciousness):
    count = {}
    res = 0
    MOD = pow(10, 9) + 7

    for rate in deliciousness:
        for i in range(22):
            sqr = pow(2, i)
            target = sqr - rate
            if target in count:
                res += count[target]
        if rate in count:
            count[rate] += 1
        else:
            count[rate] = 1
    
    return res % MOD
    # Time: O(n)
    # Space: O(n)


def main():
    result = count_pairs(deliciousness = [1,3,5,7,9])
    print(result) # 8

    result = count_pairs(deliciousness = [1,1,1,3,3,3,7])
    print(result) # 91

if __name__ == "__main__":
    main()
