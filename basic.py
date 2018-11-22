from sys import *

tokens = []


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
            if state == 0:
                tok = ""
            else:
                tok = " "
        elif tok == "\n":
            tok = ""
        elif tok == "print":
            tokens.append("print")
            tok = ""
        elif tok == "\"":
            if state == 0:
                state = 1
            elif state == 1:
                tokens.append("string:" + string + "\"")
                string = ""
                state = 0
                tok = ""
        elif state == 1:
            string +=tok
            tok = ""
    print(tokens)


def run():
    open_file(argv[1])
    data = open_file(argv[1])
    lex(data)


run()
