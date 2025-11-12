# -----------------------------
# 332. Reconstruct Itinerary ✈️
# -----------------------------

# Problem: https://leetcode.com/problems/reconstruct-itinerary/
# 
# You are given a list of airline tickets where tickets[i] = [fromi, toi] 
# represent the departure and the arrival airports of one flight. Reconstruct 
# the itinerary in order and return it.
# 
# All of the tickets belong to a man who departs from "JFK", thus, the 
# itinerary must begin with "JFK". If there are multiple valid itineraries, you 
# should return the itinerary that has the smallest lexical order when read as 
# a single string.
# 
# 
# 	For example, the itinerary ["JFK", "LGA"] has a smaller lexical order 
#   than ["JFK", "LGB"].
# 
# 
# You may assume all tickets form at least one valid itinerary. You must use all 
# the tickets once and only once.
# 
#  
# Example 1:
# 
# Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
# Output: ["JFK","MUC","LHR","SFO","SJC"]
# 
# 
# Example 2:
# 
# Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
# Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"] but it is larger in lexical order.
# 
# 
# Constraints:
# 
# 	1 <= tickets.length <= 300
# 	tickets[i].length == 2
# 	fromi.length == 3
# 	toi.length == 3
# 	fromi and toi consist of uppercase English letters.
# 	fromi != toi


# Solution: https://youtu.be/ZyB_gQ8vqGA
# Credit: Navdeep Singh founder of NeetCode
def find_itinerary(tickets):
    adj = {src: [] for src, dst in tickets}
    res = []

    for src, dst in tickets:
        adj[src].append(dst)

    for key in adj:
        adj[key].sort()

    def dfs(adj, src):
        if src in adj:
            destinations = adj[src][:]
            while destinations:
                dest = destinations[0]
                adj[src].pop(0)
                dfs(adj, dest)
                destinations = adj[src][:]
        res.append(src)

    dfs(adj, "JFK")
    res.reverse()

    if len(res) != len(tickets) + 1:
        return []

    return res

# Solution: 
# Credit: Greg Hogg


def main():
    tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
    result = find_itinerary(tickets)
    print(result) # ["JFK","MUC","LHR","SFO","SJC"]

    tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    result = find_itinerary(tickets)
    print(result) # ["JFK","ATL","JFK","SFO","ATL","SFO"]


if __name__ == "__main__":
    main()
