# looping.py
# Demonstrates for loops and while loops

print("Numbers 1 to 20:")
for i in range(1, 21):
    print(i, end=" ")
print()

num = int(input("Enter a number for its multiplication table: "))
print(f"Multiplication table of {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

total = 0
count = 1
while count <= 100:
    total += count
    count += 1
print("Sum of numbers from 1 to 100:", total)

print("Even numbers between 1 and 50:")
for n in range(1, 51):
    if n % 2 == 0:
        print(n, end=" ")
print()