# ----------------------------
# 1108. Defanging an IP Address
# ----------------------------

# Problem: https://leetcode.com/problems/defanging-an-ip-address
#
# Given a valid (IPv4) IP address, return a defanged version of that IP address.
# 
# A defanged IP address replaces every period "." with "[.]".
# 
# Example 1:
# 
# Input: address = "1.1.1.1"
# Output: "1[.]1[.]1[.]1"
# 
# Example 2:
# 
# Input: address = "255.100.50.0"
# Output: "255[.]100[.]50[.]0"
# 
# 
# Constraints:
#         The given address is a valid IPv4 address.


# Solution: https://algo.monster/liteproblems/1108
# Credit: AlgoMonster
def defang_ip_addr(address):
    # Replace all occurrences of '.' with '[.]' to defang the IP address
    return address.replace('.', '[.]')
    # Time: O(n)
    # Space: O(1)

# Alternative Solutions: https://leetcode.com/problems/defanging-an-ip-address/solutions/328895/java-python-3-3-one-liners-one-w-o-lib-w-analysis
# Credit: rock -> https://leetcode.com/u/rock/
import re

def defang_ip_addr_join_split(address):
    return '[.]'.join(address.split('.'))

def defang_ip_addr_regex(address):
    return re.sub('\.', '[.]', address)

def defang_ip_addr_comprehension(address):
    return ''.join('[.]' if c == '.' else c for c in address)


def main():
    result = defang_ip_addr(address = "1.1.1.1")
    print(result) # "1[.]1[.]1[.]1"

    result = defang_ip_addr(address = "255.100.50.0")
    print(result) # "255[.]100[.]50[.]0"

if __name__ == "__main__":
    main()
