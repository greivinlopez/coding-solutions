# ------------------------------------
# 1542. Find Longest Awesome Substring
# ------------------------------------

# Problem: https://leetcode.com/problems/find-longest-awesome-substring
#
# You are given a string s. An awesome substring is a non-empty substring of s
# such that we can make any number of swaps in order to make it a palindrome.
# 
# Return the length of the maximum length awesome substring of s.
# 
# Example 1:
# 
# Input: s = "3242415"
# Output: 5
# 
# Explanation: "24241" is the longest awesome substring, we can form the
# palindrome "24142" with some swaps.
# 
# Example 2:
# 
# Input: s = "12345678"
# Output: 1
# 
# Example 3:
# 
# Input: s = "213123"
# Output: 6
# 
# Explanation: "213123" is the longest awesome substring, we can form the
# palindrome "231132" with some swaps.
# 
# 
# Constraints:
#         1 <= s.length <= 10⁵
#         s consists only of digits.


# Solution: https://algo.monster/liteproblems/1542
# Credit: AlgoMonster
def longest_awesome(s):
    # Bitmask to track parity (odd/even count) of each digit 0-9
    # Bit i is 1 if digit i appears odd number of times, 0 if even
    parity_mask = 0
    
    # Dictionary to store first occurrence index of each parity state
    # Key: parity mask, Value: earliest index where this mask occurred
    first_occurrence = {0: -1}  # Empty prefix has mask 0 at index -1
    
    # Initialize result with minimum possible length
    max_length = 1
    
    # Process each character in the string
    for current_index, char in enumerate(s):
        # Convert character to digit
        digit = int(char)
        
        # Toggle the bit for this digit in the parity mask
        # XOR flips the bit: 0->1 (even->odd) or 1->0 (odd->even)
        parity_mask ^= 1 << digit
        
        # Case 1: Check if we've seen this exact parity mask before
        # If yes, substring between these positions has all even counts (palindrome)
        if parity_mask in first_occurrence:
            max_length = max(max_length, current_index - first_occurrence[parity_mask])
        else:
            # Record first occurrence of this parity mask
            first_occurrence[parity_mask] = current_index
        
        # Case 2: Check for palindromes with exactly one odd-count digit
        # Try flipping each bit to see if that state was seen before
        for digit_to_flip in range(10):
            # Create mask with one bit different (one digit has different parity)
            target_mask = parity_mask ^ (1 << digit_to_flip)
            
            # If this mask exists, substring between positions forms palindrome
            # with exactly one odd-count digit
            if target_mask in first_occurrence:
                max_length = max(max_length, current_index - first_occurrence[target_mask])
    
    return max_length
    # Time: O(n)
    # Space: O(1)


def main():
    result = longest_awesome(s = "3242415")
    print(result) # 5

    result = longest_awesome(s = "12345678")
    print(result) # 1

    result = longest_awesome(s = "213123")
    print(result) # 6

if __name__ == "__main__":
    main()
