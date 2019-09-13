# 1. Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.

def is_two(x):
    if x == int:
        return True
    elif x == str:
        return True
    else:
        return False
is_two(2)
is_two(1.52)


# 2. Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.
def is_vowel(abc):
    for abc in abc:
        if abc == ("a", "e", "i", "o", "u"):
            return True
        else:
            return False
is_vowel("g")

# 3. Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.
def is_consonant(x):
    if x != ("a", "e", "i", "o", "u"):
        return True
    else:
        return False
is_consonant("e")

# 4. Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.
def is_word(word):
    if word != ("a", "e", "i", "o", "u"):
        return word.capitalize()
is_word("good morning")
is_word("atta boy")
is_word("woah")

# 5. Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.
meal = 25
def calculate_tip(x):
    if x > 0 and x < 1:
        return meal * x 
calculate_tip(.18)

# 6. Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.
full_price = 32.00
def apply_discount(x):
    if x > 0 and x < 1:
        return full_price * x
apply_discount(.4)
apply_discount(.25)

full_price = 56
apply_discount(.3)

# 7. Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.
def handle_commas(x):
    ""

# 8. Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).
def get_letter_grade(x):
        if x >= 90:
            return "A"
        elif x >= 80:
            return "B"
        elif x >= 70:
            return "C"
        elif x >= 60:
            return "D"
        else:
            return "F"
get_letter_grade(90)
get_letter_grade(72)

# 9. Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.
def remove_vowels(x):
    vowels = ("a", "e", "i", "o", "u")
    for let in x:
        if x in vowels:
            return x.replace(x, "")


# # 10. Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
# anything that is not a valid python identifier should be removed
# leading and trailing whitespace should be removed
# everything should be lowercase
# spaces should be replaced with underscores
x = "Sally Kemper "
def normalize_name(x):
        return [x.lower().strip().replace(" ", "_") for x in x]
       
normalize_name(x)

# 11. Write a function named cumsum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
def cumsum(x):
   new_list = []
   for x in x:
       