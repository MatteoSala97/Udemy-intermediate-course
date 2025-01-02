list = []
for i in range(11):
    list.append(i*2)
print(list)

list2 = [i*2 for i in range(11)]
print(list2)

list3 = [i for i in range(21) if i%2==0 and i%5==0]
print(list3)
