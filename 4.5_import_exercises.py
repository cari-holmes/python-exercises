# 1. Import and test 3 of the functions from your functions exercise file.

import function_exercises as fe
fe.get_letter_grade(84)
fe.get_letter_grade(91)

from function_exercises import is_two 
is_two(2)
is_two(3)

from function_exercises import is_consonant as con
con("a")
con("b")

# 1. How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?
import itertools as it
it.product('abc', '123')

# 2. How many different ways can you combine two of the letters from "abcd"?
import itertools as it
it.combinations('abc, '123')

## profiles.json ##

# importing just the function needed from json module
# printing "ok" to test the import went through
from json import load
print("ok")
# importing the entire json module
import json 

# to read the file I saved in order to work with it
with open('profiles.json', 'r' ) as file:
    profiles = json.load(file)
# can leave the 'r' off, is a default value to open()
print("ok")
type(profiles)
# it is all wrapped up in a list
type(profiles[0])
print(profiles[0])

#Total number of users
len(profiles)

# Number of active users
[profile['isActive'] for profile in profiles ]
# or
active_users = [profile for profile in profiles if profile['isActive']]
n_active_users = len(active_users)
n_active_users

# Number of inactive users
inactive_users = [profile for profile in profiles if profile['isActive'] == False]
n_inactive_users = len(inactive_users)
n_inactive_users
# or
[profile['isActive'] == False for profile in profiles]


# Grand total of balances for all users
type('balance')
[profile['balance'] for profile in profiles]

def change_balance_type(b):
    return float(b[1:].replace(",", ""))

balance = [change_balance_type(profile['balance']) for profile in profiles]
bal = sum(balance)
bal

# Average balance per user
average = sum(balance) / len(balance)
average

# User with the lowest balance
lowest_balance_user = profiles[0]
for user in profiles [1:]:
    if change_balance_type(user['balance']) < change_balance_type(lowest_balance_user['balance']):
        lowest_balance_user = user
lowest_balance_user

### min([profiles, key=lamda profiles: change_balance_type(profile['balance'])])

# User with the highest balance
highest_balance_user = profiles[0]
for user in profiles [1:]:
    if change_balance_type(user['balance']) > change_balance_type(highest_balance_user['balance']):
        highest_balance_user = user
highest_balance_user

# Most common favorite fruit
from collections import Counter
print('ok')
# Counter is capitalized, keeps track of how many times an item is counted
Counter(profile['favoriteFruit'] for profile in profiles)

# or 

fruit_count = {}
for profile in profiles:
    fruit = profile['favoriteFruit']
    if fruit in fruit_count:
        fruit_count[fruit] += 1
    else: 
        fruit_count[fruit] = 1
fruit_count

max(fruit_count)
# Least most common favorite fruit

min(fruit_count)

# Total number of unread messages for all users
# .isdigit() prints True if all characters are digits
# .items() 
type(greeting)
greeting = [profile['greeting'] for profile in profiles]
def pull_digit(string):
    return int(''.join([char for char in string if char.isdigit()]))
num_unread_messages = [pull_digit(greeting) for greeting in greeting]
num_unread_messages
sum(num_unread_messages)
