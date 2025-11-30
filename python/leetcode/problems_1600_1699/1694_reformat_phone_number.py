# ------------------------------
# 1694. Reformat Phone Number ☎️
# ------------------------------

# Problem: https://leetcode.com/problems/reformat-phone-number
#
# You are given a phone number as a string number. number consists of digits,
# spaces ' ', and/or dashes '-'.
# 
# You would like to reformat the phone number in a certain manner. Firstly, remove
# all spaces and dashes. Then, group the digits from left to right into blocks of
# length 3 until there are 4 or fewer digits. The final digits are then grouped as
# follows:
# 
#         2 digits: A single block of length 2.
#         3 digits: A single block of length 3.
#         4 digits: Two blocks of length 2 each.
# 
# The blocks are then joined by dashes. Notice that the reformatting process
# should never produce any blocks of length 1 and produce at most two blocks of
# length 2.
# 
# Return the phone number after formatting.
# 
# Example 1:
# 
# Input: number = "1-23-45 6"
# Output: "123-456"
# 
# Explanation: The digits are "123456".
# Step 1: There are more than 4 digits, so group the next 3 digits. The 1st block
# is "123".
# Step 2: There are 3 digits remaining, so put them in a single block of length 3.
# The 2nd block is "456".
# Joining the blocks gives "123-456".
# 
# Example 2:
# 
# Input: number = "123 4-567"
# Output: "123-45-67"
# 
# Explanation: The digits are "1234567".
# Step 1: There are more than 4 digits, so group the next 3 digits. The 1st block
# is "123".
# Step 2: There are 4 digits left, so split them into two blocks of length 2. The
# blocks are "45" and "67".
# Joining the blocks gives "123-45-67".
# 
# Example 3:
# 
# Input: number = "123 4-5678"
# Output: "123-456-78"
# 
# Explanation: The digits are "12345678".
# Step 1: The 1st block is "123".
# Step 2: The 2nd block is "456".
# Step 3: There are 2 digits left, so put them in a single block of length 2. The
# 3rd block is "78".
# Joining the blocks gives "123-456-78".
# 
# 
# Constraints:
#         2 <= number.length <= 100
#         number consists of digits and the characters '-' and ' '.
#         There are at least two digits in number.


# Solution: https://algo.monster/liteproblems/1694
# Credit: AlgoMonster
def reformat_number(number):
    # Remove all dashes and spaces from the input string
    cleaned_number = number.replace("-", "").replace(" ", "")
    
    # Get the total length of cleaned digits
    total_length = len(cleaned_number)
    
    # Create groups of 3 digits for as many complete groups as possible
    groups = []
    for i in range(total_length // 3):
        start_index = i * 3
        end_index = start_index + 3
        groups.append(cleaned_number[start_index:end_index])
    
    # Handle remaining digits based on the remainder when divided by 3
    remainder = total_length % 3
    
    if remainder == 1:
        # If 1 digit remains, combine it with the last group to make two groups of 2
        # Remove the last character from the last group (making it 2 digits)
        groups[-1] = groups[-1][:2]
        # Add the last 2 digits as a new group
        groups.append(cleaned_number[-2:])
    elif remainder == 2:
        # If 2 digits remain, add them as a final group
        groups.append(cleaned_number[-2:])
    # If remainder is 0, all digits are already grouped perfectly
    
    # Join all groups with dashes
    formatted_number = "-".join(groups)
    
    return formatted_number
    # Time: O(n)
    # Space: O(n)


def main():
    result = reformat_number(number = "1-23-45 6")
    print(result) # "123-456"

    result = reformat_number(number = "123 4-567")
    print(result) # "123-45-67"

    result = reformat_number(number = "123 4-5678")
    print(result) # "123-456-78"

if __name__ == "__main__":
    main()
