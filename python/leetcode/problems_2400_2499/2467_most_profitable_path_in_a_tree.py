# ------------------------------------
# 2467. Most Profitable Path in a Tree
# ------------------------------------

# Problem: https://leetcode.com/problems/most-profitable-path-in-a-tree
#
# There is an undirected tree with n nodes labeled from 0 to n - 1, rooted at node
# 0. You are given a 2D integer array edges of length n - 1 where edges[i] = [ai,
# bi] indicates that there is an edge between nodes ai and bi in the tree.
# 
# At every node i, there is a gate. You are also given an array of even integers
# amount, where amount[i] represents:
# 
#   the price needed to open the gate at node i, if amount[i] is negative, or,
# 
#   the cash reward obtained on opening the gate at node i, otherwise.
# 
# The game goes on as follows:
# 
#   Initially, Alice is at node 0 and Bob is at node bob.
#   
#   At every second, Alice and Bob each move to an adjacent node. Alice
#   moves towards some leaf node, while Bob moves towards node 0.
#         
#   For every node along their path, Alice and Bob either spend money to
#   open the gate at that node, or accept the reward. Note that:
#                 
#       If the gate is already open, no price will be required, nor will
#       there be any cash reward.
#                 
#       If Alice and Bob reach the node simultaneously, they share the
#       price/reward for opening the gate there. In other words, if the price to open
#       the gate is c, then both Alice and Bob pay c / 2 each. Similarly, if the reward
#       at the gate is c, both of them receive c / 2 each.
#         
#   If Alice reaches a leaf node, she stops moving. Similarly, if Bob
#   reaches node 0, he stops moving. Note that these events are independent of each
#   other.
# 
# Return the maximum net income Alice can have if she travels towards the optimal
# leaf node.
# 
# Example 1:
# 
# Input: edges = [[0,1],[1,2],[1,3],[3,4]], bob = 3, amount = [-2,4,2,-4,6]
# Output: 6
# 
# Explanation:
# The above diagram represents the given tree. The game goes as follows:
# - Alice is initially on node 0, Bob on node 3. They open the gates of their
# respective nodes.
#   Alice's net income is now -2.
# - Both Alice and Bob move to node 1.
#   Since they reach here simultaneously, they open the gate together and share
# the reward.
#   Alice's net income becomes -2 + (4 / 2) = 0.
# - Alice moves on to node 3. Since Bob already opened its gate, Alice's income
# remains unchanged.
#   Bob moves on to node 0, and stops moving.
# - Alice moves on to node 4 and opens the gate there. Her net income becomes 0 +
# 6 = 6.
# Now, neither Alice nor Bob can make any further moves, and the game ends.
# It is not possible for Alice to get a higher net income.
# 
# Example 2:
# 
# Input: edges = [[0,1]], bob = 1, amount = [-7280,2350]
# Output: -7280
# 
# Explanation:
# Alice follows the path 0->1 whereas Bob follows the path 1->0.
# Thus, Alice opens the gate at node 0 only. Hence, her net income is -7280.
# 
# 
# Constraints:
#         2 <= n <= 10^5
#         edges.length == n - 1
#         edges[i].length == 2
#         0 <= ai, bi < n
#         ai != bi
#         edges represents a valid tree.
#         1 <= bob < n
#         amount.length == n
#         amount[i] is an even integer in the range [-10^4, 10^4].

from collections import defaultdict, deque

# Solution: https://youtu.be/mESeQZKfvtY
# Credit: Navdeep Singh founder of NeetCode
def most_profitable_path(edges, bob, amount):
    adj = defaultdict(list)
    for v1, v2 in edges:
        adj[v1].append(v2)
        adj[v2].append(v1)
    
    # Bob simulation - DFS
    bob_times = {}  # node on root path -> time visited
    def dfs(src, prev, time):
        if src == 0:
            bob_times[src] = time
            return True

        for nei in adj[src]:
            if nei == prev:
                continue
            if dfs(nei, src, time + 1):
                bob_times[src] = time
                return True

        return False
    dfs(bob, -1, 0)

    # Alice Simulation - BFS
    q = deque([(0, 0, -1, amount[0])])  # (node, time, parent, total profit)
    res = float("-inf")
    while q:
        node, time, parent, profit = q.popleft()

        for nei in adj[node]:
            if nei == parent:
                continue

            nei_profit = amount[nei]
            nei_time = time + 1
            if nei in bob_times:
                if nei_time > bob_times[nei]:
                    nei_profit = 0
                if nei_time == bob_times[nei]:
                    nei_profit = nei_profit // 2

            q.append((nei, nei_time, node, profit + nei_profit))
            if len(adj[nei]) == 1:
                res = max(res, profit + nei_profit)
                
    return res

def main():
    edges = [[0,1],[1,2],[1,3],[3,4]]
    result = most_profitable_path(edges, bob = 3, amount = [-2,4,2,-4,6])
    print(result) # 6

    result = most_profitable_path(edges = [[0,1]], bob = 1, amount = [-7280,2350])
    print(result) # -7280

if __name__ == "__main__":
    main()
