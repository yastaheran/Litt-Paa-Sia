# Oppgave 1: Regnefunksjoner

def addisjon(a, b):
  return (a+b)

def subtraksjon(a, b):
  return (a-b)

def divisjon(a, b):
  return (a/b)

def tommerTilCm(antallTommer):
    assert antallTommer > 0, "antallTommer kan ikke være negativ"
    return antallTommer*2.54

def skrivBeregninger():
    a = int(input("Skriv inn tall1: "))
    b = int(input("Skriv inn tall2: "))

    print("resultat av addisjon: " + str(addisjon(a, b)))
    print("resultat av subtraksjon: " + str(subtraksjon(a, b)))
    print("resultat av divisjon: " + str(divisjon(a, b)))

    tommer = int(input("Skriv inn tall3: "))

    print("resultat av konvertering til cm: " + str(tommerTilCm(tommer)))

# Test - addering
assert addisjon(11, 8) == 19, "feil ved addering"
assert addisjon(-1, -12) == -13, "feil ved addering"
assert addisjon(12, -8) == 4, "feil ved addering"

# Test - subtraksjon
assert subtraksjon(12, 2) == 10, "feil ved subtraksjon"
assert subtraksjon(-10, -10) == 0, "feil ved subtraksjon"
assert subtraksjon(-212, 21) == -233, "feil ved subtraksjon"

# Test - divisjon
assert divisjon(6, 2) == 3, "feil ved divisjon"
assert divisjon(12, 3) == 4, "feil ved divisjon"
assert divisjon(81, 9) == 9, "feil ved divisjon"

# Test - tommerTilCm
assert tommerTilCm(23) == 58.42, "feil ved konvertering"

skrivBeregninger()
