# roulette.py
import random
zahlen = []
anzahlWuerfe = input("Wie oft soll Roulette simuliert werden? ")
anzahlWuerfe = int(anzahlWuerfe)
for i in range (0,anzahlWuerfe):
    wurf = random.randint(0,36) 
    zahlen.append(wurf)
    # print(wurf, end="...")

print ()
print ("Ergebnis: ")
# print (zahlen)

for i in range(0,37):
    print (i,"er :", zahlen.count(i))


