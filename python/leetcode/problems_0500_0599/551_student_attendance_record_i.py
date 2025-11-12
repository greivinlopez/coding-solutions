# --------------------------------
# 551. Student Attendance Record I
# --------------------------------

# Problem: https://leetcode.com/problems/student-attendance-record-i
#
# You are given a string s representing an attendance record for a student where
# each character signifies whether the student was absent, late, or present on
# that day. The record only contains the following three characters:
# 
#         'A': Absent.
#         'L': Late.
#         'P': Present.
# 
# The student is eligible for an attendance award if they meet both of the
# following criteria:
# 
#   * The student was absent ('A') for strictly fewer than 2 days total.
#   * The student was never late ('L') for 3 or more consecutive days.
# 
# Return true if the student is eligible for an attendance award, or false
# otherwise.
# 
# Example 1:
# 
# Input: s = "PPALLP"
# Output: true
# 
# Explanation: The student has fewer than 2 absences and was never late 3 or more
# consecutive days.
# 
# Example 2:
# 
# Input: s = "PPALLL"
# Output: false
# 
# Explanation: The student was late 3 consecutive days in the last 3 days, so is
# not eligible for the award.
# 
# 
# Constraints:
#         1 <= s.length <= 1000
#         s[i] is either 'A', 'L', or 'P'.


# Solution: https://algo.monster/liteproblems/551
# Credit: AlgoMonster
def check_record(s):
    # Check if absences are fewer than 2
    absent_count = s.count('A')
    
    # Check if there are 3 consecutive late days
    has_three_consecutive_lates = 'LLL' in s
    
    # Student is eligible if both conditions are met:
    # - Fewer than 2 absences AND
    # - No occurrence of 3 consecutive late days
    return absent_count < 2 and not has_three_consecutive_lates
    # Time: O(n)
    # Space: O(1)


def main():
    result = check_record(s = "PPALLP")
    print(result) # True

    result = check_record(s = "PPALLL")
    print(result) # False

if __name__ == "__main__":
    main()
