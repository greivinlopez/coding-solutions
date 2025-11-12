# --------------------------------
# 1348. Tweet Counts Per Frequency
# --------------------------------

# Problem: https://leetcode.com/problems/tweet-counts-per-frequency
#
# A social media company is trying to monitor activity on their site by analyzing
# the number of tweets that occur in select periods of time. These periods can be
# partitioned into smaller time chunks based on a certain frequency (every minute,
# hour, or day).
# 
# For example, the period [10, 10000] (in seconds) would be partitioned into the
# following time chunks with these frequencies:
#         
#   * Every minute (60-second chunks): [10,69], [70,129], [130,189], ...,
#     [9970,10000]
#   * Every hour (3600-second chunks): [10,3609], [3610,7209], [7210,10000]
#   * Every day (86400-second chunks): [10,10000]
# 
# Notice that the last chunk may be shorter than the specified frequency's chunk
# size and will always end with the end time of the period (10000 in the above
# example).
# 
# Design and implement an API to help the company with their analysis.
# 
# Implement the TweetCounts class:
#         
#   * TweetCounts() Initializes the TweetCounts object.
#   * void recordTweet(String tweetName, int time) Stores the tweetName at the
#     recorded time (in seconds).
#   * List<Integer> getTweetCountsPerFrequency(String freq, String tweetName,
#     int startTime, int endTime) Returns a list of integers representing the number
#     of tweets with tweetName in each time chunk for the given period of time
#     [startTime, endTime] (in seconds) and frequency freq.
#       * freq is one of "minute", "hour", or "day" representing a frequency of
#         every minute, hour, or day respectively.
# 
# Example:
# 
# Input
# ["TweetCounts","recordTweet","recordTweet","recordTweet","getTweetCountsPerFrequ
# ency","getTweetCountsPerFrequency","recordTweet","getTweetCountsPerFrequency"]
# [[],["tweet3",0],["tweet3",60],["tweet3",10],["minute","tweet3",0,59],["minute",
# "tweet3",0,60],["tweet3",120],["hour","tweet3",0,210]]
# Output
# [null,null,null,null,[2],[2,1],null,[4]]
# 
# Explanation
# TweetCounts tweetCounts = new TweetCounts();
# tweetCounts.recordTweet("tweet3", 0);                              // New tweet
# "tweet3" at time 0
# tweetCounts.recordTweet("tweet3", 60);                             // New tweet
# "tweet3" at time 60
# tweetCounts.recordTweet("tweet3", 10);                             // New tweet
# "tweet3" at time 10
# tweetCounts.getTweetCountsPerFrequency("minute", "tweet3", 0, 59); // return
# [2]; chunk [0,59] had 2 tweets
# tweetCounts.getTweetCountsPerFrequency("minute", "tweet3", 0, 60); // return
# [2,1]; chunk [0,59] had 2 tweets, chunk [60,60] had 1 tweet
# tweetCounts.recordTweet("tweet3", 120);                            // New tweet
# "tweet3" at time 120
# tweetCounts.getTweetCountsPerFrequency("hour", "tweet3", 0, 210);  // return
# [4]; chunk [0,210] had 4 tweets
# 
# 
# Constraints:
#   0 <= time, startTime, endTime <= 10⁹
#   0 <= endTime - startTime <= 10⁴
#   There will be at most 10⁴ calls in total to recordTweet and getTweetCountsPerFrequency.


from collections import defaultdict
from sortedcontainers import SortedList
from typing import List

# Solution: 
# Credit: Navdeep Singh founder of NeetCode
class TweetCounts:
    def __init__(self):
        # Dictionary mapping frequency types to their duration in seconds
        self.frequency_duration = {
            "minute": 60,
            "hour": 3600,
            "day": 86400
        }
        # Store tweets for each user as a sorted list of timestamps
        self.tweet_data = defaultdict(SortedList)

    def recordTweet(self, tweetName: str, time: int) -> None:
        """
        Records a tweet with the given name at the specified time.
      
        Args:
            tweetName: The name/ID of the tweet
            time: The timestamp when the tweet was posted
        """
        self.tweet_data[tweetName].add(time)

    def getTweetCountsPerFrequency(
        self, freq: str, tweetName: str, startTime: int, endTime: int
    ) -> List[int]:
        """
        Returns the count of tweets per time interval based on the given frequency.
      
        Args:
            freq: The frequency type ("minute", "hour", or "day")
            tweetName: The name/ID of the tweet to count
            startTime: The start timestamp of the range (inclusive)
            endTime: The end timestamp of the range (inclusive)
          
        Returns:
            List of tweet counts for each time interval
        """
        # Get the duration for the specified frequency
        interval_duration = self.frequency_duration[freq]
      
        # Get all tweets for the specified tweet name
        tweet_timestamps = self.tweet_data[tweetName]
      
        # Initialize variables for iteration
        current_time = startTime
        result = []
      
        # Iterate through each time interval
        while current_time <= endTime:
            # Find the start index for tweets in this interval
            left_index = tweet_timestamps.bisect_left(current_time)
          
            # Find the end index for tweets in this interval
            # The interval ends at either (current_time + duration) or (endTime + 1), whichever is smaller
            interval_end = min(current_time + interval_duration, endTime + 1)
            right_index = tweet_timestamps.bisect_left(interval_end)
          
            # Count tweets in this interval (difference between indices)
            tweet_count = right_index - left_index
            result.append(tweet_count)
          
            # Move to the next interval
            current_time += interval_duration
          
        return result

def main():
    print("TO DO")

if __name__ == "__main__":
    main()
