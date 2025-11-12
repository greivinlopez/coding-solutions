# --------------------------
# 1169. Invalid Transactions
# --------------------------

# Problem: https://leetcode.com/problems/invalid-transactions
#
# A transaction is possibly invalid if:
#         
#   * the amount exceeds $1000, or;
#   * if it occurs within (and including) 60 minutes of another transaction
#     with the same name in a different city.
# 
# You are given an array of strings transaction where transactions[i] consists of
# comma-separated values representing the name, time (in minutes), amount, and
# city of the transaction.
# 
# Return a list of transactions that are possibly invalid. You may return the
# answer in any order.
# 
# Example 1:
# 
# Input: transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
# Output: ["alice,20,800,mtv","alice,50,100,beijing"]
# 
# Explanation: The first transaction is invalid because the second transaction
# occurs within a difference of 60 minutes, have the same name and is in a
# different city. Similarly the second one is invalid too.
# 
# Example 2:
# 
# Input: transactions = ["alice,20,800,mtv","alice,50,1200,mtv"]
# Output: ["alice,50,1200,mtv"]
# 
# Example 3:
# 
# Input: transactions = ["alice,20,800,mtv","bob,50,1200,mtv"]
# Output: ["bob,50,1200,mtv"]
# 
# 
# Constraints:
#         transactions.length <= 1000
#         Each transactions[i] takes the form "{name},{time},{amount},{city}"
#         Each {name} and {city} consist of lowercase English letters, and have
# lengths between 1 and 10.
#         Each {time} consist of digits, and represent an integer between 0 and
# 1000.
#         Each {amount} consist of digits, and represent an integer between 0 and
# 2000.

from collections import defaultdict

# Solution: https://algo.monster/liteproblems/1169
# Credit: AlgoMonster
def invalid_transactions(transactions):
    # Dictionary to store transactions grouped by name
    # Key: name, Value: list of tuples (time, city, index)
    transactions_by_name = defaultdict(list)
    
    # Set to store indices of invalid transactions
    invalid_indices = set()
    
    # Process each transaction
    for index, transaction_str in enumerate(transactions):
        # Parse transaction string into components
        name, time_str, amount_str, city = transaction_str.split(",")
        time = int(time_str)
        amount = int(amount_str)
        
        # Store current transaction details grouped by name
        transactions_by_name[name].append((time, city, index))
        
        # Check if amount exceeds 1000 (invalid condition 1)
        if amount > 1000:
            invalid_indices.add(index)
        
        # Check for conflicts with other transactions of the same person
        # Invalid if: same name, different city, within 60 minutes
        for prev_time, prev_city, prev_index in transactions_by_name[name]:
            if prev_city != city and abs(time - prev_time) <= 60:
                # Mark both transactions as invalid
                invalid_indices.add(index)
                invalid_indices.add(prev_index)
    
    # Return all invalid transactions
    return [transactions[i] for i in invalid_indices]
    # Time: O(n²)
    # Space: O(n)


def main():
    result = invalid_transactions(transactions = ["alice,20,800,mtv","alice,50,100,beijing"])
    print(result) # ["alice,20,800,mtv","alice,50,100,beijing"]

    result = invalid_transactions(transactions = ["alice,20,800,mtv","alice,50,1200,mtv"])
    print(result) # ["alice,50,1200,mtv"]

    result = invalid_transactions(transactions = ["alice,20,800,mtv","bob,50,1200,mtv"])
    print(result) # ["bob,50,1200,mtv"]

if __name__ == "__main__":
    main()
