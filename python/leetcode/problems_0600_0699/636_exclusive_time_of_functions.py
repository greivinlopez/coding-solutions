# --------------------------------
# 636. Exclusive Time of Functions
# --------------------------------

# Problem: https://leetcode.com/problems/exclusive-time-of-functions
#
# On a single-threaded CPU, we execute a program containing n functions. Each
# function has a unique ID between 0 and n-1.
# 
# Function calls are stored in a call stack: when a function call starts, its ID
# is pushed onto the stack, and when a function call ends, its ID is popped off
# the stack. The function whose ID is at the top of the stack is the current
# function being executed. Each time a function starts or ends, we write a log
# with the ID, whether it started or ended, and the timestamp.
# 
# You are given a list logs, where logs[i] represents the ith log message
# formatted as a string "{function_id}:{"start" | "end"}:{timestamp}". For
# example, "0:start:3" means a function call with function ID 0 started at the
# beginning of timestamp 3, and "1:end:2" means a function call with function ID 1
# ended at the end of timestamp 2. Note that a function can be called multiple
# times, possibly recursively.
# 
# A function's exclusive time is the sum of execution times for all function calls
# in the program. For example, if a function is called twice, one call executing
# for 2 time units and another call executing for 1 time unit, the exclusive time
# is 2 + 1 = 3.
# 
# Return the exclusive time of each function in an array, where the value at the
# ith index represents the exclusive time for the function with ID i.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2019/04/05/diag1b.png
# 
# Input: n = 2, logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]
# Output: [3,4]
# 
# Explanation:
# Function 0 starts at the beginning of time 0, then it executes 2 for units of
# time and reaches the end of time 1.
# Function 1 starts at the beginning of time 2, executes for 4 units of time, and
# ends at the end of time 5.
# Function 0 resumes execution at the beginning of time 6 and executes for 1 unit
# of time.
# So function 0 spends 2 + 1 = 3 units of total time executing, and function 1
# spends 4 units of total time executing.
# 
# Example 2:
# 
# Input: n = 1, logs =
# ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]
# Output: [8]
# 
# Explanation:
# Function 0 starts at the beginning of time 0, executes for 2 units of time, and
# recursively calls itself.
# Function 0 (recursive call) starts at the beginning of time 2 and executes for 4
# units of time.
# Function 0 (initial call) resumes execution then immediately calls itself again.
# Function 0 (2nd recursive call) starts at the beginning of time 6 and executes
# for 1 unit of time.
# Function 0 (initial call) resumes execution at the beginning of time 7 and
# executes for 1 unit of time.
# So function 0 spends 2 + 4 + 1 + 1 = 8 units of total time executing.
# 
# Example 3:
# 
# Input: n = 2, logs =
# ["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"]
# Output: [7,1]
# 
# Explanation:
# Function 0 starts at the beginning of time 0, executes for 2 units of time, and
# recursively calls itself.
# Function 0 (recursive call) starts at the beginning of time 2 and executes for 4
# units of time.
# Function 0 (initial call) resumes execution then immediately calls function 1.
# Function 1 starts at the beginning of time 6, executes 1 unit of time, and ends
# at the end of time 6.
# Function 0 resumes execution at the beginning of time 6 and executes for 2 units
# of time.
# So function 0 spends 2 + 4 + 1 = 7 units of total time executing, and function 1
# spends 1 unit of total time executing.
# 
# 
# Constraints:
#         1 <= n <= 100
#         2 <= logs.length <= 500
#         0 <= function_id < n
#         0 <= timestamp <= 10⁹
#         No two start events will happen at the same timestamp.
#         No two end events will happen at the same timestamp.
#         Each function has an "end" log for each "start" log.


# Solution: https://algo.monster/liteproblems/636
# Credit: AlgoMonster
def exclusive_time(n, logs):
    # Stack to track currently running functions
    function_stack = []
    
    # Initialize result array with exclusive times for each function
    exclusive_times = [0] * n
    
    # Track the previous timestamp for calculating time intervals
    previous_timestamp = 0
    
    # Process each log entry
    for log_entry in logs:
        # Parse log entry: function_id:operation:timestamp
        function_id, operation, timestamp = log_entry.split(":")
        function_id = int(function_id)
        current_timestamp = int(timestamp)
        
        # Check if this is a start operation
        if operation == "start":
            # If there's a function currently running, update its exclusive time
            if function_stack:
                top_function = function_stack[-1]
                exclusive_times[top_function] += current_timestamp - previous_timestamp
            
            # Push new function onto stack
            function_stack.append(function_id)
            previous_timestamp = current_timestamp
            
        else:  # operation == "end"
            # Pop the ending function and update its exclusive time
            # Add 1 because end timestamp is inclusive
            ending_function = function_stack.pop()
            exclusive_times[ending_function] += current_timestamp - previous_timestamp + 1
            
            # Move to next timestamp after the end
            previous_timestamp = current_timestamp + 1
    
    return exclusive_times
    # Time: O(n)
    # Space: O(n)


def main():
    result = exclusive_time(n = 2, logs = ["0:start:0","1:start:2","1:end:5","0:end:6"])
    print(result) # [3,4]

    result = exclusive_time(n = 1, logs = ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"])
    print(result) # [8]

    result = exclusive_time(n = 2, logs = ["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"])
    print(result) # [7,1]

if __name__ == "__main__":
    main()
