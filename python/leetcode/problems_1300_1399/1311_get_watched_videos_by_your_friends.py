# -------------------------------------------
# 1311. Get Watched Videos by Your Friends 📽️
# -------------------------------------------

# Problem: https://leetcode.com/problems/get-watched-videos-by-your-friends
#
# There are n people, each person has a unique id between 0 and n-1. Given the
# arrays watchedVideos and friends, where watchedVideos[i] and friends[i] contain
# the list of watched videos and the list of friends respectively for the person
# with id = i.
# 
# Level 1 of videos are all watched videos by your friends, level 2 of videos are
# all watched videos by the friends of your friends and so on. In general, the
# level k of videos are all watched videos by people with the shortest path
# exactly equal to k with you. Given your id and the level of videos, return the
# list of videos ordered by their frequencies (increasing). For videos with the
# same frequency order them alphabetically from least to greatest. 
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2020/01/02/leetcode_friends_1.png
# 
# Input: watchedVideos = [["A","B"],["C"],["B","C"],["D"]], friends =
# [[1,2],[0,3],[0,3],[1,2]], id = 0, level = 1
# Output: ["B","C"]
# 
# Explanation:
# You have id = 0 (green color in the figure) and your friends are (yellow color
# in the figure):
# Person with id = 1 -> watchedVideos = ["C"] 
# Person with id = 2 -> watchedVideos = ["B","C"] 
# The frequencies of watchedVideos by your friends are: 
# B -> 1 
# C -> 2
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2020/01/02/leetcode_friends_2.png
# 
# Input: watchedVideos = [["A","B"],["C"],["B","C"],["D"]], friends =
# [[1,2],[0,3],[0,3],[1,2]], id = 0, level = 2
# Output: ["D"]
# 
# Explanation:
# You have id = 0 (green color in the figure) and the only friend of your friends
# is the person with id = 3 (yellow color in the figure).
# 
# 
# Constraints:
#         n == watchedVideos.length == friends.length
#         2 <= n <= 100
#         1 <= watchedVideos[i].length <= 100
#         1 <= watchedVideos[i][j].length <= 8
#         0 <= friends[i].length < n
#         0 <= friends[i][j] < n
#         0 <= id < n
#         1 <= level < n
#         if friends[i] contains j, then friends[j] contains i

from collections import deque, Counter

# Solution: https://algo.monster/liteproblems/1311
# Credit: AlgoMonster
def watched_videos_by_friends(
    watchedVideos,
    friends,
    id,
    level,
):
    # Initialize BFS queue with starting person
    queue = deque([id])
    # Track visited people to avoid cycles
    visited = {id}
    
    # Perform BFS to reach the target friendship level
    for _ in range(level):
        # Process all people at current level
        current_level_size = len(queue)
        for _ in range(current_level_size):
            current_person = queue.popleft()
            # Add unvisited friends to the queue for next level
            for friend_id in friends[current_person]:
                if friend_id not in visited:
                    visited.add(friend_id)
                    queue.append(friend_id)
    
    # Count videos watched by all people at the target level
    video_count = Counter()
    for person_id in queue:
        for video in watchedVideos[person_id]:
            video_count[video] += 1
    
    # Sort videos by frequency (ascending), then alphabetically
    return sorted(video_count.keys(), key=lambda video: (video_count[video], video))
    # Time: O(n + m + v * log v)
    # Space: O(n + v)
    # n = the number of people
    # m = the total number of friendship edges
    # v = the total number of videos watched by friends at the target level.


def main():
    result = watched_videos_by_friends(watchedVideos = [["A","B"],["C"],["B","C"],["D"]], 
                                       friends = [[1,2],[0,3],[0,3],[1,2]], 
                                       id = 0, 
                                       level = 1)
    print(result) # ['B', 'C']

    result = watched_videos_by_friends(watchedVideos = [["A","B"],["C"],["B","C"],["D"]], 
                                       friends = [[1,2],[0,3],[0,3],[1,2]], 
                                       id = 0, 
                                       level = 2)
    print(result) # ['D']

if __name__ == "__main__":
    main()
