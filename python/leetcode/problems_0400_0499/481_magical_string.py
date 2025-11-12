# -----------------------
# 481. Magical String 🎩🪄
# -----------------------

# Problem: https://leetcode.com/problems/magical-string
#
# A magical string s consists of only '1' and '2' and obeys the following rules:
#         
#   * The string s is magical because concatenating the number of contiguous
#     occurrences of characters '1' and '2' generates the string s itself.
# 
# The first few elements of s is s = "1221121221221121122……". If we group the
# consecutive 1's and 2's in s, it will be "1 22 11 2 1 22 1 22 11 2 11 22 ......"
# and the occurrences of 1's or 2's in each group are "1 2 2 1 1 2 1 2 2 1 2 2
# ......". You can see that the occurrence sequence is s itself.
# 
# Given an integer n, return the number of 1's in the first n number in the
# magical string s.
# 
# Example 1:
# 
# Input: n = 6
# Output: 3
# 
# Explanation: The first 6 elements of magical string s is "122112" and it
# contains three 1's, so return 3.
# 
# Example 2:
# 
# Input: n = 1
# Output: 1
# 
# 
# Constraints:
#         1 <= n <= 10⁵


# Solution: https://algo.monster/liteproblems/481
# Credit: AlgoMonster
def magical_string(n):
    # Base case: if n is 0, return 0
    if n == 0:
        return 0
    
    # Initialize the magical string with the first three elements
    # The magical string starts as: 1, 2, 2, ...
    result = [1, 2, 2]
    
    # Index pointer to track which element determines the next group's count
    # Starting from index 2 (third element)
    group_count_index = 2
    
    # Generate the magical string until we have at least n elements
    while len(result) < n:
        # Get the previous element to determine what the next element should be
        previous_element = result[-1]
        
        # The next element alternates between 1 and 2
        # If previous was 1, current is 2; if previous was 2, current is 1
        current_element = 3 - previous_element
        
        # The number of times to append the current element is determined by
        # the value at the current group_count_index position
        repeat_count = result[group_count_index]
        
        # Append the current element 'repeat_count' times to the magical string
        result.extend([current_element] * repeat_count)
        
        # Move to the next position for determining group counts
        group_count_index += 1
    
    # Count the number of 1s in the first n elements of the magical string
    return result[:n].count(1)
    # Time: O(n)
    # Space: O(n)


def main():
    result = magical_string(6)
    print(result) # 3

    result = magical_string(1)
    print(result) # 1

if __name__ == "__main__":
    main()
