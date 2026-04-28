i = 0

while i <= 10:
    print("Table de " + str(i) + ":", end=" ")
    j = 0
    while j <= 10:
        print(i * j, end=" ")
        j = j + 1
    
    print()
    i = i + 1