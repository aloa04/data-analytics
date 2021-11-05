class Animal():
    edad:int
    patas:int
    ruido:str
    nombre: str
    kgComida: float = 0
    
    def __init__(self, edad, patas, ruido, nombre):
      self.edad =edad
      self.patas = patas
      self.ruido = ruido
      self.nombre = nombre
    
    def comer(self, alimento):
      self.kgComida += alimento
      print('Hola,', self.nombre, 'comes', self.kgComida)

    def hacerRuido(self):
      print('Hola', self.nombre, 'haces' , self.ruido)