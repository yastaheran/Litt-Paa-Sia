#Oppgave 3: Billetpris

def sjekkPris(alder):
    billettpris = 0

    if alder <= 17:
        billettpris = 30
        print("Du må betale 30kr")
    elif alder > 17:
        billettpris = 50
        print("Du må betale 50kr")
    else alder >= 63:
        billettpris = 35
        print("Du må betale 35kr")


alder = int(input("Din alder: "))
sjekkPris(alder)
