# ---------------------------------------------
# 30. Substring with Concatenation of All Words
# ---------------------------------------------

# Problem: https://leetcode.com/problems/substring-with-concatenation-of-all-words
#
# You are given a string s and an array of strings words. All the strings of words
# are of the same length.
# 
# A concatenated string is a string that exactly contains all the strings of any
# permutation of words concatenated.
#         
#   * For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd",
#     "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings.
#     "acdbef" is not a concatenated string because it is not the concatenation of any
#     permutation of words.
# 
# Return an array of the starting indices of all the concatenated substrings in s.
# You can return the answer in any order.
# 
# Example 1:
# 
# Input: s = "barfoothefoobarman", words = ["foo","bar"]
# Output: [0,9]
# 
# Explanation:
# The substring starting at 0 is "barfoo". It is the concatenation of
# ["bar","foo"] which is a permutation of words.
# The substring starting at 9 is "foobar". It is the concatenation of
# ["foo","bar"] which is a permutation of words.
# 
# Example 2:
# 
# Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
# Output: []
# 
# Explanation:
# There is no concatenated substring.
# 
# Example 3:
# 
# Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
# Output: [6,9,12]
# 
# Explanation:
# The substring starting at 6 is "foobarthe". It is the concatenation of
# ["foo","bar","the"].
# The substring starting at 9 is "barthefoo". It is the concatenation of
# ["bar","the","foo"].
# The substring starting at 12 is "thefoobar". It is the concatenation of
# ["the","foo","bar"].
# 
# 
# Constraints:
#         1 <= s.length <= 10⁴
#         1 <= words.length <= 5000
#         1 <= words[i].length <= 30
#         s and words[i] consist of lowercase English letters.

import collections

# Credit: Jaweria Batool -> https://github.com/Jaweria-B
def find_substring(s, words):
    wlen = len(words[0])
    slen = wlen * len(words)
    
    track = dict()
    
    occ = collections.Counter(words)
    
    def test():
        for key, val in track.items():
            if val != occ[key]:
                return False
        return True
    
    res = []
    
    for k in range(wlen):
        for i in words:
            track.update({i : 0})
            
        for i in range(k, slen+k, wlen):
            w = s[i: i+wlen]
            if w in words:
                track.update({w: track[w]+1})
        
        if test():
            res.append(k)
            
        for i in range(wlen+k, len(s)-slen+1, wlen):
            nw=s[i+slen-wlen:i+slen]
            pw=s[i-wlen:i]
            if nw in words:
                track.update({nw: track[nw]+1})
            if pw in words:
                track.update({pw: track[pw]-1})
            if test():
                res.append(i)
        
    return res
    # Time: O(n * m * w)
    # Space: O(m * w)
    # n = length of s
    # m = length of words
    # w = length of each word


def main():
    result = find_substring(s = "barfoothefoobarman", words = ["foo","bar"])
    print(result) # [0,9]

    result = find_substring(s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"])
    print(result) # []

    result = find_substring(s = "barfoofoobarthefoobarman", words = ["bar","foo","the"])
    print(result) # [6,9,12]

if __name__ == "__main__":
    main()
