# import csv
# import json
file = open("data_file/sample.txt")
somelines = file.read()
print(somelines)
# Split it into an array
tickle = list(somelines.split("\n"))
print(tickle[0])
file.close()

# f = open("data_file/titanic_data.csv", 'r')
# with f:
#    read = csv.reader(f)
#    for row in read:
#       print(row)
# print("file closed? ", f.closed)

# f = open("data_file/titanic_data.csv", 'r')
# with f:
#    read = csv.reader(f)
#   for row in read:
#       print(row)

# file = open("data_file/sample.txt")
# text = file.read()
# text_mode = file.mode
# print(text)
# file.close()
# print("file closed? ", file.closed)

# print(">>>>>>>>>>>>>>>>>>>>>")
# print("text mode: ", text_mode)

# print(">>>>>>>>>>>>>>>>>>>>>")
# with open("data_file/sample.txt") as f:  # closes file after it's been used.
#   data = f.readlines()
#   print(data[1])

# print("file closed? ", file.closed)

# write stuff!
# file = open('data_file/writtenfile.txt', 'w')  # w = write mode
# file.write("Hola! What's up?")
# file.close()
# print("file closed? ", file.closed)
# file = open('data_file/writtenfile.txt', 'a+')  # a+ = append mode
# file.write("\nOK!")
# file.close()
