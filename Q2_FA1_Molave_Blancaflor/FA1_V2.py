# Input numbers and operation type from user
x = float(input("Enter first number here: "))
y = float(input("Enter second number here: "))
typeofoperation = str(input("Which operation?"))
print("Addition - 1")
print("Subtraction - 2")
print("Multiplication - 3")
print("Division - 4")

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
if (typeofoperation == "1"):
   addition(x,y)

elif (typeofoperation == "2"):
   subtraction(x,y)

elif (typeofoperation == "3"):
   multiplication(x,y)

elif (typeofoperation == "4"):
   division(x,y)
    
