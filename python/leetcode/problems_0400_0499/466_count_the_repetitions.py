# --------------------------
# 466. Count The Repetitions
# --------------------------

# Problem: https://leetcode.com/problems/count-the-repetitions
#
# We define str = [s, n] as the string str which consists of the string s
# concatenated n times.
# 
#   * For example, str == ["abc", 3] =="abcabcabc".
# 
# We define that string s1 can be obtained from string s2 if we can remove some
# characters from s2 such that it becomes s1.
# 
#   * For example, s1 = "abc" can be obtained from s2 = "abdbec" based on our
#     definition by removing the bolded underlined characters.
# 
# You are given two strings s1 and s2 and two integers n1 and n2. You have the two
# strings str1 = [s1, n1] and str2 = [s2, n2].
# 
# Return the maximum integer m such that str = [str2, m] can be obtained from
# str1.
# 
# Example 1:
# 
# Input: s1 = "acb", n1 = 4, s2 = "ab", n2 = 2
# Output: 2
# 
# Example 2:
# 
# Input: s1 = "acb", n1 = 1, s2 = "acb", n2 = 1
# Output: 1
# 
# 
# Constraints:
#         1 <= s1.length, s2.length <= 100
#         s1 and s2 consist of lowercase English letters.
#         1 <= n1, n2 <= 10⁶


# Solution: https://algo.monster/liteproblems/466
# Credit: AlgoMonster
def get_max_repetitions(s1, n1, s2, n2):
    s2_length = len(s2)
    
    # Build a transition table for each starting position in s2
    # This pre-calculation finds the result of matching one s1 against s2 starting at a specific index.
    # Key: starting index in s2 (0 to s2_length - 1)
    # Value: (number of complete s2 cycles, ending index in s2) after processing one s1
    transition_table = {}
    
    for start_index in range(s2_length):
        complete_cycles = 0
        current_index = start_index
        
        # Process one complete s1 string
        for char in s1:
            if char == s2[current_index]:
                current_index += 1
                
            # Check if we completed one cycle of s2
            if current_index == s2_length:
                complete_cycles += 1
                current_index = 0
                
        transition_table[start_index] = (complete_cycles, current_index)
    
    # Simulate processing n1 copies of s1 using the transition table
    total_s2_cycles = 0
    current_s2_index = 0
    
    for _ in range(n1):
        # Get transition result from current position in s2
        cycles_gained, next_index = transition_table[current_s2_index]
        total_s2_cycles += cycles_gained
        current_s2_index = next_index
    
    # Calculate how many complete str2 (s2 * n2) we can form
    return total_s2_cycles // n2
    # Time: O(m × n + n₁)
    # Space: O(n)


def main():
    result = get_max_repetitions(s1 = "acb", n1 = 4, s2 = "ab", n2 = 2)
    print(result) # 2

    result = get_max_repetitions(s1 = "acb", n1 = 1, s2 = "acb", n2 = 1)
    print(result) # 1

if __name__ == "__main__":
    main()
