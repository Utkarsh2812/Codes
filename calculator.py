def add( a , b ):
    return a + b

def subtract( a , b ):
    return a - b

def multiply( a , b ):
    return a * b

def divide( a , b ):
    return a/b

def exponential( a , b):
    return a ** b

def floor_division( a , b ):
    return a // b

def modulus( a , b):
    return a % b

print("Select the below options: ")
print("1) Add\n 2) Subtract\n 3) Multiply\n 4) Divide\n 5) Exponent\n 6) Floor Division\n 7) Modulus")

choice = input("Enter your choice\n 1/2/3/4/5/6/7\n")
if choice in ('1' , '2' , '3' , '4' , '5' , '6' , '7'):
    a = int(input('Enter a Number: '))
    b = int(input('Enter a Number: '))
    if choice == '1':
        print(f"{a} + {b} = {add(a,b)}")
    elif choice == "2":
        print(f"{a} - {b} = {subtract(a,b)}")
    elif choice == '3':
        print(f"{a} x {b} = {multiply(a,b)}")
    elif choice == '4':
        print(f"{a} / {b} = {divide(a,b)}")
    elif choice == '5':
        print(f"{a} ^ {b} = {exponential(a,b)}")
    elif choice == '6':
        print(f"{a} // {b} = {floor_division(a,b)}")
    elif choice == '7':
        print(f"{a} % {b} = {modulus(a,b)}")
else:
    print("Invalid Input !")


