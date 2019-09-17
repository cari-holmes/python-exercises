print("~~ Welcome to your checkbook! ~~\n")

prompt = '> Your option: '

### 

print("How would you like to proceed?")
print("""
1) View current balance
2) Make a withdrawl (record a debit)
3) Make a deposit (record a credit)
4) View savings account 
5) Exit\n""")

### add in function of how to proceed between each if statement

option = input(prompt)
if option == "1":
    print("Your current balance is $3,500\n")
elif option == "2":
    print("How much do you wish to withdraw?\n")
    # prompt user yes or no
elif option == "3":
    print("How much to do you wish to deposit?\n")
elif option == "4":
    print("You have $500 in your saving account.\n")
elif option == "5":
    print("Thank you, have a great day!\n")
else:
    print("Sorry, that is an invalid option.\n")

# pick an option 1 thru 5
# i need to make a loop to go back to main menu after each prompt response

# print("How would you like to proceed?")
# print("""
# 1) View current balance
# 2) Make a withdrawl (record a debit)
# 3) Make a deposit (record a credit)
# 4) View savings account 
# 5) Exit\n""")

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