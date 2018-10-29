# JSON module
import json

numbers = [2,3,5,8,90,34]

filename = 'numbers.json'
with open(filename, 'w') as fobj:
    json.dump(numbers, fobj)

with open(filename) as fobj:
    numbers2 = json.load(fobj)
print(numbers2)

# reconstruction ...

