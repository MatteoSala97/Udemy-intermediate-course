auto = {
    "marca" : "Volkswagen",
    "modello" : "Golf",
    "alimentazione" : "Benzina",
    "cambio_automatico" : True,
    "cilindrate" : [999, 1200, 1500, 2000]
}

marca = auto["marca"]
marca = auto.get("marca")

print(marca)

chiavi = auto.keys()
valori = auto.values()

print(chiavi)
print(valori)