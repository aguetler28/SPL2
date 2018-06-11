# uebung3.py
import random
zahlen = []

for i in range (0,10):
    wurf = random.randint(1,6) 
    zahlen.append(wurf)
    print(wurf, end="...")

print ()
print ("Ergebnis: ")
print (zahlen)

for i in range(1,7):
    print (i,"er :", zahlen.count(i))


