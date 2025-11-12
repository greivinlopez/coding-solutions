# ---------------------------------------------
# 423. Reconstruct Original Digits from English
# ---------------------------------------------

# Problem: https://leetcode.com/problems/reconstruct-original-digits-from-english
#
# Given a string s containing an out-of-order English representation of digits
# 0-9, return the digits in ascending order.
# 
# Example 1:
# 
# Input: s = "owoztneoer"
# Output: "012"
# 
# Example 2:
# 
# Input: s = "fviefuro"
# Output: "45"
# 
# 
# Constraints:
#       1 <= s.length <= 10⁵
#       s[i] is one of the characters ["e","g","f","i","h","o","n","s","r","u","t","w","v","x","z"].
#       s is guaranteed to be valid.

from collections import Counter, defaultdict

# Solution: https://leetcode.com/problems/reconstruct-original-digits-from-english/solutions/1131114/python-go-o-n-by-dictionary-w-diagram
# Credit: Brian Chiang -> https://leetcode.com/u/brianchiang_tw/
def original_digits(s):
    def mapping_rebuild(digit_occ_dict, char_occ_dict):
        ## Rebuild the number and its occurrence from character frequency analysis
        # "z" only shows up in "zero"
        digit_occ_dict [0] = char_occ_dict['z']

        # "w" only shows up in "two"
        digit_occ_dict [2] = char_occ_dict['w']

        # "u" only shows up in "four"
        digit_occ_dict [4] = char_occ_dict['u']

        # "x" only shows up in "six"
        digit_occ_dict [6] = char_occ_dict['x']

        # "g" only shows up in "eight"
        digit_occ_dict [8] = char_occ_dict['g']

        # "o" only shows up in "zero", "one", "two", "four"
        digit_occ_dict [1] = char_occ_dict['o'] - digit_occ_dict [0] - digit_occ_dict [2] - digit_occ_dict [4]

        # "h" only shows up in "three", "eight"
        digit_occ_dict [3] = char_occ_dict['h'] - digit_occ_dict [8]

        # "f" only shows up in "four", "five"
        digit_occ_dict [5] = char_occ_dict['f'] - digit_occ_dict [4]

        # "s" only shows up in "six", "seven"
        digit_occ_dict [7] = char_occ_dict['s'] - digit_occ_dict [6]

        # "i" only shows up in "five", "six", "eight", "nine"
        digit_occ_dict [9] = char_occ_dict['i'] - digit_occ_dict [5] - digit_occ_dict [6] - digit_occ_dict [8]

        return
    # ----------------------------------------------------------
    
    ## dictionary of input s
    # key: ascii character
    # value: occurrence of ascii character
    char_occ_dict = Counter(s)
    
    ## dictionary
    # key: digit
    # value: occurrence of digit
    digit_occ_dict = defaultdict( int )
    
    # rebuild digit-occurrence mapping from input s and its char-occurrence mapping
    mapping_rebuild( digit_occ_dict , char_occ_dict)
    
    # rebuild digit string in ascending order
    digit_string = "".join( (str(digit) * digit_occ_dict [digit]) for digit in range(0, 10) )
    
    return digit_string
       

def main():
    result = original_digits("owoztneoer")
    print(result) # "012"

    result = original_digits("fviefuro")
    print(result) # "45"

if __name__ == "__main__":
    main()
