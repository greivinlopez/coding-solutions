# -------------
# 135. Candy 🍬
# -------------

# Problem: https://leetcode.com/problems/candy/
# 
# There are n children standing in a line. Each child is assigned a rating value 
# given in the integer array ratings.
# 
# You are giving candies to these children subjected to the following requirements:
# 
# - Each child must have at least one candy.
# - Children with a higher rating get more candies than their neighbors.
# 
# Return the minimum number of candies you need to have to distribute the candies 
# to the children.

# Solution: https://youtu.be/1IzCRCcK17A
# Credit: Navdeep Singh founder of NeetCode
def candy(ratings):
    n = len(ratings)
    # Initialize with one candy becuase each child must have at least one candy.
    candies = [1] * n 

    # Iterate from left to right 
    for i in range(1, n):
        # Check if current rating is greater than left neighbor
        if ratings[i] > ratings[i - 1]:
            # Rating is higher so deserves more candy than left neighbor
            candies[i] = candies[i - 1] + 1

    # Iterate from right to left
    for i in range(n - 2, -1, -1):
        # Check if current rating is greater than right neighbor
        if ratings[i] > ratings[i + 1]:
            # Take max to check if the value is already greater than its right neighbor + 1.
            candies[i] = max(candies[i], candies[i + 1] + 1)
    
    return sum(candies)


def main():
    result = candy(ratings = [1,0,2])
    print(result) # 5

    result = candy(ratings = [1,2,2])
    print(result) # 4

if __name__ == "__main__":
    main()