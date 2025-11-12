# -------------------------
# 299. Bulls and Cows 🐂 🐄
# -------------------------

# Problem: https://leetcode.com/problems/bulls-and-cows
#
# You are playing the Bulls and Cows game with your friend.
# 
# You write down a secret number and ask your friend to guess what the number is.
# 
# When your friend makes a guess, you provide a hint with the following info:    
#   * The number of "bulls", which are digits in the guess that are in the
#     correct position.
#   * The number of "cows", which are digits in the guess that are in your
#     secret number but are located in the wrong position. Specifically, the non-bull
#     digits in the guess that could be rearranged such that they become bulls.
# 
# Given the secret number secret and your friend's guess guess, return the hint
# for your friend's guess.
# 
# The hint should be formatted as "xAyB", where x is the number of bulls and y is
# the number of cows. Note that both secret and guess may contain duplicate
# digits.
# 
# Example 1:
# 
# Input: secret = "1807", guess = "7810"
# Output: "1A3B"
# 
# Explanation: Bulls are connected with a '|' and cows are underlined:
# "1807"
#   |
# "7810"
# 
# Example 2:
# 
# Input: secret = "1123", guess = "0111"
# Output: "1A1B"
# 
# Explanation: Bulls are connected with a '|' and cows are underlined:
# "1123"        "1123"
#   |      or     |
# "0111"        "0111"
# Note that only one of the two unmatched 1s is counted as a cow since the non-
# bull digits can only be rearranged to allow one 1 to be a bull.
# 
# 
# Constraints:
#         1 <= secret.length, guess.length <= 1000
#         secret.length == guess.length
#         secret and guess consist of digits only.

from collections import Counter

# Solution: https://leetcodethehardway.com/solutions/0200-0299/bulls-and-cows-medium#approach-1-hashmap
# Credit: LeetCode The Hard Way -> https://leetcodethehardway.com/
def get_hint(secret, guess):
    secret_freq = Counter(secret)
    bulls = cows = 0
    n = len(secret)

    for i in range(n):
        if secret[i] == guess[i]:
            bulls += 1
            secret_freq[secret[i]] -= 1

    for i in range(n):
        if guess[i] in secret_freq and secret_freq[guess[i]] > 0 and guess[i] != secret[i]:
            cows += 1
            secret_freq[guess[i]] -= 1

    return f'{bulls}A{cows}B'
    # Time: O(n)
    # Space: O(1)


def main():
    result = get_hint(secret = "1807", guess = "7810")
    print(result) # "1A3B"

    result = get_hint(secret = "1123", guess = "0111")
    print(result) # "1A1B"

if __name__ == "__main__":
    main()
