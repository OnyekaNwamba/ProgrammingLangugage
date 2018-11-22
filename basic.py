from sys import *


def open_file(filename):
    #print(filename)
    data = open(filename, "r").read()
    return data


def lex(fileContents):
    tok = ""
    state = 0
    string = ""
    fileContents = list(fileContents)
    for char in fileContents:
        tok +=char
        if tok == " ":
            tok = ''
        elif tok == "print":
            print("found a print!")
            tok = ""
        elif tok == "\"":
            if state == 0:
                state = 1
            elif state == 1:
                print("found a string!")
                string = ""
                state = 0
        elif state == 1:
            string +=char
            tok = ""



def run():
    open_file(argv[1])
    data = open_file(argv[1])
    lex(data)


run()
