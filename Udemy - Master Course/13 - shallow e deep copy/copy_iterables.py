# shallow copy e deep copy

l1 = [1, 2, [3,4], (5,11)]
l2 = list(l1)

print(l2==l1)

# problema della shallow copy - come dice il nome è una copia superficiale
# gli elementi lista e tupla etc. vengono reindirizzati, non copiati
# questo genera problematiche a livello di modifiche

#utilizzo della deep copy

import copy 
l1 = [1, 2, [3,4], (5,11)]
l2 = copy.deepcopy(l1)

print(l2 == l1)