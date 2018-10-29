for number in range(1,21):
    print(number)

# range()
numbers = list(range(1,1000001))
#for number in numbers:
#   print(number)

print(min(numbers))
print(max(numbers))
print(sum(numbers))

odds = list(range(1,20,2))
for odd in odds:
    print(odd)

multiples = list(range(3,30,3))
for multiple in multiples:
    print(multiple)

cubes = []
for cube in range(1,10):
    cubes.append(cube ** 3)
for cube in cubes:
    print(cube)

cubes = []
cubes = [cube**3 for cube in range(1,10)]
print(cubes)

# list slice
print(cubes[0:2])
print(cubes[1:4])
print(cubes[:5])
print(cubes[4:])
print(cubes[-3:])

# copy a list from cubes, they are two lists.
cubes_backup = cubes[:]

# a list variable point to cubes, only have one list.
cubes_backup = cubes

for cube in cubes[:]:
    print("number: " + str(cube))

