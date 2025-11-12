# ------------------------------
# 937. Reorder Data in Log Files
# ------------------------------

# Problem: https://leetcode.com/problems/reorder-data-in-log-files
#
# You are given an array of logs. Each log is a space-delimited string of words,
# where the first word is the identifier.
# 
# There are two types of logs:
#         
#   * Letter-logs: All words (except the identifier) consist of lowercase
#     English letters.    
#   * Digit-logs: All words (except the identifier) consist of digits.
# 
# Reorder these logs so that:
#   1. The letter-logs come before all digit-logs.
#   2. The letter-logs are sorted lexicographically by their contents. If their
#      contents are the same, then sort them lexicographically by their identifiers.
#   3. The digit-logs maintain their relative ordering.
# 
# Return the final order of the logs.
# 
# Example 1:
# 
# Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3
# art zero"]
# Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2
# 3 6"]
# 
# Explanation:
# The letter-log contents are all different, so their ordering is "art can", "art
# zero", "own kit dig".
# The digit-logs have a relative order of "dig1 8 1 5 1", "dig2 3 6".
# 
# Example 2:
# 
# Input: logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act
# zoo"]
# Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
# 
# 
# Constraints:
#   
#   1 <= logs.length <= 100
#   3 <= logs[i].length <= 100
#   All the tokens of logs[i] are separated by a single space.
#   logs[i] is guaranteed to have an identifier and at least one word after the identifier.


# Solution: https://algo.monster/liteproblems/937
# Credit: AlgoMonster
def reorder_log_files(logs):
    
    def get_sort_key(log):
        # Split log into identifier and content (split only on first space)
        identifier, content = log.split(" ", 1)
        
        # Check if this is a letter-log (first character of content is alphabetic)
        if content[0].isalpha():
            # Letter-log: sort by (0, content, identifier)
            # 0 ensures letter-logs come first
            return (0, content, identifier)
        else:
            # Digit-log: return (1,) to place after letter-logs
            # Single element tuple maintains relative order among digit-logs
            return (1,)
    
    # Sort logs using the custom key function
    return sorted(logs, key=get_sort_key)
    # Time: O(n * m * log(n))
    # Space: O(n * m)
    # n = number of elements
    # m = the average length of each log string.


def main():
    result = reorder_log_files(logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"])
    print(result) # ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]

    result = reorder_log_files(logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"])
    print(result) # ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]

if __name__ == "__main__":
    main()
