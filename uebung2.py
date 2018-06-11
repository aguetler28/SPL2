# Zahlen einlesen
liste = []
eingabe = ""
while(eingabe != "q"):
    eingabe = input("Bitte eine Zahl eingeben: ")
    if (eingabe != "q"):
        zahl = int(eingabe)
        liste.append(zahl)

print("ende.")

liste.sort()
print(liste)
