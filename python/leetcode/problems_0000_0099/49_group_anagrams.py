# --------------------
# 49. Group Anagrams
# --------------------

# Problem: https://leetcode.com/problems/group-anagrams/
# Given an array of strings strs, group the anagrams together. 
# ou can return the answer in any order.

# Solution: https://youtu.be/vzdNOK2oB2E
# Credit: Navdeep Singh founder of NeetCode 
def group_anagrams(strs):
    # Time: O(m * n)
    groups = {}

    # Iterate over strings
    for s in strs: # O(m)
        count = {}

        # Count frequency of each character
        for char in s: # O(n)
            count[char] = count.get(char, 0) + 1

        # Convert count Dict to List, sort it, and then convert to Tuple (we cannot use dicts or lists as keys in a hashmap)
        tup = tuple(sorted(count.items())) # O(1) because there is limited amount of possible keys in the alphabet -> O(26) + O(26*log26) + O(26)

        if tup in groups:
            groups[tup].append(s)
        else:
            groups[tup] = [s] 
        
    return list(groups.values())

# Solution: https://youtu.be/eDmxPfVa81k
# Credit: Greg Hogg
from collections import defaultdict
def group_anagrams_alt(strs):
    # n is the number of strings, m is the length of largest string
    # Time: O(n * m)
    # Space: O(n * m)
    anagrams_dict = defaultdict(list)
    for s in strs: # n
        count = [0] * 26
        for c in s:
            count[ord(c) - ord("a")] += 1
        key = tuple(count)
        anagrams_dict[key].append(s)

    return list(anagrams_dict.values())

def main():
    result = group_anagrams_alt(["eat","tea","tan","ate","nat","bat"]) 
    # Output [["bat"],["nat","tan"],["ate","eat","tea"]]
    print(result)
    result = group_anagrams_alt([""]) # [[""]]
    print(result)
    result = group_anagrams_alt(["a"]) # [["a"]]
    print(result)

if __name__ == "__main__":
    main()