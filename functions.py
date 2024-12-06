def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

temperature = float(input("Please enter the temperature in celsius: "))
converted = celsius_to_fahrenheit(temperature)
print(f"{converted} fahrenheit")
