num = 1  # Initial number

while num <= 10:  # Condition to check
    multiplier = 1  # Initial multiplier for each number

    while multiplier <= 10:  # Inner loop to calculate the table
        result = num * multiplier
        print(num, "x", multiplier, "=", result)
        multiplier += 1  # Increment the multiplier

    num += 1  # Increment the number
    print()  # Print an empty line between tables




num = 2
while num <= 10:
    print("table of ",num)
    mul = 1

    while mul <= 10: 
        result = num * mul
        print(num, "*", mul, "=", result)
        mul += 1
        
    num += 1
    print()
