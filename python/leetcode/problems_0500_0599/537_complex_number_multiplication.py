# ----------------------------------
# 537. Complex Number Multiplication
# ----------------------------------

# Problem: https://leetcode.com/problems/complex-number-multiplication
#
# A complex number can be represented as a string on the form "real+imaginaryi"
# where:
#         
#   * real is the real part and is an integer in the range [-100, 100].
#   * imaginary is the imaginary part and is an integer in the range [-100, 100].
#   * i² == -1.
# 
# Given two complex numbers num1 and num2 as strings, return a string of the
# complex number that represents their multiplications.
# 
# Example 1:
# 
# Input: num1 = "1+1i", num2 = "1+1i"
# Output: "0+2i"
# 
# Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to
# the form of 0+2i.
# 
# Example 2:
# 
# Input: num1 = "1+-1i", num2 = "1+-1i"
# Output: "0+-2i"
# 
# Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it
# to the form of 0+-2i.
# 
# 
# Constraints:
#         num1 and num2 are valid complex numbers.


# Solution: https://algo.monster/liteproblems/537
# Credit: AlgoMonster
def complex_number_multiply(num1, num2):
    # Parse the real and imaginary parts from the first complex number
    # Remove the trailing 'i' and split by '+' to get both parts
    real_part_1, imaginary_part_1 = map(int, num1[:-1].split("+"))
    
    # Parse the real and imaginary parts from the second complex number
    real_part_2, imaginary_part_2 = map(int, num2[:-1].split("+"))
    
    # Calculate the real part of the product: a1*a2 - b1*b2
    result_real = real_part_1 * real_part_2 - imaginary_part_1 * imaginary_part_2
    
    # Calculate the imaginary part of the product: a1*b2 + a2*b1
    result_imaginary = real_part_1 * imaginary_part_2 + real_part_2 * imaginary_part_1
    
    # Format and return the result as "a+bi"
    return f"{result_real}+{result_imaginary}i"
    # Time: O(1)
    # Space: O(1)


def main():
    result = complex_number_multiply(num1 = "1+1i", num2 = "1+1i")
    print(result) # "0+2i"

    result = complex_number_multiply(num1 = "1+-1i", num2 = "1+-1i")
    print(result) # "0+-2i"

if __name__ == "__main__":
    main()
