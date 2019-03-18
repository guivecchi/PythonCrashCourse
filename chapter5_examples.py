# Chapter about if statements

cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':  # Two equal signs
        print(car.upper())
    else:
        print(car.title())

print('\n')

requested_topping = 'mushrooms'
if requested_topping != 'anchovies':  # Inequality sign
    print("Hold the anchovies!")

print('\n')

requested_toppings = ['mushrooms', 'onions', 'pineapple']
if 'mushrooms' in requested_toppings:
    print("Urgh!")
if 'parmesan' not in requested_toppings:
    print("You should add Parmesan!")

print('\n')

age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
elif age < 18 and age >= 16:
    print("You'll be able to vote soon!")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

print('\n')

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print("Adding " + requested_topping + ".")
print("\nFinished making your pizza!")

print('\n')
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

print('\n')

available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")
print("\nFinished making your pizza!")
