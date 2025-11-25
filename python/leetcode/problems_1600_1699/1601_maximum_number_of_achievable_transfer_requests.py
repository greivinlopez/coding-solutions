# ----------------------------------------------------
# 1601. Maximum Number of Achievable Transfer Requests
# ----------------------------------------------------

# Problem: https://leetcode.com/problems/maximum-number-of-achievable-transfer-requests
#
# We have n buildings numbered from 0 to n - 1. Each building has a number of
# employees. It's transfer season, and some employees want to change the building
# they reside in.
# 
# You are given an array requests where requests[i] = [fromᵢ, toᵢ] represents an
# employee's request to transfer from building fromᵢ to building toᵢ.
# 
# All buildings are full, so a list of requests is achievable only if for each
# building, the net change in employee transfers is zero. This means the number of
# employees leaving is equal to the number of employees moving in. For example if
# n = 3 and two employees are leaving building 0, one is leaving building 1, and
# one is leaving building 2, there should be two employees moving to building 0,
# one employee moving to building 1, and one employee moving to building 2.
# 
# Return the maximum number of achievable requests.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2020/09/10/move1.jpg
# 
# Input: n = 5, requests = [[0,1],[1,0],[0,1],[1,2],[2,0],[3,4]]
# Output: 5
# 
# Explantion: Let's see the requests:
# From building 0 we have employees x and y and both want to move to building 1.
# From building 1 we have employees a and b and they want to move to buildings 2
# and 0 respectively.
# From building 2 we have employee z and they want to move to building 0.
# From building 3 we have employee c and they want to move to building 4.
# From building 4 we don't have any requests.
# We can achieve the requests of users x and b by swapping their places.
# We can achieve the requests of users y, a and z by swapping the places in the 3
# buildings.
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2020/09/10/move2.jpg
# 
# Input: n = 3, requests = [[0,0],[1,2],[2,1]]
# Output: 3
# 
# Explantion: Let's see the requests:
# From building 0 we have employee x and they want to stay in the same building 0.
# From building 1 we have employee y and they want to move to building 2.
# From building 2 we have employee z and they want to move to building 1.
# We can achieve all the requests.
# 
# Example 3:
# 
# Input: n = 4, requests = [[0,3],[3,1],[1,2],[2,0]]
# Output: 4
# 
# 
# Constraints:
#         1 <= n <= 20
#         1 <= requests.length <= 16
#         requests[i].length == 2
#         0 <= fromᵢ, toᵢ < n


# Solution: https://algo.monster/liteproblems/1601
# Credit: AlgoMonster
def maximum_requests(n, requests):

    def is_valid_combination(bitmask: int) -> bool:
        # Track net change in employee count for each building
        building_balance = [0] * n
        
        # Process each request based on the bitmask
        for request_idx, (from_building, to_building) in enumerate(requests):
            # Check if current request is selected (bit is set)
            if bitmask >> request_idx & 1:
                building_balance[from_building] -= 1  # Employee leaves
                building_balance[to_building] += 1     # Employee arrives
        
        # Check if all buildings have balanced employee count (net zero change)
        return all(balance == 0 for balance in building_balance)
    
    max_achievable_requests = 0
    
    # Try all possible combinations of requests using bitmask
    # Total combinations = 2^(number of requests)
    for bitmask in range(1 << len(requests)):
        # Count number of selected requests in current combination
        selected_count = bitmask.bit_count()
        # For Python less than 3.10 use:
        # selected_count = bin(bitmask).count('1')
        
        # Only check validity if this combination has more requests than current best
        if max_achievable_requests < selected_count and is_valid_combination(bitmask):
            max_achievable_requests = selected_count
    
    return max_achievable_requests
    # Time: O(2ᵐ * (m + n))
    # Space: O(n)


def main():
    result = maximum_requests(n = 5, requests = [[0,1],[1,0],[0,1],[1,2],[2,0],[3,4]])
    print(result) # 5

    result = maximum_requests(n = 3, requests = [[0,0],[1,2],[2,1]])
    print(result) # 3

    result = maximum_requests(n = 4, requests = [[0,3],[3,1],[1,2],[2,0]])
    print(result) # 4

if __name__ == "__main__":
    main()
