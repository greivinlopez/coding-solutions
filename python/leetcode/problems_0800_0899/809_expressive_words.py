# ---------------------
# 809. Expressive Words
# ---------------------

# Problem: https://leetcode.com/problems/expressive-words
#
# Sometimes people repeat letters to represent extra feeling. For example:
# 
#         "hello" -> "heeellooo"
#         "hi" -> "hiiii"
# 
# In these strings like "heeellooo", we have groups of adjacent letters that are
# all the same: "h", "eee", "ll", "ooo".
# 
# You are given a string s and an array of query strings words. A query word is
# stretchy if it can be made to be equal to s by any number of applications of the
# following extension operation: choose a group consisting of characters c, and
# add some number of characters c to the group so that the size of the group is
# three or more.
#         
#   * For example, starting with "hello", we could do an extension on the
#     group "o" to get "hellooo", but we cannot get "helloo" since the group "oo" has
#     a size less than three. Also, we could do another extension like "ll" -> "lllll"
#     to get "helllllooo". If s = "helllllooo", then the query word "hello" would be
#     stretchy because of these two extension operations: query = "hello" -> "hellooo"
#     -> "helllllooo" = s.
# 
# Return the number of query strings that are stretchy.
# 
# Example 1:
# 
# Input: s = "heeellooo", words = ["hello", "hi", "helo"]
# Output: 1
# 
# Explanation:
# We can extend "e" and "o" in the word "hello" to get "heeellooo".
# We can't extend "helo" to get "heeellooo" because the group "ll" is not size 3
# or more.
# 
# Example 2:
# 
# Input: s = "zzzzzyyyyy", words = ["zzyy","zy","zyy"]
# Output: 3
# 
# 
# Constraints:
#         1 <= s.length, words.length <= 100
#         1 <= words[i].length <= 100
#         s and words[i] consist of lowercase letters.


# Solution: https://algo.monster/liteproblems/809
# Credit: AlgoMonster
def expressive_words(s, words):
    def is_stretchy(source, target):
        source_len, target_len = len(source), len(target)
        
        # Target cannot be stretched if it's longer than source
        if target_len > source_len:
            return False
        
        source_idx = target_idx = 0
        
        # Process both strings character by character
        while source_idx < source_len and target_idx < target_len:
            # Characters must match at current positions
            if source[source_idx] != target[target_idx]:
                return False
            
            # Count consecutive occurrences in source
            source_group_end = source_idx
            while source_group_end < source_len and source[source_group_end] == source[source_idx]:
                source_group_end += 1
            source_group_count = source_group_end - source_idx
            
            # Count consecutive occurrences in target
            target_group_end = target_idx
            while target_group_end < target_len and target[target_group_end] == target[target_idx]:
                target_group_end += 1
            target_group_count = target_group_end - target_idx
            
            # Move indices to next group
            source_idx = source_group_end
            target_idx = target_group_end
            
            # Check stretching rules:
            # 1. Source must have at least as many characters as target
            # 2. If source has fewer than 3 characters, counts must match exactly
            if source_group_count < target_group_count or \
                (source_group_count < 3 and source_group_count != target_group_count):
                return False
        
        # Both strings must be fully processed
        return source_idx == source_len and target_idx == target_len
    
    # Count how many words can be stretched to match s
    return sum(is_stretchy(s, word) for word in words)
    # Time: O(m * n + m * w)
    # Space: O(1)
    # n = the length of string s
    # m = the number of words in the words array
    # w = the average length of words in the array.


def main():
    result = expressive_words(s = "heeellooo", words = ["hello", "hi", "helo"])
    print(result) # 1

    result = expressive_words(s = "zzzzzyyyyy", words = ["zzyy","zy","zyy"])
    print(result) # 3

if __name__ == "__main__":
    main()
