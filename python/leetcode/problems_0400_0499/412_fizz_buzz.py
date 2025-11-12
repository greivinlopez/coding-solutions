# --------------
# 412. Fizz Buzz
# --------------

# Problem: https://leetcode.com/problems/fizz-buzz
#
# Given an integer n, return a string array answer (1-indexed) where:
#         answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
#         answer[i] == "Fizz" if i is divisible by 3.
#         answer[i] == "Buzz" if i is divisible by 5.
#         answer[i] == i (as a string) if none of the above conditions are true.
# 
# Example 1:
# 
# Input: n = 3
# Output: ["1","2","Fizz"]
# 
# Example 2:
# 
# Input: n = 5
# Output: ["1","2","Fizz","4","Buzz"]
# 
# Example 3:
# 
# Input: n = 15
# Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13"
# ,"14","FizzBuzz"]
# 
# Constraints:
#         1 <= n <= 10⁴


# Solution: https://leetcode.com/problems/fizz-buzz/solutions/1369285/python-3-beats-100-0-simple
def fizz_buzz(n):
    f, b, fb = 'Fizz', 'Buzz', 'FizzBuzz'
    arr = [str(x + 1) for x in range(n)]
    
    for i in range(2, n, 3):
        arr[i] = f
    
    for i in range(4, n, 5):
        arr[i] = b
    
    for i in range(14, n, 15):
        arr[i] = fb
    
    return arr


def main():
    result = fizz_buzz(3)
    print(result) # ["1","2","Fizz"]

    result = fizz_buzz(5)
    print(result) # ["1","2","Fizz","4","Buzz"]

    result = fizz_buzz(15)
    print(result) # ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]

if __name__ == "__main__":
    main()
