"""
This program is an assistant working on the Python's console able to take some basic instructions
Vincent Bauffe, November 2019
"""
import sys

def dispatch(command):
    try:
        if command[0] == "file":
            return file_opening(command[1])
        elif command[0] == "info":
            return info()
        elif command[0] == "dictionary":
            return dictionary()
        elif command[0] == "search":
            return search(command[1])
        elif command[0] == "sum":
            length = len(command)
            return sum(command[1:length])
        elif command[0] == "avg":
            length = len(command)
            return average(command[1:length])
        elif command[0] == "help":
            return help()
        elif command[0] == "exit":
            return exit()
    except:
        return "This command is invalid or you need to open the file first"

def file_opening(filename):
    try:
        global file
        file = open(filename, "r")
        return "Loaded {0}".format(filename)
    except:
        return "This file name doesn't exist"

def info():
    try:
        nbr_line = 0
        nbr_char = 0
        for i in file:
            nbr_line += 1
            nbr_char += len(i)
        return "There is {0} lines and {1} characters in the file".format(nbr_line, nbr_char)
    except:
        return "File not open yet"

def dictionary():
    try:
        str = file.read()
        global list
        list = str.split("\n")
        for i in range(len(list)):
            list[i] = list[i].split(",")
            list[i] = list[i][0]
        print(list)
        return "Dictionary created"
    except:
        return "Error while creating the dictionary"

def search(word):
    try:
        length = len(word)
        total_letter = 0
        last_delta = 1000
        for word_dic in list:
            for letter in word:
                if letter in word_dic:
                    total_letter += 1
            delta = length - total_letter
            if delta < last_delta:
                find_word = word_dic
            else:
                last_delta = delta
        return "The closest word is {0}".format(find_word)
    except:
        return "An error has occured while searching"

def sum(list):
    try:
        total = 0
        for i in list:
            j = float(i)
            total += j
        return "The sum is {0}".format(total)
    except:
        return "The arguments must be integer or float"

def average(list):
    try:
        avg = 0
        iteration = 0
        for i in list:
            j = float(i)
            avg += j
            iteration += 1
        avg = avg / iteration
        return "The average is {0}".format(avg)
    except:
        return "The arguments must be integer or float"

def help():
    msg = "This program is very useful and can do multiple things.\nFirst you'll need to load a file, and then you can call different functions.\nFor instance, try these :\n - file <name> load the file with the given name\n - info : shows the number of lines and characters in the file.\n - dictionary : converts the file into a dictionary\n - search : searchs for the most similar word to the entry\n - sum : returns the sum of the given numbers\n - avg : returns the average of the given numbers\n - exit : exits everything"
    return msg

def exit():
    try:
        file.close()
        return "File closed\nSystem terminating"
    except:
        return "Error while terminating program"



print("Bienvenue dans votre outil personnalisé !")

while True:
    command = input().split()
    print(dispatch(command))
    if dispatch(command) == "File closed\nSystem terminating":
        sys.exit()
