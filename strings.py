"""
Using string manipulation
Referenced lesson(s): 2 & 3
"""

# TODO: Section 1:
# Ask a user to input their full name and set it equal to a variable of "full_name".
# Greet the user by printing the statement "Hello _____, welcome to your personality quiz!"
# Make sure the comma comes directly after the "full_name" variable.
full_name = input("What is your full name; ")
print("Hello", full_name, "welcome to your personality quiz!")
####################################################################################################

# TODO: Section 2:
# Set a variable "classic" to equal "thE GREat GatSBy". Then use functions learned in this section
# to capitalize the first letter of each word, make all characters lowercase, and all characters
# uppercase. Set each of these variations equal to a variable. Print each variable on a different
# line.
classic = "thE GREat GatSby"
print(classic.title())
print(classic.upper())
print(classic.lower())
####################################################################################################

# TODO: Section 3:
# Write a program that asks a user 3 unique questions about them.
# The questions can be anything like your favorite movie, food, sport, etc.
food = input("What is your favorite food?")
sport = input("What is your favorite sport?")

# TODO: Section 3.1:
# After receiving all of the inputs, make a series of print statements that reflect the question.
# You should use f shorthand when inserting the variables into the strings. Your output should read
# like the following:

# "1. Your favorite movie is Avatar."
# "2. Your favorite food is pasta."
# "3. Your favorite sport is track."
print(f"Your favorite food is {food}")
print(f"Your favorite sport is {sport}")
####################################################################################################

# TODO: Section 4:
# It looks like the below list was meant to be one long string. Use what you learned in this
# section to join the items together. Set this to a new variable called 'phrase' and print it to
# check your output.
listy = ["This", "shouldn't be", "a list."]
phrase = " ".join(listy)
print(phrase)