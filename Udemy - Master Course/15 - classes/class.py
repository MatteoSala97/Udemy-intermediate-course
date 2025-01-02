class Persona:
    età = 30
    nome = "Mario"

#istanzio un oggetto
p1 = Persona()
print(p1.età,p1.nome)

# -----------------------------------------

class Persona:
  def __init__(self, nome, età):
    self.nome = nome
    self.età = età

p2 = Persona("Luigi",40)
print(p2.età,p2.nome)

# -----------------------------------------

class Persona:
  def __init__(self, nome, età):
    self.nome = nome
    self.età = età

  def saluti(self):
      print("Ciao, il mio nome è: " + self.nome)


p3 = Persona("Luigi",40)
print(p3.età,p3.nome)
p3.saluti()

# -----------------------------------------

p3.età = 45
p3.nome = "Luigi Rossi"
print(p3.età,p3.nome)

# elimare un parametro o un oggetto

del p3.età 
del p3

# ereditarietà

class Tecnico(Persona):
  pass

t1 = Tecnico("Sergio Bianchi",30)
t1.saluti()

# esempio completo con attributo

class Tecnico(Persona):
  def __init__(self, nome, età, anno):
    super().__init__(nome, età)
    self.inizioAttività = anno

t2 = Tecnico("Lisa Giallo", 35, 2019)

# esempio completo con metodo specializzato

class Tecnico(Persona):
  def __init__(self, nome, età, anno):
    super().__init__(nome, età)
    self.inizioAttività = anno

  def saluti(self):
      print("Ciao, il mio nome è: " + self.nome + " sono Tecnico dall'anno: " + str(self.inizioAttività))

t3 = Tecnico("Mirco Bruno", 40, 2015)

t3.saluti() 
