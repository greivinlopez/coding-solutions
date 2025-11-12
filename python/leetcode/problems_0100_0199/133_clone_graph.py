# -----------------
# 133. Clone Graph
# -----------------

# Problem: https://leetcode.com/problems/clone-graph/
# 
# Given a reference of a node in a connected undirected graph.
# 
# Return a deep copy (clone) of the graph.
# 
# Each node in the graph contains a value (int) and a list (List[Node]) of its 
# neighbors.
# 
# class Node {
#     public int val;
#     public List<Node> neighbors;
# }

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


# Solution: https://youtu.be/mQeF6bN8hMk
# Credit: Navdeep Singh founder of NeetCode
def clone_graph(node):
    oldToNew = {}

    def dfs(node):
        if node in oldToNew:
            return oldToNew[node]

        copy = Node(node.val)
        oldToNew[node] = copy
        for nei in node.neighbors:
            copy.neighbors.append(dfs(nei))
        return copy

    return dfs(node) if node else None

# Solution: https://youtu.be/wWE7YzuBBkE
# Credit: Greg Hogg
def clone_graph(node):
    if not node:
        return None

    start = node
    o_to_n = {}
    stk = [start]
    visited = set()
    visited.add(start)

    while stk:
        node = stk.pop()
        o_to_n[node] = Node(val=node.val)

        for nei in node.neighbors:
            if nei not in visited:
                visited.add(nei)
                stk.append(nei)

    for old_node, new_node in o_to_n.items():
        for nei in old_node.neighbors:
            new_nei = o_to_n[nei]
            new_node.neighbors.append(new_nei)

    return o_to_n[start]

def main():
    # To be created
    print('TODO')

if __name__ == "__main__":
    main()