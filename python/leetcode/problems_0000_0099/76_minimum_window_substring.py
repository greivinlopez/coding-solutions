# --------------------------------
# 76. Minimum Window Substring 🪟
# --------------------------------

# Problem: https://leetcode.com/problems/minimum-window-substring/
# 
# Given two strings s and t of lengths m and n respectively, return the minimum 
# window substring of s such that every character in t (including duplicates) 
# is included in the window. If there is no such substring, return the empty string "".
# 
# The testcases will be generated such that the answer is unique.

# Solution: https://www.youtube.com/watch?v=jSto0O4AJbM
# Credit: Navdeep Singh founder of NeetCode
def min_window(s, t):
    if len(s) < len(t):
        return ""

    countT, window = {}, {}
    for c in t:
        countT[c] = 1 + countT.get(c, 0)

    have, need = 0, len(countT)
    res, resLen = [-1, -1], float("infinity")
    l = 0
    for r in range(len(s)):
        c = s[r]
        window[c] = 1 + window.get(c, 0)

        if c in countT and window[c] == countT[c]:
            have += 1

        while have == need:
            # update our result
            if (r - l + 1) < resLen:
                res = [l, r]
                resLen = r - l + 1
            # pop from the left of our window
            window[s[l]] -= 1
            if s[l] in countT and window[s[l]] < countT[s[l]]:
                have -= 1
            l += 1
    l, r = res
    return s[l : r + 1] if resLen != float("infinity") else ""

def main():
    result = min_window(s = "ADOBECODEBANC", t = "ABC") # "BANC"
    print(result)
    result = min_window(s = "a", t = "a") # "a"
    print(result)
    result = min_window(s = "a", t = "aa") # ""
    print(result)

if __name__ == "__main__":
    main()