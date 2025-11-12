# -----------------------------
# 316. Remove Duplicate Letters
# -----------------------------

# Problem: https://leetcode.com/problems/remove-duplicate-letters
#
# Given a string s, remove duplicate letters so that every letter appears once and
# only once. You must make sure your result is the smallest in lexicographical
# order among all possible results.
# 
# Example 1:
# 
# Input: s = "bcabc"
# Output: "abc"
# 
# Example 2:
# 
# Input: s = "cbacdcbc"
# Output: "acdb"
# 
# 
# Constraints:
#         1 <= s.length <= 10⁴
#         s consists of lowercase English letters.
# 
# 
# Note: This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/


# Credit: Jaweria Batool -> https://github.com/Jaweria-B
def remove_duplicate_letters(s):
    stack = []
    seen = set() 
    last_occ = {c: i for i, c in enumerate(s)}
    
    for i, c in enumerate(s):
        if c not in seen:
            
            while stack and c < stack[-1] and i < last_occ[stack[-1]]:
                seen.discard(stack.pop())
            seen.add(c)
            stack.append(c)
    
    return ''.join(stack)
    # Time: O(n)
    # Space: O(1)


def main():
    result = remove_duplicate_letters(s = "bcabc")
    print(result) # "abc"

    result = remove_duplicate_letters(s = "cbacdcbc")
    print(result) # "acdb"

if __name__ == "__main__":
    main()
