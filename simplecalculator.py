# mini 1st easy calculator program

operations = input("Enter an operator (+ - * / ) :")
num1 = float(input("Enter the first number :"))
num2 = float(input("Enter the second number :"))
if operations == "+":
    result = num1 + num2
    print(round(result))
elif operations == "-":
    result = num1 - num2
    print(round(result))
elif operations == "*":
    result = num1 * num2
    print(round(result))
elif operations == "/":
    result = num1 /num2
    print(round(result))
else:
    print(f"{operations} is not a valid operations")






# mini 2nd medium calculator program


print("************")
print("1 - Add")
print("2 - subtract")
print("3 - multiply")
print("4 - Divide")
print("***************")
option = int(input("choose an operation : "))

if (option in [1,2,3,4]):
    num1 = int(input("Enter first number : "))
    num2 = int(input("Enter second number : "))

    if(option == 1):
        result = num1+ num2
    elif (option == 2):
        result = num1-num2
    elif (option == 3):
        result = num1 * num2
    elif (option ==4 ):
        result = num1 // num2
else:
    print("Invalid operation entered")

print("The result of the operations is {} ".format(result))



# mini 3rd hard calculator program coming up


