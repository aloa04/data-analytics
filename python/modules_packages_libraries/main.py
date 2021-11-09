'''
#Archivo main.py
#from RETOS.utilidades.interacciones.cordialidad import saludar
#from RETOS.utilidades.kpis import puntuacion
#from HTTP_REQUESTS.chuck_norris_dice import obtenerChiste
#from RETOS.MODELS.coche import Coche
#from RETOS.MODELS.persona import Persona
#from RETOS.MODELS.Empleado import Empleado
from animal import Animal
from carnivoro import Carnivoro
from herbivoro import Herbivoro
from omnivoro import Omnivoro
#puntos = puntuacion(0)
 
#print(f'{saludar("Pedro")} tu puntuación es de {puntos}')
 
#Lo ejecutamos
#obtenerChiste()

#miCoche: Coche = Coche('Fiat', 'Punto', 'Negro', '6451FMB', '123', 'Martín')
  
#miCoche.acelerar(presion=3)

#yo: Persona = Persona('Rafa', 'Perez Solans','22')
#yo.saludar()

#employee: Empleado = Empleado('Rafa', 'Perez Solans',22,'Desarrollador', 50, 5)
#employee.saludar()
#employee.cobrar()
#employee.trabajar(2)

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