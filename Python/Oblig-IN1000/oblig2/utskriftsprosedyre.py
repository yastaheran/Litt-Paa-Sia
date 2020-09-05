#Oppgave 1: Utskriftsprosedyre

def prosedyre():
    navn = input("Skriv inn navn: ")
    sted = input("Hvor kommer du fra? ")
    print("Hei, " + navn + "! Du er fra " + sted + ".")

for i in range(3):
    prosedyre()
