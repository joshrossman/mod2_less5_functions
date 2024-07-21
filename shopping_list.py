#price allows a non-number
#extra space by add
aisle, category, estimate =False, False, False
shopping_list, my_aisle, my_category, my_estimate, storage_list=[],[],[],[],[]

def new_item():
    shopping_list.append(input("Add item:").lower())
    if aisle==True:
        while True:
            try:
                new_price_data=int(input("Add Aisle:"))
                if 0<new_price_data<100:
                    break
                else:
                   print("Please print an aisle number between 1 and 99.")
            except:
                print("Please print an aisle number between 1 and 99.")
        my_aisle.append(new_price_data)
    else:
        my_aisle.append('NA') 
    my_category.append(input("Add category (Frozen, Produce, Dairy, Bakery, etc.):")) if category==True else my_category.append('NA')
    my_estimate.append(input("Add price:")) if estimate==True else my_estimate.append('NA')
    storage_list.append('')
        
def remove_item():
        my_removed_item=input("List item to remove:").lower()
        my_removed_item=make_print_pretty(shopping_list,my_removed_item)
        if my_removed_item in shopping_list:
            my_removed_index= shopping_list.index(my_removed_item)
            shopping_list.pop(my_removed_index)
            my_aisle.pop(my_removed_index)
            my_category.pop(my_removed_index)
            my_estimate.pop(my_removed_index)
            storage_list.pop(my_removed_index)
            print(f"List update! Removed:{my_removed_item}")
        else:
            print("LIST NOT UPDATED: Item is not in the list!")
    
def settings():
    print("Please choose your settings:")
    global aisle, estimate, category
    aisle=input("Include aisle? Y/N  ")
    aisle=True if aisle.lower()=="y" or aisle.lower() =="yes" else False  
    estimate=input("Include price estimate? Y/N  ")
    estimate=True if estimate.lower()=="y" or estimate.lower() =="yes" else False 
    category=input("Include category? Y/N  ")
    category=True if category.lower()=="y" or category.lower() =="yes" else False
def make_print_pretty(my_list,my_var=0):
    longest_var=0
    if my_var==0:
        for i in range(len(my_list)):
            if longest_var<len(my_list[i]):
                longest_var=len(my_list[i])
        for i in range(len(my_list)):
            while len(my_list[i])<longest_var:
                my_list[i]+=" "
    else:
        for i in range(len(my_list)):
            if longest_var<len(my_list[i]):
                longest_var=len(my_list[i])
        while len(my_var)<longest_var:
            my_var+=' '
        else:
            return my_var
def sort_list(my_choice, my_var1,my_var2,my_var3,my_var4,back_for):
    global my_aisle, my_estimate, shopping_list,my_category
    storage_var=''
    if my_choice=="abc":
        my_choice=my_var1
    elif my_choice=="aisle":
        my_choice=my_var2
    elif my_choice=="cat":
        my_choice=my_var4
    elif my_choice=="price":
        my_choice=my_var3
    for i in range(len(shopping_list)):
        if str(my_choice[i])[0]!="0":
            print(str(my_choice[i])[0])
            my_choice[i]="z"+str(my_choice[i])
        storage_var=str(my_choice[i])+"***"+str(my_var1[i])+"***" + str(my_var2[i])+"***"+ str(my_var3[i])+"***" + str(my_var4[i])+"***"
        storage_list[i]=storage_var
    storage_list.sort()
    if back_for==False:
        storage_list.reverse()
    for i in range(len(storage_list)):
        storage_var_list=storage_list[i].split("***")
        shopping_list[i]= storage_var_list[1]
        my_aisle[i] = storage_var_list[2]
        my_estimate[i]  = storage_var_list[3]
        my_category[i] = storage_var_list[4]
    

def print_list():
    global my_estimate
    make_print_pretty(shopping_list)
    make_print_pretty(my_category)
    for i in range(len(shopping_list)):
        print(f"\n\033[1m Item: \033[0m{shopping_list[i]} ",end='')
        if aisle:
            try:
                int(my_aisle[i])
                if int(my_aisle[i])<10: 
                    my_aisle[i]='0'+str(my_aisle[i])
                else:
                    aisle_filler=''
            except:
                    aisle_filler=''
            print(f"\033[1m Aisle:\033[0m {my_aisle[i]}",end='')
        if category:
            print(f"\033[1m  Category:\033[0m{my_category[i]}",end='')
        if estimate:
            print(f"\033[1m Price:\033[0m{my_estimate[i]}",end='')

    print(f"\nYou have total of {len(shopping_list)} items.")
    total=0
    
    if estimate:
        for i in range(len(my_estimate)):
            try:
                my_estimate[i]=float(my_estimate[i])
                total+=my_estimate[i]
            except:
                continue
        print(f"Your total shopping amount will be {total}")
print("Welcome to the shopping list app!") 
settings()
while True:
    my_task=input("What would you like to do?\n[A]dd, [R]emove, [P]rint List, [C]hange settings, [S]ort list, or [E]xit?").lower()
    if my_task=="a" or my_task=="add" or my_task=="add item":
        new_item()
    elif my_task=="r" or my_task=="remove" or my_task=="remove item":
        remove_item() 
    elif my_task=="p" or my_task=="print" or my_task=="print list":
        print_list()
    elif my_task=="c" or my_task=="change settings" or my_task=="settings" or my_task=="change":
        settings()  
    elif my_task=="e" or my_task=="exit":
        break  
    elif my_task=="s" or my_task=="sort" or my_task=="sort list":
        while True:
            my_sort_choice=input("How would you like to sort your list?\nPlease input your choice number:\n[1]Alphabetical - A to Z [2]Alphabetical - Z to A\n[3]By Aisle - Lower to Higher [4]By Aisle - Higher to Lower\n[5]By price - Lower to Higher [6]By price - Higher to Lower\n[7]By Category")
            try:
                int(my_sort_choice)
                if 0< int(my_sort_choice) <8:
                    break
                else:
                    print("Must be between 1 and 7")
            except:
                print("Please input a number between 1 and 7.")
        if my_sort_choice=="1": 
            sort_list("abc",shopping_list, my_aisle, my_estimate, my_category, True)
        elif my_sort_choice=="2": 
            sort_list("abc", shopping_list, my_aisle, my_estimate, my_category, False)
        elif my_sort_choice=="3": 
            sort_list("aisle", shopping_list, my_aisle, my_estimate, my_category, True)
        elif my_sort_choice=="4": 
            sort_list("aisle", shopping_list, my_aisle, my_estimate, my_category, False)
        elif my_sort_choice=="5": 
            sort_list("price", shopping_list, my_aisle, my_estimate, my_category, True)
        elif my_sort_choice=="6": 
            sort_list("price", shopping_list, my_aisle, my_estimate, my_category, False)
        elif my_sort_choice=="7": 
            sort_list("cat", shopping_list, my_aisle, my_estimate, my_category, True)
    else:
        print("Not a valid choice! Please choose from the list above!")
        

       
   

