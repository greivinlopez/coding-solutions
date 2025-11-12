# --------------------------
# 811. Subdomain Visit Count
# --------------------------

# Problem: https://leetcode.com/problems/subdomain-visit-count
#
# A website domain "discuss.leetcode.com" consists of various subdomains. At the
# top level, we have "com", at the next level, we have "leetcode.com" and at the
# lowest level, "discuss.leetcode.com". When we visit a domain like
# "discuss.leetcode.com", we will also visit the parent domains "leetcode.com" and
# "com" implicitly.
# 
# A count-paired domain is a domain that has one of the two formats "rep d1.d2.d3"
# or "rep d1.d2" where rep is the number of visits to the domain and d1.d2.d3 is
# the domain itself.
#         
#   * For example, "9001 discuss.leetcode.com" is a count-paired domain that
#     indicates that discuss.leetcode.com was visited 9001 times.
# 
# Given an array of count-paired domains cpdomains, return an array of the count-
# paired domains of each subdomain in the input. You may return the answer in any
# order.
# 
# Example 1:
# 
# Input: cpdomains = ["9001 discuss.leetcode.com"]
# Output: ["9001 leetcode.com","9001 discuss.leetcode.com","9001 com"]
# 
# Explanation: We only have one website domain: "discuss.leetcode.com".
# As discussed above, the subdomain "leetcode.com" and "com" will also be visited.
# So they will all be visited 9001 times.
# 
# Example 2:
# 
# Input: cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com",
# "5 wiki.org"]
# Output: ["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5
# org","1 intel.mail.com","951 com"]
# 
# Explanation: We will visit "google.mail.com" 900 times, "yahoo.com" 50 times,
# "intel.mail.com" once and "wiki.org" 5 times.
# For the subdomains, we will visit "mail.com" 900 + 1 = 901 times, "com" 900 + 50
# + 1 = 951 times, and "org" 5 times.
# 
# 
# Constraints:
#         1 <= cpdomain.length <= 100
#         1 <= cpdomain[i].length <= 100
#         cpdomain[i] follows either the "repᵢ d1ᵢ.d2ᵢ.d3ᵢ" format or the "repi d1ᵢ.d2ᵢ" format.
#         repᵢ is an integer in the range [1, 10⁴].
#         d1ᵢ, d2ᵢ, and d3ᵢ consist of lowercase English letters.

from collections import Counter

# Solution: https://algo.monster/liteproblems/811
# Credit: AlgoMonster
def subdomain_visits(cpdomains):
    # Counter to store the visit count for each domain/subdomain
    domain_counter = Counter()
    
    # Process each count-paired domain
    for count_paired_domain in cpdomains:
        # Extract the visit count from the beginning of the string
        space_index = count_paired_domain.index(' ')
        visit_count = int(count_paired_domain[:space_index])
        
        # Iterate through each character to find domain separators
        for index, char in enumerate(count_paired_domain):
            # When we find a space or dot, the substring after it is a valid domain
            if char in ' .':
                # Extract the domain starting from the character after the separator
                domain = count_paired_domain[index + 1:]
                # Add the visit count to this domain
                domain_counter[domain] += visit_count
    
    # Format the results as "count domain" strings
    result = []
    for domain, count in domain_counter.items():
        result.append(f'{count} {domain}')
    
    return result
    # Time: O(n * m)
    # Space: O(n * m)
    # n = the number of domains in the input list
    # m = the average length of each domain string.


def main():
    result = subdomain_visits(cpdomains = ["9001 discuss.leetcode.com"])
    print(result) # ['9001 discuss.leetcode.com', '9001 leetcode.com', '9001 com']

    result = subdomain_visits(cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"])
    print(result) # ['900 google.mail.com', '901 mail.com', '951 com', '50 yahoo.com', '1 intel.mail.com', '5 wiki.org', '5 org']

if __name__ == "__main__":
    main()
