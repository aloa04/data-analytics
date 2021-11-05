'''
from models.animal_kingdom.animals import Animal
leon = animal(3, 4, 'roar', 'león')
leon.hacerRuido()

from models.animal_kingdom.carnivoro import Carnivoro 
leon = Carnivoro(3, 4, 'roar', 'leon', 'vianda')
leon.comer(20, 'vianda')

from models.animal_kingdom.herbivoro import Herbivoro 
vaca = Herbivoro(3, 4, 'muu', 'vaca')
vaca.hacerRuido()
vaca.comer(20)
'''
from models.animal_kingdom.omnivoro import Omnivoro 
pepe = Omnivoro(40, 2, 'Ye compare', 'Pepe')
pepe.hacerRuido()
pepe.comer(3)