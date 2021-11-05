from models.animal_kingdom.carnivoro import Carnivoro
from models.animal_kingdom.herbivoro import Herbivoro

class Omnivoro(Carnivoro, Herbivoro):

  def __init__ (self, edad, patas, ruido, nombre):
    super(Omnivoro, self).__init__(edad, patas, ruido, nombre)

  def comer(self, alimento):
    self.kgComida += alimento
    print(f'{self.nombre} ha comido {self.kgComida} kg de vegetales')