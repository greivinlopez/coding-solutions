# ------------------------------
# 1286. Iterator for Combination
# ------------------------------

# Problem: https://leetcode.com/problems/iterator-for-combination
#
# Design the CombinationIterator class:
#         
#   * CombinationIterator(string characters, int combinationLength)
#     Initializes the object with a string characters of sorted distinct lowercase
#     English letters and a number combinationLength as arguments.
#   * next() Returns the next combination of length combinationLength in
#     lexicographical order.
#   * hasNext() Returns true if and only if there exists a next combination.
# 
# Example 1:
# 
# Input
# ["CombinationIterator", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
# [["abc", 2], [], [], [], [], [], []]
# Output
# [null, "ab", true, "ac", true, "bc", false]
# 
# Explanation
# CombinationIterator itr = new CombinationIterator("abc", 2);
# itr.next();    // return "ab"
# itr.hasNext(); // return True
# itr.next();    // return "ac"
# itr.hasNext(); // return True
# itr.next();    // return "bc"
# itr.hasNext(); // return False
# 
# 
# Constraints:
#         1 <= combinationLength <= characters.length <= 15
#         All the characters of characters are unique.
#         At most 10⁴ calls will be made to next and hasNext.
#         It is guaranteed that all calls of the function next are valid.


# Solution: https://algo.monster/liteproblems/1286
# Credit: AlgoMonster
class CombinationIterator:
    def __init__(self, characters: str, combinationLength: int):
        """
        Initialize the iterator with all combinations of given length.
      
        Args:
            characters: A sorted string of distinct lowercase English letters
            combinationLength: The length of combinations to generate
        """
        def generate_combinations(index: int) -> None:
            """
            Recursively generate all combinations using backtracking.
          
            Args:
                index: Current position in the characters string
            """
            # Base case: combination of desired length is formed
            if len(current_combination) == combinationLength:
                all_combinations.append(''.join(current_combination))
                return
          
            # Base case: reached end of characters string
            if index == string_length:
                return
          
            # Include current character in combination
            current_combination.append(characters[index])
            generate_combinations(index + 1)
          
            # Backtrack: exclude current character from combination
            current_combination.pop()
            generate_combinations(index + 1)
      
        # Initialize variables for combination generation
        all_combinations = []
        string_length = len(characters)
        current_combination = []
      
        # Generate all combinations
        generate_combinations(0)
      
        # Store combinations and initialize iterator index
        self.combinations = all_combinations
        self.current_index = 0

    def next(self) -> str:
        """
        Return the next combination in lexicographical order.
      
        Returns:
            The next combination string
        """
        result = self.combinations[self.current_index]
        self.current_index += 1
        return result

    def hasNext(self) -> bool:
        """
        Check if there are more combinations available.
      
        Returns:
            True if more combinations exist, False otherwise
        """
        return self.current_index < len(self.combinations)


def main():
    print("TO DO")

if __name__ == "__main__":
    main()
