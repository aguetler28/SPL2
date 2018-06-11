# strings.py

# Erweiterung
# Eingabe
# Alexander Xaver Franz Maximilian Friedrich
# 
# Ausgabe
# Rednaxela Revax Znarf Nailimixam Hcirdeirf

def ReverseString(text):
    rev = ""
    von = len(text)-1
    bis = -1
    aendern = -1
    for i in range (von, bis, aendern):
        ch = text[i]
        rev = rev + ch
    return rev
    

eingabe = input("Hallo: wer bist du? ")
print ("Normal : ", eingabe)
print ("Reverse: ", ReverseString(eingabe))

for i in range (0,len(eingabe)):
    print(eingabe[i], end=".")
print()

von = len(eingabe)-1
bis = -1
aendern = -1

for i in range (von, bis, aendern):
    ch = eingabe[i]
    if (i == von):
        ch = ch.upper()
    if (i == 0):
        ch = ch.lower()
    print(ch, end=".")
print()
