import csv

class Item:
    #attributi di classe 
    sconto = 0.8
    archivio = [] 
    
    def __init__(self, name: str, price: float, quantity=1):
        
        # Validazione dei parametri del costruttore
        assert price >= 0, f"Prezzo negativo {price} non consentito."
        assert quantity > 0, f"Quantità negativa {quantity} non consentita."         

        self._name = name
        self._price = price
        self._quantity = quantity
        
        # Archiviazione di item istanziato
        Item.archivio.append(self)
        
    def prezzo_totale(self):
        return self._price * self._quantity

    def get_name(self):
        return self._name
    
    def applica_sconto(self):
        self._price = self._price * self.sconto
        
    def __repr__(self) -> str:
        return f"\nNome dell'item: {self.get_name()}, prezzo unitario: {self._price} e quantità: {self._quantity}\n"
        
    @classmethod #decoratore per aprire il file
    def crea_items_da_csv(cls):
        with open(r'C:\Users\matteo.sala\Documents\Udemy Courses\Udemy - Master Course\16 - csv\items.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            items = list(reader)
            
            for i in items:
                Item(
                    name=i.get('name'), 
                    price=float(i.get('price')), 
                    quantity=int(i.get('quantity')),
                )
                
Item.crea_items_da_csv()
# print(Item.archivio)
            

item1 = Item("Penna", 1.5, 10)
item2 = Item("Quaderno", 3, 5)  
item3 = Item("Gomma", 1)

# print(f"Il prezzo totale dell'item {item1.get_name()} è {item1.prezzo_totale()}")
# print(f"Il prezzo totale dell'item {item2.get_name()} è {item2.prezzo_totale()}")
# print(f"Il prezzo totale dell'item {item3.get_name()} è {item3.prezzo_totale()}")

# print(Item.sconto)
# print(item1.sconto)

# print(Item.__dict__) #Restituisce tutti gli attributi a livello di classe
# print(item1.__dict__) #Restituisce tutti gli attributi a livello di istanza 

# item3.applica_sconto()
# print(f"Il prezzo scontato dell'item {item3.get_name()} è {item3.prezzo_totale()}")

# print(Item.archivio) 

for i in Item.archivio:
    print(f"Nome: {i.get_name()}, Prezzo: {i._price}, Quantità: {i._quantity}")