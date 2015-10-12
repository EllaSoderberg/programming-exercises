# Programmeringsteknik webbkurs KTH inlämningsuppgift 1.
# Ella Söderberg
# 5/10-2015
"""Detta program undersöker hur många iterationer som behövs för att ett
fyrsiffrigt heltal (där inte alla fyra siffror har samma värde) genom Kaprekars
rutin ska komma fram till Kaprekars konstant, 6174. """

#Skriv in ett fyrsiffrigt tal

firstnumber = input("Skriv ett fyrasiffrigt heltal (ex. 3923) där inte alla fyra siffror har samma värde (ex. 4444): ")
newnumber = firstnumber
upcount = 0

#Kollar att alla fyra siffror inte är lika

while (all(x == newnumber[0] for x in newnumber)):
    firstnumber = input("Alla fyra siffror får inte ha samma värde. Skriv ett nytt fyrasiffrigt tal: ")
    newnumber = firstnumber
print("...")

#Kollar att talet är ett fyrsiffrigt heltal
    
while not (len(newnumber) == 4 and newnumber.isdigit()):
    firstnumber = input("Något stämmer inte med det du skrev in, skriv ett nytt fyrasiffrigt heltal: ")
    newnumber = firstnumber
print("..")

#Loopar Kaprekars rutin och skriver sedan ut antalet iterationer.
    
while (newnumber != "6174"):
    sort = sorted(newnumber)
    sortreverse = sorted(newnumber, reverse=True)
    small = int("".join(sort))
    large = int("".join(sortreverse))
    newnumber = str(large - small)
    newnumber = newnumber.zfill(4)
    upcount += 1
print("Antal iterationer för", firstnumber + ":", upcount)
