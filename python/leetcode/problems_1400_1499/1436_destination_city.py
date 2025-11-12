# ----------------------
# 1436. Destination City
# ----------------------

# Problem: https://leetcode.com/problems/destination-city
#
# You are given the array paths, where paths[i] = [cityAᵢ, cityBᵢ] means there
# exists a direct path going from cityAᵢ to cityBᵢ. Return the destination city,
# that is, the city without any path outgoing to another city.
# 
# It is guaranteed that the graph of paths forms a line without any loop,
# therefore, there will be exactly one destination city.
# 
# Example 1:
# 
# Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
# Output: "Sao Paulo"
# 
# Explanation: Starting at "London" city you will reach "Sao Paulo" city which is
# the destination city. Your trip consist of: "London" -> "New York" -> "Lima" ->
# "Sao Paulo".
# 
# Example 2:
# 
# Input: paths = [["B","C"],["D","B"],["C","A"]]
# Output: "A"
# 
# Explanation: All possible trips are: 
# "D" -> "B" -> "C" -> "A". 
# "B" -> "C" -> "A". 
# "C" -> "A". 
# "A". 
# Clearly the destination city is "A".
# 
# Example 3:
# 
# Input: paths = [["A","Z"]]
# Output: "Z"
# 
# Constraints:
#         1 <= paths.length <= 100
#         paths[i].length == 2
#         1 <= cityAᵢ.length, cityBᵢ.length <= 10
#         cityAᵢ != cityBᵢ
#         All strings consist of lowercase and uppercase English letters and the
# space character.


# Solution: https://youtu.be/Hi8vMnnTZHE
# Credit: Navdeep Singh founder of NeetCode
def dest_city(paths):
    s = set()
    for p in paths:
        s.add(p[0])
    
    for p in paths:
        if p[1] not in s:
            return p[1]
    # Time: O(n)
    # Space: O(n)

# Credit: Jeel Gajera -> https://github.com/JeelGajera
def dest_city_alt(paths):
    route = {}
    n = len(paths)
    for i in range(n):
        route[paths[i][0]] = paths[i][1]

    source = list(route.keys())
    city = source[0]
    while city in source:
        city = route[city]
    else:
        return city
    # Time: O(n²)
    # Space: O(n)


def main():
    result = dest_city([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]])
    print(result) # "Sao Paulo"

    result = dest_city([["B","C"],["D","B"],["C","A"]])
    print(result) # "A"

    result = dest_city([["A","Z"]])
    print(result) # "Z"

if __name__ == "__main__":
    main()
