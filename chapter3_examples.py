# Chapter about lists

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])
print(bicycles[-1] + "\n")  # Get the last element in a list

# Appending
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati')
print(motorcycles)

# Inserting in a determined position
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(1, 'ducati')
print(motorcycles)

# Removing an item
motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[0]
print(motorcycles)
print("\n\n")

# Using pop
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
# Pop can be used in any position. Ex: motorcycles.pop(0)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
print("\n")

# If the position is not known, we can remove an item by value
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
# we could use a variable such as italian_bike = 'ducati'
motorcycles.remove('ducati')
print(motorcycles)
# Remove deletes only the first ocurrence
print('\n')

# Organizing a list
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()  # Sorts alphabetically
print(cars)
cars.sort(reverse=True)
print(cars)
print('\n')

cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("Here is the sorted list:")
print(sorted(cars))  # Doesn't modify the list

cars.reverse()  # Invert the list

print(len(cars))  # Get the length of the list
