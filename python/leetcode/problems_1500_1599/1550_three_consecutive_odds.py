# ----------------------------
# 1550. Three Consecutive Odds
# ----------------------------

# Problem: https://leetcode.com/problems/three-consecutive-odds
#
# Given an integer array arr, return true if there are three consecutive odd
# numbers in the array. Otherwise, return false.
# 
# Example 1:
# 
# Input: arr = [2,6,4,1]
# Output: false
# 
# Explanation: There are no three consecutive odds.
# 
# Example 2:
# 
# Input: arr = [1,2,34,3,4,5,7,23,12]
# Output: true
# 
# Explanation: [5,7,23] are three consecutive odds.
# 
# 
# Constraints:
#         1 <= arr.length <= 1000
#         1 <= arr[i] <= 1000


# Solution: https://algo.monster/liteproblems/1550
# Credit: AlgoMonster
def three_consecutive_odds(arr):
    # Counter to track consecutive odd numbers
    consecutive_odd_count = 0
    
    # Iterate through each element in the array
    for number in arr:
        # Check if the current number is odd using bitwise AND
        # (odd numbers have LSB = 1, even numbers have LSB = 0)
        if number & 1:
            # Increment counter for consecutive odd numbers
            consecutive_odd_count += 1
            
            # If we found 3 consecutive odd numbers, return True
            if consecutive_odd_count == 3:
                return True
        else:
            # Reset counter when we encounter an even number
            consecutive_odd_count = 0
    
    # No three consecutive odd numbers found
    return False
    # Time: O(n)
    # Space: O(1)

# One liner solution
# Solution: https://leetcode.com/problems/three-consecutive-odds/solutions/6732151/3-approaches-with-images-example-walkthr-7c05
# Credit: Sung Jinwoo -> https://leetcode.com/u/LeadingTheAbyss/
def three_consecutive_odds_short(arr):
    return '111' in ''.join(str(x & 1) for x in arr)
    # Time: O(n)
    # Space: O(1)


def main():
    result = three_consecutive_odds(arr = [2,6,4,1])
    print(result) # False

    result = three_consecutive_odds(arr = [1,2,34,3,4,5,7,23,12])
    print(result) # True

if __name__ == "__main__":
    main()
