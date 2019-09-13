# 1. Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.

def is_two(x):
    if x == 2 or x == "2":
        return True
    else:
        return False
is_two(2)
is_two(1.52)

assert is_two(2) == True
assert is_two("2") == True
assert is_two(two) == True

# 2. Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.
def is_vowel(abc):
    vowels = ["a", "e", "i", "o", "u"]
    return abc in vowels

is_vowel("b")

assert is_vowel("a") == True
assert is_vowel("e") == True
assert is_vowel("i") == True
assert is_vowel("o") == True
assert is_vowel("u") == True

# 3. Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.
def is_consonant(x):
    return not is_vowel(x)
is_consonant("c")

# 4. Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.
def is_word(word):
    if word != ("a", "e", "i", "o", "u"):
        return word.capitalize()
is_word("good morning")
is_word("atta boy")
is_word("woah")

# def cap_con(word):
#     if cap_con(word[0]):
#         return word.capitalize()
#     return word
# cap_con(cat)

# 5. Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.
def calculate_tip(percentage, bill):
    amount_tip = percentage * bill
    return amount_tip

assert calculate_tip(.2, 20) == 4.0

# meal = 25
# def calculate_tip(x):
#     if x > 0 and x < 1:
#         return meal * x 
# calculate_tip(.18)

# 6. Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.
def apply_discount(org_price,discount_price):
    discount_amount = org_price * discount_price
    return org_price - discount_price

# full_price = 32.00
# def apply_discount(x):
#     if x > 0 and x < 1:
#         return full_price * x
# apply_discount(.4)
# apply_discount(.25)

# full_price = 56
# apply_discount(.3)

# 7. Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.
def handle_commas(x):
    x = x.replace(',', '')
    return float(x)
handle_commas('4,000,000')

# assert handle_commas('1,000') == 1000.00
# assert handle_commas('100') == 100.00
# assert handle_commas('1,000,000') == 1000000

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
def remove_spec_chars(s):
    for c in ['$', '%', '@']:
        return c

def normalize_name(s):
    return remove_spec_char(s).lower().strip().replace(" ", "_")

# def normalize_name(x):
#         return " ".join([x.lower().strip().replace(" ", "_") for x in x])
       
# normalize_name(x)

# 11. Write a function named cumsum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
def cumsum(x):
    sum = [x[0]]
    for sum in x[1:]:
        sum.append(sum[-1]+x)
    return sum
cumsum([1, 1, 1])

# def cumsum(x):
#     list = []
#     list = [sum(list(i + 1)) for x in range(0, len(list))]
#     return x.append(list)
    
# cumsum([1, 2, 3])