# ----------------------
# 2306. Naming A Company
# ----------------------

# Problem: https://leetcode.com/problems/naming-a-company
#
# You are given an array of strings ideas that represents a list of names to be
# used in the process of naming a company. The process of naming a company is as
# follows:
# 
#   Choose 2 distinct names from ideas, call them ideaA and ideaB.
#         
#   Swap the first letters of ideaA and ideaB with each other.
#         
#   If both of the new names are not found in the original ideas, then the
# name ideaA ideaB (the concatenation of ideaA and ideaB, separated by a space) is
# a valid company name.
#         
#   Otherwise, it is not a valid name.
# 
# Return the number of distinct valid names for the company.
# 
# Example 1:
# 
# Input: ideas = ["coffee","donuts","time","toffee"]
# Output: 6
# Explanation: The following selections are valid:
# - ("coffee", "donuts"): The company name created is "doffee conuts".
# - ("donuts", "coffee"): The company name created is "conuts doffee".
# - ("donuts", "time"): The company name created is "tonuts dime".
# - ("donuts", "toffee"): The company name created is "tonuts doffee".
# - ("time", "donuts"): The company name created is "dime tonuts".
# - ("toffee", "donuts"): The company name created is "doffee tonuts".
# Therefore, there are a total of 6 distinct company names.
# The following are some examples of invalid selections:
# - ("coffee", "time"): The name "toffee" formed after swapping already exists in
# the original array.
# - ("time", "toffee"): Both names are still the same after swapping and exist in
# the original array.
# - ("coffee", "toffee"): Both names formed after swapping already exist in the
# original array.
# 
# Example 2:
# 
# Input: ideas = ["lack","back"]
# Output: 0
# Explanation: There are no valid selections. Therefore, 0 is returned.
# 
# 
# Constraints:
#         2 <= ideas.length <= 5 * 10^4
#         1 <= ideas[i].length <= 10
#         ideas[i] consists of lowercase English letters.
#         All the strings in ideas are unique.


# Solution: https://youtu.be/NrHpgTScOcY
# Credit: Navdeep Singh founder of NeetCode
def distinct_names(ideas):
    suffixes = dict()
    for idea in ideas:
        if idea[0] not in suffixes:
            suffixes[idea[0]] = set()
        suffixes[idea[0]].add(idea[1:])

    if len(suffixes) < 2:
        return 0

    num_distinct_names = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for prefix_1 in suffixes:
        for prefix_2 in suffixes:
            if prefix_2 > prefix_1:
                num_suffixes_1 = len(suffixes[prefix_1])
                num_suffixes_2 = len(suffixes[prefix_2])
                for suffix in suffixes[prefix_1]:
                    if suffix in suffixes[prefix_2]:
                        num_suffixes_1 -= 1
                        num_suffixes_2 -= 1
                num_distinct_names += 2 * num_suffixes_1 * num_suffixes_2

    return num_distinct_names


def main():
    result = distinct_names(ideas = ["coffee","donuts","time","toffee"])
    print(result) # 6

    result = distinct_names(ideas = ["lack","back"])
    print(result) # 0

if __name__ == "__main__":
    main()
