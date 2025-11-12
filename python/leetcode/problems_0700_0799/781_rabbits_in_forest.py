# -------------------------
# 781. Rabbits in Forest 🐇
# -------------------------

# Problem: https://leetcode.com/problems/rabbits-in-forest
#
# There is a forest with an unknown number of rabbits. We asked n rabbits "How
# many rabbits have the same color as you?" and collected the answers in an
# integer array answers where answers[i] is the answer of the iᵗʰ rabbit.
# 
# Given the array answers, return the minimum number of rabbits that could be in
# the forest.
# 
# Example 1:
# 
# Input: answers = [1,1,2]
# Output: 5
# 
# Explanation:
# The two rabbits that answered "1" could both be the same color, say red.
# The rabbit that answered "2" can't be red or the answers would be inconsistent.
# Say the rabbit that answered "2" was blue.
# Then there should be 2 other blue rabbits in the forest that didn't answer into
# the array.
# The smallest possible number of rabbits in the forest is therefore 5: 3 that
# answered plus 2 that didn't.
# 
# Example 2:
# 
# Input: answers = [10,10,10]
# Output: 11
# 
# 
# Constraints:
#         1 <= answers.length <= 1000
#         0 <= answers[i] < 1000

from collections import Counter

# Solution: https://algo.monster/liteproblems/781
# Credit: AlgoMonster
def num_rabbits(answers):
    # Count frequency of each answer
    # Key: answer value (number of other rabbits with same color)
    # Value: how many rabbits gave this answer
    answer_counts = Counter(answers)
    
    # Initialize minimum total rabbits
    total_rabbits = 0
    
    # Process each unique answer and its frequency
    for answer_value, frequency in answer_counts.items():
        # Calculate group size for this color
        # If a rabbit says there are 'x' others with same color,
        # then total rabbits of that color = x + 1 (including itself)
        group_size = answer_value + 1
        
        # Calculate minimum number of groups needed
        # Using ceiling division: (frequency + group_size - 1) // group_size
        # This gives us the minimum number of complete groups needed
        num_groups = (frequency + group_size - 1) // group_size
        
        # Add total rabbits from all groups of this color
        # Each group has 'group_size' rabbits
        total_rabbits += num_groups * group_size
    
    return total_rabbits
    # Time: O(n)
    # Space: O(n)


def main():
    result = num_rabbits(answers = [1,1,2])
    print(result) # 5

    result = num_rabbits(answers = [10,10,10])
    print(result) # 11

if __name__ == "__main__":
    main()
