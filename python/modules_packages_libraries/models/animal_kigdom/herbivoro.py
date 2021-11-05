from models.animal_kingdom.animals import Animal

class Herbivoro(Animal):

  def __init__ (self, edad, patas, ruido, nombre):
    super(Herbivoro, self).__init__(edad, patas, ruido, nombre)

  def comer(self, alimento):
    self.kgComida += alimento
    print(f'El {self.nombre} ha comido {self.kgComida} kg de vegetales')