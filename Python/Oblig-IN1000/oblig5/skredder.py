# Oppgave 5: Egen oppgaven
# Skriv et beregningsprogram for skreddere med en funksjon som leser inn en fil
# der hver linje beskriver et navn på et mål og selve målet i tommer. Eksempel:
# Skulderbredde 4
# Halsvidde 3.2
# Livvidde 10
# La programmet legge disse målene i en ordbok med navn på målet som nøkkelverdi
# og returner ordboken. Lag deretter en prosedyre som tar imot en liste av mål
# og benytter seg av tommerTilCm som du skrev tidligere for å skrive ut målene
# i centimeter

def lesFil(filnavn):
    maalbok = {}
    fil = open(filnavn)

    for linje in fil:
        info = linje.split()
        maalbok[info[0]] = float(info[1])

    fil.close()
    return maalbok

def tommerTilCm(antallTommer):
    assert antallTommer > 0, "antallTommer kan ikke være negativ"
    return antallTommer*2.54

def skrivUtMaal(maalbok):
    for x in maalbok:
        print(x + ": " + str(tommerTilCm(maalbok[x])) + " cm.")

dict = lesFil("skredderfil.txt")
skrivUtMaal(dict)
