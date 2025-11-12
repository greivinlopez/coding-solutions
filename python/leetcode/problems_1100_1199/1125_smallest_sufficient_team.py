# ------------------------------
# 1125. Smallest Sufficient Team
# ------------------------------

# Problem: https://leetcode.com/problems/smallest-sufficient-team
#
# In a project, you have a list of required skills req_skills, and a list of
# people. The ith person people[i] contains a list of skills that the person has.
# 
# Consider a sufficient team: a set of people such that for every required skill
# in req_skills, there is at least one person in the team who has that skill. We
# can represent these teams by the index of each person.
#         
#   * For example, team = [0, 1, 3] represents the people with skills
#     people[0], people[1], and people[3].
# 
# Return any sufficient team of the smallest possible size, represented by the
# index of each person. You may return the answer in any order.
# 
# It is guaranteed an answer exists.
# 
# Example 1:
# 
# Input: req_skills = ["java","nodejs","reactjs"], people =
# [["java"],["nodejs"],["nodejs","reactjs"]]
# Output: [0,2]
# 
# Example 2:
# 
# Input: req_skills = ["algorithms","math","java","reactjs","csharp","aws"],
# people = [["algorithms","math","java"],["algorithms","math","reactjs"],["java","
# csharp","aws"],["reactjs","csharp"],["csharp","math"],["aws","java"]]
# Output: [1,2]
# 
# 
# Constraints:
#         1 <= req_skills.length <= 16
#         1 <= req_skills[i].length <= 16
#         req_skills[i] consists of lowercase English letters.
#         All the strings of req_skills are unique.
#         1 <= people.length <= 60
#         0 <= people[i].length <= 16
#         1 <= people[i][j].length <= 16
#         people[i][j] consists of lowercase English letters.
#         All the strings of people[i] are unique.
#         Every skill in people[i] is a skill in req_skills.
#         It is guaranteed a sufficient team exists.


# Solution: https://algo.monster/liteproblems/1125
# Credit: AlgoMonster
def smallest_sufficient_team(req_skills, people):
    # Create a mapping from skill name to its bit position
    skill_to_bit = {skill: bit_pos for bit_pos, skill in enumerate(req_skills)}
    
    num_skills = len(req_skills)
    num_people = len(people)
    
    # Convert each person's skills to a bitmask representation
    # person_skillmasks[i] represents all skills of person i as a bitmask
    person_skillmasks = [0] * num_people
    for person_idx, person_skills in enumerate(people):
        for skill in person_skills:
            person_skillmasks[person_idx] |= 1 << skill_to_bit[skill]
    
    # DP arrays for tracking the smallest team
    # min_team_size[mask] = minimum number of people needed to cover skills represented by mask
    min_team_size = [float('inf')] * (1 << num_skills)
    
    # last_person[mask] = the last person added to achieve this skill mask
    last_person = [0] * (1 << num_skills)
    
    # prev_mask[mask] = the previous skill mask before adding last_person[mask]
    prev_mask = [0] * (1 << num_skills)
    
    # Base case: 0 people needed to cover 0 skills
    min_team_size[0] = 0
    
    # Try all possible skill combinations
    for current_mask in range(1 << num_skills):
        # Skip if this mask is not reachable
        if min_team_size[current_mask] == float('inf'):
            continue
        
        # Try adding each person to the current team
        for person_idx in range(num_people):
            # Calculate new skill mask after adding this person
            new_mask = current_mask | person_skillmasks[person_idx]
            
            # If adding this person results in a smaller team for new_mask
            if min_team_size[current_mask] + 1 < min_team_size[new_mask]:
                min_team_size[new_mask] = min_team_size[current_mask] + 1
                last_person[new_mask] = person_idx
                prev_mask[new_mask] = current_mask
    
    # Reconstruct the team by backtracking from the full skill mask
    result_team = []
    current_mask = (1 << num_skills) - 1  # All skills covered
    
    while current_mask:
        result_team.append(last_person[current_mask])
        current_mask = prev_mask[current_mask]
    
    return result_team
    # Time: O(2ᵐ * n)
    # Space: O(2ᵐ)


def main():
    result = smallest_sufficient_team(req_skills = ["java","nodejs","reactjs"], people = [["java"],["nodejs"],["nodejs","reactjs"]])
    print(result) # [2, 0]

    result = smallest_sufficient_team(req_skills = ["algorithms","math","java","reactjs","csharp","aws"], people = [["algorithms","math","java"],["algorithms","math","reactjs"],["java","csharp","aws"],["reactjs","csharp"],["csharp","math"],["aws","java"]])
    print(result) # [2, 1]

if __name__ == "__main__":
    main()
