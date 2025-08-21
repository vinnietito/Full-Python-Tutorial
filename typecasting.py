#Type casting- it is the process of converting a variable from one datatype to another
#str(), int(), float(), bool()

name = "Rueben Amorim"
age = 31
gps = 4.91
is_student = False


print(type(name))
print(type(age))
print(type(gps))
print(type(is_student))

gps = int(gps)
print(gps)
age = str(age)
name = bool(name)

print(int(is_student))
print(float(age))

print(str(age))
print(type(age))
print(name)