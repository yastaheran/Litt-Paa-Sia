# Oppgave 3: Reiseplan
steder = []
klesplagg = []
avreisedatoer = []

#for-loop for reisemal
for x in range(5):
    reisemal = input("Skriv inn ditt reisemal: ")
    steder.append(reisemal)
print()

#for-loop for avreisedatoer
for x in range(5):
    dato = input("Skriv inn avreisedatoer: ")
    avreisedatoer.append(dato)
print()

#for-loop for klesplagg
for x in range(5):
    item = input("Skriv inn klesplagget: ")
    klesplagg.append(item)
print()

#setter alle listene i en ny liste
reiseplan = [steder, avreisedatoer, klesplagg]

#print ut alle lister + innhold i reiseplan
listenr = 0
for liste in reiseplan:
    print("Liste " + str(listenr) + " :")
    for x in liste:
        print(x, end = '\n')
    listenr += 1
    print()

#la brukeren oppgi en plass i reiseplan og skrive ut elementet på den oppgitte plassen
i1 = int(input("Indeks for liste: "))
i2 = int(input("Indeks for element i valgt liste: "))

if i1 <= (len(reiseplan)-1) and i1 >=0 and i2 <= (len(reiseplan[i1])-1) and i2 >=0:
    print(reiseplan[i1][i2])
else:
    print("Ugyldig input")
