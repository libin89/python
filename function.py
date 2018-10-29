def build_person(first_name, last_name, age=''):
    """return a dictionary"""
    person = {'first':first_name, 'last':last_name}
    if age:
        person['age'] = age
    return person


def get_formatted_name(first_name, last_name):
    """return completed name"""
    full_name = first_name.title() + ' ' + last_name.title()
    return full_name

def greet_users(names):
    """greet to everyone in the name list"""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)


# *topping is a null tuple
def make_pizza(size, *toppings):
    """describe the pizza that is made"""
    print("\nMake a " + str(size) + "-inch pizza with the following topping:")
    for topping in toppings:
        print("- " + topping)

# **user_info is a null dictionary
def build_profile(first, last, **user_info):
    """create a dictionary, contain user's information we know"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key,value in user_info.items():
        profile[key] = value
    return profile

