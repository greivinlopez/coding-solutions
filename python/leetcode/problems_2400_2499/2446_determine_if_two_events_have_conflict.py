# -------------------------------------------
# 2446. Determine if Two Events Have Conflict
# -------------------------------------------

# Problem: https://leetcode.com/problems/determine-if-two-events-have-conflict
#
# You are given two arrays of strings that represent two inclusive events that
# happened on the same day, event1 and event2, where:
# 
#         event1 = [startTime₁, endTime₁] and
#         event2 = [startTime₂, endTime₂].
# 
# Event times are valid 24 hours format in the form of HH:MM.
# 
# A conflict happens when two events have some non-empty intersection (i.e., some
# moment is common to both events).
# 
# Return true if there is a conflict between two events. Otherwise, return false.
# 
# Example 1:
# 
# Input: event1 = ["01:15","02:00"], event2 = ["02:00","03:00"]
# Output: true
# 
# Explanation: The two events intersect at time 2:00.
# 
# Example 2:
# 
# Input: event1 = ["01:00","02:00"], event2 = ["01:20","03:00"]
# Output: true
# 
# Explanation: The two events intersect starting from 01:20 to 02:00.
# 
# Example 3:
# 
# Input: event1 = ["10:00","11:00"], event2 = ["14:00","15:00"]
# Output: false
# 
# Explanation: The two events do not intersect.
# 
# 
# Constraints:
#         event1.length == event2.length == 2
#         event1[i].length == event2[i].length == 5
#         startTime₁ <= endTime₁
#         startTime₂ <= endTime₂
#         All the event times follow the HH:MM format.

# Credit: Jaweria Batool -> https://github.com/Jaweria-B
def have_conflict(event1, event2):
    e1_s, e1_e = event1
    e2_s, e2_e = event2
    
    def compare(time1, time2):
        t1_hr, t1_mint = time1.split(":")
        t1_hr, t1_mint = int(t1_hr), int(t1_mint)
        
        t2_hr, t2_mint = time2.split(":")
        t2_hr, t2_mint = int(t2_hr), int(t2_mint)
        
        if (t1_hr == t2_hr and t1_mint < t2_mint) or t2_hr > t1_hr  :
            return False
        
        return True
    
    return compare(e1_e, e2_s) and compare(e2_e, e1_s)
    # Time: O(1)
    # Space: O(1)


def main():
    result = have_conflict(event1 = ["01:15","02:00"], event2 = ["02:00","03:00"])
    print(result) # True

    result = have_conflict(event1 = ["01:00","02:00"], event2 = ["01:20","03:00"])
    print(result) # True

    result = have_conflict(event1 = ["10:00","11:00"], event2 = ["14:00","15:00"])
    print(result) # False

if __name__ == "__main__":
    main()
