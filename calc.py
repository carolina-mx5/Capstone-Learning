# calculator program

# addition operation
def add(x, y):
    return x + y
# subtraction operation
def sub(x, y):
    return x - y

# multiplication operation
def mult(x, y):
    return x * y

# division operation
def div(x, y):
    if y == 0:
        return "undefined"
    return x / y

# print options to choose from
print("Select which math operation you'd like to perform")
print("1 - Addition")
print("2 - Subtraction")
print("3 - Multiplication")
print("4 - Division")

option = input("Enter option 1, 2, 3, 4\n") # gets user option input

num1 = float(input("Enter first number: ")) # gets user input for 1st num
num2 = float(input("Enter second number: ")) # gets user input for 2nd mum

# prints out the answer based on which math operation was chosen
if option == '1':
    print(num1,"+",num2,"=", add(num1, num2))

elif option == '2':
    print(num1,"-",num2,"=", sub(num1, num2))

elif option == '3':
    print(num1,"*",num2,"=", mult(num1, num2))

elif option == '4':
    print(num1,"/",num2,"=", div(num1, num2))

else:
    print("Whoops! Looks like you typed an invalid option.") # prints error msg if option 1-4 was not chosen