# ------------------------------
# 1316. Distinct Echo Substrings
# ------------------------------

# Problem: https://leetcode.com/problems/distinct-echo-substrings
#
# Return the number of distinct non-empty substrings of text that can be written
# as the concatenation of some string with itself (i.e. it can be written as a +
# a where a is some string).
# 
# Example 1:
# 
# Input: text = "abcabcabc"
# Output: 3
# 
# Explanation: The 3 substrings are "abcabc", "bcabca" and "cabcab".
# 
# Example 2:
# 
# Input: text = "leetcodeleetcode"
# Output: 2
# 
# Explanation: The 2 substrings are "ee" and "leetcodeleetcode".
# 
# 
# Constraints:
#         1 <= text.length <= 2000
#         text has only lowercase English letters.


# Solution: https://algo.monster/liteproblems/1316
# Credit: AlgoMonster
def distinct_echo_substrings(text):

    def get_hash(left: int, right: int) -> int:
        return (hash_values[right] - hash_values[left - 1] * powers[right - left + 1]) % MOD
    
    # Initialize constants and variables
    n = len(text)
    BASE = 131  # Prime base for rolling hash
    MOD = 10**9 + 7  # Large prime modulus to avoid collisions
    
    # Precompute hash values and powers of base
    # hash_values[i] stores hash of text[0:i]
    # powers[i] stores BASE^i mod MOD
    hash_values = [0] * (n + 10)
    powers = [1] * (n + 10)
    
    # Build hash array and power array
    for i, char in enumerate(text):
        # Convert character to number (a=1, b=2, ...)
        char_value = ord(char) - ord('a') + 1
        # Calculate cumulative hash
        hash_values[i + 1] = (hash_values[i] * BASE + char_value) % MOD
        # Calculate powers of base
        powers[i + 1] = (powers[i] * BASE) % MOD
    
    # Set to store unique echo substring hashes
    unique_echo_hashes = set()
    
    # Check all possible echo substrings
    # i is the starting position (0-indexed)
    for i in range(n - 1):
        # j is the ending position (0-indexed), step by 2 for even length
        for j in range(i + 1, n, 2):
            # Calculate midpoint of substring
            midpoint = (i + j) >> 1
            
            # Get hash of first half [i, midpoint]
            first_half_hash = get_hash(i + 1, midpoint + 1)
            
            # Get hash of second half [midpoint+1, j]
            second_half_hash = get_hash(midpoint + 2, j + 1)
            
            # If both halves are identical, it's an echo substring
            if first_half_hash == second_half_hash:
                unique_echo_hashes.add(first_half_hash)
    
    return len(unique_echo_hashes)
    # Time: O(n²)
    # Space: O(n)


def main():
    result = distinct_echo_substrings(text = "abcabcabc")
    print(result) # 3

    result = distinct_echo_substrings(text = "leetcodeleetcode")
    print(result) # 2

if __name__ == "__main__":
    main()
