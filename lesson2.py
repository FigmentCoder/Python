# Python Crash Course Lesson 2
# I used the # character used to make comments in code to label each exercise I did
# as well as make notes and write down definitions.  This way I've got everything for Lesson in one place

# Variables are labels that you can assign to values

#1
print("Hello Python world!")

#2
message = "Hello Python world!"
print(message)

#3
message = "Hello Python Crash Course world!"
print(message)

# The # symbol is used for a comment.  If you would like to comment out lines of code as you do the exercises
# because you start to get too many outputs in the terminal to keep track of you can place a # before lines in
# your code file, like so
# message = "Hello Python Crash Course world!"
# print(message)

# Try it Yourself
# 2-1
simple = "I like the simplicty of python"
print(simple)
# 2-2
raven = "How is a raven like a writing desk?"
print(raven)
raven = "They both produce flat notes"
print(raven)

# A string is a series of characters.  Anything inside quotes is considered a string in Python

# The method title() appears after the variable in the print() call.  
# A method is an action that Python an perform on a piece of data
#4
name = "ada lovelace"
print(name.title())

# Upper and lower case methods on the name variable
#5
name = "Ada Lovelace"
print(name.upper())
print(name.lower())

# These strings are called f-strings.  The f is for format, because Python formats 
# the string by replacing the name of any variable in braces with its value
#6
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)

#7
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")

#8 
# Me experimenting to see if I can use + to combine strings without using f and it looks like I can
# + is often used in many programming to combine string values.  It's not just for performing addition.
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print("Hello, " + full_name.title() + "!")

# In programming, whitespace refers to any nonprinting characters, such as spaces, tabs, and end-of-line symbols
# 9
print("Python")

print("\tPython")

print("Languages:\nPython\nC\nJavascript")

print("Languages:\n\tPython\n\tC\n\tJavaScript")

#10
favorite_language ='python '
favorite_language.rstrip()
favorite_language.lstrip()

#11
nostarch_url = 'https://nostarch.com'
nostarch_url.removeprefix('https://')

# A syntax error occurs when Python doesn't recgnize a section of your program as valid Python code
message = "One of Python's strengths is its diverse community."
print(message)

# Commented out because to use a single quote for this string is a syntax error and the program won't run any more :(
# message = 'One of Python's strengths is its diverse community.'
# print(message)

# Try it Yourself
# 2-3
name = "Michael"
print("Greetings, " + name + "Would you like to play a game?")
print("Sure, how about global thermal nuclear war?")

#2-4
print(name.lower())
print(name.upper())
print(name.title())

#2-5
print("Sir Francis Bacon once said, "+ '"Suspicions amongst thoughts are like bats amongst birds they ever fly by twilight."')

#2-6
famous_person = "Sir Francis Bacon"
print(famous_person + " once said, " + '"Suspicions amongst thoughts are like bats amongst birds they ever fly by twilight."')

#2-7
name = " \tLeibnez\n ".strip()
print(name)

#2-8
filename = "python_notes.txt".removesuffix(".txt")
print(filename)

# Numbers
print(2 + 3)
print(3 - 2)
print(2 * 3)
print(3 / 2)

print(3 ** 2)
print(3 ** 3)
print( 10 ** 6)

print(2 + 3*4)
print((2+3) * 4)

print(.1 + .1)
print(.2 + .2)
print(2 * .1)
print(2 * .2)

print(0.2 + .1)
print(2 * .2)

print(4/2)
print(1 + 2.0)
print(2 * 3.0)
print(3.0 ** 2)

# When you're writing long numbers, you can group digits using underscores to make large numbers more readable
universe_age = 14_000_000_000
print(universe_age)

x,y,z = 0,0,0
print(x,y,z)

# A constant is a variable whose value stays the same through out the lifecycle of the program
# Constants are written in all capital letters by convention in Python
MAX_CONNECTIONS = 5000

# Try it Yourself
# 2-9
print(4+4)
print(12-4)
print(2*4)
print(2**3)

# 2-10
favorite_number = 14
print(favorite_number)

print(3 ** 3)

# A note on comments.  Comments can be controversial.  When you are beginning to program comments are helpful, because they help you
# remember what you're writing in code.  However, when you're past the learning phase and are writing programs
# I recommend you only write comments if the code itself is unclear as to what it's doing.  But if you find yourself writing code
# that is unclear in what it's doing, then you should really consider re-writing it.  The code should explain itself
# In large solutions I've worked on when there are thousands and hundreds of thousands of lines of code you'll find few comments
# If you're working with larger solutions and you have comments everywhere then you have to switch language contexts between
# English and the programming language you're writing in.  My advice write good code that explains itself and use comments sparingly

# I agree with all of the zen of Python points except one
# There should be only one-- and preferably only one -- obvious way to do it
# I will ammend this to read, There are perhaps 2-3 obvious ways to solve a given problem
# I'm hesitant to make such over arching and absolute statements as the author did when it comes to modeling problems and solutions in code.