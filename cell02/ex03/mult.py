num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num = num1 * num2

print(num)

if num > 0:
    print("This number is positive.")
elif num < 0:
    print("This number is negative.")
elif num == 0:
    print("This number is both positive and negative.")