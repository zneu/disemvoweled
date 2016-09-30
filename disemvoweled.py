#try and except, loop
#accept a list of words
#remove vowels from each word
#put vowels into new list
#return that list with the first letter capitalized

disemvoweled = []

print("Make a list of items, they will have no vowels!")

def show_help():
    print("\nSeperate each item with a comma.")
    print("Type DONE to quit, SHOW to see the current list, and HELP to get this message.")

def show_list():
    count = 1
    for item in disemvoweled:
        print("{}: {}".format(count,item))
        count += 1

def anti_vowel(iterable):
    iterable = iterable.replace('a',"").replace('e',"").replace('i',"").replace('o',"").replace('u',"")
    disemvoweled.append(iterable.capitalize())

show_help()

while True:
    words = input ("> ")
    if words == "DONE":
        print("\nHere's your list!")
        show_list()
        break
    elif words == "HELP":
        show_help()
        continue
    elif words == "SHOW":
        show_list()
        continue
    else:
        word_list = words.split(", ")
        for x in word_list:
            try:
                anti_vowel(x)
            except ValueError:
                break
