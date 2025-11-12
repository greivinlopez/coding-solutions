# --------------------------------
# 564. Find the Closest Palindrome
# --------------------------------

# Problem: https://leetcode.com/problems/find-the-closest-palindrome
#
# Given a string n representing an integer, return the closest integer (not
# including itself), which is a palindrome. If there is a tie, return the smaller
# one.
# 
# The closest is defined as the absolute difference minimized between two
# integers.
# 
# Example 1:
# 
# Input: n = "123"
# Output: "121"
# 
# Example 2:
# 
# Input: n = "1"
# Output: "0"
# 
# Explanation: 0 and 2 are the closest palindromes but we return the smallest
# which is 0.
# 
# 
# Constraints:
#         1 <= n.length <= 18
#         n consists of only digits.
#         n does not have leading zeros.
#         n is representing an integer in the range [1, 10¹⁸ - 1].


# Solution: 
# Credit: Navdeep Singh founder of NeetCode
def nearest_palindromic(n):
    original_num = int(n)
    length = len(n)
    
    # Initialize candidate set with edge cases:
    # 1. Largest palindrome with (length-1) digits: 999...999
    # 2. Smallest palindrome with (length+1) digits: 100...001
    candidates = {10 ** (length - 1) - 1, 10 ** length + 1}
    
    # Extract the left half of the number (including middle digit if odd length)
    prefix_length = (length + 1) // 2
    prefix = int(n[:prefix_length])
    
    # Generate palindromes by mirroring prefix-1, prefix, and prefix+1
    for prefix_variant in range(prefix - 1, prefix + 2):
        # Create palindrome by mirroring the prefix
        palindrome = prefix_variant
        
        # Determine what to mirror (exclude middle digit if odd length)
        suffix_to_mirror = prefix_variant if length % 2 == 0 else prefix_variant // 10
        
        # Mirror the digits to create the full palindrome
        while suffix_to_mirror > 0:
            palindrome = palindrome * 10 + suffix_to_mirror % 10
            suffix_to_mirror //= 10
        
        candidates.add(palindrome)
    
    # Remove the original number from candidates (we need a different palindrome)
    candidates.discard(original_num)
    
    # Find the nearest palindrome from candidates
    nearest_palindrome = -1
    for candidate in candidates:
        distance_to_candidate = abs(candidate - original_num)
        distance_to_current_nearest = abs(nearest_palindrome - original_num)
        
        # Update if this is the first candidate, or if it's closer,
        # or if it's equally close but smaller
        if (nearest_palindrome == -1 or 
            distance_to_candidate < distance_to_current_nearest or
            (distance_to_candidate == distance_to_current_nearest and 
                candidate < nearest_palindrome)):
            nearest_palindrome = candidate
    
    return str(nearest_palindrome)
    # Time: O(n)
    # Space: O(n)
    # n = the length of the input string


def main():
    result = nearest_palindromic("123")
    print(result) # "121"

    result = nearest_palindromic("1")
    print(result) # "0"

if __name__ == "__main__":
    main()
