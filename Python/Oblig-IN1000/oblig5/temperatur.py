# Oppgave 2: Temperatur
tempMonth = "max_temperatures_per_month.csv"
tempDaily2018 = "max_daily_temperature_2018.csv"
updatedTempMonth = "updated_max_temperatures_per_month.csv"

def konverterFil(filnavn):
    oversikt = {}
    fil = open(filnavn)

    for linje in fil:
        info = linje.split(',')
        oversikt[info[0]] = float(info[1]) #husk å endre til float

    fil.close()
    return oversikt

def lesFil(ordbok, filnavn):
    fil = open(filnavn)

    for linje in fil:
        info = linje.split(',')
        for entry in ordbok:
            if entry == info[0]:
                if float(ordbok[entry]) < float(info[2]):
                    ordbok[entry] = info[2]

    fil.close()
    return ordbok

def skrivFil(ordbok, filnavn):
    fil = open(filnavn, "w")

    for entry in ordbok:
        info = entry + "," + str(ordbok[entry])
        fil.write(info)

    fil.close()


konverterFilRes = konverterFil(tempMonth)
lesFilRes = lesFil(konverterFilRes, tempDaily2018)
skrivFil(lesFilRes, updatedTempMonth)
