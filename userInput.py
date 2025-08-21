#input() - A function that prompts the user to enter data and it returns the entered data in a string

name = input("What is your Name?: ")
age = input("How old are you?: ")
team = input("Which tema do you support?: ")

age = int(age)
age = age + 1

print(f"Hello {name}!, ")
print(f"I have confirmed you are {age} years old,")
print(f"and also a very big supporter of {team}!-The biggest team in the world.")