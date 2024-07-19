#Task 2: Use inputs to ask the user what operation 
# they want to perform, and what numbers they want to use.

def addition(x,y):
    return x+y
def subtraction(x,y):
    return x-y
def division(x,y):
    return x/y
def multiplication(x,y):
    return x*y

my_operator=input("What operation would you like to perform? [A]ddition, [S]ubtraction, [M]ultiplication, or [D]ivision?").lower()
if my_operator=="a" or my_operator=="addition":
    my_operator="a"
elif my_operator=="s" or my_operator=="subtraction":
    my_operator="s"
elif my_operator=="m" or my_operator=="multiplication":
     my_operator="m"
elif my_operator=="d" or my_operator=="division":
     my_operator="d"
else:
    input("Please make another selection. Not a valid choice!\n")

num_one = input("Please input your first number:\n")
num_one = input("Please input your second number:\n")
