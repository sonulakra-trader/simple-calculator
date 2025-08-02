
a = float(input("enter first number :"))
b = float(input("enter second number :"))

if b==0:
    print("error: cannot divide by zero")
else:
    print("Addition:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)
    print("Division:", a / b)
    print("Floor Division:", a // b)
    print("Remainder (Modulo):", a % b)
    print("Power (a^b):", a ** b)
