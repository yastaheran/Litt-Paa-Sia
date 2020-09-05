ordbok = {
    "Kari" : ["brød", "egg", "pølser"],
    "Ali" : ["brød", "egg", "lam"],
    "Solveig" : ["egg", "salami", "pølser"]
}

def printMatplanFor(navn):
    if navn in ordbok:
        print("Matplan for " + navn + ": " + str(ordbok[navn]))
    else:
        print("Beboer finnes ikke.")

navn = input("Skriv navnet på en beboer: ")
printMatplanFor(navn)
