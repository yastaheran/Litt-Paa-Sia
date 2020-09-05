#Oppgave 1: Lister

#Del 1.1
listen = [1, 4, 22]
listen.append(12)

print(listen[0])
print(listen[2])

#Del 1.2
nyListe = []

for x in range(4):
    navn = input("legg til navn: ")
    nyListe.append(navn)

#Del 1.3
if "ole" in nyListe:
    print("Du husket meg!")
else:
    print("Glemte du meg?")
