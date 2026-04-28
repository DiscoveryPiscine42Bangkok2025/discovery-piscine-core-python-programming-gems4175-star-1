import time

num = int(input("Enter a number less than 25: "))
if num > 25:
    print("Error")
else:
    while num <= num:
        print("Inside the loop, my variable is", num)
        time.sleep(1)
        num += 1