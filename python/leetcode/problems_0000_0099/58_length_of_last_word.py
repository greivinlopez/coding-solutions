# ------------------------
# 58. Length of Last Word
# ------------------------

# Problem: https://leetcode.com/problems/length-of-last-word/
# 
# Given a string s consisting of words and spaces, return the length of the last word in the string.
# 
# A word is a maximal substring consisting of non-space characters only.

# Solution: https://youtu.be/KT9rltZTybQ
# Credit: Navdeep Singh founder of NeetCode 
# Differ from code below
def length_of_last_word(s):
    # Time: O(n)
    # Space: O(1)
    count = 0
    for i in range(len(s) - 1, -1, -1):
        char = s[i]
        if char == " ":
            if count >= 1:
                return count
        else:
            count += 1
    return count

# Solution: https://leetcode.com/problems/length-of-last-word/solutions/7110842/python-solution-beats-100-00/
# Credit: Moti Alemu -> https://leetcode.com/u/motialemu/
def length_of_last_word_alt(s):
    # Time: O(n)
    # Space: O(1)
    i= len(s)-1
    while i >= 0 and s[i] == " ": 
        i-=1 
    c=0 
    while i >= 0 and s[i] != " ": 
        c+=1 
        i-=1
    return c 

def length_of_last_word_one_liner(s):
    return len(s.split()[-1])

def main():
    result = length_of_last_word_alt("Hello World") # 5
    print(result)
    result = length_of_last_word_alt("   fly me   to   the moon  ") # 4
    print(result)
    result = length_of_last_word_alt("luffy is still joyboy") # 6
    print(result)

if __name__ == "__main__":
    main()