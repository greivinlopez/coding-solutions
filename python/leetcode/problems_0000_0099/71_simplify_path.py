# -----------------------
# 71. Simplify Path
# -----------------------

# Problem: https://leetcode.com/problems/simplify-path/
# 
# You are given an absolute path for a Unix-style file system, which always 
# begins with a slash '/'. Your task is to transform this absolute path into 
# its simplified canonical path.
# 
# The rules of a Unix-style file system are as follows:
# 
# - A single period '.' represents the current directory.
# - A double period '..' represents the previous/parent directory.
# - Multiple consecutive slashes such as '//' and '///' are treated as a single slash '/'.
# - Any sequence of periods that does not match the rules above should be treated as a valid directory or file name. For example, '...' and '....' are valid directory or file names.
# 
# The simplified canonical path should follow these rules:
# 
# - The path must start with a single slash '/'.
# - Directories within the path must be separated by exactly one slash '/'.
# - The path must not end with a slash '/', unless it is the root directory.
# - The path must not have any single or double periods ('.' and '..') used to denote current or parent directories.
# 
# Return the simplified canonical path.

# Solution: https://youtu.be/qYlHrAKJfyA
# Credit: Navdeep Singh founder of NeetCode 
def simplify_path(path):
    stack = []

    for i in path.split("/"):
        #  if i == "/" or i == '//', it becomes '' (empty string)

        if i == "..":
            if stack:
                stack.pop()
        elif i == "." or i == '':
            # skip "." or an empty string
            continue
        else:
            stack.append(i)

    res = "/" + "/".join(stack)
    return res


def main():
    result = simplify_path("/home/") 
    # Expected Output: "/home"
    print(result)
    result = simplify_path("/home//foo/")
    # Expected Output: "/home/foo"
    print(result)
    result = simplify_path("/home/user/Documents/../Pictures")
    # Expected Output: "/home/user/Pictures"
    print(result)
    result = simplify_path("/../")
    # Expected Output: "/"
    print(result)
    result = simplify_path("/.../a/../b/c/../d/./")
    # Expected Output: "/.../b/d"
    print(result)

if __name__ == "__main__":
    main()