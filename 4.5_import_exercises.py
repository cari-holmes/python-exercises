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
# import json 

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

# Grand total of balances for all users
[profile['balance'] for profile in profiles]

# Average balance per user

# User with the lowest balance
min(profiles, key=lamda profile: handle_balance(profile['balance']))

# User with the highest balance

# Most common favorite fruit

# Least most common favorite fruit

# Total number of unread messages for all users
# .isdigit()

# .items() 