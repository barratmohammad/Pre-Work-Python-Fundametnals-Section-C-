Enter number 1: 10
Enter number 2: abc
That's not a valid number. Using 0 instead.
Enter number 3: 5

Your numbers: 10, 0, 5
Sum: 15
Average: 5.00

# number_collector.py

number = [1,2,3]

for i in range (1,4):
    try:
        value = int(input(f"Enter number {i}: "))
    except ValueError:
        print("That's not a valid number. Using 0 instead.")
        value = 0
    number.append(value)

#Extract numbers
num1, num2, num3 = numbers

#Calculations
total = sum(numbers)
average = total/3

#Output
print(f"\nYour numbers: {num1}, {num2}, {num3}")
print(f"Sum: {total}")
print(f"Average: {average:.2f}")