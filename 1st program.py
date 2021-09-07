# this program says hello and asks for my name

print('Hello everybody!')
print("What is your name?")
myName = input()
print("Hello " + myName)
print("")

print("To use a number in a print statement, must be converted to a string")
print("What is your favourite number?")
myNumber = int(input())
# myNumCalculated = myNumber + 5
print("The input has been converted from string to integer with myNumber = int(input()")
print("and then in the next print statement, we have the string, your number, etc,")
print("followed by '+ str(myNumber + 5)' (not in quotes) - the calculation is done first ")
print("and the output converted to a string!")
print("Your number added to the number 5 = " + str(myNumber + 5))
print("")

print("The conversion from str to int can also be done on the final line.")
print("So str(int(myNumber)+5) would have had the same effect and saved the")
print("conversion of 'myNumber = int(input())' line. However, the 'myNumber")
print("=input()' would need to remain.")
