# -----------------
# 190. Reverse Bits
# -----------------

# Problem: https://leetcode.com/problems/reverse-bits/
# 
# Reverse bits of a given 32 bits signed integer.
# 
#  
# Example 1:
# 
# Input: n = 43261596
# 
# Output: 964176192
# 
# Explanation:
#  		
# 			43261596
# 			00000010100101000001111010011100
# 		
# 		
# 			964176192
# 			00111001011110000010100101000000
# 		
# 
# Example 2:
# 
# Input: n = 2147483644
# 
# Output: 1073741822
# 
# Explanation:
# 	
# 			2147483644
# 			01111111111111111111111111111100
# 		
# 		
# 			1073741822
# 			00111111111111111111111111111110
# 		
#  
# Constraints:
# 
# 	0 <= n <= 231 - 2
# 	n is even.
# 
# Follow up: If this function is called many times, how would you optimize it?


# Solution: https://youtu.be/UcoN6UjAI64
# Credit: Navdeep Singh founder of NeetCode
def reverse_bits(n):
    res = 0
    for i in range(32):
        bit = (n >> i) & 1
        res += (bit << (31 - i))
    return res


def main():
    result = reverse_bits(43261596)
    print(result) # 964176192

    result = reverse_bits(2147483644)
    print(result) # 1073741822

if __name__ == "__main__":
    main()
