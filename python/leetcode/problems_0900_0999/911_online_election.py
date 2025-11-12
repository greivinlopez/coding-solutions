# --------------------
# 911. Online Election
# --------------------

# Problem: https://leetcode.com/problems/online-election
#
# You are given two integer arrays persons and times. In an election, the ith vote
# was cast for persons[i] at time times[i].
# 
# For each query at a time t, find the person that was leading the election at
# time t. Votes cast at time t will count towards our query. In the case of a tie,
# the most recent vote (among tied candidates) wins.
# 
# Implement the TopVotedCandidate class:
#         
#   * TopVotedCandidate(int[] persons, int[] times) Initializes the object
#     with the persons and times arrays.
#   * int q(int t) Returns the number of the person that was leading the
#     election at time t according to the mentioned rules.
# 
# Example 1:
# 
# Input
# ["TopVotedCandidate", "q", "q", "q", "q", "q", "q"]
# [[[0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30]], [3], [12], [25], [15],
# [24], [8]]
# Output
# [null, 0, 1, 1, 0, 0, 1]
# 
# Explanation
# TopVotedCandidate topVotedCandidate = new TopVotedCandidate([0, 1, 1, 0, 0, 1,
# 0], [0, 5, 10, 15, 20, 25, 30]);
# topVotedCandidate.q(3); // return 0, At time 3, the votes are [0], and 0 is
# leading.
# topVotedCandidate.q(12); // return 1, At time 12, the votes are [0,1,1], and 1
# is leading.
# topVotedCandidate.q(25); // return 1, At time 25, the votes are [0,1,1,0,0,1],
# and 1 is leading (as ties go to the most recent vote.)
# topVotedCandidate.q(15); // return 0
# topVotedCandidate.q(24); // return 0
# topVotedCandidate.q(8); // return 1
# 
# 
# Constraints:
#         1 <= persons.length <= 5000
#         times.length == persons.length
#         0 <= persons[i] < persons.length
#         0 <= times[i] <= 10⁹
#         times is sorted in a strictly increasing order.
#         times[0] <= t <= 10⁹
#         At most 10⁴ calls will be made to q.


# Credit: Jaweria Batool -> https://github.com/Jaweria-B
class TopVotedCandidate:
    def __init__(self, persons, times):      
        vote_count = {}
        winner = [0] * len(persons)
        mostVotePerson = -1
        
        for i in range(len(persons)):
            if persons[i] in vote_count:
                vote_count[persons[i]] += 1
            else:
                vote_count[persons[i]] = 1
            
            if mostVotePerson == -1 or vote_count[persons[i]] >= vote_count[mostVotePerson]:
                mostVotePerson = persons[i]
        
            winner[i] = mostVotePerson
        
        self.times = times
        self.winner = winner
        
    def q(self, t):        
        left = 0
        right = len(self.winner)-1
        
        while left <= right:
            mid = (right+left)//2
                        
            if self.times[mid] <= t:
                left = mid + 1
                
            else:
                right = mid - 1

        return self.winner[left-1]


def main():
    print("TO DO")

if __name__ == "__main__":
    main()
