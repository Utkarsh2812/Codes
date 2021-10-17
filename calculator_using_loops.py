print(f'''The functions which this calculator can perform are
1.Addition
2.Subtraction
3.Multiplication
4.Division''')

n = input("Enter your selection: ")

if n in ('1' , '2' , '3' , '4' , '5' , '6' , '7'):
    a = int(input('Enter a Number: '))
    b = int(input('Enter a Number: '))
    
    if n == '1':
        c = a+b
        print(f"{a} + {b} = {c}")
    elif n == "2":
        c = a-b
        print(f"{a} - {b} = {c}")
    elif n == '3':
        c = a*b
        print(f"{a} x {b} = {c}")
    elif n == '4':
        c = a/b
        print(f"{a} / {b} = {c}")
else:
    print("Invalid Input")
