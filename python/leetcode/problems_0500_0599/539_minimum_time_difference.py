# ----------------------------
# 539. Minimum Time Difference
# ----------------------------

# Problem: https://leetcode.com/problems/minimum-time-difference
#
# Given a list of 24-hour clock time points in "HH:MM" format, return the minimum
# minutes difference between any two time-points in the list.
# 
# Example 1:
# 
# Input: timePoints = ["23:59","00:00"]
# Output: 1
# 
# Example 2:
# 
# Input: timePoints = ["00:00","23:59","00:00"]
# Output: 0
# 
# 
# Constraints:
#         2 <= timePoints.length <= 2 * 10^4
#         timePoints[i] is in the format "HH:MM".


# Solution: https://youtu.be/LVBDzeUmNIQ
# Credit: Navdeep Singh founder of NeetCode
def find_min_difference(timePoints):
    def time_to_min(t):
        hour, minute = map(int, t.split(":"))
        return 60 * hour + minute

    exists = [False] * (60 * 24)
    first_m, last_m = 60 * 24, 0
    for t in timePoints:
        m = time_to_min(t)
        if exists[m]:
            return 0
        exists[m] = True
        first_m = min(first_m, m)
        last_m = max(last_m, m)

    res = (
        60 * 24 -
        last_m +
        first_m
    )
    prev_m = first_m
    for m in range(first_m + 1, len(exists)):
        if exists[m]:
            diff = m - prev_m
            res = min(res, diff)
            prev_m = m
    
    return res
    # Time: O(n) 
    # Space: O(1)


def main():
    result = find_min_difference(timePoints = ["23:59","00:00"])
    print(result) # 1

    result = find_min_difference(timePoints = ["00:00","23:59","00:00"])
    print(result) # 0

if __name__ == "__main__":
    main()
