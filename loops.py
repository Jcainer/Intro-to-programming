def factorial(n):
    number = 1
    for i in range (1, n+1):
        number *= i
        print(f"factorial result is {number}")
    return number

user_input = int(input("Enter the number to see the factorials of: "))
factorial(user_input)
