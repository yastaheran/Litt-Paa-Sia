#Oppgave 1: Utskrift og innlesing med variabler

#DEL 1.2-1.3
navn = input("Ditt navn: ")
print("Hei " + navn + "!")

#DEL 1.4-1.5
heltall1 = int(input("Skriv inn heltall1: "))
heltall2 = int(input("Skriv inn heltall2: "))
diff = tall1-tall2
print("Differenase: ")
print(diff)

#DEL 1.6
navn1 = input("Skriv inn navn1: ")
navn2 = input("Skriv inn navn2: ")
sammen = navn1 + navn2
print(sammen)

#DEL 1.7
og = " og "
position = len(navn1)
nySammen = sammen[:position] + og + sammen[position:]
print(nySammen)
