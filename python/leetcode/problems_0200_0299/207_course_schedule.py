# --------------------
# 207. Course Schedule
# --------------------

# Problem: https://leetcode.com/problems/course-schedule/
# 
# There are a total of numCourses courses you have to take, labeled from 0 to 
# numCourses - 1. You are given an array prerequisites where 
# prerequisites[i] = [ai, bi] indicates that you must take course bi first if 
# you want to take course ai.
# 
# 
# 	For example, the pair [0, 1], indicates that to take course 0 you have to 
#   first take course 1.
# 
# 
# Return true if you can finish all courses. Otherwise, return false.
# 
#  
# Example 1:
# 
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.
# 
# 
# Example 2:
# 
# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
# 
#  
# Constraints:
# 
# 	1 <= numCourses <= 2000
# 	0 <= prerequisites.length <= 5000
# 	prerequisites[i].length == 2
# 	0 <= ai, bi < numCourses
# 	All the pairs prerequisites[i] are unique.


# Solution: https://youtu.be/EgI5nU9etnU
# Credit: Navdeep Singh founder of NeetCode
def can_finish(numCourses, prerequisites):
    # dfs
    preMap = {i: [] for i in range(numCourses)}

    # map each course to : prereq list
    for crs, pre in prerequisites:
        preMap[crs].append(pre)

    visiting = set()

    def dfs(crs):
        if crs in visiting:
            return False
        if preMap[crs] == []:
            return True

        visiting.add(crs)
        for pre in preMap[crs]:
            if not dfs(pre):
                return False
        visiting.remove(crs)
        preMap[crs] = []
        return True

    for c in range(numCourses):
        if not dfs(c):
            return False
    return True

# Solution: https://youtu.be/nz5V5pOiT8w
# Credit: Greg Hogg
# Very similar solution
def can_finish_alt(numCourses, prerequisites):
    g = defaultdict(list)
    courses = prerequisites
    for a, b in courses:
        g[a].append(b)

    UNVISITED = 0
    VISITING = 1
    VISITED = 2
    states = [UNVISITED] * numCourses

    def dfs(node):
        state = states[node]
        if state == VISITED: return True
        elif state == VISITING: return False

        states[node] = VISITING

        for nei in g[node]:
            if not dfs(nei): 
                return False
        
        states[node] = VISITED
        return True
    
    for i in range(numCourses):
        if not dfs(i):
            return False
    
    return True 

def main():
    result = can_finish(numCourses = 2, prerequisites = [[1,0]])
    print(result) # True

    result = can_finish(numCourses = 2, prerequisites = [[1,0],[0,1]])
    print(result) # False

if __name__ == "__main__":
    main()
