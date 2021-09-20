import time

# creating Choices starting point - list with user text input with specified contents.
# We can remove parts of the list once they've been used and we don't need to use
# the orange they tried to set fire to once it's been eaten. Or something.
choices = []

# OOOO, WE GOT A FUNCTION!
# so we need to split the verb_a string to get the actual verb if there's a noun there.
# fsck it. Use "split". In a function. Which we've not studied yet. Arse.
# 18 September: NOT NECESSARY!
# def spit(string):

# is it necessary to actually define this function? Can't we just use verb = list(verb_a.split(" ")) later?
# li = list(string.split(" "))  # so the string will be verb_a
# return li


# so then we go and split verb_a which we extract from choices into verb
# INTRO:
print("Welcome to the Underworld.")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("""
It's been a while.
It's pitch dark.

In your pocket is a torch you last used in 2007, a box
of matches from gods know when, a rock, some paper, and what
feels like a rubber band.
What do you use?
""")
# Define the contents of the pockets.

item_01 = ["paperclip", "paper clip", "rubber band", "rock", "box of matches", "torch"]
# INPUT -->
choices.append(input("> ").lower())


# provide a variable for next line:
noun_a = choices[0]
# check if people have "A thing" or "THE thing"...
noun_a1 = list(noun_a.split(" "))
# print(noun_a1)
# print("CHECK THIS ABOVE!")
if noun_a1[0] == "the":
    noun_a1.pop(0)
elif noun_a1[0] == "a":
    noun_a1.pop(0)

noun_a = ' '.join(noun_a1)
# print(noun_a, "this is to check noun_a has had THE or A removed.")
# "test_thing" below is just used for testing the thing. so it's = any(x in our_test_variable for x in big_long_list)
if any(test_thing in noun_a for test_thing in item_01):
    print("OK!")  # it works!! It lives!!
else:
    print("Where did you get that from?")  # rhetorical question. "pass" is a better option.
# Did they use the torch?
if "torch" in noun_a:
    print("""
You hold the torch in front of you, and try to switch it on. You hear
a fizz and a click and for a few seconds you cast a soft light around
you.
""")
    time.sleep(2)
    print("""          
You see reflections from the new light source on the ground, and you seem to be in
a room that stretches a couple of meters in front of you. There are boxes
casting shadows, and no windows. 
""")
    time.sleep(2)
    print("""
The torch fades and dies. 
What do you do? 
""")
    choices.append(input("> ").lower())
    # print(choices)  # to see where we are - we are at choices[1]
    print(f"{choices[1]} doesn't help")

else:
    print(f"You take the {noun_a} and hold it up. What do you do with it?")
choices.append(input("> ").lower())
verb_a = choices[1]
# verb = spit(verb_a) # <-- this function is unnecessary, unless we need to do it again, but it's not much
# code and typing in the command is a better form of learning.
verb = list(verb_a.split(" "))
# to do: 1/ should really check if verb includes -ing already. They could be blowing it out.
if "ping" == verb[0]:
    ing = False
elif "ing" in verb[0]:
    print(verb)
    print("True")
    ing = True
# OMFG - you can't ping something without pinging it.
else:
    ing = False

# Define positive response in a big list of possible yeses:
answer_yes = ["yes", "kinda", "a bit", "slightly", "loads", "yeah", "yup", "yus", "si", "really"]
# we'll use it after the next input. Also handy to have for positive responses later.

print(f"You've got a {noun_a} and you've tried to {verb_a}... Is this helping?")
does_it_help = input("> ") or "no"
does_it_help = does_it_help.lower()
# punctuation removal:
punctuation = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''
helping = ""
for x in does_it_help:
    if x not in punctuation:
        helping = helping + x
print(helping)


# print(verb[0])
#        2/ should also check if verb ends in e. !FIXED! kind of, with the ing correction below.
#        3/ Also should check if "it" is present -- so choices[1] could be something like "put it up your bum"
# solution to 3 - rephrase line
if ing:  # so if it's verbing
    if helping in answer_yes:  # so if result of the input for helping is in the list
        print(f"Great! {str(verb[0])} the {noun_a} is helping!")
    else:
        # think we may need to check noun_a for an "a" or "the"
        print(f"OK, so {str(verb[0])} the {noun_a} wasn't such a great idea.")

if not ing:
    if helping in answer_yes:  # so if result of the input for helping is in the list
        print(f"Great! {str(verb[0])}ing the {noun_a} is helping!")
    else:
        # think we may need to check noun_a for an "a" or "the"
        print(f"OK, so {str(verb[0])}ing the {noun_a} wasn't such a great idea.")

# LET'S END THIS NOW!
print("Thanks for playing... Goodbye!")
print("BTW, your choices were:")
for n in range(len(choices)):
    print(choices[n])
