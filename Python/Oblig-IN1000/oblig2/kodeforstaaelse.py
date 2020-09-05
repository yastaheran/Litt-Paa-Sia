#Oppgave 4: Kodeforståelse

# Svar oppgave 4.1: Koden slår sammen en int og str uten konverting. Vil føre til error.
# Svar oppgave 4.2: Problemer oppstår når if testen består og man får TypeError. Ved bruk av str() løses dette.

a = input("Tast inn et heltall! ")
b = int(a)

if b < 10:
    print (b + "Hei!")
