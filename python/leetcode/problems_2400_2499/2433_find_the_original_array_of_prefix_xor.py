# -------------------------------------------
# 2433. Find The Original Array of Prefix Xor
# -------------------------------------------

# Problem: https://leetcode.com/problems/find-the-original-array-of-prefix-xor
#
# You are given an integer array pref of size n. Find and return the array arr of
# size n that satisfies:
# 
#         pref[i] = arr[0] ^ arr[1] ^ ... ^ arr[i].
# 
# Note that ^ denotes the bitwise-xor operation.
# 
# It can be proven that the answer is unique.
# 
# Example 1:
# 
# Input: pref = [5,2,0,3,1]
# Output: [5,7,2,3,2]
# 
# Explanation: From the array [5,7,2,3,2] we have the following:
# - pref[0] = 5.
# - pref[1] = 5 ^ 7 = 2.
# - pref[2] = 5 ^ 7 ^ 2 = 0.
# - pref[3] = 5 ^ 7 ^ 2 ^ 3 = 3.
# - pref[4] = 5 ^ 7 ^ 2 ^ 3 ^ 2 = 1.
# 
# Example 2:
# 
# Input: pref = [13]
# Output: [13]
# 
# Explanation: We have pref[0] = arr[0] = 13.
# 
# 
# Constraints:
#         1 <= pref.length <= 10⁵
#         0 <= pref[i] <= 10⁶


# Credit: Jaweria Batool -> https://github.com/Jaweria-B
def find_array(pref):
    n = len(pref)
    
    for i in range(n-1, 0, -1):
        pref[i] = pref[i] ^ pref[i-1]
        
    return pref
    # Time: O(n)
    # Space: O(1)


def main():
    result = find_array(pref = [5,2,0,3,1])
    print(result) # [5,7,2,3,2]

    result = find_array(pref = [13])
    print(result) # [13]

if __name__ == "__main__":
    main()
