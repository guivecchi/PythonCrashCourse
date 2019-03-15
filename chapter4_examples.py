# Chapter about Working with Lists
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")

print("\n")

for value in range(1, 5):  # Doesn't loop in the last one
    print(value)

print('\n')

even_numbers = list(range(2, 11, 2))
print(even_numbers)

print('\n')

squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)
print(min(squares))
print(max(squares))
print(sum(squares))

print("\n")

# List comprehension: how to create a list more concisely
squares = [value**2 for value in range(1, 11)]
print(squares[:4])

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[3:]:
    print(player.title())

# Copying a list
# friends_foods = my_foods[:] - friends_foods gets the same value but is a different list
# friends_foods = my_foods - friends_foods becomes a pointer to my_foods
print('\n\n')

# TUPLES = immutable lists - parenthesis instead of brackets
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# dimensios[0] = 250 throws a error. Correction is redefining the tuple: dimensions = (250,50)
