# vengono definiti iteratori tutti quegli oggetti che posso essere attraversati
# in python gli iteratori sono oggetti che implementano i metodi __iter__() e __next__()

list1 = [1,2,34,5,6,]

my_iter = iter(list1)

print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

# è sempre meglio andare a pescare i dati da un generatore che da una struttra dati consolidata per questioni di memoria

x = range(1,11)
print(x)

# print(next(x)) # questo provoca errore perché è un iterabile ma non un iteratore

print(next(iter(x)))