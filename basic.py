from sys import *
import re

tokens = []


def open_file(filename):
    #print(filename)
    data = open(filename, "r").read()
    date = data + "<EOF>"
    return data


def lex(fileContents):
    isExpr = 0
    tok = ""
    state = 0
    string = ""
    expr = ""
    n = ""
    fileContents = list(fileContents)
    for char in fileContents:
        tok +=char
        if tok == " ":
            if state == 0:
                tok = ""
            else:
                tok = " "
        elif tok == "\n" or tok == "<EOF>":
            if expr !="" and isExpr == 1:
                tokens.append("EXPR:" + expr)
                expr = ""
            elif expr !="" and isExpr == 0:
                #we know its a number
                tokens.append("NUM:" + expr)
                expr = ""
            tok = ""
        elif tok == "print":
            tokens.append("PRINT")
            tok = ""
        elif tok =="0" or tok=="1" or tok=="2" or tok=="3" or tok=="4" or tok=="5" or tok=="6" or tok=="7" or tok=="8" or tok=="9":
            print("NUMBER:")
            expr = expr + tok
            tok = ""
        elif tok == "+":
            isExpr = 1
            expr = expr + tok
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
    print(expr)
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
