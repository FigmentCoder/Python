# Python Crash Course Lesson 4

# For every magician in the list of magicians print magician
magicians = ['alice', 'david','carolina']
for magician in magicians:
    print(magician)

for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")

for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
print("Thank you, everyone.  That was a great magic show!")

# Python uses indentation to determine how a line, or group of lines, is related 
# to the rest of the program

# This is a logical error. The syntax is valid Python code, but the code does 
# not produce the desired result because a problem occurs in its logic
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
print(f"I can't wait to see your next trick, {magician.title()}.\n")

# The colon at the end of a for statement tells Python to interpret the next 
# line as the start of a loop.

# Try it Yourself
# 4-1
pizzas = ['St. Louis', 'Neopolitan', 'Roma', 'Chicago']
for pizza in pizzas:
    print("I like to eat " + pizza + " style pizzas")

animals = ['Dog', 'Cat', 'Fish']
for animal in animals:
    print(animal)

for animal in animals:
    print("A " +  animal + " would make a great pet")

for animal in animals:
    print("A " +  animal + " would make a great pet")
print("All of these animals make great pets")

for value in range(1, 5):
    print(value)

numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2, 11, 2))
print(even_numbers)

squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)
print(squares)

digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))

# https://realpython.com/list-comprehension-python/
# https://www.w3schools.com/python/python_lists_comprehension.asp
# To use this syntax, begin with a descriptive name for the list, such as 
# squares. Next, open a set of square brackets and define the expression for 
# the values you want to store in the new list. In this example the expression is 
# value**2, which raises the value to the second power. Then, write a for loop 
# to generate the numbers you want to feed into the expression, and close the 
# square brackets.

squaresP = [square ** 2 for square in range(1,11)]
print(squaresP)

# Try It Yourself
# 4-3
numbers = list(range(1,21))
for number in numbers:
    print(number)

# numbers = list(range(1,1_000_001))
# for number in numbers:
#    print(number)

# 4-4
numbers = list(range(1,1_000_001))
print(min(numbers))
print(max(numbers))

# 4-5
print(sum(numbers))

# 4-6
odd_numbers = list(range(1, 20, 2))
for odd_number in odd_numbers:
    print(odd_number)

# 4-7
multiples_of_three = list(range(0,31,3))
for multiple in multiples_of_three:
    print(multiple)

# 4-8
cubes = []
for number in range(1, 11):
    cube = number**3
    cubes.append(cube)
for cube in cubes:
    print(cube)

print("4-8 / 4-9")
cubes = [cube ** 3 for cube in range(1,11)]
for cube in cubes:
    print(cube)

players = ['charles','martina','michael','florence','eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[:2])
print(players[:-3])

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

my_foods = ['pizza','fakafekm','carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

my_foods.append('cannoli')
friend_foods.append('ice cream')

print(my_foods)
print(friend_foods)

# This doesn't work:
# Instead of assigning a copy of my_foods to friend_foods, we set friend_foods equal to my_foods. 
friend_foods = my_foods

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

# Try it yourself
# 4-10
# 4-11
# 4-12

# Python refers to values that cannot change as 
# immutable, and an immutable list is called a tuple.

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

singleton = (3,)
print(singleton)

# It doesn’t often make sense to build a tuple with one element, but this can happen 
# when tuples are generated automatically.

# I'm not sure completely agree with this statement, based on my experience with other languages
# Perhpas there is a more Python way to do things, but I can think of perhaps one use case
# This is a case well beyond our introduction to Python, but If i were to mode a type Option
# that models the presence or non presence of an item, I might use an empty tuple to model the none presence
# and a tuple with one element to model the presence of an item.  Again this is advanced use case
# there may be some more appropriate way in Python I'm not aware of yet.

for dimension in dimensions:
    print(dimension)

print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400,100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

# Try it yourself
# 4-13

# Try it yourself
# 4-14
# 4-15