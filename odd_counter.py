odd = 0
for i in range(10):
    num = int(input("Enter the number: "))
    if num % 2 != 0:
        odd += 1
print("Total odd numbers: ", odd)