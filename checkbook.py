# Welcome to my application!
print("~~ Welcome to your checkbook! ~~\n")

# How the user will be prompted
prompt = '> Your option: '

# menu options the user can pick from to proceed
def menu():
    print("How would you like to proceed?")
    print("""
    1) View current balance
    2) Make a withdrawl 
    3) Make a deposit 
    4) View savings  
    5) Exit\n""")

# opens and reads the checkbook text file balance
def read_balance():
    f = open("checkbook.txt", "r")
    bal = f.read()
    return bal

# opens and writes to the checkbook text file
def write_balance(new_balance):
    f = open("checkbook.txt", "w")
    f.write(str(new_balance))

# this function takes the read_balance function as current_balance and adds the deposit amount to it to create a new balance, then calls the write_balance(new_balance) function to display the new amount
def make_deposit(deposit_amount):
    current_amount = read_balance()
    new_balance = int(current_amount) + int(deposit_amount)
    write_balance(new_balance)

# this function takes the current_amount, (the read_balance()), and subtracts the withdraw_amount from it to to create a new balance, then calls the write_balance(new_balance) function to display the new amount
def make_withdraw(withdraw_amount):
    current_amount = read_balance()
    new_balance = int(current_amount) - int(withdraw_amount)
    write_balance(new_balance)

def read_savings():
    f = open("savings.txt", "r")
    balance = f.read()
    return balance

def write_savings(new_balance):
    f = open("savings.txt", "w")
    f.write(str(new_balance))

# this function calls the menu() function to prompt the user on how they wish to proceed. 
def main():
    menu()
    option = input(prompt)
    print("\n")

# if the user picks opt 1., it will display their current balance by calling the read_balance() function, then calls the main() function to continue.
    if option == "1":
        print("Your current balance is "+ read_balance())  
        print("\n")
        input("Press 'ENTER' to continue.")
        main()  

# if the user picks opt 2., it prompts user to enter withdraw amount, then calls the make_withdraw(withdraw_amount) function to perform the operation and prints the read_balance() to show new amount.
    elif option == "2":
        withdraw_amount = input("How much do you wish to withdraw?\n")
        
########## in order to get a comparisson for the number in the 'if' statement, I need to convert the str to a float        
        if int(read_balance()) > 0: 
            make_withdraw(withdraw_amount)
            print("Your new balance is " + read_balance())
            print("\n")
            input("Press 'ENTER' to continue.")
        else: 
            print("Insufficient funds. \n")
        

        main()

# if user picks opt 3., user is prompted to enter deposit amount then the make_deposit(deposit_amount) is called, then read_balance() function displays new balance after deposit
    elif option == "3":
        deposit_amount = input("How much to do you wish to deposit?\n")
        make_deposit(deposit_amount)
        print("Your new balance is " + read_balance())
        print("\n")
        input("Press 'ENTER' to continue.")
        main()

###
    elif option == "4":
        print("Your current balance is " + read_savings() + " in your savings.")
        print("\n")
        input("Press 'ENTER' to continue.")
        main()

# if user picks opt 4., prints exit string and exits the application
    elif option == "5":
        print("Thank you, have a great day!\n")

# if user picks option not listed, prints sorry statement the calls main() function to bring back to main menu and pick again.
    else:
        print("Sorry, that is an invalid option.\n")
        main()

main()





### things to do:
    # make amounts floats
    # transfer from checking to savings
    # negative balance

# print("How would you like to proceed?")
# print("""
# 1) View current balance
# 2) Make a withdrawl (record a debit)
# 3) Make a deposit (record a credit)
# 4) View savings account 
# 5) Exit\n""")
### transfer between accounts


# ~~~~~~~ Python checkbook project: ~~~~~~~~

# "~~ Welcome to your checkbook!~~"
# "How would you like to proceed?"

# 1. View current balance
# 2. Make a withdrawl (record a debit)
# 3. Make a deposit (record a credit)
# 4. View savings account (transfer to saving account option)
# 5. Exit

# > Your option: 
# # if option is invalid
# > Sorry, that option is invalid. Please (press "Enter" to) try again.
# > Your option:

# Option 1.
# Your current balance is $3,500

#     Would you like to make a withdrawl? [yes/no]

#     # if yes
#     Please enter amount you wish to withdraw:
#     # amount entered
#     Would you like to see your balance? [yes/no*]
#     Your current balance is $xxx
    
#     Would you like to make a withdrawl? [yes/no]
#     #if no
#     go to main menu
# How would you like to proceed?
# 1. View current balance
# 2. Make a withdrawl (record a debit)
# 3. Make a deposit (record a credit)
# 4. View savings account (transfer to saving account option)
# 5. Exit

#     #if no* go to main menu
#     How would you like to proceed?
#     1. View current balance
#     2. Make a withdrawl (record a debit)
#     3. Make a deposit (record a credit)
#     4. View savings account (transfer to saving account option)
#     5. Exit

# Option 2. 
# How much do you wish to withdraw?
# $xxx
# Would you like to see your balance? [yes/no]

# Option 3. 
# How much to do you wish to deposit?
# $xxx
# Would you like to see your current balance? [yes/no]

# # if yes
# show current balance

# Would you like to make a withdrawl? [yes/no]
# # yes make withdraw/no go to main menu

# # if no
# return to main menu

# Option 4.
# You have $xxx in your saving account.
# How would you like to proceed?
#     1. View current balance
#     2. Make a withdrawl (record a debit)
#     3. Make a deposit (record a credit)
#     4. View savings account 
#     5. Exit

# Option 5. 
# Thank you, have a great day!
# Exit