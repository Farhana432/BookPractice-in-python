import sys

print("This is the name of the program:", sys.argv[0])

print("Argument List:", str(sys.argv))


print(sys.argv)
print(type(sys.argv))
arguments = str(sys.argv)
a = arguments[1]
b = arguments[2]
print(a+b)