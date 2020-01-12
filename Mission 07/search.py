"""
This program allows you to scan through a file to find all the occurrences of a given list of words
Vincent Bauffe, November 2019
"""


def readfile(filename):
    """
    This function open a file and return a list with all the lines
    :param filename: a string containing the name of the file
    :return: a list with string containing the lines ie: ["line1", "line2"]
    """
    try:
        with open(filename, "r") as file:
            text = file.readlines()
            for i in range(len(text)):
                text[i] = text[i].rstrip()
        return text
    except:
        print("Error readfile()")


def get_words(line):
    """
    Seperates all the words and only keep the alpha's
    :param line: a string ie : "line1"
    :return: a list with all the words ie : ["word1", "word2"]
    """
    try:
        alphabet = "abcdefghijklmnopqrstuvwqyz "
        lineL = list(line.lower())
        for word in lineL:
            if word not in alphabet:
                lineL.remove(word)
        lineS = "".join(lineL)
        lineL = lineS.split(" ")
        for word in lineL:
            if word == "":
                lineL.remove(word)
        return lineL
    except:
        print("Error get_words()")


def create_index(filename):
    """
    Creates an index with all the words and an inner dictionary giving {word : {line : occurency}}
    :param filename: The file with which we are creating the index
    :return: The whole index, with nested dictionaries
    """
    try:
        index = {}
        whole_text = readfile(filename)
        for line in whole_text:  # Creates my blank dictionnary
            for word in get_words(line):
                index[word] = {}
        for line in whole_text:
            for word in get_words(line):
                index[word][whole_text.index(line)] = 0
        for line in whole_text:
            for word in get_words(line):
                index[word][whole_text.index(line)] += 1
        return index
    except:
        print("Error create_index()")


def get_lines(words, index):
    """
    Finds all the line where all the words in words[] are
    :param words: list ie : ["the", "republic"]
    :param index: nested dictionary
    :return: list with line number ie : [line_number1, line_number2]
    """
    try:
        occurency = []
        new_list = []
        try:
            for key in words:
                for line in index[key]:
                    occurency.append(line)
            for i in occurency:
                if occurency.count(i) == len(words) and i not in new_list:
                    new_list.append(i)
        except:
            pass
        return new_list
    except:
        print("Error get_lines")


print(get_lines(["the", "oui", "republic"], create_index("test")))

#filename = input("To exit simply type 'exit'\nHello, please give the name of the file you want to analyze :\n")

# while False:
#    instruction = input("Which are the words you are looking for ?\nPlease separate them with a space\n")
#    if instruction == "exit":
#       print("Thanks for using my tool")
#       break
#   words = instruction.split(" ")
#   print("Here are all the lines with your words in them :", get_lines(words, create_index(filename)))
