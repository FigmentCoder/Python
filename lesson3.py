# Python Crash Course Lesson 3
# A list is a collection of items in a particular order

from py_linq import Enumerable

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

print(bicycles[0])

print(bicycles[0].title())

print(bicycles[1])
print(bicycles[3])

print("ult " + bicycles[-1]) # ult
print("pen ult " + bicycles[-2]) # pen ult
print("anti pen ult " + bicycles[-3]) # anti pen ult

# Experiment with Py LINQ
bicyclesP = Enumerable(bicycles).last().title()
print(bicyclesP)

message = f"My first bicyle was a {bicycles[0].title()}"
print(message)

message = f"My first bicyle was a {bicycles[0].title()}"
print(message)

# Experiment with Py LINQ
messageP = "My first bicycle was a " + Enumerable(bicycles).first().title()
print(messageP)

# Try it Yourself
# 3-1
names = ['Rene', 'Francis', 'Blaise']
print(names[0])
print(names[1])
print(names[2])
# Experimenting with loops
for n in names:
    print("name from loop" + n)

# 3-2
greeting = "Hello, "
print(greeting + names[0])
print(greeting + names[1])
print(greeting + names[2])
# Experimenting with loops
for n in names:
    print(greeting + "from loop " + n)

# 3-3
vehicles = ['Tesla X', 'Corolla Hybrid', 'Rav4 Prime']
for v in vehicles:
    print("I would like to own a", v)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# motorcycles[0] = 'ducati'
# print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)

motorcycles.insert(0, 'ducati')
print(motorcycles)

del(motorcycles[0])
print(motorcycles)

# motorcycles.clear()
# print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}")

first_owned =  motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is to expensive for me.")

print("\n")

# Try it Yourself
# 3-4
print("3-4")
dinner_guests = [
    'C.S. Lewis',
    'Rene Descartes',
    'Francis Bacon',
    'Jules Verne',
    'Blaise Pascal',
    'Alexandre Dumas']
print(dinner_guests)
for g in dinner_guests:
    print("Please come to dinner, " + g)

print("\n")
# 3-5
print("3-5")
guest_who_cannot_make_it = 'Francis Bacon'
dinner_guests.remove(guest_who_cannot_make_it)
print(guest_who_cannot_make_it + " can't make it to dinner he's on an affair of state for the King")
print("We'll invite Lucy Maud Montgonery instead ")
dinner_guests.append('Lucy Maud Montgomery')
print(dinner_guests)
print("\n")

# 3-6
print("3-6")
dinner_guests = [
    'C.S. Lewis',
    'Rene Descartes',
    'Francis Bacon',
    'Jules Verne',
    'Blaise Pascal',
    'Alexandre Dumas']
print(dinner_guests)
for g in dinner_guests:
    print("Good day, " + g + " I found a bigger table so I'm inviting more people")

dinner_guests.insert(0, 'Thomas Aquinas')
dinner_guests.insert(3, 'Dorothy Sayers')
dinner_guests.append('Immanuel Kant')
for g in dinner_guests:
    print("You are cordially invited to dinner, " + g)

print("\n")

# 3-7
print("3-7")
while len(dinner_guests) > 2:
    g = dinner_guests.pop()
    print("Dear, " + g+ " I'm sorry I can't invite you to dinner, my new table won't arrive on time, supply chain issues")

for g in dinner_guests:
    print(g + ", we'll still be having dinner, while there will be fewer of us in number, we'll have more food to eat :)")

print("\n")

cars = ['bwm', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

print("\n")

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

print("\n")
cars = ['bwm', 'audi', 'toyota', 'subaru']
print(len(cars))

# Try it Yourself
# 3-8
places = ['London', 'Paris', 'Athens', 'Sicily']
print(places)
print(sorted(places))
print(places)
print(sorted(places,reverse=True))
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse=True)
print(places)
# 3-9
print(len(dinner_guests))
# 3-10