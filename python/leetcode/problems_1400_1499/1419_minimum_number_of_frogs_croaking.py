# -----------------------------------------
# 1419. Minimum Number of Frogs Croaking 🐸
# -----------------------------------------

# Problem: https://leetcode.com/problems/minimum-number-of-frogs-croaking
#
# You are given the string croakOfFrogs, which represents a combination of the
# string "croak" from different frogs, that is, multiple frogs can croak at the
# same time, so multiple "croak" are mixed.
# 
# Return the minimum number of different frogs to finish all the croaks in the
# given string.
# 
# A valid "croak" means a frog is printing five letters 'c', 'r', 'o', 'a', and
# 'k' sequentially. The frogs have to print all five letters to finish a croak. If
# the given string is not a combination of a valid "croak" return -1.
# 
# Example 1:
# 
# Input: croakOfFrogs = "croakcroak"
# Output: 1
# 
# Explanation: One frog yelling "croak" twice.
# 
# Example 2:
# 
# Input: croakOfFrogs = "crcoakroak"
# Output: 2
# 
# Explanation: The minimum number of frogs is two.
# The first frog could yell "crcoakroak".
# The second frog could yell later "crcoakroak".
# 
# Example 3:
# 
# Input: croakOfFrogs = "croakcrook"
# Output: -1
# 
# Explanation: The given string is an invalid combination of "croak" from
# different frogs.
# 
# 
# Constraints:
#         1 <= croakOfFrogs.length <= 10⁵
#         croakOfFrogs is either 'c', 'r', 'o', 'a', or 'k'.


# Solution: https://algo.monster/liteproblems/1419
# Credit: AlgoMonster
def min_number_of_frogs(croakOfFrogs):
    # If the string length is not divisible by 5, it's impossible to form complete "croak"s
    if len(croakOfFrogs) % 5 != 0:
        return -1
    
    # Create a mapping from each character to its position in "croak"
    char_to_index = {char: index for index, char in enumerate('croak')}
    
    # Track count of frogs at each stage of croaking
    # stage_count[i] represents frogs that have completed up to position i in "croak"
    stage_count = [0] * 5
    
    # max_frogs: maximum number of concurrent frogs needed
    # active_frogs: current number of frogs that are croaking
    max_frogs = 0
    active_frogs = 0
    
    # Process each character in the input string
    for char in croakOfFrogs:
        # Get the position of current character in "croak"
        position = char_to_index.get(char)
        
        # If character is not in "croak", return -1
        if position is None:
            return -1
        
        # Increment count for this stage
        stage_count[position] += 1
        
        if position == 0:  # Character is 'c' - a new frog starts croaking
            active_frogs += 1
            max_frogs = max(max_frogs, active_frogs)
        else:
            # Check if there's a frog at the previous stage to continue
            if stage_count[position - 1] == 0:
                return -1  # Invalid sequence
            
            # Move one frog from previous stage to current stage
            stage_count[position - 1] -= 1
            
            if position == 4:  # Character is 'k' - a frog completes croaking
                active_frogs -= 1
    
    # All frogs must complete their croaking (active_frogs should be 0)
    if active_frogs != 0:
        return -1
    
    return max_frogs
    # Time: O(n)
    # Space: O(1)


def main():
    result = min_number_of_frogs(croakOfFrogs = "croakcroak")
    print(result) # 1

    result = min_number_of_frogs(croakOfFrogs = "crcoakroak")
    print(result) # 2

    result = min_number_of_frogs(croakOfFrogs = "croakcrook")
    print(result) # -1

if __name__ == "__main__":
    main()
