### 1. Conditional Basics
# A. prompt the user for a day of the week, print out whether the day is Monday or not
today_is = input("Enter a day of the week")

today = "Thursday"
if today=="Thursday":
    print("It is almost the weekend.")
else:
    print("I am not sure what day it is.")

# B. prompt the user for a day of the week, print out whether the day is a weekday or a weekend
day = input("What is the day of the week?")

day_of_the_week = "Sunday"
if day_of_the_week == "Thursday":
    print("It is a weekday.")
else:
    print("Maybe it is the weekend!")

# C. create variables and make up values for
'''the number of hours worked in one week
the hourly rate
how much the week's paycheck will be'''

num_of_hours_worked = 40
hourly_rate = 25
weeks_paycheck = num_of_hours_worked * hourly_rate
print(weeks_paycheck)

### 2. Loop Basics
# A. While Loops
'''Create an integer variable i with a value of 5.
Create a while loop that runs so long as i is less than or equal to 15
Each loop iteration, output the current value of i, then increment i by one.'''

i = 5
while i <= 15:
    print(i)
    i += 1

# Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.
i = 0
while i <= 100:
    print(i)
    i += 2

# Alter your loop to count backwards by 5's from 100 to -10
i = 100
while i >= -10:
    print(i)
    i -= 5

# Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000. Output should equal:
i = 2
while i < 100_000_000:
    print(i)
    i = i**2

# Write a loop that uses print to create the output shown below.
i = 100
while i > 5:
    print(i)
    i -= 5

# B. For Loops
# Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number
num = input('enter a number')
num=int(num)
for num in range(1,11):
    print(print(str(i)+"*"+str(num)+"="+str(i*num))

# Create a for loop that uses print to create the output shown below.
for num in range(1,10):
    print(str(num)*num)

# C. break and continue
# Prompt the user for an odd number between 1 and 50. Use a loop and a break statement to continue prompting the user if they enter invalid input. (Hint: use the isdigit method on strings to determine this). Use a loop and the continue statement to output all the odd numbers between 1 and 50, except for the number the user entered.
odd_number = ""
while True:
    if odd_number.isdigit() and int(odd_number) %2==0 and int(odd_number) > 1 and int(odd_number) < 50:
        break

# D. The input function can be used to prompt for input and use that input in your python code. Prompt the user to enter a positive number and write a loop that counts from 0 to that number. (Hints: first make sure that the value the user entered is a valid number, also note that the input function returns a string, so you'll need to convert this to a numeric type.)
positive_num = ""
while True:
    if positive_num.isdigit() and int(positive_number) > 0:
        break

for i in range(int(positive_number)+1):
    print(i)
    
# E. Write a program that prompts the user for a positive integer. Next write a loop that prints out the numbers from the number the user entered down to 1.
my_num = ""
while True:
    if my_num.isdigit() and int(my_num) > 0:
        break
for i in range(int(my_num), 0, -1):
    print(i)

### 3. Fizzbuzz
## One of the most common interview questions for entry-level programmers is the FizzBuzz test. Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills.
""" Write a program that prints the numbers from 1 to 100.
For multiples of three print "Fizz" instead of the number
For the multiples of five print "Buzz".
For numbers which are multiples of both three and five print "FizzBuzz".
"""

for x in range(1, 101):
    if x % 3 == 0 and x % 5 == 0:
        print('FizzBuzz')
    elif x % 5 == 0:
        print('Buzz')
    elif x % 3 == 0: 
        print('Fizz')
    else:
        print(str(x))

### 4. Display a table of powers.
'''Prompt the user to enter an integer.
Display a table of squares and cubes from 1 to the value entered.
Ask if the user wants to continue.
Assume that the user will enter valid data.
Only continue if the user agrees to.'''

while True:
    num_test=int(input("Please enter an integer"))
    for i in range(1,num_test+1):
        if i==1:
            print('number  | squared  | cubed')
            print('__  |  __  |  __')
    print(i,'  |', i**2,'  |',i**3)
    user_choice=input("Should we continue ?")
    if user_choice=="no":
        break
