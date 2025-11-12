# --------------------------------
# 825. Friends Of Appropriate Ages
# --------------------------------

# Problem: https://leetcode.com/problems/friends-of-appropriate-ages
#
# There are n persons on a social media website. You are given an integer array
# ages where ages[i] is the age of the iᵗʰ person.
# 
# A Person x will not send a friend request to a person y (x != y) if any of the
# following conditions is true:
# 
#         age[y] <= 0.5 * age[x] + 7
#         age[y] > age[x]
#         age[y] > 100 && age[x] < 100
# 
# Otherwise, x will send a friend request to y.
# 
# Note that if x sends a request to y, y will not necessarily send a request to x.
# Also, a person will not send a friend request to themself.
# 
# Return the total number of friend requests made.
# 
# Example 1:
# 
# Input: ages = [16,16]
# Output: 2
# 
# Explanation: 2 people friend request each other.
# 
# Example 2:
# 
# Input: ages = [16,17,18]
# Output: 2
# 
# Explanation: Friend requests are made 17 -> 16, 18 -> 17.
# 
# Example 3:
# 
# Input: ages = [20,30,100,110,120]
# Output: 3
# 
# Explanation: Friend requests are made 110 -> 100, 120 -> 110, 120 -> 100.
# 
# 
# Constraints:
#         n == ages.length
#         1 <= n <= 2 * 10⁴
#         1 <= ages[i] <= 120


# Solution: https://algo.monster/liteproblems/825
# Credit: AlgoMonster
def num_friend_requests(ages):
    # Count frequency of each age (ages range from 1 to 120)
    age_count = [0] * 121
    for age in ages:
        age_count[age] += 1
    
    total_requests = 0
    
    # Check all possible age pairs
    for age_x in range(121):
        if age_count[age_x] == 0:
            continue
            
        for age_y in range(121):
            if age_count[age_y] == 0:
                continue
            
            # Friend request conditions (person x will NOT send request to y if):
            # 1. age_y <= 0.5 * age_x + 7
            # 2. age_y > age_x
            # 3. age_y > 100 and age_x < 100
            if age_y <= 0.5 * age_x + 7:
                continue
            if age_y > age_x:
                continue
            if age_y > 100 and age_x < 100:
                continue
            
            # Valid friend request scenario
            if age_x == age_y:
                # Same age: each person can send to others of same age (excluding themselves)
                total_requests += age_count[age_x] * (age_count[age_y] - 1)
            else:
                # Different ages: all people of age_x can send to all people of age_y
                total_requests += age_count[age_x] * age_count[age_y]
    
    return total_requests
    # Time: O(n + m²)
    # Space: O(m)
    # n = the length of the array ages
    # m = the maximum possible age value (121 in this problem).


def main():
    result = num_friend_requests(ages = [16,16])
    print(result) # 2

    result = num_friend_requests(ages = [16,17,18])
    print(result) # 2

    result = num_friend_requests(ages = [20,30,100,110,120])
    print(result) # 3

if __name__ == "__main__":
    main()
