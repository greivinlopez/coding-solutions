# -------------------------------
# 388. Longest Absolute File Path
# -------------------------------

# Problem: https://leetcode.com/problems/longest-absolute-file-path
#
# Suppose we have a file system that stores both files and directories. An example
# of one system is represented in the following picture:
# 
# https://assets.leetcode.com/uploads/2020/08/28/mdir.jpg
# 
# Here, we have dir as the only directory in the root. dir contains two
# subdirectories, subdir1 and subdir2. subdir1 contains a file file1.ext and
# subdirectory subsubdir1. subdir2 contains a subdirectory subsubdir2, which
# contains a file file2.ext.
# 
# In text form, it looks like this (with ⟶ representing the tab character):
# 
# dir
# ⟶ subdir1
# ⟶ ⟶ file1.ext
# ⟶ ⟶ subsubdir1
# ⟶ subdir2
# ⟶ ⟶ subsubdir2
# ⟶ ⟶ ⟶ file2.ext
# 
# If we were to write this representation in code, it will look like this: "dir\n\
# tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.
# ext". Note that the '\n' and '\t' are the new-line and tab characters.
# 
# Every file and directory has a unique absolute path in the file system, which is
# the order of directories that must be opened to reach the file/directory itself,
# all concatenated by '/'s. Using the above example, the absolute path to
# file2.ext is "dir/subdir2/subsubdir2/file2.ext". Each directory name consists of
# letters, digits, and/or spaces. Each file name is of the form name.extension,
# where name and extension consist of letters, digits, and/or spaces.
# 
# Given a string input representing the file system in the explained format,
# return the length of the longest absolute path to a file in the abstracted file
# system. If there is no file in the system, return 0.
# 
# Note that the testcases are generated such that the file system is valid and no
# file or directory name has length 0.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2020/08/28/dir1.jpg
# 
# Input: input = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
# Output: 20
# 
# Explanation: We have only one file, and the absolute path is
# "dir/subdir2/file.ext" of length 20.
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2020/08/28/dir2.jpg
# 
# Input: input = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsu
# bsubdir2\n\t\t\tfile2.ext"
# Output: 32
# 
# Explanation: We have two files:
# "dir/subdir1/file1.ext" of length 21
# "dir/subdir2/subsubdir2/file2.ext" of length 32.
# We return 32 since it is the longest absolute path to a file.
# 
# Example 3:
# 
# Input: input = "a"
# Output: 0
# 
# Explanation: We do not have any files, just a single directory named "a".
# 
# 
# Constraints:
#         1 <= input.length <= 10⁴
#         input may contain lowercase or uppercase English letters, a new line
# character '\n', a tab character '\t', a dot '.', a space ' ', and digits.
#         All file and directory names have positive length.


# Solution: https://leetcode.com/problems/longest-absolute-file-path/solutions/601155/python-o-n-solution-with-stack
# Credit: https://leetcode.com/u/eroneko/
def length_longest_path(input):
    stack = [(-1, 0)]  # (current level, length of the current path)
    foundFile = False
    nextLevel = currLevel = currLen = maxLen = 0
    i, n = 0, len(input)
    while i < n:
        c = input[i]
        if c == '\n':
            # Found a file in the previous item, calculate its path length.
            if foundFile:
                maxLen = max(maxLen, currLen)
                foundFile = False

            # Check the level for the next item.
            nextLevel = 0
            while input[i + 1] == '\t':
                nextLevel += 1
                i += 1

            if currLevel < nextLevel:  # Go down.
                currLen += 1  # '/' takes one pisition in the path.
                stack.append((currLevel, currLen))
            else:  # Stay on the same or go up.
                while stack[-1][0] >= nextLevel:
                    stack.pop()

                currLen = stack[-1][-1]

            currLevel = nextLevel
        else:
            if c == '.':
                foundFile = True

            currLen += 1

        i += 1  # Process the next char.

    if foundFile:  # Process the last file if any.
        maxLen = max(maxLen, currLen)

    return maxLen


def main():
    result = length_longest_path(input = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext")
    print(result) # 20

    result = length_longest_path(input = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext")
    print(result) # 32

    result = length_longest_path(input = "a")
    print(result) # 0

if __name__ == "__main__":
    main()
