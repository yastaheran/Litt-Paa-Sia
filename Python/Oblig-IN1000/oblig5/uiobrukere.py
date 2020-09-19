# Oppgave 4: UiO-brukere
uiobrukere = { 'yast': 'ifi.uio.no', 'olan': 'ifi.uio.no', 'karian': 'student.matnat.uio.no'}

# Bonus - unike brukernavn
def lagBrukernavn(fulltnavn, ordbok):
    navn = fulltnavn.split()
    etternavn = navn[1]
    brukernavn = navn[0] + etternavn[0]

    for i in range(0, len(etternavn)):
        brukernavn = navn[0] + etternavn[0:i+1]
        if brukernavn.lower() not in ordbok:
            return brukernavn.lower()

def lagEpost(brukernav, epostsuffix):
    return brukernav + "@" + epostsuffix

def printEposter(ordbok):
    for x in ordbok:
        print(lagEpost(x, ordbok[x]))

def leggTilOrdbok(brukernavn, epostsuffix):
    uiobrukere[brukernavn] = epostsuffix

# Bonus - Tester
assert lagBrukernavn("Yas Taheranpour") == "yast", "lagBrukernavn() - failed"
assert lagBrukernavn("Yas Taheranpour") == "yasta", "lagBrukernavn() - failed"
assert lagEpost("yast", "ifi.uio.no") == "yast@ifi.uio.no", "lagBrukernavn() - failed"

# Kjør program
i = 1
while i != 0:
    print("i = leggTilOrdbok() \np = printEpost() \ns = Avslutt")
    valg = input("> ")

    if valg == "i":
        brukernavn = input("brukernavn: ")
        epostsuffix = input("epostsuffix: ")
        leggTilOrdbok(brukernavn, epostsuffix)
    elif valg == "p":
        printEposter(uiobrukere)
    elif valg == "s":
        i = 0
    else:
        print("unvalid command")
