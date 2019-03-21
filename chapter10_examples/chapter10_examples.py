## Chapter about files and exceptions
with open('pi_digits.txt') as file_object: # The keyword with closes the file once access to it is no longer needed
    contents = file_object.read()
    line = contents.rstrip # rstrip prevents from printing a blank line

## "with open('text_files/filename.txt') as file_object:" if in a folder
print('\n')

## Absolute Paths:
# file_path = '/home/ehmatthes/other_files/text_files/filename.txt'
# with open(file_path) as file_object:

filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
    
pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))
print('\n')

filename = 'pi_million_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

## birthday = input("Enter your birthday, in the form mmddyy: ")
birthday = str(52597)
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")

## WRITING TO A FILE
filename = 'programming.txt'

with open(filename, 'w') as file_object: # You can open a file in read mode ('r'), write mode ('w'), 
                                         # append mode ('a'), or a mode that allows you to read and 
                                         # write to the file ('r+')
                                         # 'w' recreates the file everytime!
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")

## APPENDING TO A FILE

with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")

print('\n\n')
## EXCEPTIONS
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

print('\n')
    
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    except ValueError:
        print("Type a valid number")
    else:
        print(answer)
print('\n')

def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        # msg = "Sorry, the file " + filename + " does not exist."
        # print(msg)
        pass
    else: 
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")

filenames = ['alice.txt', 'siddhartha.txt', 'pi_digits.txt', 'programming.txt']
for filename in filenames:
    count_words(filename)

print('\n\n')
## STORING DATA
import json

numbers = [2, 3, 5, 7, 11, 13]
filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)

with open(filename, 'r') as f_obj:
    numbers = json.load(f_obj)
print(numbers)

print('\n')
import json

filename = 'username.json'
try: 
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError: 
    username = input("What is your name? ")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        print("We'll remember you when you come back, " + username + "!")
else:
    print("Welcome back, " + username + "!")