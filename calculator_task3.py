#Task 3: Ensure your code can handle division by zero 
# and other potential errors. So if you divide by 0, 
# there is error handling set up to prevent an error from
#  showing in the console.

#Task 2: Use inputs to ask the user what operation 
# they want to perform, and what numbers they want to use.


#bugs
#If you give bad input, it will not work on the first problems 
# afterwards 


def addition(x,y):
    print(f"{x} + {y} = {float(x)+float(y)}")
def subtraction(x,y):
    print(f"{x} - {y} = {float(x)-float(y)}")
def division(x,y):
    try:
        print(f"{x} / {y} = {float(x)/float(y)}")
    except ZeroDivisionError:
        print("You cannot divide by Zero!")
def multiplication(x,y):
    print(f"{x} * {y} = {float(x)*float(y)}")


    

stay=0
while stay==0:
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

    num_one=True
    while num_one:
        num_one = input("Please input your first number:\n")
        try:
            num_one=int(num_one)
            break
        except:
            print("Not a valid number!")
            num_one=True
    num_two=True
    while num_two:
        num_two = input("Please input your second number:\n")
        try:
            num_two=int(num_two)
            break
        except:
            print("Not a valid number!")
            num_two=True
    
    if my_operator=="a":
        addition(num_one,num_two)
    elif my_operator=="m":
        multiplication(num_one,num_two)
    elif my_operator=="s":
        subtraction(num_one,num_two)
    elif my_operator=="d":
        division(num_one,num_two)
    
    go_again = ''
    while True:
        go_again = input("Would you like to perform another operation? Y/N\n").lower()
        
        if go_again=="n" or go_again=="no":
            stay=1
            break
        elif go_again=="y" or go_again=="yes":
            print("Okay!")
            break   
        else:
            print("Not a valid input")
   
