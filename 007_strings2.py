# I'm currently referencing https://www.learnpython.org/
# to learn how to utilize simple Python concepts.
# -- Peter

# There are additional variations on defining strings
# that make it easier to include things such as carriage 
# returns, backslashes and Unicode characters. These 
# are beyond the scope of this tutorial, but are covered 
# in the Python documentation.

# The two following global variables are used by me (this creator)
# to space out the different sections (so called chapters) of my work
# in this particular file.

insert_line = " "
asterisks = "************ ////////////// ************"

# From here onward are the different "chapters" of me learning coding.

print(insert_line)
print("Begin code testing:")
print(insert_line)

one = 1
two = 2
three = one + two
print(one, two, three)

hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)
 

print(insert_line)
print(asterisks)
print(insert_line)

# Assignments can be done on more than one variable
# "simultaneously" on the same line like this

a, b = 3, 4

print("The following line contains two integers.")
print("both defined in the same fancy variable:")
print(a,b)

print(insert_line)
print(asterisks)
print(insert_line)

# The target of this exercise is to create a string,
# an integer, and a floating point number. The string
# should be named mystring and should contain the 
# word "hello". The floating point number should be
# named myfloat and should contain the number 10.0,
# and the integer should be named myint and should
# contain the number 20.

# This is my example given the instructions.

second_mystring = "hello"
second_myfloat = 10.0
first_myint = 20

print("This is mystring: ")
print(second_mystring)
print(insert_line)

print("This is myfloat: ")
print(second_myfloat)
print(insert_line)

print("This is myint: ")
print(first_myint)
print(insert_line)
print("This is myint minus myfloat minus 0.5: ")
print(first_myint - second_myfloat - 0.5)


print(insert_line)
print(asterisks)
print(insert_line)

# Below is the example given by the website.
# This is the first time that I've run across isinstance and have to look into it.

this_string = "hello"
this_float = 10.0
this_int = 20

if second_mystring == "hello":
	print("String: %s" % this_string)
if  isinstance(this_float, float) and this_float == 10.0:
	print("Float: %f" % this_float)
if isinstance(this_int, int) and this_int == 20:
	print("Integer: %d" % this_int)
