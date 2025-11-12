# ------------------------------
# 187. Repeated Dna Sequences 🧬
# ------------------------------

# Problem: https://leetcode.com/problems/repeated-dna-sequences/
# 
# The DNA sequence is composed of a series of nucleotides abbreviated as 
# 'A', 'C', 'G', and 'T'.
# 
# 
# 	For example, "ACGAATTCCG" is a DNA sequence.
# 
# 
# When studying DNA, it is useful to identify repeated sequences within the DNA.
# 
# Given a string s that represents a DNA sequence, return all the 10-letter-long
# sequences (substrings) that occur more than once in a DNA molecule. You may 
# return the answer in any order.
# 
#  
# Example 1:
# Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# Output: ["AAAAACCCCC","CCCCCAAAAA"]
# Example 2:
# Input: s = "AAAAAAAAAAAAA"
# Output: ["AAAAAAAAAA"]
# 
#  
# Constraints:
# 
# 	1 <= s.length <= 105
# 	s[i] is either 'A', 'C', 'G', or 'T'.


# Solution: https://youtu.be/FzTYfsmtOso
# Credit: Navdeep Singh founder of NeetCode
def find_repeated_dna_sequences(s):
    result = set()
    previous_sequences = set()
    for i in range(len(s) - 9):
        current = s[i:i+10]
        if current in previous_sequences:
            result.add(current)
        previous_sequences.add(current)
    return list(result)


def main():
    result = find_repeated_dna_sequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")
    print(result) # ["AAAAACCCCC","CCCCCAAAAA"]

    result = find_repeated_dna_sequences("AAAAAAAAAAAAA")
    print(result) # ["AAAAAAAAAA"]

if __name__ == "__main__":
    main()
