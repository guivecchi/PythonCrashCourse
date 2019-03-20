# Chapter about functions
def greet_user(username):
    """Display a simple greeting."""
    print("Hello, " + username.title() + "!")

user = 'Jesse'
greet_user(user)

print('\n')

def describe_pet(pet_name, animal_type='dog'): # Dog is the default value (default values have to be the last arguments)
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet(pet_name='harry', animal_type='hamster') # Avoids confusion and order doesn't matter
describe_pet('willie', 'cat') # Order matters
describe_pet(pet_name = 'rex') # Or only 'rex'

print('\n\n')

# Returning a value
def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

print('\n')

def build_person(first_name, last_name, age=''):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', 27)
print(musician)
print('\n')

# Passing a list to a function
def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames) # greet_user(usernames[:]) would pass a copy (non-editable) version of the list

print('\n\n')
# Passing an arbitrary number of arguments
def make_pizza(size, *toppings): # * creates an empty tuple
    """Print the list of toppings that have been requested."""
    print("\n" + str(size)) 
    print(toppings)

make_pizza(12, 'pepperoni')
make_pizza(16, 'mushrooms', 'green peppers', 'extra cheese')

print('\n')
# Using Arbitrary Keyword Arguments
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)

## Importing functions can be found on page 188.
## Basically import name imports all functions from name.py
## import last_name from name.py as ln imports only one function and gives it an alias (ln). 
## Alias can be used when importing a module (file with many functions)
## The function can be used as name.first_name
## from pizza import * imports all functions from pizza module