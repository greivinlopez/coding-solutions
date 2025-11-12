# ---------------------
# 752. Open the Lock 🔒
# ---------------------

# Problem: https://leetcode.com/problems/open-the-lock/
# 
# You have a lock in front of you with 4 circular wheels. Each wheel has 10 
# slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can 
# rotate freely and wrap around: for example we can turn '9' to be '0', or '0'
# to be '9'. Each move consists of turning one wheel one slot.
# 
# The lock initially starts at '0000', a string representing the state of the 
# 4 wheels.
# 
# You are given a list of deadends dead ends, meaning if the lock displays any 
# of these codes, the wheels of the lock will stop turning and you will be 
# unable to open it.
# 
# Given a target representing the value of the wheels that will unlock the lock, 
# return the minimum total number of turns required to open the lock, or -1 if 
# it is impossible.
# 
# Example 1:
# 
# Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
# Output: 6
# Explanation: 
# A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
# Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
# because the wheels of the lock become stuck after the display becomes the dead end "0102".
# 
# Example 2:
# 
# Input: deadends = ["8888"], target = "0009"
# Output: 1
# Explanation: We can turn the last wheel in reverse to move from "0000" -> "0009".
# 
# Example 3:
# 
# Input: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
# Output: -1
# Explanation: We cannot reach the target without getting stuck.
#  
# 
# Constraints:
# 
#   1 <= deadends.length <= 500
#   deadends[i].length == 4
#   target.length == 4
#   target will not be in the list deadends.
#   target and deadends[i] consist of digits only.

from collections import deque

# Solution: https://youtu.be/Pzg3bCDY87w
# Credit: Navdeep Singh founder of NeetCode
def open_lock(deadends, target):
    if "0000" in deadends:
        return -1

    def children(wheel):
        res = []
        for i in range(4):
            digit = str((int(wheel[i]) + 1) % 10)
            res.append(wheel[:i] + digit + wheel[i + 1 :])
            digit = str((int(wheel[i]) + 10 - 1) % 10)
            res.append(wheel[:i] + digit + wheel[i + 1 :])
        return res

    q = deque()
    visit = set(deadends)
    q.append(["0000", 0])  # [wheel, turns]
    while q:
        wheel, turns = q.popleft()
        if wheel == target:
            return turns
        for child in children(wheel):
            if child not in visit:
                visit.add(child)
                q.append([child, turns + 1])
    return -1
        

def main():
    result = open_lock(deadends = ["0201","0101","0102","1212","2002"], target = "0202")
    print(result) # 6

    result = open_lock(deadends = ["8888"], target = "0009")
    print(result) # 1

if __name__ == "__main__":
    main()
