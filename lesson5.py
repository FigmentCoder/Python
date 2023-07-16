cars = ['audi','bmw','subaru','toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# At the heart of every if statement is an expression that can be evaluated as 
# True or False and is called a conditional test.      

car = 'audi'
print(car == 'bmw')

car = 'Audi'
print(car.lower() == 'audi')

requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")

age = 18
print(age == 18)

answer = 17
if answer != 42:
    print("That is not the correct answer.  Please try again!")

age = 19
print (age < 21)
print(age <= 21)
print(age > 21)
print(age >= 21)

age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)

age_1 = 22
print(age_0 >= 21 and age_1 >= 21)

requested_toppings = ['mushrooms','onions','pineapple']
print('mushrooms' in requested_toppings)
print('pepperoni' in requested_toppings)

banned_users = ['andrew','carolina','david']
user = 'marie'
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")

game_active = True
can_edit = False

# Try It Yourself
# 5-1
book = "Discourse on Method"
print("Is the book == 'Discourse on Method'? I predict true.")
print(book == 'Discourse on Method')

book = "Discourse on Method"
print("Is the book == " + book  + " I predict true.")
print(book == 'Discourse on Method')

print("Is the book == 'Alice in Wonderland'? I predict false.")
print(book == 'Alice in Wonderland')
# 5-2
print("Is (2+2) == 5, some people think so, I do not, I predict false")
print((2+2) == 5)

print("Is the book " + book + " == " + book.lower() + " I predict false")
print(book == book.lower())

print("Is 6 > 3?, I predict true")
print(6 > 3)

# And
print("In propositional logic I predict False and False is False")
print(False and False)

print("In propositional logic I predict False and True is False")
print(False and True)

print("In propositional logic I predict True and False is False")
print(True and False)

print("In propositional logic I predict True and True is True")
print(True and True)

# Inclusive Or
print("In propositional logic I predict False or False is False")
print(False or False)

print("In propositional logic I predict False or True is True")
print(False or True)

print("In propositional logic I predict True or False is True")
print(True or False)

print("In propositional logic I predict True or True is True")
print(True or True)

# Exclusive Or, it's unfortunate that in Python the ^ symbol is used as this is used for 'and' in Mathematics and Philosophy
print("In propositional logic I predict False ^ False is False")
print(False ^ False)

print("In propositional logic I predict False ^ True is True")
print(False ^ True)

print("In propositional logic I predict True ^ False is True")
print(True ^ False)

print("In propositional logic I predict True ^ True is False")
print(True ^ True)

age = 19
if age > 18:
    print("You are old enough to vote!")

age = 19
if age > 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")

age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

age = 12
if age < 4:
    print("Your admits cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")

age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40
print(f"Your admission cost is ${price}.")

age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20
print(f"Your admission cost is ${price}.")

age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20
print(f"Your admission cost is ${price}.")
# With this change, 
# every block of code must pass a specific test in order to be executed.

requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("adding extra cheese.")

# 5-3
alien_color = 'green'
if alien_color == 'green':
    print("The alien's color is green, you just earned 5 points")

alien_color = 'red'
if alien_color == 'green':
    print("The alien's color is green, you just earned 5 points")
# 5-4
alien_color = 'red'
if alien_color == 'green':
    print("The alien's color is green, you just earned 5 points")
else:
    print("The alien's color is not green, you just earned 10 points")
# 5-5
alien_color = 'green'
if alien_color == 'green':
    print("The alien's color is green, you just earned 5 points")
elif alien_color =='yellow':
    print("The alien's color is yellow, you just earned 10 points")
elif alien_color =='red':
    print("The alien's color is red, you just earned 15 points")

alien_color = 'yellow'
if alien_color == 'green':
    print("The alien's color is green, you just earned 5 points")
elif alien_color =='yellow':
    print("The alien's color is yellow, you just earned 10 points")
elif alien_color =='red':
    print("The alien's color is red, you just earned 15 points")

alien_color = 'red'
if alien_color == 'green':
    print("The alien's color is green, you just earned 5 points")
elif alien_color =='yellow':
    print("The alien's color is yellow, you just earned 10 points")
elif alien_color =='red':
    print("The alien's color is red, you just earned 15 points")

# 5-6
age = 64
if age < 2:
    print("Person is a baby")
elif age == 2 or age < 4: # >= 2 and age < 4
    print("Person is a toddler")
elif age == 4 or age < 13: # >= 4 and age < 13
    print("Person is a kid")
elif age == 13 or age < 20: # >= 13 and age < 13
    print("Person is a teenager")
elif age == 20 or age < 65: # >= 20 and age < 65
    print("Person is an adult")
elif age >= 65:
    print("Person is an edler")
# 5-7
favorite_fruits = ['apple','pear','tomato','avacado','black berry']

if 'apple' in favorite_fruits:
    print("apple is one of my favorite fruits!")
if 'pear' in favorite_fruits:
    print("pear is one of my favorite fruits!")
if 'tomato' in favorite_fruits:
    print("tomato is one of my favorite fruits!")
if 'avacado' in favorite_fruits:
    print("avacado is one of my favorite fruits!")
if 'black berry' in favorite_fruits:
    print("black berry is one of my favorite fruits!")

requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
        print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")
print("\nFinished making your pizza!")

# 5-8
user_names = ['rene','francis','clive','admin','blaise']
for user_name in user_names:
    if user_name == 'admin':
        print("Good day, " + user_name + " Would you like to see a status report?")
    else:
        print("Salutations, " + user_name + " Thank you for logging in again")

user_names = []
if not user_names:
    print("We need to find some users!")

user_names = []
if len(user_names) == 0:
    print("We need to find some users!")

# 5-10

# 5-11