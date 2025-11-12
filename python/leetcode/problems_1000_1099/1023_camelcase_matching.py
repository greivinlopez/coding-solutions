# -----------------------
# 1023. Camelcase Matching
# -----------------------

# Problem: https://leetcode.com/problems/camelcase-matching
#
# Given an array of strings queries and a string pattern, return a boolean array
# answer where answer[i] is true if queries[i] matches pattern, and false
# otherwise.
# 
# A query word queries[i] matches pattern if you can insert lowercase English
# letters into the pattern so that it equals the query. You may insert a character
# at any position in pattern or you may choose not to insert any characters at
# all.
# 
# Example 1:
# 
# Input: queries =
# ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FB"
# Output: [true,false,true,true,false]
# 
# Explanation: "FooBar" can be generated like this "F" + "oo" + "B" + "ar".
# "FootBall" can be generated like this "F" + "oot" + "B" + "all".
# "FrameBuffer" can be generated like this "F" + "rame" + "B" + "uffer".
# 
# Example 2:
# 
# Input: queries =
# ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern =
# "FoBa"
# Output: [true,false,true,false,false]
# 
# Explanation: "FooBar" can be generated like this "Fo" + "o" + "Ba" + "r".
# "FootBall" can be generated like this "Fo" + "ot" + "Ba" + "ll".
# 
# Example 3:
# 
# Input: queries =
# ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern =
# "FoBaT"
# Output: [false,true,false,false,false]
# 
# Explanation: "FooBarTest" can be generated like this "Fo" + "o" + "Ba" + "r" +
# "T" + "est".
# 
# 
# Constraints:
#         1 <= pattern.length, queries.length <= 100
#         1 <= queries[i].length <= 100
#         queries[i] and pattern consist of English letters.


# Solution: 
# Credit: Navdeep Singh founder of NeetCode
def camel_match(queries, pattern):

    def is_match(query, pattern):
        query_len, pattern_len = len(query), len(pattern)
        query_idx = 0
        pattern_idx = 0
        
        # Try to match all characters in the pattern
        while pattern_idx < pattern_len:
            # Skip lowercase letters in query that don't match current pattern character
            while query_idx < query_len and query[query_idx] != pattern[pattern_idx] and query[query_idx].islower():
                query_idx += 1
            
            # Check if we've exhausted the query or current characters don't match
            if query_idx == query_len or query[query_idx] != pattern[pattern_idx]:
                return False
            
            # Move both pointers forward after successful match
            query_idx += 1
            pattern_idx += 1
        
        # After matching all pattern characters, only lowercase letters should remain in query
        while query_idx < query_len and query[query_idx].islower():
            query_idx += 1
        
        # All characters in query should be consumed
        return query_idx == query_len
    
    # Apply the matching function to all queries
    return [is_match(query, pattern) for query in queries]
    # Time: O(k * (m + n))
    # Space: O(k)
    # n = the length of the pattern string
    # m = the average length of each query string
    # k = the number of queries


def main():
    result = camel_match(queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FB")
    print(result) # [True, False, True, True, False]

    result = camel_match(queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBa")
    print(result) # [True, False, True, False, False]

    result = camel_match(queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBaT")
    print(result) # [False, True, False, False, False]

if __name__ == "__main__":
    main()
