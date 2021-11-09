from RETOS.MODELS.persona import Persona

class Empleado(Persona):
    puesto:str
    hora:float
    hTrabajados:int = 0
    #cobro: float = 0.0
    
    
    def __init__(self,nombre, apellidos, edad, puesto, hora, hTrabajados):
      super(Empleado, self).__init__(nombre, apellidos, edad)
      self.puesto = puesto
      self.hora = hora
      self.hTrabajados = hTrabajados
    
    def trabajar(self, horas:int):
      self.hTrabajados += horas
      print('Hola,' , self.nombre, 'trabajas', self.hTrabajados, 'horas')

    def cobrar(self):
      cobro = self.hora*self.hTrabajados
      print('Cobras', cobro, '€')