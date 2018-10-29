# input(prompt-string) get string input from user
message = input("Tell me something, and I will repeat it back to you: ")
print(message)

prompt = "if you tell who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print("\nHello, " + name + "!")

# int(var) convert string to int numeric
age = input("How old are you? ")
if int(age) >= 18:
    print(age + "? you are adult.")
else:
    print("NOT adult!")

# while condition:
#     do something

# break and continue


responses = {}
poll_active = True

while poll_active:
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like? ")
    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat.strip() == 'no':
        poll_active = False
print("\n---poll results ---")
for name,response in responses.items():
    print(name.title() + " would like to climb " + response.title() + ".")
