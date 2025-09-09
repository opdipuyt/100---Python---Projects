import sys

number = input("Which multiplication tabel do you want \n ")

if( number ==""):
    print("Number was left empty ")
    sys.exit()

number = int(number)

for i in range(1, 11):
    print("{number} x {multiplier} = {result}".format(number = number , multiplier = i, result = number*i))



# for loop use

num = int(input("Enter a number here : "))

for x in range(1, 11):
    print(num, "x", x,"=", num*x)


# while loop use

n = int(input("Enter your multiplication number : "))
i = 1
while i<=10:
    print(n,"x",i,"=",n*i)
    i+= 1


### for loop 

number = int(input("Enter the tabel number which you want : "))
times = int(input("Enter the number of time of times you want to multiply : "))

y = 1
y = y+1

for y in range(1,times):

    print(number,"*",y,"=", number*y)
