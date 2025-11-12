# ------------------
# 899. Orderly Queue
# ------------------

# Problem: https://leetcode.com/problems/orderly-queue
#
# You are given a string s and an integer k. You can choose one of the first k
# letters of s and append it at the end of the string.
# 
# Return the lexicographically smallest string you could have after applying the
# mentioned step any number of moves.
# 
# Example 1:
# 
# Input: s = "cba", k = 1
# Output: "acb"
# 
# Explanation:
# In the first move, we move the 1st character 'c' to the end, obtaining the
# string "bac".
# In the second move, we move the 1st character 'b' to the end, obtaining the
# final result "acb".
# 
# Example 2:
# 
# Input: s = "baaca", k = 3
# Output: "aaabc"
# 
# Explanation:
# In the first move, we move the 1st character 'b' to the end, obtaining the
# string "aacab".
# In the second move, we move the 3rd character 'c' to the end, obtaining the
# final result "aaabc".
# 
# 
# Constraints:
#         1 <= k <= s.length <= 1000
#         s consist of lowercase English letters.


# Solution: https://algo.monster/liteproblems/899
# Credit: AlgoMonster
def orderly_queue(s, k):  
    if k == 1:
        # When k=1, we can only rotate the string
        # Try all possible rotations and find the minimum
        min_string = s
        
        # Generate all rotations by moving first character to end
        for _ in range(len(s) - 1):
            s = s[1:] + s[0]  # Move first character to end
            min_string = min(min_string, s)  # Keep track of minimum
            
        return min_string
    
    else:
        # When k >= 2, we can achieve any permutation
        # The smallest permutation is the sorted string
        return "".join(sorted(s))
    # Time: O(n²)
    # Space: O(n)


def main():
    result = orderly_queue(s = "cba", k = 1)
    print(result) # "acb"

    result = orderly_queue(s = "baaca", k = 3)
    print(result) # "aaabc"

if __name__ == "__main__":
    main()
