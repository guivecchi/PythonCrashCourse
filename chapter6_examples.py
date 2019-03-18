# Chapter about dictionaries
alien_0 = {'color': 'green', 'points': 5}  # Can be created empty
print(alien_0['color'])

# Can be use either to create a new key or to change the value of a key that already is in a dictionary
alien_0['color'] = 'blue'
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
print('\n\n')

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))
# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3
# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))
del alien_0['speed']  # Deletes a key
print(alien_0)

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
print("Sarah's favorite language is " +
      favorite_languages['sarah'].title() + ".")
print('\n\n')

# Looping through dictionaries
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

# Key vem antes do dois pontos, Value vem depois
for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)
print('\n')

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")
print('\n')

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print(" Hi " + name.title() +
              ", I see your favorite language is " +
              favorite_languages[name].title() + "!")
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

print('\n')

print("The following languages have been mentioned:")
# Set doesn't show duplicates and sorted sorts alphabetically
for language in sorted(set(favorite_languages.values())):
    print(language.title())
print('\n\n')

# A list of dictionaries
# Make an empty list for storing aliens.
aliens = []
# Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
# Show the first 5 aliens:
for alien in aliens[0:5]:
    print(alien)
print("...")
# Show how many aliens have been created.
print("Total number of aliens: " + str(len(aliens)))
print('\n\n')

# A list inside a Dictionary
# Store information about a pizza being ordered.
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],

}
# Summarize the order.
print("You ordered a " + pizza['crust'] + "-crust pizza " +
      "with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)

print('\n\n')

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}
for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())

print('\n\n')

# Dictionary in a dictionary
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())
