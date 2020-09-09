#Oppgave 1: Parametere og returverdier

def adder(tall1, tall2):
    return (tall1 + tall2)

print(adder(21, 29))
print(adder(214, 123))

def tellForekomst(minTekst, minBokstave):
    forekomst = 0

    for x in minTekst:
        if x == minBokstave:
            forekomst += 1

    print(minBokstave + " forekommer " + str(forekomst) + " ganger i tekststreng " + minTekst)

tekststreng = input("Skriv inn en tekststreng: ")
bokstav = input("Skriv inn en bokstav: ")
tellForekomst(tekststreng, bokstav)
