# ----------------------------------
# 1268. Search Suggestions System 🔍
# ----------------------------------

# Problem: https://leetcode.com/problems/search-suggestions-system
#
# You are given an array of strings products and a string searchWord.
# 
# Design a system that suggests at most three product names from products after
# each character of searchWord is typed. Suggested products should have common
# prefix with searchWord. If there are more than three products with a common
# prefix return the three lexicographically minimums products.
# 
# Return a list of lists of the suggested products after each character of
# searchWord is typed.
# 
# Example 1:
# 
# Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord
# = "mouse"
# Output: [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse
# ","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]
# 
# Explanation: products sorted lexicographically =
# ["mobile","moneypot","monitor","mouse","mousepad"].
# After typing m and mo all products match and we show user
# ["mobile","moneypot","monitor"].
# After typing mou, mous and mouse the system suggests ["mouse","mousepad"].
# 
# Example 2:
# 
# Input: products = ["havana"], searchWord = "havana"
# Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
# 
# Explanation: The only word "havana" will be always suggested while typing the
# search word.
# 
# 
# Constraints:
#         1 <= products.length <= 1000
#         1 <= products[i].length <= 3000
#         1 <= sum(products[i].length) <= 2 * 10⁴
#         All the strings of products are unique.
#         products[i] consists of lowercase English letters.
#         1 <= searchWord.length <= 1000
#         searchWord consists of lowercase English letters.


# Solution: https://youtu.be/D4T2N0yAr20
# Credit: Navdeep Singh founder of NeetCode
def suggested_products(products, searchWord):
    res = []
    products.sort()
    
    l, r = 0, len(products) - 1
    for i in range(len(searchWord)):
        c = searchWord[i]
        
        while l <= r and (len(products[l]) <= i or products[l][i] != c):
            l += 1
        while l <= r and (len(products[r]) <= i or products[r][i] != c):
            r -= 1
        
        res.append([])
        remain = r - l + 1
        for j in range(min(3, remain)):
            res[-1].append(products[l + j])
    
    return res
    # Time: O(n * log(n) + m * l)
    # Space: O(1)
    # n = number of products
    # m = length of the search word
    # l = average length of a product


def main():
    result = suggested_products(products = ["mobile",
                                            "mouse",
                                            "moneypot",
                                            "monitor",
                                            "mousepad"], 
                                            searchWord = "mouse")
    print(result) # [['mobile', 'moneypot', 'monitor'], ['mobile', 'moneypot', 'monitor'], ['mouse', 'mousepad'], ['mouse', 'mousepad'], ['mouse', 'mousepad']]

    result = suggested_products(products = ["havana"], searchWord = "havana")
    print(result) # [['havana'], ['havana'], ['havana'], ['havana'], ['havana'], ['havana']]

if __name__ == "__main__":
    main()
