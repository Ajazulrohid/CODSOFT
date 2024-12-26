num1 = float(input("Enter Number1 :  "))
num2 = float(input("Enter Number2 :  "))
print("Enter Operation 1 : ADD ,2 : SUBTRACT, 3: MULTIPLY,4 DIVISION")
operation = int(input("Enter choice(1/2/3/4): "))
if (operation == 1) :
    print(num1 + num2)
elif(operation == 2) :
    print(num1 - num2)
elif(operation == 3):
    print(num1 * num2)
elif(operation == 4):
    print(num1/num2)
else:
    print("Invalid Operation")
