#Oppgave 5: Egen Oppgave

# Lag en quiz med multiple choice-oppgaver og kortesvarsoppgaver
# Riktig svar = 1 poeng
# Feil svar (kortsvarsoppgaver) = 0 poeng
# Feil svar (multiple choice) = -2 poeng

#skrive denne om til ordbok
totalsum = 0
spm = {
    "Hvor mange meter er det i en kilometer?" : "1000",
    "Hva er hovedstaden i Norge?" : "Oslo",
    "hva er 2 + 2?" : "4",
    "hva er 3x3?" : "9",
    "hvor ligger Lier?" : "Viken"
}

def sjekkSvar(spmnr, svar):
    global totalsum
    global spm

    if svar == spm[spmnr]:
        print("Riktig!")
        totalsum += 1
    else:
        print("Feil!")

print("Velkommen til Quizmaster!")
print("For hvert riktig svar får du 1 poeng")
brukernavn = input("Hva heter du? ")

for x in spm:
    print(x)
    svar = input("> ")
    sjekkSvar(x, svar)

print(brukernavn + " fikk: " + str(totalsum) + " poeng!")

#bruke lister for å vise hvor de gjorde feil/Riktig i tillegg til dette
if totalsum == 5:
    print("Du svarte riktig på alle spm!")
elif totalsum < 5 and totalsum > 0:
    print("Du klarte mange, men må jobbe litt ekstra!")
else:
    print("Prøv igjen!")
