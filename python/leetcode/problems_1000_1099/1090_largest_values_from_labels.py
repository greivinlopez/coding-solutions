# --------------------------------
# 1090. Largest Values From Labels
# --------------------------------

# Problem: https://leetcode.com/problems/largest-values-from-labels
#
# You are given n item's value and label as two integer arrays values and labels.
# You are also given two integers numWanted and useLimit.
# 
# Your task is to find a subset of items with the maximum sum of their values such
# that:
#         
#   * The number of items is at most numWanted.
#   * The number of items with the same label is at most useLimit.
# 
# Return the maximum sum.
# 
# Example 1:
# 
# Input: values = [5,4,3,2,1], labels = [1,1,2,2,3], numWanted = 3, useLimit = 1
# Output: 9
# 
# Explanation:
# The subset chosen is the first, third, and fifth items with the sum of values 5
# + 3 + 1.
# 
# Example 2:
# 
# Input: values = [5,4,3,2,1], labels = [1,3,3,3,2], numWanted = 3, useLimit = 2
# Output: 12
# 
# Explanation:
# The subset chosen is the first, second, and third items with the sum of values 5
# + 4 + 3.
# 
# Example 3:
# 
# Input: values = [9,8,8,7,6], labels = [0,0,0,1,1], numWanted = 3, useLimit = 1
# Output: 16
# 
# Explanation:
# The subset chosen is the first and fourth items with the sum of values 9 + 7.
# 
# 
# Constraints:
#         n == values.length == labels.length
#         1 <= n <= 2 * 10⁴
#         0 <= values[i], labels[i] <= 2 * 10⁴
#         1 <= numWanted, useLimit <= n

from collections import Counter
from collections import defaultdict

# Solution: https://algo.monster/liteproblems/1090
# Credit: AlgoMonster
def largest_vals_from_labels_alt(values, labels, numWanted, useLimit):
    # Initialize result sum and count of selected items
    total_sum = 0
    items_selected = 0
    
    # Counter to track how many times each label has been used
    label_usage_count = Counter()
    
    # Create pairs of (value, label) and sort by value in descending order
    # This greedy approach ensures we pick the highest values first
    value_label_pairs = sorted(zip(values, labels), reverse=True)
    
    # Iterate through sorted pairs from highest to lowest value
    for value, label in value_label_pairs:
        # Check if we can still use this label (haven't reached useLimit)
        if label_usage_count[label] < useLimit:
            # Use this item: increment label count and update results
            label_usage_count[label] += 1
            items_selected += 1
            total_sum += value
            
            # Stop if we've selected the desired number of items
            if items_selected == numWanted:
                break
    
    return total_sum
    # Time: O(n * log(n))
    # Space: O(1)


# Solution: https://leetcode.com/problems/largest-values-from-labels/solutions/7106947/simple-python-solution-beats-100
# Credit: user6403Hl -> https://leetcode.com/u/user6403Hl/
def largest_vals_from_labels(values, labels, numWanted, useLimit):
    items = sorted(zip(values, labels), reverse=True)
    used = defaultdict(int)
    ans = 0
    taken = 0
    for v, l in items:
        if taken == numWanted:
            break
        if used[l] < useLimit:
            ans += v
            used[l] += 1
            taken += 1
    return ans
    # Time: O(n * log(n))
    # Space: O(n)


def main():
    result = largest_vals_from_labels(values = [5,4,3,2,1], labels = [1,1,2,2,3], numWanted = 3, useLimit = 1)
    print(result) # 9

    result = largest_vals_from_labels(values = [5,4,3,2,1], labels = [1,3,3,3,2], numWanted = 3, useLimit = 2)
    print(result) # 12

    result = largest_vals_from_labels(values = [9,8,8,7,6], labels = [0,0,0,1,1], numWanted = 3, useLimit = 1)
    print(result) # 16

if __name__ == "__main__":
    main()
