#Oppgave 1: Parametere og returverdier

# Del 1.1
def adder(tall1, tall2):
    return (tall1 + tall2)

print(adder(21, 29))
print(adder(214, 123))

# Del 1.2
tekststreng = input("Skriv inn en tekststreng: ")
bokstav = input("Skriv inn en bokstav: ")

# Del 1.3
def tellForekomst(minTekst, minBokstave):
    forekomst = 0

    for x in tekststreng:
        if tekststreng[x] == bokstav:
            forekomst++
    print(bokstav + " forekommer " + " ganger i tekststreng " + tekststreng)

tellForekomst(tekstreng, bokstav)
