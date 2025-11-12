# ------------------------------------
# 1093. Statistics from a Large Sample
# ------------------------------------

# Problem: https://leetcode.com/problems/statistics-from-a-large-sample
#
# You are given a large sample of integers in the range [0, 255]. Since the sample
# is so large, it is represented by an array count where count[k] is the number of
# times that k appears in the sample.
# 
# Calculate the following statistics:
#         
#   * minimum: The minimum element in the sample.
#   * maximum: The maximum element in the sample.
#   * mean: The average of the sample, calculated as the total sum of all
#     elements divided by the total number of elements.
#   * median:
#       * If the sample has an odd number of elements, then the median is the middle 
#         element once the sample is sorted.
#       * If the sample has an even number of elements, then the median is the 
#         average of the two middle elements once the sample is sorted.
#   * mode: The number that appears the most in the sample. It is guaranteed
#     to be unique.
# 
# Return the statistics of the sample as an array of floating-point numbers
# [minimum, maximum, mean, median, mode]. Answers within 10⁻⁵ of the actual answer
# will be accepted.
# 
# Example 1:
# 
# Input: count = [0,1,3,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
# 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
# 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
# 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
# 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
# 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
# 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
# Output: [1.00000,3.00000,2.37500,2.50000,3.00000]
# 
# Explanation: The sample represented by count is [1,2,2,2,3,3,3,3].
# The minimum and maximum are 1 and 3 respectively.
# The mean is (1+2+2+2+3+3+3+3) / 8 = 19 / 8 = 2.375.
# Since the size of the sample is even, the median is the average of the two
# middle elements 2 and 3, which is 2.5.
# The mode is 3 as it appears the most in the sample.
# 
# Example 2:
# 
# Input: count = [0,4,3,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
# 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
# 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
# 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
# 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
# 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
# 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
# 
# Output: [1.00000,4.00000,2.18182,2.00000,1.00000]
# 
# Explanation: The sample represented by count is [1,1,1,1,2,2,2,3,3,4,4].
# The minimum and maximum are 1 and 4 respectively.
# The mean is (1+1+1+1+2+2+2+3+3+4+4) / 11 = 24 / 11 = 2.18181818... (for display
# purposes, the output shows the rounded number 2.18182).
# Since the size of the sample is odd, the median is the middle element 2.
# The mode is 1 as it appears the most in the sample.
# 
# 
# Constraints:
#         count.length == 256
#         0 <= count[i] <= 10⁹
#         1 <= sum(count) <= 10⁹
#         The mode of the sample that count represents is unique.


# Solution: https://algo.monster/liteproblems/1093
# Credit: AlgoMonster
def sample_stats(count):
    
    def find_kth_element(k):
        cumulative_count = 0
        for value, frequency in enumerate(count):
            cumulative_count += frequency
            if cumulative_count >= k:
                return value
    
    # Initialize statistics variables
    minimum_value = float('inf')
    maximum_value = -1
    total_sum = 0
    total_count = 0
    mode_value = 0
    
    # Single pass to calculate min, max, sum, count, and mode
    for value, frequency in enumerate(count):
        if frequency > 0:
            # Update minimum and maximum
            minimum_value = min(minimum_value, value)
            maximum_value = max(maximum_value, value)
            
            # Update sum and count for mean calculation
            total_sum += value * frequency
            total_count += frequency
            
            # Update mode if current frequency is higher
            if frequency > count[mode_value]:
                mode_value = value
    
    # Calculate median based on whether total count is odd or even
    if total_count & 1:  # Odd number of elements
        median = find_kth_element(total_count // 2 + 1)
    else:  # Even number of elements
        median = (find_kth_element(total_count // 2) + 
                    find_kth_element(total_count // 2 + 1)) / 2.0
    
    # Calculate mean
    mean = total_sum / total_count
    
    # Return all statistics as floats
    return [float(minimum_value), float(maximum_value), mean, median, float(mode_value)]
    # Time: O(n + k)
    # Space: O(1)
    # n = the length of the count array
    # k = the total number of elements (sum of all counts).


def main():
    count = [0,1,3,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    result = sample_stats(count)
    print(result) # [1.0, 3.0, 2.375, 2.5, 3.0]

    count = [0,4,3,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    result = sample_stats(count)
    print(result) # [1.0, 4.0, 2.1818181818181817, 2, 1.0]

if __name__ == "__main__":
    main()
