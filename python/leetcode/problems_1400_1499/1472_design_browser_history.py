# ---------------------------
# 1472. Design Browser History
# ---------------------------

# Problem: https://leetcode.com/problems/design-browser-history
#
# You have a browser of one tab where you start on the homepage and you can visit
# another url, get back in the history number of steps or move forward in the
# history number of steps.
# 
# Implement the BrowserHistory class:
# 
#         BrowserHistory(string homepage) Initializes the object with the
# homepage of the browser.
# 
#         void visit(string url) Visits url from the current page. It clears up
# all the forward history.
# 
#         string back(int steps) Move steps back in history. If you can only
# return x steps in the history and steps > x, you will return only x steps.
# Return the current url after moving back in history at most steps.
# 
#         string forward(int steps) Move steps forward in history. If you can only
# forward x steps in the history and steps > x, you will forward only x steps.
# Return the current url after forwarding in history at most steps.
# 
# Example:
# 
# Input:
# ["BrowserHistory","visit","visit","visit","back","back","forward","visit","forwa
# rd","back","back"]
# [["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["
# linkedin.com"],[2],[2],[7]]
# Output:
# [null,null,null,null,"facebook.com","google.com","facebook.com",null,"linkedin.c
# om","google.com","leetcode.com"]
# Explanation:
# BrowserHistory browserHistory = new BrowserHistory("leetcode.com");
# browserHistory.visit("google.com");       // You are in "leetcode.com". Visit
# "google.com"
# browserHistory.visit("facebook.com");     // You are in "google.com". Visit
# "facebook.com"
# browserHistory.visit("youtube.com");      // You are in "facebook.com". Visit
# "youtube.com"
# browserHistory.back(1);                   // You are in "youtube.com", move back
# to "facebook.com" return "facebook.com"
# browserHistory.back(1);                   // You are in "facebook.com", move
# back to "google.com" return "google.com"
# browserHistory.forward(1);                // You are in "google.com", move
# forward to "facebook.com" return "facebook.com"
# browserHistory.visit("linkedin.com");     // You are in "facebook.com". Visit
# "linkedin.com"
# browserHistory.forward(2);                // You are in "linkedin.com", you
# cannot move forward any steps.
# browserHistory.back(2);                   // You are in "linkedin.com", move
# back two steps to "facebook.com" then to "google.com". return "google.com"
# browserHistory.back(7);                   // You are in "google.com", you can
# move back only one step to "leetcode.com". return "leetcode.com"
# 
# 
# Constraints:
#         1 <= homepage.length <= 20
#         1 <= url.length <= 20
#         1 <= steps <= 100
#         homepage and url consist of  '.' or lower case English letters.
#         At most 5000 calls will be made to visit, back, and forward.


# Solution: https://youtu.be/i1G-kKnBu8k
# Credit: Navdeep Singh founder of NeetCode
# Linked List Implementation
class ListNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class BrowserHistory:
    def __init__(self, homepage: str):
        self.cur = ListNode(homepage)

    # O(1)
    def visit(self, url: str) -> None:
        self.cur.next = ListNode(url, self.cur)
        self.cur = self.cur.next

    # O(n)
    def back(self, steps: int) -> str:
        while self.cur.prev and steps > 0:
            self.cur = self.cur.prev
            steps -= 1
        return self.cur.val

    # O(n)
    def forward(self, steps: int) -> str:
        while self.cur.next and steps > 0:
            self.cur = self.cur.next
            steps -= 1
        return self.cur.val

# Array Implementation
class BrowserHistory:    
    def __init__(self, homepage: str):
        self.i = 0
        self.len = 1
        self.history = [homepage]

    # O(1)
    def visit(self, url: str) -> None:
        if len(self.history) < self.i + 2:
            self.history.append(url)
        else:
            self.history[self.i + 1] = url
        self.i += 1
        self.len = self.i + 1

    # O(1)
    def back(self, steps: int) -> str:
        self.i = max(self.i - steps, 0)
        return self.history[self.i]

    # O(1)
    def forward(self, steps: int) -> str:
        self.i = min(self.i + steps, self.len - 1)
        return self.history[self.i]


def main():
    print("TO DO")

if __name__ == "__main__":
    main()
