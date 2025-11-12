# ---------------------------------------------------------
# 1010. Pairs of Songs With Total Durations Divisible by 60
# ---------------------------------------------------------

# Problem: https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60
#
# You are given a list of songs where the ith song has a duration of time[i]
# seconds.
# 
# Return the number of pairs of songs for which their total duration in seconds is
# divisible by 60. Formally, we want the number of indices i, j such that i < j
# with (time[i] + time[j]) % 60 == 0.
# 
# Example 1:
# 
# Input: time = [30,20,150,100,40]
# Output: 3
# 
# Explanation: Three pairs have a total duration divisible by 60:
# (time[0] = 30, time[2] = 150): total duration 180
# (time[1] = 20, time[3] = 100): total duration 120
# (time[1] = 20, time[4] = 40): total duration 60
# 
# Example 2:
# 
# Input: time = [60,60,60]
# Output: 3
# 
# Explanation: All three pairs have a total duration of 120, which is divisible by
# 60.
# 
# 
# Constraints:
#         1 <= time.length <= 6 * 10⁴
#         1 <= time[i] <= 500

from collections import Counter

# Solution: https://algo.monster/liteproblems/1010
# Credit: AlgoMonster
def num_pairs_divisible_by_60(time):
    # Count frequency of each remainder when divided by 60
    remainder_count = Counter(t % 60 for t in time)
    
    # Initialize result counter
    result = 0
    
    # For remainders 1 to 29, pair with their complement (60 - remainder)
    # Each pair sums to 60, making them divisible by 60
    for remainder in range(1, 30):
        complement = 60 - remainder
        result += remainder_count[remainder] * remainder_count[complement]
    
    # Handle special case: remainder 0
    # Songs with remainder 0 can pair with each other
    # Use combination formula: n * (n - 1) / 2
    result += remainder_count[0] * (remainder_count[0] - 1) // 2
    
    # Handle special case: remainder 30
    # Songs with remainder 30 can pair with each other (30 + 30 = 60)
    # Use combination formula: n * (n - 1) / 2
    result += remainder_count[30] * (remainder_count[30] - 1) // 2
    
    return result
    # Time: O(n)
    # Space: O(1)


def main():
    result = num_pairs_divisible_by_60(time = [30,20,150,100,40])
    print(result) # 3

    result = num_pairs_divisible_by_60(time = [60,60,60])
    print(result) # 3

if __name__ == "__main__":
    main()
