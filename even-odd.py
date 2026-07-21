# def is_even(n):
#     return n % 2 == 0

# def is_odd(n):
#     return n % 2 != 0

# n= int(input("Enter a number: "))

# if n == 0:
#     print(f"{n} is neither even nor odd.")
# elif is_even(n):
#     print(f"{n} is even.")
# else:
#     print(f"{n} is odd.")

def even_odd(num):
    if num == 0:
        return "The number is neither even nor odd."
    elif num % 2 == 0:
        return "The number is even."
    else:
        return "The number is odd."

def Check_even_odd():
    num = int(input("Enter a number: "))
    result = even_odd(num)
    print(result)

Check_even_odd()