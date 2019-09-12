# Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.

def is_two(x):
    if x == int:
        return True
    elif x == str:
        return True
    else:
        return False
is_two(2)
is_two(1.52)


# Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.
def is_vowel(abc):
    for let in abc:
        if abc == ("a", "e", "i", "o", "u"):
            return True
        else:
            return False
is_vowel("g")

# Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.
def is_consonant(x):
    for let in x:
        if x != ("a", "e", "i", "o", "u"):
            return True
        else:
            return False
is_consonant("c")

# Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.
def is_word(word):
    for word in word:
        if word [0] != ("a", "e", "i", "o", "u"):
            return word.capitalize()
is_word("good morning")
is_word("atta boy")

# Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.
def calculate_tip:
    