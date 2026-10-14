x = float(input("Enter first number here."))
y = float(input("Enter second number here"))
typeofoperation = str(input("Which operation? (Addition, Subtraction, Multiplication, Division)"))

def addition(x,y):
    answer = x + y
    print("The answer is:", answer)
    return x + y

def subtraction(x,y):
    answer = x - y
    print("The answer is:", answer)
    return x - y

def multiplication(x, y):
    answer = x * y
    print("The answer is:", answer)
    return x * y

def division(x, y):
    answer = x / y
    print("The answer is:", answer)
    return x / y


if (typeofoperation == "Addition"):
   addition(x,y)

elif (typeofoperation == "Subtraction"):
   subtraction(x,y)

elif (typeofoperation == "Multiplication"):
   multiplication(x,y)

elif (typeofoperation == "Division"):
   division(x,y)
    