#Oppgave 3: Problemløsning med beslutninger
#3.3

#funksjon for å sammenligne input
def sammenlign(dato1, dato2):
    if dato2 > dato1:
        print("riktig")
    elif dato2 < dato1:
        print("feil")
    elif dato2 == dato1:
        print("samme")
    else:
        print("error")


#input fra bruker
print("Oppgi dato i format MMDD")
dato1 = int(input("Dato 1: "))
dato2 = int(input("Dato 2: "))

sammenlign(dato1, dato2)
