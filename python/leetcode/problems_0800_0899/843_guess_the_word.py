# -------------------
# 843. Guess the Word
# -------------------

# Problem: https://leetcode.com/problems/guess-the-word
#
# You are given an array of unique strings words where words[i] is six letters
# long. One word of words was chosen as a secret word.
# 
# You are also given the helper object Master. You may call Master.guess(word)
# where word is a six-letter-long string, and it must be from words.
# Master.guess(word) returns:
# 
#   * -1 if word is not from words, or
#   * an integer representing the number of exact matches (value and position)
#     of your guess to the secret word.
# 
# There is a parameter allowedGuesses for each test case where allowedGuesses is
# the maximum number of times you can call Master.guess(word).
# 
# For each test case, you should call Master.guess with the secret word without
# exceeding the maximum number of allowed guesses. You will get:
#         
#   * "Either you took too many guesses, or you did not find the secret word."
#     if you called Master.guess more than allowedGuesses times or if you did not call
#     Master.guess with the secret word, or
#   * "You guessed the secret word correctly." if you called Master.guess with
#     the secret word with the number of calls to Master.guess less than or equal to
#     allowedGuesses.
# 
# The test cases are generated such that you can guess the secret word with a
# reasonable strategy (other than using the bruteforce method).
# 
# Example 1:
# 
# Input: secret = "acckzz", words = ["acckzz","ccbazz","eiowzz","abcczz"],
# allowedGuesses = 10
# Output: You guessed the secret word correctly.
# 
# Explanation:
# master.guess("aaaaaa") returns -1, because "aaaaaa" is not in wordlist.
# master.guess("acckzz") returns 6, because "acckzz" is secret and has all 6
# matches.
# master.guess("ccbazz") returns 3, because "ccbazz" has 3 matches.
# master.guess("eiowzz") returns 2, because "eiowzz" has 2 matches.
# master.guess("abcczz") returns 4, because "abcczz" has 4 matches.
# We made 5 calls to master.guess, and one of them was the secret, so we pass the
# test case.
# 
# Example 2:
# 
# Input: secret = "hamada", words = ["hamada","khaled"], allowedGuesses = 10
# Output: You guessed the secret word correctly.
# 
# Explanation: Since there are two words, you can guess both.
# 
# 
# Constraints:
#         1 <= words.length <= 100
#         words[i].length == 6
#         words[i] consist of lowercase English letters.
#         All the strings of wordlist are unique.
#         secret exists in words.
#         10 <= allowedGuesses <= 30


# Solution: https://leetcode.com/problems/guess-the-word/solutions/6180077/easy-o-n-2-python-solution-strategic-guessing-and-narrowing-down-solution-set
# Credit: Varun Mohan -> https://leetcode.com/u/varunmohan05/
def find_secret_word(words, master):
    # Helper function to calculate the number of matching letters at the same positions
    def letter_matches(word1, word2):
        matches = 0
        for i in range(len(word1)):
            if word1[i] == word2[i]:
                matches += 1
        return matches

    # Precompute match scores between all pairs of words
    scoreMap = {word: {} for word in words}  
    for word1 in words:
        for word2 in words:
            score = letter_matches(word1, word2)
            scoreMap[word1][word2] = score

    candidates = words[:]
    while candidates:
        # Step 1: Evaluate each word as a potential guess
        bucketSizes = {}
        for guess in candidates:
            # Calculate the size of the largest bucket for this guess
            matchBuckets = {}
            for word in candidates:
                score = scoreMap[guess][word]
                if score not in matchBuckets:
                    matchBuckets[score] = 0
                matchBuckets[score] += 1
            bucketSizes[guess] = max(matchBuckets.values())

        # Step 2: Choose the word with the smallest largest bucket size
        guessWord = min(bucketSizes, key=bucketSizes.get)

        # Step 3: Make the guess
        score = master.guess(guessWord)
        if score == 6:  # Secret word found
            return

        # Step 4: Filter candidates based on the match score with the guessed word
        candidates = [
            word for word in candidates if scoreMap[guessWord][word] == score
        ]
    # Time: O(n²)
    # Space: O(n²)


def main():
    print("TO DO")

if __name__ == "__main__":
    main()
