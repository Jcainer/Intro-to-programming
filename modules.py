def numbers():
    number1 = float(input("enter number 1: "))
    number2 = float(input("enter number 2: "))
    return number1, number2

def calculator(number1, number2):
    sum_result = number1 + number2
    difference = number1 - number2
    product = number1 * number2
    quotient = number1 / number2
    return sum_result, difference, product, quotient

def print_calculations(sum_result,difference,product, quotient):
    print(f"the sum is: {sum_result}")
    print(f"the difference is: {difference}")
    print(f"the product is: {product}")
    print(f"the quotient is: {quotient}")

def file_handling(sum_result,difference,product,quotient):
    file = open("calculations.txt", "a+" )
    file.write(f"the sum is: {sum_result}\n")
    file.write(f"the difference is: {difference}\n")
    file.write(f"the product is: {product}\n")
    file.write(f"the quotient is: {quotient}")

num1, num2 = numbers()
results = calculator(num1, num2)
sum_result, difference, product, quotient = results
print_calculations(sum_result, difference, product, quotient)
file_handling(sum_result, difference, product, quotient)
    
