#Variables - container for a value(String, Integer, Float, Bollean)
#Strings
first_name = "Vincent"
food = "Chapo"
email = "vincentnjuguna69@gmail.com"

#Integers
age = 23
quantity = 5
num_of_students = 30

#float
price = 1000.99

#Boolean
is_student = False
for_sale = True

if for_sale:
    print("That item is for sale")
else:
    print("That item is not availbale")

if is_student:
    print("You are a student and you are going to graduate at the end of th year!")
else:
    print("You are not a student. Please enroll for a course at the college!!!")



#Output
print(f"Hello {first_name}, You are {age} years old and you like {food} aloot")
print(f"You are buying {quantity} items")
print(f"Your class has {num_of_students} number of students in total")
print(f"The price of a brand new AMG C63 is {price}")
print(f"Are you a student? {is_student}")