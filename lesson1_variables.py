# Variables - a value stored in a thing. Case Sensitive.
a = 1       # integer
a1 = 0.1    # float
b = "1"     # string can be either single or double quotes

# everything else is a function. Or a statement.
print(a + a1)
print(b)

# to find out which data type is being used, use type() function:
print(type(a1))
print(type(b))
# tabs and blocks - a block of code that is acted upon is shown by an indentation
# and a colon: The number of spaces needs to remain the same throughout the block.
if a > a1:
    print("1 is greater than 0.1")
    print("Hooray!")

# Variables can be defined, eg:
x = str(4)    # x will be the string '4'
y = int(4)    # y will be the integer 4
z = float(4)  # z will be the float 4.0
print(x)
print(y)
print(z)

# multiple Variables can also be assigned on a single line:
x, y, z = "apple", "orange", "mint"
print(x)
print(y)
print(z)

# or one value to multiple variables:
_food = _fruit = _seed = "apple"
print(_food)
print(_fruit)
print(_seed)

# A tuple is a group of things (variable possibilities). They can be extracted
# or unpacked after a variable is defined. THIS IS A LIST![] and () is a tuple. I think.
socks = ["red sock", "green sock", "blue sock"]
f, g, h = socks
print(f)
print(g)
print(h)

socks = ("red sock", "green sock", "blue sock")
f, g, h = socks
print(f)
print(g)
print(h)
# The Print() statement - print statements containing strings and numbers will cause an error.
print(len(f))   # len shows the length of the string.
print(f[0])  # prints first character of f string variable - index 0
print(f[0:2])  # prints the first three characters - index 0 to index 2 - separated by :
