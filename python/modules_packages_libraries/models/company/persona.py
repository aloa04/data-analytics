class Persona():
    nombre:str
    apellido:str
    edad:int
    
    
    def __init__(self, nombre, apellidos, edad):
      self.nombre = nombre
      self.apellidos = apellidos
      self.edad = edad
    
    def saludar(self):
      print('Hola, me llamo', self.nombre, self.apellidos, 'y tengo ' ,self.edad, 'años')

