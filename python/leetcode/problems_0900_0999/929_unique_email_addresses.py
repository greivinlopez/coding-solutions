# ---------------------------
# 929. Unique Email Addresses
# ---------------------------

# Problem: https://leetcode.com/problems/unique-email-addresses/
# 
# Every valid email consists of a local name and a domain name, separated by 
# the '@' sign. Besides lowercase letters, the email may contain one or more 
# '.' or '+'.
# 
#   For example, in "alice@leetcode.com", "alice" is the local name, and 
# "leetcode.com" is the domain name.
# 
# If you add periods '.' between some characters in the local name part of an 
# email address, mail sent there will be forwarded to the same address without 
# dots in the local name. Note that this rule does not apply to domain names.
# 
#   For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the 
# same email address.
# 
# If you add a plus '+' in the local name, everything after the first plus sign 
# will be ignored. This allows certain emails to be filtered. Note that this rule 
# does not apply to domain names.
# 
#   For example, "m.y+name@email.com" will be forwarded to "my@email.com".
# 
# It is possible to use both of these rules at the same time.
# 
# Given an array of strings emails where we send one email to each emails[i], return the number of different addresses that actually receive mails.
# 
#  
# Example 1:
# 
# Input: emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
# Output: 2
# Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails.
# 
# Example 2:
# 
# Input: emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
# Output: 3
#  
# 
# Constraints:
# 
#   1 <= emails.length <= 100
#   1 <= emails[i].length <= 100
#   emails[i] consist of lowercase English letters, '+', '.' and '@'.
#   Each emails[i] contains exactly one '@' character.
#   All local and domain names are non-empty.
#   Local names do not start with a '+' character.
#   Domain names end with the ".com" suffix.
#   Domain names must contain at least one character before ".com" suffix.

# Solution: https://youtu.be/TC_xLIWl7qY
# Credit: Navdeep Singh founder of NeetCode
def num_unique_emails(emails):
    unique_emails: set[str] = set()
    for email in emails:
        local_name, domain_name = email.split('@')
        local_name = local_name.split('+')[0]
        local_name = local_name.replace('.', '')
        email = local_name + '@' + domain_name
        unique_emails.add(email)
    return len(unique_emails)


def main():
    emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
    result = num_unique_emails(emails)
    print(result) # 2

    emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
    result = num_unique_emails(emails)
    print(result) # 3

if __name__ == "__main__":
    main()
