# -------------------------------------------------------
# 1606. Find Servers That Handled Most Number of Requests
# -------------------------------------------------------

# Problem: https://leetcode.com/problems/find-servers-that-handled-most-number-of-requests
#
# You have k servers numbered from 0 to k-1 that are being used to handle multiple
# requests simultaneously. Each server has infinite computational capacity but
# cannot handle more than one request at a time. The requests are assigned to
# servers according to a specific algorithm:
#         
#   * The iᵗʰ (0-indexed) request arrives.
#   * If all servers are busy, the request is dropped (not handled at all).
#   * If the (i % k)ᵗʰ server is available, assign the request to that server.
#   * Otherwise, assign the request to the next available server (wrapping
#     around the list of servers and starting from 0 if necessary). For example, if
#     the iᵗʰ server is busy, try to assign the request to the (i+1)ᵗʰ server, then
#     the (i+2)ᵗʰ server, and so on.
# 
# You are given a strictly increasing array arrival of positive integers, where
# arrival[i] represents the arrival time of the iᵗʰ request, and another array
# load, where load[i] represents the load of the iᵗʰ request (the time it takes to
# complete). Your goal is to find the busiest server(s). A server is considered
# busiest if it handled the most number of requests successfully among all the
# servers.
# 
# Return a list containing the IDs (0-indexed) of the busiest server(s). You may
# return the IDs in any order.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2020/09/08/load-1.png
# 
# Input: k = 3, arrival = [1,2,3,4,5], load = [5,2,3,3,3]
# Output: [1]
# 
# Explanation:
# All of the servers start out available.
# The first 3 requests are handled by the first 3 servers in order.
# Request 3 comes in. Server 0 is busy, so it's assigned to the next available
# server, which is 1.
# Request 4 comes in. It cannot be handled since all servers are busy, so it is
# dropped.
# Servers 0 and 2 handled one request each, while server 1 handled two requests.
# Hence server 1 is the busiest server.
# 
# Example 2:
# 
# Input: k = 3, arrival = [1,2,3,4], load = [1,2,1,2]
# Output: [0]
# 
# Explanation:
# The first 3 requests are handled by first 3 servers.
# Request 3 comes in. It is handled by server 0 since the server is available.
# Server 0 handled two requests, while servers 1 and 2 handled one request each.
# Hence server 0 is the busiest server.
# 
# Example 3:
# 
# Input: k = 3, arrival = [1,2,3], load = [10,12,11]
# Output: [0,1,2]
# 
# Explanation: Each server handles a single request, so they are all considered
# the busiest.
# 
# 
# Constraints:
#         1 <= k <= 10⁵
#         1 <= arrival.length, load.length <= 10⁵
#         arrival.length == load.length
#         1 <= arrival[i], load[i] <= 10⁹
#         arrival is strictly increasing.

# ------------------
# pip install sortedcontainers
# ------------------
from sortedcontainers import SortedList
from heapq import heappop, heappush

# Solution: https://algo.monster/liteproblems/1606
# Credit: AlgoMonster
def busiest_servers(k, arrival, load):
    # Initialize a sorted list of available servers (0 to k-1)
    available_servers = SortedList(range(k))
    
    # Min heap to track busy servers: (end_time, server_id)
    busy_servers = []
    
    # Counter array to track number of requests handled by each server
    request_count = [0] * k
    
    # Process each request
    for request_id, (arrival_time, processing_time) in enumerate(zip(arrival, load)):
        # Free up servers that have completed their tasks by current arrival time
        while busy_servers and busy_servers[0][0] <= arrival_time:
            end_time, server_id = heappop(busy_servers)
            available_servers.add(server_id)
        
        # Skip this request if no servers are available
        if not available_servers:
            continue
        
        # Find the next available server using round-robin strategy
        # Start looking from server (request_id % k)
        target_server = request_id % k
        server_index = available_servers.bisect_left(target_server)
        
        # If no server >= target_server exists, wrap around to the first server
        if server_index == len(available_servers):
            server_index = 0
        
        # Assign the request to the selected server
        selected_server = available_servers[server_index]
        request_count[selected_server] += 1
        
        # Mark server as busy until arrival_time + processing_time
        heappush(busy_servers, (arrival_time + processing_time, selected_server))
        available_servers.remove(selected_server)
    
    # Find servers with maximum request count
    max_requests = max(request_count)
    return [server_id for server_id, count in enumerate(request_count) if count == max_requests]
    # Time: O(n * (log k + k))
    # Space: O(k)


def main():
    result = busiest_servers(k = 3, arrival = [1,2,3,4,5], load = [5,2,3,3,3] )
    print(result) # [1] 

    result = busiest_servers(k = 3, arrival = [1,2,3,4], load = [1,2,1,2])
    print(result) # [0]

    result = busiest_servers(k = 3, arrival = [1,2,3], load = [10,12,11])
    print(result) # [0,1,2]

if __name__ == "__main__":
    main()
