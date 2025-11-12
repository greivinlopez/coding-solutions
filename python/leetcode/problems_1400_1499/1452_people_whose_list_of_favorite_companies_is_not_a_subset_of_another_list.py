# -----------------------------------------------------------------------------
# 1452. People Whose List of Favorite Companies Is Not a Subset of Another List
# -----------------------------------------------------------------------------

# Problem: https://leetcode.com/problems/people-whose-list-of-favorite-companies-is-not-a-subset-of-another-list
#
# Given the array favoriteCompanies where favoriteCompanies[i] is the list of
# favorites companies for the ith person (indexed from 0).
# 
# Return the indices of people whose list of favorite companies is not a subset of
# any other list of favorites companies. You must return the indices in increasing
# order.
# 
# Example 1:
# 
# Input: favoriteCompanies = [["leetcode","google","facebook"],["google","microsof
# t"],["google","facebook"],["google"],["amazon"]]
# Output: [0,1,4]
# 
# Explanation:
# Person with index=2 has favoriteCompanies[2]=["google","facebook"] which is a
# subset of favoriteCompanies[0]=["leetcode","google","facebook"] corresponding to
# the person with index 0.
# Person with index=3 has favoriteCompanies[3]=["google"] which is a subset of
# favoriteCompanies[0]=["leetcode","google","facebook"] and
# favoriteCompanies[1]=["google","microsoft"].
# Other lists of favorite companies are not a subset of another list, therefore,
# the answer is [0,1,4].
# 
# Example 2:
# 
# Input: favoriteCompanies =
# [["leetcode","google","facebook"],["leetcode","amazon"],["facebook","google"]]
# Output: [0,1]
# 
# Explanation: In this case favoriteCompanies[2]=["facebook","google"] is a subset
# of favoriteCompanies[0]=["leetcode","google","facebook"], therefore, the answer
# is [0,1].
# 
# Example 3:
# 
# Input: favoriteCompanies = [["leetcode"],["google"],["facebook"],["amazon"]]
# Output: [0,1,2,3]
# 
# 
# Constraints:
#         1 <= favoriteCompanies.length <= 100
#         1 <= favoriteCompanies[i].length <= 500
#         1 <= favoriteCompanies[i][j].length <= 20
#         All strings in favoriteCompanies[i] are distinct.
#         All lists of favorite companies are distinct, that is, If we sort
# alphabetically each list then favoriteCompanies[i] != favoriteCompanies[j].
#         All strings consist of lowercase English letters only.


# Solution: https://algo.monster/liteproblems/1452
# Credit: AlgoMonster
def people_indexes(favoriteCompanies):
    # Map company names to unique integer IDs for efficient set operations
    company_to_id = {}
    next_id = 0
    
    # Number of people
    num_people = len(favoriteCompanies)
    
    # Convert each person's company list to a set of company IDs
    company_id_sets = [set() for _ in range(num_people)]
    
    # Build the mapping and convert company names to IDs
    for person_idx, companies in enumerate(favoriteCompanies):
        for company in companies:
            # Assign a unique ID to each company if not already assigned
            if company not in company_to_id:
                company_to_id[company] = next_id
                next_id += 1
            # Add the company ID to this person's set
            company_id_sets[person_idx].add(company_to_id[company])
    
    # Find people whose favorite companies are not a subset of others
    result = []
    for i in range(num_people):
        # Check if person i's companies are a subset of any other person's companies
        is_subset_of_another = False
        for j in range(num_people):
            # Skip comparing with self
            if i == j:
                continue
            # Check if set i is a subset of set j
            if company_id_sets[i].issubset(company_id_sets[j]):
                is_subset_of_another = True
                break
        
        # If not a subset of any other person's list, add to result
        if not is_subset_of_another:
            result.append(i)
    
    return result
    # Time: O(n * m * k + n² * m)
    # Space: O(n * m)


def main():
    result = people_indexes(favoriteCompanies = [["leetcode","google","facebook"],
                                                 ["google","microsoft"],
                                                 ["google","facebook"],
                                                 ["google"],
                                                 ["amazon"]])
    print(result) # [0, 1, 4]

    result = people_indexes(favoriteCompanies = [["leetcode","google","facebook"],
                                                 ["leetcode","amazon"],
                                                 ["facebook","google"]])
    print(result) # [0, 1]

    result = people_indexes(favoriteCompanies = [["leetcode"],
                                                 ["google"],
                                                 ["facebook"],
                                                 ["amazon"]])
    print(result) # [0, 1, 2, 3]

if __name__ == "__main__":
    main()
