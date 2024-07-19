aisle, category, estimate =False, False, False
shopping_list, my_aisle, my_category, my_estimate=[],[],[],[]

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
        
def remove_item():
        my_removed_item=input("List item to remove:").lower()
        my_removed_item=make_print_pretty(shopping_list,my_removed_item)
        if my_removed_item in shopping_list:
            my_removed_index= shopping_list.index(my_removed_item)
            shopping_list.pop(my_removed_index)
            my_aisle.pop(my_removed_index)
            my_category.pop(my_removed_index)
            my_estimate.pop(my_removed_index)
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
def print_list():
    global my_estimate
    make_print_pretty(shopping_list)
    make_print_pretty(my_category)
    for i in range(len(shopping_list)):
        print(f"\n\033[1m Item: \033[0m{shopping_list[i-1]} ",end='')
        if aisle:
            if type(my_aisle[i-1])==int:
                if int(my_aisle[i-1])<10: 
                    aisle_filler='0' 
                else:
                    aisle_filler=''
            else:
                    aisle_filler=''
            print(f"\033[1m Aisle:\033[0m{aisle_filler}{my_aisle[i-1]}",end='')
        if category:
            print(f"\033[1m  Category:\033[0m{my_category[i-1]}",end='')
        if estimate:
            print(f"\033[1m Price:\033[0m{my_estimate[i-1]}",end='')

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
    my_task=input("What would you like to do?\n[A]dd, [R]emove, [P]rint List, [C]hange settings, or [E]xit?").lower()
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
    else:
        print("Not a valid choice! Please choose from the list above!")
        

       
   

