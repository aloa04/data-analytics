from models.animal_kingdom.animals import Animal

class Carnivoro(Animal):

  def __init__ (self, edad, patas, ruido, nombre):
    super(Carnivoro, self).__init__(edad, patas, ruido, nombre)

  def comer(self, alimento):
    self.kgcomida += alimento
    print(f'El {self.nombre} ha comido {self.kgcomida} kg de carne')