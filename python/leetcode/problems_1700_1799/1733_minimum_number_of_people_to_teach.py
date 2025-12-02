# ---------------------------------------
# 1733. Minimum Number of People to Teach
# ---------------------------------------

# Problem: https://leetcode.com/problems/minimum-number-of-people-to-teach
#
# On a social network consisting of m users and some friendships between users,
# two users can communicate with each other if they know a common language.
# 
# You are given an integer n, an array languages, and an array friendships where:
#         
#   * There are n languages numbered 1 through n,
#   * languages[i] is the set of languages the i​​​​​ᵗʰ​​​​ user knows, and
#   * friendships[i] = [u​​​​​ᵢ​​​, v​​​​​ᵢ] denotes a friendship between the users 
#     u​​​​​​​​​​ᵢ​​​​​ and vᵢ.
# 
# You can choose one language and teach it to some users so that all friends can
# communicate with each other. Return the minimum number of users you need to
# teach.
# 
# Note that friendships are not transitive, meaning if x is a friend of y and y is
# a friend of z, this doesn't guarantee that x is a friend of z.
# 
# Example 1:
# 
# Input: n = 2, languages = [[1],[2],[1,2]], friendships = [[1,2],[1,3],[2,3]]
# Output: 1
# 
# Explanation: You can either teach user 1 the second language or user 2 the first
# language.
# 
# Example 2:
# 
# Input: n = 3, languages = [[2],[1,3],[1,2],[3]], friendships =
# [[1,4],[1,2],[3,4],[2,3]]
# Output: 2
# 
# Explanation: Teach the third language to users 1 and 3, yielding two users to
# teach.
# 
# 
# Constraints:
#         2 <= n <= 500
#         languages.length == m
#         1 <= m <= 500
#         1 <= languages[i].length <= n
#         1 <= languages[i][j] <= n
#         1 <= u​​​​​​ᵢ < v​​​​​​ᵢ <= languages.length
#         1 <= friendships.length <= 500
#         All tuples (u​​​​ᵢ, v​​​​​ᵢ) are unique
#         languages[i] contains only unique values


# Solution: https://algo.monster/liteproblems/1733
# Credit: AlgoMonster
def minimum_teachings(n, languages, friendships):
    from collections import Counter

    def can_communicate(user1, user2):
        # Get languages for both users (convert to 0-indexed)
        user1_languages = languages[user1 - 1]
        user2_languages = languages[user2 - 1]
        
        # Check if any language is common between the two users
        for lang1 in user1_languages:
            for lang2 in user2_languages:
                if lang1 == lang2:
                    return True
        return False
    
    # Find all users who are in friendships that cannot communicate
    users_needing_language = set()
    for user1, user2 in friendships:
        if not can_communicate(user1, user2):
            # Both users in this friendship need to learn a common language
            users_needing_language.add(user1)
            users_needing_language.add(user2)
    
    # Count how many problematic users already know each language
    language_count = Counter()
    for user in users_needing_language:
        # For each user who needs to communicate, count their known languages
        for language_id in languages[user - 1]:
            language_count[language_id] += 1
    
    # The minimum teachings needed is:
    # Total problematic users - Maximum users who already know the same language
    # If we teach the most commonly known language to those who don't know it,
    # we minimize the number of teachings
    if language_count:
        return len(users_needing_language) - max(language_count.values())
    else:
        # If no problematic users exist, no teaching is needed
        return 0
    # Time: O(k × m² + k × m)
    # Space: O(k + n)


def main():
    result = minimum_teachings(n = 2, languages = [[1],[2],[1,2]], friendships = [[1,2],[1,3],[2,3]])
    print(result) # 1

    result = minimum_teachings(n = 3, languages = [[2],[1,3],[1,2],[3]], friendships = [[1,4],[1,2],[3,4],[2,3]])
    print(result) # 2

if __name__ == "__main__":
    main()
