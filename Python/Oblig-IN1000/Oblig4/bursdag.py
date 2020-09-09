# Oppgave 5: Egen oppgave
#Et program som lar bruker holde styr på, legge til og skrive ut venners bursdag
bursdager = {}

def skrivUt():
    for x in bursdager:
        print(x + " - " + str(bursdager[x]))

def leggTil(venn, bursdag):
    bursdager[venn] = bursdag;

def finnPerson(navn):
    if navn in bursdager:
        print("Person funnet!")
        print(navn + " sin bursdag er : " + str(bursdager[navn]))
    else:
        print("Person med navn " + navn + " ikke funnet!")

print("Bursdagskalenderen. \n Hold oversikt over dine venners bursdager.")
print("Hva ønsker du å gjøre i dag? \n 1: Legg til ny person 2: Finn person 3: Skriv ut full oversikt eller 0: Avslutt?")
inn = int(input(">"))

while inn != 0:
    if inn == 1:
        venn = input("Personens navn: ")
        bursdag = int(input("Bursdagsdato [DDMM]: "))
        leggTil(venn, bursdag)
    elif inn == 2:
        person = input("Personens navn: ")
        finnPerson(person)
    elif inn == 3:
        skrivUt()
    else:
        print("Ugyldig kommando")
    print("Hva ønsker du å gjøre i dag? \n 1: Legg til ny person 2: Finn person 3: Skriv ut full oversikt eller 0: Avslutt?")
    inn = int(input(">"))
