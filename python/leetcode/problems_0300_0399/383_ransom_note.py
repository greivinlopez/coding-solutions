# ----------------
# 383. Ransom Note
# ----------------

# Problem: https://leetcode.com/problems/ransom-note/
# 
# Given two strings ransomNote and magazine, return true if ransomNote can be 
# constructed by using the letters from magazine and false otherwise.
# 
# Each letter in magazine can only be used once in ransomNote.
#  
# Example 1:
# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:
# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:
# Input: ransomNote = "aa", magazine = "aab"
# Output: true
# 
#  
# Constraints:
# 
# 	1 <= ransomNote.length, magazine.length <= 10^5
# 	ransomNote and magazine consist of lowercase English letters.


# Solution: Not video found
# Credit: Navdeep Singh founder of NeetCode
from collections import Counter

def can_construct(ransomNote, magazine):
    r_counter = Counter(ransomNote)
    m_counter = Counter(magazine)
    # magazine contains (>=) ransomNote
    for c in ransomNote:
        if m_counter[c] < r_counter[c]:
            return False
    return True

# Solution: https://youtu.be/i3bvxJyUB40
# Credit: Greg Hogg
# Brute Force Solution
def can_construct_brute(ransomNote, magazine):
    for letter in ransomNote:
        if letter in magazine:
            position = magazine.index(letter)
            magazine = magazine[:position] + magazine[position+1:]
        else:
            return False

    return True
    # Time: O(R * M)
    # Space: O(1)

# Optimal Solution
from collections import Counter
def can_construct_optimal(ransomNote, magazine):
    hashmap = Counter(magazine) # TC for Counter is O(n)

    for ch in ransomNote:
        if hashmap[ch] > 0:
            hashmap[ch]-=1
        else:
            return False
    return True
    # Time: O(R + M)  -> R = len(ransomNote), M = len(magazine)
    # Space: O(M)     -> we're using a hashmap 

def main():
    result = can_construct(ransomNote = "a", magazine = "b")
    print(result) # False

    result = can_construct(ransomNote = "aa", magazine = "ab")
    print(result) # False

    result = can_construct(ransomNote = "aa", magazine = "aab")
    print(result) # True

if __name__ == "__main__":
    main()
