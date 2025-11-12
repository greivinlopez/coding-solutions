# -----------------------------------
# 1352. Product of the Last K Numbers
# -----------------------------------

# Problem: https://leetcode.com/problems/product-of-the-last-k-numbers
#
# Design an algorithm that accepts a stream of integers and retrieves the product
# of the last k integers of the stream.
# 
# Implement the ProductOfNumbers class:
#         
#   * ProductOfNumbers() Initializes the object with an empty stream.
#   * void add(int num) Appends the integer num to the stream.
#   * int getProduct(int k) Returns the product of the last k numbers in the
#     current list. You can assume that always the current list has at least k
#     numbers.
# 
# The test cases are generated so that, at any time, the product of any contiguous
# sequence of numbers will fit into a single 32-bit integer without overflowing.
# 
# Example:
# 
# Input
# ["ProductOfNumbers","add","add","add","add","add","getProduct","getProduct","get
# Product","add","getProduct"]
# [[],[3],[0],[2],[5],[4],[2],[3],[4],[8],[2]]
# Output
# [null,null,null,null,null,null,20,40,0,null,32]
# 
# Explanation
# ProductOfNumbers productOfNumbers = new ProductOfNumbers();
# productOfNumbers.add(3);        // [3]
# productOfNumbers.add(0);        // [3,0]
# productOfNumbers.add(2);        // [3,0,2]
# productOfNumbers.add(5);        // [3,0,2,5]
# productOfNumbers.add(4);        // [3,0,2,5,4]
# productOfNumbers.getProduct(2); // return 20. The product of the last 2 numbers
# is 5 * 4 = 20
# productOfNumbers.getProduct(3); // return 40. The product of the last 3 numbers
# is 2 * 5 * 4 = 40
# productOfNumbers.getProduct(4); // return 0. The product of the last 4 numbers
# is 0 * 2 * 5 * 4 = 0
# productOfNumbers.add(8);        // [3,0,2,5,4,8]
# productOfNumbers.getProduct(2); // return 32. The product of the last 2 numbers
# is 4 * 8 = 32
# 
# 
# Constraints:
#       0 <= num <= 100
#       1 <= k <= 4 * 10⁴
#       At most 4 * 10⁴ calls will be made to add and getProduct.
#       The product of the stream at any point in time will fit in a 32-bit integer.
# 
# Follow-up: Can you implement both GetProduct and Add to work in O(1) time
# complexity instead of O(k) time complexity?


# Solution: https://algo.monster/liteproblems/1352
# Credit: AlgoMonster
class ProductOfNumbers:
    def __init__(self):
        """
        Initialize the data structure.
        Maintains a prefix product array starting with 1.
        """
        # Prefix product array - stores cumulative products
        # Starting with 1 allows for easier calculation of products
        self.prefix_products = [1]

    def add(self, num: int) -> None:
        """
        Add a number to the stream.
      
        Args:
            num: The number to add to the stream
          
        If num is 0, reset the prefix products array since any product 
        containing 0 will be 0.
        Otherwise, append the cumulative product.
        """
        if num == 0:
            # Reset the array when encountering 0
            # Any product containing 0 will be 0
            self.prefix_products = [1]
            return
      
        # Append the cumulative product
        # New product = last cumulative product * current number
        self.prefix_products.append(self.prefix_products[-1] * num)

    def getProduct(self, k: int) -> int:
        """
        Return the product of the last k numbers in the stream.
      
        Args:
            k: Number of recent elements to multiply
          
        Returns:
            The product of the last k numbers, or 0 if any of them is 0
        """
        # If we don't have k elements in our prefix array,
        # it means there was a 0 in the last k elements
        if len(self.prefix_products) <= k:
            return 0
      
        # Calculate product of last k elements using prefix products
        # Product = (product of all elements) / (product of elements before the last k)
        return self.prefix_products[-1] // self.prefix_products[-k - 1]


def main():
    print("TO DO")

if __name__ == "__main__":
    main()
