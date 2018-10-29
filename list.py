names = ['alen', 'bambo', 'tom', 'jeans']
print(names[0])
print(names[-1].title())

print(names[1].title() + ": welcome to here.")

names = []
names.append("json")
names.append("wolf")
print(names)
names[0] = "star"
print(names)
names.insert(0, "json")
print(names)

# append() insert() del
del names[2]
print(names)

# pop()
popped_name = names.pop()
print(names)
print(popped_name)

# list pop(0)
names = ['tim', 'jane', 'kom']
print(names)
print(names.pop(1))
print(names)

# Use remove() if you only know value of element
# remove() just remove the first value matched in a list
# we must loop to remove it if want to remove all the same element of a list
names.remove('kom')
print(names)

names.remove("tim")
print(names)

# practices
client_list = ['robin', 'jone', 'july']
print("I will invote " + client_list[0].title() + ", " + client_list[1].title()
      + "and " + client_list[2].title() + " to join dinner.")
print("But, " + client_list[0].title() + " can't come.")
client_list[0] = 'bob'
print("I will invote " + client_list[0].title() + ", " + client_list[1].title()
      + " and " + client_list[2].title() + " to join dinner.")

print("I find a bigger dinner table, so i want to invote more people to come")
client_list.insert(0, 'jeans')
client_list.insert(2, 'rose')
client_list.append("Tom")
print(client_list[0].title() + ", i'am glad to invote you to join dinner.")      
print(client_list[1].title() + ", i'am glad to invote you to join dinner.")
print(client_list[2].title() + ", i'am glad to invote you to join dinner.")
print(client_list[3].title() + ", i'am glad to invote you to join dinner.")
print(client_list[4].title() + ", i'am glad to invote you to join dinner.")
print(client_list[5].title() + ", i'am glad to invote you to join dinner.")

print("A dinner table which i buy can't reach here in time, so i only invote two persons not more.")      
print(client_list.pop() + ", i'am sorry i can't invote you to dinner.")
print(client_list.pop() + ", i'am sorry i can't invote you to dinner.")
print(client_list.pop() + ", i'am sorry i can't invote you to dinner.")
print(client_list.pop() + ", i'am sorry i can't invote you to dinner.")
print(client_list[0] + ", you are already in the list of dinner.")
print(client_list[1] + ", you are already in the list of dinner.")
del client_list[0]
del client_list[0]
print("Now list is null")
print(client_list)


# list.sort() will change the list sequence forever.
# And we can use list.sort(reverse=True) to reverse sequence.
# sorted(list) will not change the original list, just return  a list sorted.
# list.reverse() will reverse the list forever, ofcourse we can call reverse()
# again to recover.
# len(list) get size of list.
places = ['Great Wall', 'White House', 'HongKong']
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
print(len(places))

# Note that we can always use index -1 to access the last element of list.
# ofcourse, python will report indexerror if list is null.
print(places[-1])

# for loop to operate list.
for place in places:
    print(place)
    print(" is the place i will go.")
print("All is good places.")
