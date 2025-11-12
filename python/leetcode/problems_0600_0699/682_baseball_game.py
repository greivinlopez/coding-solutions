# ------------------
# 682. Baseball Game
# ------------------

# Problem: https://leetcode.com/problems/baseball-game/
# 
# You are keeping the scores for a baseball game with strange rules. At the 
# beginning of the game, you start with an empty record.
# 
# You are given a list of strings operations, where operations[i] is the ith 
# operation you must apply to the record and is one of the following:
# 
# 	An integer x.
# 		Record a new score of x.
# 	
# 	'+'.
# 		Record a new score that is the sum of the previous two scores.
# 	
# 	'D'.
# 		Record a new score that is the double of the previous score.
# 	
# 	'C'.
# 		Invalidate the previous score, removing it from the record.
#
# 
# Return the sum of all the scores on the record after applying all the 
# operations.
# 
# The test cases are generated such that the answer and all intermediate 
# calculations fit in a 32-bit integer and that all operations are valid.
# 
#  
# Example 1:
# 
# Input: ops = ["5","2","C","D","+"]
# Output: 30
# Explanation:
# "5" - Add 5 to the record, record is now [5].
# "2" - Add 2 to the record, record is now [5, 2].
# "C" - Invalidate and remove the previous score, record is now [5].
# "D" - Add 2 * 5 = 10 to the record, record is now [5, 10].
# "+" - Add 5 + 10 = 15 to the record, record is now [5, 10, 15].
# The total sum is 5 + 10 + 15 = 30.
# 
# 
# Example 2:
# 
# Input: ops = ["5","-2","4","C","D","9","+","+"]
# Output: 27
# Explanation:
# "5" - Add 5 to the record, record is now [5].
# "-2" - Add -2 to the record, record is now [5, -2].
# "4" - Add 4 to the record, record is now [5, -2, 4].
# "C" - Invalidate and remove the previous score, record is now [5, -2].
# "D" - Add 2 * -2 = -4 to the record, record is now [5, -2, -4].
# "9" - Add 9 to the record, record is now [5, -2, -4, 9].
# "+" - Add -4 + 9 = 5 to the record, record is now [5, -2, -4, 9, 5].
# "+" - Add 9 + 5 = 14 to the record, record is now [5, -2, -4, 9, 5, 14].
# The total sum is 5 + -2 + -4 + 9 + 5 + 14 = 27.
# 
# 
# Example 3:
# 
# Input: ops = ["1","C"]
# Output: 0
# Explanation:
# "1" - Add 1 to the record, record is now [1].
# "C" - Invalidate and remove the previous score, record is now [].
# Since the record is empty, the total sum is 0.
# 
# 
# Constraints:
# 
# 	* 1 <= operations.length <= 1000
# 	* operations[i] is "C", "D", "+", or a string representing an integer in the 
#     range [-3 * 104, 3 * 104].
# 	* For operation "+", there will always be at least two previous scores on 
#     the record.
# 	* For operations "C" and "D", there will always be at least one previous 
#     score on the record.


# Solution: https://youtu.be/Id_tqGdsZQI
# Credit: Navdeep Singh founder of NeetCode
def cal_points(operations):
    score_stack = []
    
    for o in operations:
        
        # it is +, D, or C
        # if stack isn't of sufficient length, then operation is voided
        if o == "+" and len(score_stack) >= 2:
            summed = score_stack[-2] + score_stack[-1]
            score_stack.append(summed)
            
        elif o == "D" and len(score_stack) >= 1:
            doubled = score_stack[-1] * 2
            score_stack.append(doubled)
            
        elif o == "C" and len(score_stack) >= 1:
            score_stack.pop() 
            
        else: 
            score_stack.append(int(o))

    return sum(score_stack)
    # Time: O(n)
    # Space: O(n)

# Solution: https://youtu.be/365VRBxje4E
# Credit: Greg Hogg
# Same Solution

def main():
    result = cal_points(["5","2","C","D","+"])
    print(result) # 30

    result = cal_points(["5","-2","4","C","D","9","+","+"])
    print(result) # 27

    result = cal_points(["1","C"])
    print(result) # 0

if __name__ == "__main__":
    main()
