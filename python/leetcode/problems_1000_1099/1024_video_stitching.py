# ---------------------
# 1024. Video Stitching
# ---------------------

# Problem: https://leetcode.com/problems/video-stitching
#
# You are given a series of video clips from a sporting event that lasted time
# seconds. These video clips can be overlapping with each other and have varying
# lengths.
# 
# Each video clip is described by an array clips where clips[i] = [startᵢ, endᵢ]
# indicates that the ith clip started at startᵢ and ended at endᵢ.
# 
# We can cut these clips into segments freely.
#         
#   * For example, a clip [0, 7] can be cut into segments [0, 1] + [1, 3] +
# [3, 7].
# 
# Return the minimum number of clips needed so that we can cut the clips into
# segments that cover the entire sporting event [0, time]. If the task is
# impossible, return -1.
# 
# Example 1:
# 
# Input: clips = [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], time = 10
# Output: 3
# 
# Explanation: We take the clips [0,2], [8,10], [1,9]; a total of 3 clips.
# Then, we can reconstruct the sporting event as follows:
# We cut [1,9] into segments [1,2] + [2,8] + [8,9].
# Now we have segments [0,2] + [2,8] + [8,10] which cover the sporting event [0,
# 10].
# 
# Example 2:
# 
# Input: clips = [[0,1],[1,2]], time = 5
# Output: -1
# 
# Explanation: We cannot cover [0,5] with only [0,1] and [1,2].
# 
# Example 3:
# 
# Input: clips = [[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5
# ],[2,6],[3,4],[4,5],[5,7],[6,9]], time = 9
# Output: 3
# 
# Explanation: We can take clips [0,4], [4,7], and [6,9].
# 
# 
# Constraints:
#         1 <= clips.length <= 100
#         0 <= startᵢ <= endᵢ <= 100
#         1 <= time <= 100


# Solution: https://algo.monster/liteproblems/1024
# Credit: AlgoMonster
def video_stitching(clips, time):
    # Store the furthest end point reachable from each starting position
    furthest_reach = [0] * time
    
    # Build the furthest reach array from all clips
    for start, end in clips:
        # Only consider clips that start before the target time
        if start < time:
            furthest_reach[start] = max(furthest_reach[start], end)
    
    # Initialize variables for the greedy algorithm
    num_clips = 0  # Number of clips used
    max_reach = 0   # Maximum position we can reach so far
    prev_end = 0    # End position of the last selected clip
    
    # Iterate through each position in the time interval
    for current_pos, furthest_from_here in enumerate(furthest_reach):
        # Update the maximum reachable position
        max_reach = max(max_reach, furthest_from_here)
        
        # If we can't reach beyond current position, there's a gap
        if max_reach <= current_pos:
            return -1
        
        # If we've reached the end of the previous clip's coverage
        if prev_end == current_pos:
            # Select a new clip that extends furthest
            num_clips += 1
            prev_end = max_reach
    
    return num_clips
    # Time: O(n + t)
    # Space: O(t)
    # t = the time value.


def main():
    result = video_stitching(clips = [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], time = 10)
    print(result) # 3

    result = video_stitching(clips = [[0,1],[1,2]], time = 5)
    print(result) # -1

    result = video_stitching(clips = [[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]], time = 9)
    print(result) # 3

if __name__ == "__main__":
    main()
