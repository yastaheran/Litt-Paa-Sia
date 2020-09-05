#!/usr/bin/env python
#Oppgave 3: Problemløsning med beslutninger
#3.1-3.2

#funksjon for å sammenligne input
def sammenlign():
 if dag2 > dag1 and mnd2 >= mnd1:
        print("riktig")
    elif dag2 < dag1 and mnd2 <= mnd1:
        print("feil")
    elif dag2 == dag1 and mnd2 == mnd1:
        print("samme")
    else:
        print("error")


#input fra bruker
dag1 = int(input("Dag1: "))
mnd1 = int(input("Måned1: "))
dag2 = int(input("Dag2: "))
mnd2 = int(input("Måned2: "))

sammenlign(dag1, mnd1, dag2, mnd2)
