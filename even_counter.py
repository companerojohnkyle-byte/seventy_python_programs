even = 0
for i in range(10):
    num = int(input("Enter the number: "))
    if num % 2 == 0:
        even += 1
print("Total even numbers: ", even)