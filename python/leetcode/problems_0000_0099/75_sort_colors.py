# -----------------------
# 75. Sort Colors 🟥⬜🟦
# -----------------------

# Problem: https://leetcode.com/problems/sort-colors/
# 
# Given an array nums with n objects colored red, white, or blue, sort them 
# in-place so that objects of the same color are adjacent, with the colors 
# in the order red, white, and blue.
# 
# We will use the integers 0, 1, and 2 to represent the color red, white, 
# and blue, respectively.
# 
# You must solve this problem without using the library's sort function.

# Solution: https://www.youtube.com/watch?v=4xbWSRZHqac
# Credit: Navdeep Singh founder of NeetCode
def sort_colors(nums):
    l, r = 0, len(nums)-1
    i = 0

    while i <= r:
        if nums[i]==0:
            nums[l],nums[i] = nums[i],nums[l]
            l+=1
        elif nums[i]==2:
            nums[i],nums[r] = nums[r],nums[i]
            r-=1
            i-=1
        i+=1

# Solution: https://youtu.be/1DJ2kGoNPWQ
# Credit: Greg Hogg
def sort_colors_alt(nums):
    # Time: O(n)
    # Space: O(1)
    counts = [0, 0, 0]

    for color in nums:
        counts[color] += 1
    
    R, W, B = counts
    
    nums[:R]    = [0] * R
    nums[R:R+W] = [1] * W 
    nums[R+W:]  = [2] * B

def main():
    matrix = [2,0,2,1,1,0]
    sort_colors(matrix) # [0,0,1,1,2,2]
    print(matrix)
    matrix = [2,0,1]
    sort_colors(matrix) # [0,1,2]
    print(matrix)

if __name__ == "__main__":
    main()