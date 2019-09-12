# 1. Conditional Basics

# A. prompt the user for a day of the week, print out whether the day is Monday or not
today_is = input("Enter a day of the week")
ptiny(today_is)
today = "Thursday"
if today=="Thursday":
    print("It is almost the weekend.")
else:
    print("I am not sure what day it is.")

# B. prompt the user for a day of the week, print out whether the day is a weekday or a weekend
day = ("What is the day of the week?")
print(day)
day_of_the_week = "Sunday"
if day_of_the_week == "Thursday":
    print("It is a weekday.")
else:
    print("Maybe it is the weekend!")

# C. create variables and make up values for
## the number of hours worked in one week
## the hourly rate
## how much the week's paycheck will be
num_of_hours_worked = 40
hourly_rate = 25
weeks_paycheck = num_of_hours_worked * hourly_rate
print(weeks_paycheck)

# 2. Loop Basics

# A. While Loops
## Create an integer variable i with a value of 5.
## Create a while loop that runs so long as i is less than or equal to 15
## Each loop iteration, output the current value of i, then increment i by one.
i = 5
while i <= 15:
    print(i)
    i += 1

## Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.
i = 0
while i <= 100:
    print(i)
    i += 2

## Alter your loop to count backwards by 5's from 100 to -10
i = 100
while i >= -10:
    print(i)
    i -= 5

## Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000. Output should equal:
i = 2
while i < 100_000_000:
    print(i)
    i = i**2

## Write a loop that uses print to create the output shown below.
i = 100
while i > 5:
    print(i)
    i -= 5

# B. For Loops
## * Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number

num=int(num)
for num in range(1,11):
    print(num)

## Create a for loop that uses print to create the output shown below.
for num in range(1,10):
    print(str(num)*num)

# C. break and continue
## Prompt the user for an odd number between 1 and 50. Use a loop and a break statement to continue prompting the user if they enter invalid input. (Hint: use the isdigit method on strings to determine this). Use a loop and the continue statement to output all the odd numbers between 1 and 50, except for the number the user entered.
