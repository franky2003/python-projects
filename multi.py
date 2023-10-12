def multiplication_table(number):
    print(f"Multiplication table for {number}:")
    for i in range(1, 11):
        result = number * i
        print(f"{number} x {i} = {result}")

number=int(input("Enter the number:"))
multiplication_table(number)