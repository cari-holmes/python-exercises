print("~~ Welcome to your checkbook! ~~\n")


prompt = '> Your option: '


def menu():
    print("How would you like to proceed?")
    print("""
    1) View current balance
    2) Make a withdrawl (record a debit)
    3) Make a deposit (record a credit)
    4) View savings account 
    5) Exit\n""")


def read_balance():
    f = open("checkbook.txt", "r")
    bal = f.read()
    return bal

def write_balance(new_balance):
    f = open("checkbook.txt", "w")
    f.write(str(new_balance))

def make_deposit(funds):
    current_amount = read_balance()
    new_balance = int(current_amount) + int(funds)
    write_balance(new_balance)

def make_withdraw(withdraw_amount):
    current_amount = read_balance()
    new_balance = int(current_amount) - int(withdraw_amount)
    write_balance(new_balance)

def main():
    menu()
    option = input(prompt)
    if option == "1":
        print("Your current balance is "+ read_balance())  
        input("Press 'Enter' to continue")
        main()  
    elif option == "2":
        withdraw_amount = input("How much do you wish to withdraw?\n")
        make_withdraw(withdraw_amount)
        print("Your new Balance is " + read_balance())
        # prompt user yes or no
    elif option == "3":
        deposit_amount = input("How much to do you wish to deposit?\n")
        make_deposit(deposit_amount)
        print("The new balance is " + read_balance())
    elif option == "4":
        print("You have $500 in your saving account.\n")
    elif option == "5":
        print("Thank you, have a great day!\n")
    else:
        print("Sorry, that is an invalid option.\n")

main()


# print("How would you like to proceed?")
# print("""
# 1) View current balance
# 2) Make a withdrawl (record a debit)
# 3) Make a deposit (record a credit)
# 4) View savings account 
# 5) Exit\n""")
### transfer between accounts

### loop to stay on menu unless I exit application
### how to add prompts after the if statement
### 

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