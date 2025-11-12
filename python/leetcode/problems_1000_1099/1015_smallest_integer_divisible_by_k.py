# -------------------------------------
# 1015. Smallest Integer Divisible by K
# -------------------------------------

# Problem: https://leetcode.com/problems/smallest-integer-divisible-by-k
#
# Given a positive integer k, you need to find the length of the smallest positive
# integer n such that n is divisible by k, and n only contains the digit 1.
# 
# Return the length of n. If there is no such n, return -1.
# 
# Note: n may not fit in a 64-bit signed integer.
# 
# Example 1:
# 
# Input: k = 1
# Output: 1
# 
# Explanation: The smallest answer is n = 1, which has length 1.
# 
# Example 2:
# 
# Input: k = 2
# Output: -1
# 
# Explanation: There is no such positive integer n divisible by 2.
# 
# Example 3:
# 
# Input: k = 3
# Output: 3
# 
# Explanation: The smallest answer is n = 111, which has length 3.
# 
# 
# Constraints:
#         1 <= k <= 10⁵


# Solution: https://algo.monster/liteproblems/1015
# Credit: AlgoMonster
def smallest_rep_unit_div_by_k(k):
    # Initialize remainder when 1 is divided by k
    remainder = 1 % k
    
    # Try repunits of length 1 to k
    # If a solution exists, it must be found within k iterations
    # (by pigeonhole principle - there are only k possible remainders)
    for length in range(1, k + 1):
        # Check if current repunit is divisible by k
        if remainder == 0:
            return length
        
        # Calculate remainder of next repunit
        # Next repunit = current * 10 + 1
        # Using modular arithmetic to avoid overflow
        remainder = (remainder * 10 + 1) % k
    
    # No repunit divisible by k was found
    return -1
    # Time: O(k)
    # Space: O(1)


def main():
    result = smallest_rep_unit_div_by_k(1)
    print(result) # 1

    result = smallest_rep_unit_div_by_k(2)
    print(result) # -1

    result = smallest_rep_unit_div_by_k(3)
    print(result) # 3

if __name__ == "__main__":
    main()
