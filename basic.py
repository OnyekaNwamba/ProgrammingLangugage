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
            tokens.append("PRINT")
            tok = ""
        elif tok == "\"":
            if state == 0:
                state = 1
            elif state == 1:
                tokens.append("STRING:" + string + "\"")
                string = ""
                state = 0
                tok = ""
        elif state == 1:
            string +=tok
            tok = ""
    return tokens
    #print(tokens)

def parse(toks):
    i = 0
    while(i<len(toks)):
        if toks[i] + " " + toks[i + 1][0:6] == "PRINT STRING":
            print(toks[i+1][7:])
            i = i + 2

def run():
    open_file(argv[1])
    data = open_file(argv[1])
    toks = lex(data)
    parse(toks)


run()
