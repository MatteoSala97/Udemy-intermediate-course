# generatore = sottoinsieme di iteratori e iterabili che hano una occupazione di memoria molto limitata
# in quanto il valore numerato viene generato a runtime e non è salvato in strutture dati

#esempio stupido di generatore
for i in range(6):
    print(i)
    
for i in range(0, 100, 5):
    print(i)
    
    
# generatore con comprehension

gen = (i/2 for i in [0,9,12,32] if i < 30)
for item in gen:
    print(item)