# -------------------
# 721. Accounts Merge
# -------------------

# Problem: https://leetcode.com/problems/accounts-merge/
# 
# Given a list of accounts where each element accounts[i] is a list of strings, 
# where the first element accounts[i][0] is a name, and the rest of the 
# elements are emails representing emails of the account.
# 
# Now, we would like to merge these accounts. Two accounts definitely belong to 
# the same person if there is some common email to both accounts. Note that even 
# if two accounts have the same name, they may belong to different people as 
# people could have the same name. A person can have any number of accounts 
# initially, but all of their accounts definitely have the same name.
# 
# After merging the accounts, return the accounts in the following format: the 
# first element of each account is the name, and the rest of the elements are 
# emails in sorted order. The accounts themselves can be returned in any order.
# 
#  
# Example 1:
# 
# 
# Input: accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
# Output: [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
# Explanation:
# The first and second John's are the same person as they have the common email "johnsmith@mail.com".
# The third John and Mary are different people as none of their email addresses are used by other accounts.
# We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'], 
# ['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.
# 
# 
# Example 2:
# 
# 
# Input: accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
# Output: [["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]]
# 
#  
# Constraints:
# 
# 	1 <= accounts.length <= 1000
# 	2 <= accounts[i].length <= 10
# 	1 <= accounts[i][j].length <= 30
# 	accounts[i][0] consists of English letters.
# 	accounts[i][j] (for j > 0) is a valid email.

from collections import defaultdict

# Solution: https://youtu.be/6st4IxEF-90
# Credit: Navdeep Singh founder of NeetCode
class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n
    
    def find(self, x):
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x
    
    def union(self, x1, x2):
        p1, p2 = self.find(x1), self.find(x2)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True

def accounts_merge(accounts):
    uf = UnionFind(len(accounts))
    emailToAcc = {} # email -> index of acc

    for i, a in enumerate(accounts):
        for e in a[1:]:
            if e in emailToAcc:
                uf.union(i, emailToAcc[e])
            else:
                emailToAcc[e] = i

    emailGroup = defaultdict(list) # index of acc -> list of emails
    for e, i in emailToAcc.items():
        leader = uf.find(i)
        emailGroup[leader].append(e)

    res = []
    for i, emails in emailGroup.items():
        name = accounts[i][0]
        res.append([name] + sorted(emailGroup[i])) # array concat
    return res


def main():
    accounts = [
        ["John","johnsmith@mail.com","john_newyork@mail.com"],
        ["John","johnsmith@mail.com","john00@mail.com"],
        ["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]
    ]
    result = accounts_merge(accounts)
    print(result) 
    # [ ['Mary', 'mary@mail.com'], 
    # ['John', 'johnnybravo@mail.com'], 
    # ['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'] ]

if __name__ == "__main__":
    main()
