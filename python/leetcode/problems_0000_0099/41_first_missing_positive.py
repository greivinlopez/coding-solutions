# ---------------------------
# 41. First Missing Positive
# ---------------------------

# Problem: https://leetcode.com/problems/first-missing-positive/
# Given an unsorted integer array nums. Return the smallest positive integer
# that is not present in nums.
# 
# You must implement an algorithm that runs in O(n) time and uses 
# O(1) auxiliary space.

# Solution: https://youtu.be/8g78yfzMlao
# Credit: Navdeep Singh founder of NeetCode 
def first_missing_positive(nums):
    # Time: O(n)
    # Space: O(1)
    A = nums
    for i in range(len(A)):
        if A[i] < 0:
            A[i] = 0
        
    for i in range(len(A)):
        val = abs(A[i])
        if 1 <= val <= len(A):
            if A[val - 1] > 0:
                A[val - 1] *= -1
            elif A[val - 1] == 0:
                A[val - 1] = -1 * (len(A) + 1)
    
    for i in range( 1, len(A)+ 1):
        if A[i -1] >= 0:
            return i
    
    return len(A) + 1

# Alternative Solution
def first_missing_positive_alt(nums):
    new = set(nums)
    i = 1
    while i in new:
        i += 1
    return i

def main():
    result = first_missing_positive_alt([1,2,0]) # 3
    print(result)
    result = first_missing_positive_alt([3,4,-1,1]) # 2
    print(result)
    result = first_missing_positive_alt([7,8,9,11,12]) # 1
    print(result)

if __name__ == "__main__":
    main()