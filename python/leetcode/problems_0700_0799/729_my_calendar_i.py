# ------------------
# 729. My Calendar I
# ------------------

# Problem: https://leetcode.com/problems/my-calendar-i/
# 
# You are implementing a program to use as your calendar. We can add a new 
# event if adding the event will not cause a double booking.
# 
# A double booking happens when two events have some non-empty intersection 
# (i.e., some moment is common to both events.).
# 
# The event can be represented as a pair of integers startTime and endTime 
# that represents a booking on the half-open interval [startTime, endTime), 
# the range of real numbers x such that startTime <= x < endTime.
# 
# Implement the MyCalendar class:
# 
# 	MyCalendar() Initializes the calendar object.
# 	boolean book(int startTime, int endTime) Returns true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.
# 
#  
# Example 1:
# 
# 
# Input
# ["MyCalendar", "book", "book", "book"]
# [[], [10, 20], [15, 25], [20, 30]]
# Output
# [null, true, false, true]
# 
# Explanation
# MyCalendar myCalendar = new MyCalendar();
# myCalendar.book(10, 20); // return True
# myCalendar.book(15, 25); // return False, It can not be booked because time 15 is already booked by another event.
# myCalendar.book(20, 30); // return True, The event can be booked, as the first event takes every time less than 20, but not including 20.
# 
#  
# Constraints:
# 
# 
# 	0 <= start < end <= 10^9
# 	At most 1000 calls will be made to book.


# Solution: https://youtu.be/fIxck3tlId4
# Credit: Navdeep Singh founder of NeetCode
class MyCalendar:
    def __init__(self):
        self.calendar = CalendarNode(-1, -1)

    def book(self, start: int, end: int) -> bool:

        def bookHelper(cur, targetStart, targetEnd):
            if targetStart > cur.end:
                # go to the right
                if not cur.right:
                    # we can insert event
                    cur.right = CalendarNode(targetStart, targetEnd)
                    return True
                return bookHelper(cur.right, targetStart, targetEnd)
            elif targetEnd < cur.start:
                # got to the left
                if not cur.left:
                    # we can insert event
                    cur.left = CalendarNode(targetStart, targetEnd)
                    return True
                return bookHelper(cur.left, targetStart, targetEnd)
            return False
        
        return bookHelper(self.calendar, start, end-1) # "end-1" because "end" bound is exclusive (see example 1) 
    
class CalendarNode:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None


def main():
    print("TO DO")

if __name__ == "__main__":
    main()
