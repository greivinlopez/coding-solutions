# ----------------------------------------
# 1691. Maximum Height by Stacking Cuboids 
# ----------------------------------------

# Problem: https://leetcode.com/problems/maximum-height-by-stacking-cuboids
#
# Given n cuboids where the dimensions of the ith cuboid is cuboids[i] = [widthᵢ,
# lengthᵢ, heightᵢ] (0-indexed). Choose a subset of cuboids and place them on each
# other.
# 
# You can place cuboid i on cuboid j if widthᵢ <= widthⱼ and lengthᵢ <= lengthⱼ
# and heightᵢ <= heightⱼ. You can rearrange any cuboid's dimensions by rotating it
# to put it on another cuboid.
# 
# Return the maximum height of the stacked cuboids.
# 
# Example 1:
# 
# Input: cuboids = [[50,45,20],[95,37,53],[45,23,12]]
# Output: 190
# 
# Explanation:
# Cuboid 1 is placed on the bottom with the 53x37 side facing down with height 95.
# Cuboid 0 is placed next with the 45x20 side facing down with height 50.
# Cuboid 2 is placed next with the 23x12 side facing down with height 45.
# The total height is 95 + 50 + 45 = 190.
# 
# Example 2:
# 
# Input: cuboids = [[38,25,45],[76,35,3]]
# Output: 76
# 
# Explanation:
# You can't place any of the cuboids on the other.
# We choose cuboid 1 and rotate it so that the 35x3 side is facing down and its
# height is 76.
# 
# Example 3:
# 
# Input: cuboids = [[7,11,17],[7,17,11],[11,7,17],[11,17,7],[17,7,11],[17,11,7]]
# Output: 102
# 
# Explanation:
# After rearranging the cuboids, you can see that all cuboids have the same
# dimension.
# You can place the 11x7 side down on all cuboids so their heights are 17.
# The maximum height of stacked cuboids is 6 * 17 = 102.
# 
# 
# Constraints:
#         n == cuboids.length
#         1 <= n <= 100
#         1 <= widthᵢ, lengthᵢ, heightᵢ <= 100


# Solution: https://algo.monster/liteproblems/1691
# Credit: AlgoMonster
def max_height(cuboids):
    # Sort each cuboid's dimensions in ascending order
    # This ensures we can use any dimension as height while maintaining validity
    for cuboid in cuboids:
        cuboid.sort()
    
    # Sort all cuboids lexicographically
    # This helps establish a potential stacking order
    cuboids.sort()
    
    num_cuboids = len(cuboids)
    
    # dp[i] represents the maximum height achievable with cuboid i at the top
    dp = [0] * num_cuboids
    
    # Process each cuboid as a potential top of the stack
    for i in range(num_cuboids):
        # Check all previous cuboids as potential bases
        for j in range(i):
            # A cuboid j can be placed below cuboid i if:
            # - width of j <= width of i (cuboids[j][1] <= cuboids[i][1])
            # - depth of j <= depth of i (cuboids[j][2] <= cuboids[i][2])
            # Note: length is already satisfied due to sorting
            if (cuboids[j][1] <= cuboids[i][1] and 
                cuboids[j][2] <= cuboids[i][2]):
                # Update maximum height if stacking on cuboid j is better
                dp[i] = max(dp[i], dp[j])
        
        # Add current cuboid's height (largest dimension after sorting)
        dp[i] += cuboids[i][2]
    
    # Return the maximum height among all possible configurations
    return max(dp)
    # Time: O(n²)
    # Space: O(n)


def main():
    result = max_height(cuboids = [[50,45,20],[95,37,53],[45,23,12]])
    print(result) # 190

    result = max_height(cuboids = [[38,25,45],[76,35,3]])
    print(result) # 76

    result = max_height(cuboids = [[7,11,17],[7,17,11],[11,7,17],[11,17,7],[17,7,11],[17,11,7]])
    print(result) # 102

if __name__ == "__main__":
    main()
