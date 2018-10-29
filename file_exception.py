# file path: python looks for file in current path.
# we can use relative path
# or absolute path
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())

# read file line by line
file_name = 'pi_digits.txt'

with open(file_name) as obj:
    for line in obj:
        print(line.rstrip())

with open(file_name) as obj:
    lines = obj.readlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

number = input("Enter a int number: ")
if number in pi_string:
    print("The number appears in the digits of pi.")
else:
    print("The number does not appear.")


# Write file
# read mode: 'r', write mode: 'w', append mode: 'a', read/write mode: 'r+'
# when use 'w', if file is exist, file will be cleared
# also, python only write string to text file. if you want to save numeric,
# you must convert numeric to string via str().
filename = 'programming.txt'
with open(filename, 'w') as obj:
    obj.write("I love programming.\n")
    obj.write("I love creating new games.\n")
with open(filename, 'a') as obj:
    obj.write("I also love finding meaning in large datasets.\n")
    obj.write("I love creating apps that can run in a browser.\n")

# exception: try-except
# ZeroDivisionError exception
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

# try-except-else
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
        print("You can't divide by 0!")
    else:
        print(answer)

# FileNotFoundError exception    
def count_words(filename):
    """calculate a file's word numbers"""
    try:
        with open(filename) as fobj:
            contents = fobj.read()
    except FileNotFoundError:
        #msg = "Sorry, th file " + filename + " does not exist."
        #print(msg)
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) +
              " words.")
filenames = ['briand_book.txt', 'pi_digits.txt', 'alice.txt']
for filename in filenames:
    count_words(filename)
    
