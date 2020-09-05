#Oppgave 2: ordbok

ordbok = {
    "annas" : 12.29,
    "melk" : 14.90,
    "brød" : 24.90,
    "yoghurt" : 12.90,
    "pizza" : 39.90
}

# Del 2.1
for x in ordbok:
    print(x + " - kr " + str(ordbok[x]))

# Del 2.2
print("Legg til to varer med pris.")

for x in range(2):
    varenavn = input("Varenavn: ")
    ordbok[varenavn] = float(input("pris: "))

for x in ordbok:
    print(x + " - kr " + str(ordbok[x]))
