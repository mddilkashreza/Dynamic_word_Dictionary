# have a python dictionary that have a key/value pair that represents
# a word and its definition
# collect input from the user, input is a word
# check if the word is in the dictionary
# print the definition


from PyDictionary import PyDictionary

dictionary = PyDictionary()

while True:
    word = input("Enter Your Word:")
    if word == "":
        break
    print(dictionary.getMeanings(word))
