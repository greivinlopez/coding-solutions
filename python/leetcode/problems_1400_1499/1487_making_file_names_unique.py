# ---------------------------------
# 1487. Making File Names Unique 📁
# ---------------------------------

# Problem: https://leetcode.com/problems/making-file-names-unique
#
# Given an array of strings names of size n. You will create n folders in your
# file system such that, at the iᵗʰ minute, you will create a folder with the name
# names[i].
# 
# Since two files cannot have the same name, if you enter a folder name that was
# previously used, the system will have a suffix addition to its name in the form
# of (k), where, k is the smallest positive integer such that the obtained name
# remains unique.
# 
# Return an array of strings of length n where ans[i] is the actual name the
# system will assign to the iᵗʰ folder when you create it.
# 
# Example 1:
# 
# Input: names = ["pes","fifa","gta","pes(2019)"]
# Output: ["pes","fifa","gta","pes(2019)"]
# 
# Explanation: Let's see how the file system creates folder names:
# "pes" --> not assigned before, remains "pes"
# "fifa" --> not assigned before, remains "fifa"
# "gta" --> not assigned before, remains "gta"
# "pes(2019)" --> not assigned before, remains "pes(2019)"
# 
# Example 2:
# 
# Input: names = ["gta","gta(1)","gta","avalon"]
# Output: ["gta","gta(1)","gta(2)","avalon"]
# 
# Explanation: Let's see how the file system creates folder names:
# "gta" --> not assigned before, remains "gta"
# "gta(1)" --> not assigned before, remains "gta(1)"
# "gta" --> the name is reserved, system adds (k), since "gta(1)" is also
# reserved, systems put k = 2. it becomes "gta(2)"
# "avalon" --> not assigned before, remains "avalon"
# Example 3:
# Input: names = ["onepiece","onepiece(1)","onepiece(2)","onepiece(3)","onepiece"]
# Output: ["onepiece","onepiece(1)","onepiece(2)","onepiece(3)","onepiece(4)"]
# Explanation: When the last folder is created, the smallest positive valid k is
# 4, and it becomes "onepiece(4)".
# 
# 
# Constraints:
#         1 <= names.length <= 5 * 10⁴
#         1 <= names[i].length <= 20
#         names[i] consists of lowercase English letters, digits, and/or round brackets.

from collections import defaultdict

# Solution: https://algo.monster/liteproblems/1487
# Credit: AlgoMonster
def get_folder_names(names):
    # Dictionary to track the next available suffix number for each base name
    name_counter = defaultdict(int)
    
    for i, name in enumerate(names):
        # Check if the current name already exists
        if name in name_counter:
            # Get the next suffix number to try
            suffix_num = name_counter[name]
            
            # Find the smallest available suffix by incrementing
            while f'{name}({suffix_num})' in name_counter:
                suffix_num += 1
            
            # Update the next available suffix for this base name
            name_counter[name] = suffix_num + 1
            
            # Modify the current name with the suffix
            names[i] = f'{name}({suffix_num})'
        
        # Mark the final name (original or modified) as used
        name_counter[names[i]] = 1
        
    return names
    # Time: O(n)
    # Space: O(n)
    # n = the sum of the lengths of all file names in the names array.


def main():
    result = get_folder_names(names = ["pes","fifa","gta","pes(2019)"])
    print(result) # ['pes', 'fifa', 'gta', 'pes(2019)']

    result = get_folder_names(names = ["gta","gta(1)","gta","avalon"])
    print(result) # ['gta', 'gta(1)', 'gta(2)', 'avalon']

    result = get_folder_names(names = ["onepiece","onepiece(1)","onepiece(2)","onepiece(3)","onepiece"])
    print(result) # ['onepiece', 'onepiece(1)', 'onepiece(2)', 'onepiece(3)', 'onepiece(4)']

if __name__ == "__main__":
    main()
