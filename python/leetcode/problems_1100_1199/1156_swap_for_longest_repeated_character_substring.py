# ---------------------------------------------------
# 1156. Swap For Longest Repeated Character Substring
# ---------------------------------------------------

# Problem: https://leetcode.com/problems/swap-for-longest-repeated-character-substring
#
# You are given a string text. You can swap two of the characters in the text.
# 
# Return the length of the longest substring with repeated characters.
# 
# Example 1:
# 
# Input: text = "ababa"
# Output: 3
# 
# Explanation: We can swap the first 'b' with the last 'a', or the last 'b' with
# the first 'a'. Then, the longest repeated character substring is "aaa" with
# length 3.
# 
# Example 2:
# 
# Input: text = "aaabaaa"
# Output: 6
# 
# Explanation: Swap 'b' with the last 'a' (or the first 'a'), and we get longest
# repeated character substring "aaaaaa" with length 6.
# 
# Example 3:
# 
# Input: text = "aaaaa"
# Output: 5
# 
# Explanation: No need to swap, longest repeated character substring is "aaaaa"
# with length is 5.
# 
# 
# Constraints:
#         1 <= text.length <= 2 * 10⁴
#         text consist of lowercase English characters only.

from collections import Counter
from itertools import groupby

# Solution: https://leetcode.com/problems/swap-for-longest-repeated-character-substring/solutions/2919301/python-3-9-lines-groupby-w-example-t-s-95-15
# Credit: Capt Spaulding -> https://leetcode.com/u/Spaulding_/
def max_rep_opt1(text):
    c = Counter(text)

    ch, ct = zip(*[(k, sum(1 for _ in g))
                    for k, g in groupby(text)])

    n = len(ch)

    ans = max(ct[i] + (ct[i] < c[ch[i]]) for i in range(n))

    for i in range(1, n - 1):
        if ch[i - 1] == ch[i + 1] and ct[i] == 1:
            sm = ct[i - 1] + ct[i + 1]
            ans = max(ans, sm + (sm < c[ch[i - 1]]))

    return ans
    # Time: O(n)
    # Space: O(n)

def main():
    result = max_rep_opt1(text = "ababa")
    print(result) # 3

    result = max_rep_opt1(text = "aaabaaa")
    print(result) # 6

    result = max_rep_opt1(text = "aaaaa")
    print(result) # 5 <=== this one fails

if __name__ == "__main__":
    main()
