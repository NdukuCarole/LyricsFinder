
import sys
from lyrics import searchsong
from songdatabase import select_data




#prompt main menu
def menu(): 
    print()
choice = input('''
                    1:search \n
                    2:View saved songs\n
                    3:exit\n
                    
                    please enter your choice\n''')

if choice == "1":

#prompt second menu from the search option
        print()
        choice = input('''
                    1:search lyrics \n
                    2.show saved songs\n
                    3:Back\n
                    4:exit\n
                    
                    please enter your choice\n''') 


        if choice == "1":
                searchsong()
                


#prompt a menu from the search album choice
        elif choice == "2":
           select_data() 
#exit the menu
        elif choice == "3":
#the main menu will be displayed 
            menu()  
        elif choice == "4":
# this sub menu program is terminated
            sys.exit



elif choice == "2":
        sys.exit

elif choice == "3":
        sys.exit

#if no option is selected from the main menu
else:
        print("You must select an option")
print()
menu()