# Title   : Dictionary
# Author  : Ryan Carr
# Purpose : Load a dictionary from a json file and ask user for a word to define.
#           If the word cannot be found suggest up to 3 possible alternatives.

from json import load
from difflib import get_close_matches


def ask_question(question):
    return input(question + ":\n")


def load_dictionary():
    fh = open("data.json", "r")
    dictionary = load(fh)
    fh.close()
    return dictionary


def print_definition(definition):
    for word in definition:
        print(word)


def main():
    MAX_MATCHES = 3
    dictionary = load_dictionary()
    answer = ask_question("Please enter a word")

    if answer.lower() in dictionary.keys():
        print_definition(dictionary[answer.lower()])
    else:
        matches = get_close_matches(answer.lower(), dictionary.keys(), MAX_MATCHES)
        count = 0

        while True:
            if count >= MAX_MATCHES:
                print("I'm sorry, I couldn't find your word.")
                break
            answer = ask_question("Did you mean %s? (Y/N)" % matches[count])
            if answer.lower().startswith("y") and count < MAX_MATCHES:
                print_definition(dictionary[matches[count]])
                count += 1
                break
            elif answer.lower().startswith("n") and count < MAX_MATCHES:
                count += 1
                continue
            else:
                print("You need to type in either Y or N to continue")


if __name__ == "__main__":
    main()
