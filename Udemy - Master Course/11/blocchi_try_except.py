nomi = ['marco', 'luca','giovanni','antonio','matteo']

try: 
    nomi.remove('marta')
except ValueError:
    print("Nome non presente nella lista")
    
print(f"{nomi}")

