# Input numbers and operation type from user
x = float(input("Enter first number here: "))
y = float(input("Enter second number here: "))
typeofoperation = str(input("Which operation? (Addition, Subtraction, Multiplication, Division):"))

# Define functions for each operation
# Addition function
def addition(x,y):
    answer = x + y
    print("The answer is:", answer)
    return x + y
# Subtraction function
def subtraction(x,y):
    answer = x - y
    print("The answer is:", answer)
    return x - y
# Multiplication function
def multiplication(x, y):
    answer = x * y
    print("The answer is:", answer)
    return x * y
# Division function
def division(x, y):
    answer = x / y
    print("The answer is:", answer)
    return x / y

# Execute the appropriate function based on user input
if (typeofoperation == "Addition"):
   addition(x,y)

elif (typeofoperation == "Subtraction"):
   subtraction(x,y)

elif (typeofoperation == "Multiplication"):
   multiplication(x,y)

elif (typeofoperation == "Division"):
   division(x,y)
    