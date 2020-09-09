#Oppgave 4: Å telle bokstaver og ord
ordbok = {}

def antBokstaver(ord):
    antall = 0
    for x in ord:
        antall += 1
    print(antall)

def unikeOrd(tekst):
    ordene = tekst.split()
    ordbok[ordene[0]] = 1

    for x in range(1, len(ordene)-1):
        if ordene[x] in ordbok:
            ordbok[ordene[x]] += 1 #hvis ordet finnes, skal verdien økes
        else:
            ordbok[ordene[x]] = 1 #legg til ordet pluss verdi

    for x in ordbok:
        print(x + " - " + str(ordbok[x]))

ord = input("Skriv inn et ord: ")
tekst = input("Skriv inn en setning: ")
antBokstaver(ord)
unikeOrd(tekst)
