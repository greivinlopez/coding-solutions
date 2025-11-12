# ---------------------------------
# 3169. Count Days Without Meetings
# ---------------------------------

# Problem: https://leetcode.com/problems/count-days-without-meetings
#
# You are given a positive integer days representing the total number of days an
# employee is available for work (starting from day 1). You are also given a 2D
# array meetings of size n where, meetings[i] = [start_i, end_i] represents the
# starting and ending days of meeting i (inclusive).
# 
# Return the count of days when the employee is available for work but no meetings
# are scheduled.
# 
# Note: The meetings may overlap.
# 
# Example 1:
# 
# Input: days = 10, meetings = [[5,7],[1,3],[9,10]]
# Output: 2
# 
# Explanation:
# There is no meeting scheduled on the 4th and 8th days.
# 
# Example 2:
# 
# Input: days = 5, meetings = [[2,4],[1,3]]
# Output: 1
# 
# Explanation:
# There is no meeting scheduled on the 5th day.
# 
# Example 3:
# 
# Input: days = 6, meetings = [[1,6]]
# Output: 0
# 
# Explanation:
# Meetings are scheduled for all working days.
# 
# 
# Constraints:
#         1 <= days <= 10^9
#         1 <= meetings.length <= 10^5
#         meetings[i].length == 2
#         1 <= meetings[i][0] <= meetings[i][1] <= days


# Solution: https://youtu.be/VFYTULYpApM
# Credit: Navdeep Singh founder of NeetCode
def count_days(days, meetings):
    meetings.sort()
    
    prev_end = 0
    
    for start, end in meetings:
        start = max(start, prev_end + 1)
        length = end - start + 1
        days -= max(length, 0)
        prev_end = max(prev_end, end)
        
    return days
    # Time: O(n * log(n))
    # Space: O(1)


def main():
    result = count_days(days = 10, meetings = [[5,7],[1,3],[9,10]])
    print(result) # 2

    result = count_days(days = 5, meetings = [[2,4],[1,3]])
    print(result) # 1

    result = count_days(days = 6, meetings = [[1,6]])
    print(result) # 0

if __name__ == "__main__":
    main()
