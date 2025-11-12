# ----------------------------
# 93. Restore IP Addresses 🌐
# ----------------------------

# Problem: https://leetcode.com/problems/restore-ip-addresses/
# 
# A valid IP address consists of exactly four integers separated by single dots. 
# Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.
# 
# For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, 
# but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.
# 
# Given a string s containing only digits, return all possible valid IP addresses 
# that can be formed by inserting dots into s. You are not allowed to reorder or 
# remove any digits in s. You may return the valid IP addresses in any order.

# Solution: https://youtu.be/RF_M9tX4Eag
# Credit: Navdeep Singh founder of NeetCode
def restore_ip_addresses(s):
    res = []
    if len(s) > 12:
        return res

    def backtrack(i, dots, curIP):
        if dots == 4 and i == len(s):
            res.append(curIP[:-1]) # remove last '.'
            return
        if dots > 4:
            return
        
        for j in range(i, min(i + 3, len(s))):
            if int(s[i:j+1]) <= 255 and (i == j or s[i] != '0'):
                backtrack(j + 1, dots + 1, curIP + s[i:j+1] + '.')

    backtrack(0, 0, '')
    return res


def main():
    result = restore_ip_addresses('25525511135')
    print(result) # ["255.255.11.135","255.255.111.35"]

    result = restore_ip_addresses('0000')
    print(result) # ["0.0.0.0"]

    result = restore_ip_addresses('101023')
    print(result) # ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]

if __name__ == "__main__":
    main()