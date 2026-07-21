num = int(input("Enter a number: "))

def factorial(num):
    if num < 0:
        return "Factorial is not defined for negative numbers."
    result = 1
    for i in range(2, num + 1):
        result *= i
    return result

result = factorial(num)
print(f"The factorial of {num} is: {result}")