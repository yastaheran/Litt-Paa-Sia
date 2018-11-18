"""
Created on Wed Nov  2 17:23:31 2016

@author: yast
"""

Colors used:
0;31 - Red
0;32 - Green
0;34 - Blue 
0;35 - Purple
0;36 - Cyan
1;32 - Light Green
1;34 - Light Blue
1;33 - Yellow
1;35 - Light Purple
1;36 - Light Cyan

def main():
    if you in cake:
        something
    else:
        something cooler




"""
Det jeg gjør:
Åpner begge filene, leser hver linje i en loop og setter dem inn i en dictionary
Så for hver linje i filen som blir farget så prøver jeg å matche alle regexene på linjen
hvis de matcher, så henter jeg ut riktig farge fra den dictionarien der jeg lagrer fargene
altså fra .theme-filen og så skriver jeg ut matchen i riktig farge
søk opp re.compile() og re.search for å matche regexen med teksten
og hvordan dictionaries funker
det er som HashMaps

tror den riktige måten å gjøre det på er å lagre indexen der noe blir matchet, samt hvilken farge, og så sette sammen alle matchene og fargene til slutt
"""
