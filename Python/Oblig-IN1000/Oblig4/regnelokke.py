#Oppgave 2 : Regning med løkker
tall = int(input("tast inn tall: "))
num = []
minSum = 0

while tall != 0:
    num.append(tall)
    tall = int(input("tast inn tall: "))

for x in range(0, len(num)):
    minSum += num[x]

print(minSum)

#finn storste
storste = num[0]
for x in num:
    if storste < x:
        storste = x
print(storste)

#finn minste
minste = num[0]
for x in num:
    if minste > x:
        minste = x
print(minste)
