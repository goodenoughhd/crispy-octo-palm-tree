'''
Create a program to add and multiply two numbers. 
For this, create two functions add_numbers() and multiply_numbers().
These functions should compute the result and return them to the function call.
The results should be printed from outside the function.
'''

def add_numbers(n1, n2):
    result = n1 + n2
    return result

def multiply_numbers(n1, n2):
    result = n1 * n2
    return result

num1 = 5
num2 = 6

sum_of_numbers = add_numbers(num1, num2)
multiply = multiply_numbers(num1, num2)

print("The sum is", sum_of_numbers)
print("The multiply result is", multiply)