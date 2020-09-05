#Oppgave 5: Egen Oppgave

# Lag en quiz med multiple choice-oppgaver og kortesvarsoppgaver
# Riktig svar = 1 poeng
# Feil svar (kortsvarsoppgaver) = 0 poeng
# Feil svar (multiple choice) = -2 poeng

totalsum = 0
def stillSpm(spmnr):
    if spmnr == 0:
        print("Hvor mange meter er det i en kilometer?")
        svar = int(input("> "))
        return svar
    elif spmnr == 1:
        print("Hva er hovedstaden i Norge?")
        svar = input("> ")
        return svar
    elif spmnr == 2:
        print("hva er 2 + 2?")
        print("A: 1 B: 3 C: 22 D: 4")
        svar = input("> ")
        return svar
    elif spmnr == 3:
        print("hva er 3x3?")
        svar = int(input("> "))
        return svar
    elif spmnr == 4:
        print("hvor ligger Lier?")
        print("A: Viken B: Oslo C: Telemark")
        svar = input("> ")
        return svar

def sjekkSvar(spmnr, svar):
    global totalsum
    if spmnr == 0:
        if svar == 1000:
            print("Riktig!")
            totalsum += 1
        else:
            print("Feil!")
    elif spmnr == 1:
        if svar == "Oslo":
            print("Riktig!")
            totalsum += 1
        else:
            print("Feil!")
    elif spmnr == 2:
        if svar == "D":
            print("Riktig!")
            totalsum += 1
        else:
            print("Feil!")
            totalsum -= 2
    elif spmnr == 3:
        if svar == 9:
            print("Riktig!")
            totalsum += 1
        else:
            print("Feil!")
    elif spmnr == 4:
        if svar == "A":
            print("Riktig!")
            totalsum += 1
        else:
            totalsum -= 2
            print("Feil!")
    else:
        print("5")

print("Velkommen til Quizmaster!")
print("For hvert riktig svar får du 1 poeng, 0 poeng for feil svar på kortsvarsoppgaver og -2 poeng for feil på multiplechoice.")
brukernavn = input("Hva heter du? ")

for x in range(5):
    svar = stillSpm(x);
    sjekkSvar(x, svar)

print(brukernavn + " fikk: " + str(totalsum) + " poeng!")

if totalsum == 5:
    print("Du svarte riktig på alle spm!")
elif totalsum < 5 and totalsum > 0:
    print("Du klarte mange, men må jobbe litt ekstra!")
else:
    print("Prøv igjen!")
