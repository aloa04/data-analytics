#Reto 1
print ('\n---- TASK 1----\n')
name:str = 'Pablo'
surname:str = 'Bottero'
age:float = '23'
email:str = 'botterogandia@gmail.com'
phone:float = '611639206'
married:bool = False
childs:bool = False
friends:str = ['Rafa', 'Ana', 'Belen', 'Javi']
films = {
    'film1' : 'Cruella',
    'film2' : 'Midsommar',
    'film3' : 'Oculus'
}
print (f'{name} {surname} has {age} years, his email is {email} and his phone is {phone}')
print (f'Do you think {name} is married? {married}. But has he childs? {childs}')
print (f'His friends are {friends} and with them he has seen some movies shuch as {films}, but the one he has liked the most is {films.get("film1")}.') 

'''
RETO 2
Escribe un programa capaz de mostrar todos los números impares desde un número de inicio y otro final.
Por ejemplo: teniendo numero_inicial = 2 y numero_final = 8, el programa debe imprimir por consola: [3, 5, 7]
'''
print(*range(1,20,2))

for i in range(1,20):
  if i%2!=0:
    print(i)

print(*[n for n in range(1,20) if n % 2 != 0])

'''
RETO 3
Escribe un programa que sea capaz de mostrar los números del 1 al 100 en orden inverso.
'''
print(*range(100,0, -1))

'''
RETO 4
Escribe un programa que sea capaz de mostrar los elementos de una lista en orden inverso al original.
Por ejemplo: teniendo [1,2,3,4,5] el programa debe mostrar por pantalla [5,4,3,2,1]
'''
nums = [1,2,3,4,5,6,7,8,9,10]
nums2 = list(reversed(nums))
print(*nums2)

'''
RETO 5
Escribe un programa que sea capaz de pedirle a un usuario por consola** que introduzca una contraseña y mientras que ésta no sea "admin", el programa seguirá pidiéndola
Si la contraseña es errónea, deberá sacarle un mensaje de error y volver a pedirle la contraseña hasta que la introduzca bien. Si el usuario introduce "admin" correctamente, el programa le deberá mostrar un mensaje "Bienvenido al programa señor ADMIN" y luego terminar.
NOTA: Para pedir por pantalla y guardarlo en una variable llamada password debes hacer uso de password:str = input('Introduce una contraseña')
'''
pswd = ''
while pswd != "admin":
  pswd = input('Intruduzca contraseña: ')
  if pswd != "admin":
    print('Error')
  if pswd == "admin":
    print("Bienvenido al programa señor ADMIN")
    break

'''
RETO 6
Escribe un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
'''
edad = int(input('¿Cuántos años tienes? '))
if edad >= 18:
  print('¡Ya eres mayor de edad!')
else:
  print('¡Aun eres menor de edad!')


'''
RETO 7
Escribe un programa que contenga dos variables. Una de ellas representa la contraseña de un usuario y la otra un texto introducido. El programa debe poder mostrar por pantalla si las dos cadenas de texto son iguales sin tener en cuenta mayúsculas y minúsculas.
'''
contra = input('Escribe una contraseña: ')
text = "elefante"
print('El texto y la contraseña son iguales?')
print(contra.lower() == text.lower())


'''
RETO 8
Escribe un programa que pueda decirte si un número (número entero) es primo o no
'''
num:int = ()
def es_primo(num):
  for n in range(2,num):
    if num % n == 0:
      print('El número', num, 'no es primo')
      return False
    else:
      print('El número', num, 'es primo')
      return True
print(es_primo(57))


'''
RETO 9
Escribe un programa que pueda decirte si un año (número entero) es bisiesto o no
Matemáticamente podemos saber si un año es bisiesto si este es múltiplo de 4. Si además es múltiplo de 100 no será bisiesto (ten en cuenta que 100 es múltiplo de 4 y por tanto cualquier número que sea múltiplo de 100 también es múltiplo de 4) a no ser que sea múltiplo de 400, que sí será bisiesto.
'''
año= int(input('Escribe un año: '))
if año % 4 == 0 and (año %100 != 0 or año %400 ==0):
    print ('El año', año, 'es bisiesto')
else:
   print('El año', año, 'no es bisiesto')


'''
RETO 10
Escribe un programa que guarde en una variable el siguiente contenido:
{'titulo':'El Más Allá','aka':'E tu vivrai nel terrore - Laldilà','director':'Lucio Fulci', 'año':1981, 'país':'Italia'}
'''
peli= {'titulo':'El Más Allá','aka':'E tu vivrai nel terrore - Laldilà','director':'Lucio Fulci', 'año':1981, 'país':'Italia'}
for x in peli:
  print(peli[x])


'''
RETO 11
Escribe un programa que pida al usuario los siguientes datos por consola:
Título de la película
Director
Año
País
E introduzca esos valores en una variable GLOBAL llamada "pelicula"
'''
print('Escribe lo siguiente:')
titulo = input('Titulo de una pelicula: ')
director = input('Director de la pelicula: ')
año = input('Año de la pelicula: ')
pais = input('Pais de la pelicula: ')
pelicula = [titulo, director, año, pais]
print(*pelicula)


'''
RETO 12
Escribe un programa que almacene en una lista (Array) todos los nombres de los alumnos del curso Programación para No Programadores y los muestre en por pantalla.
'''
alumnos = ['Pepe','Monica','Maria','Alex','Claudia','Diego']
print(*alumnos, sep= '\n')


'''
RETO 12 (repe)
Escribe una función que calcule el área de un triángulo, recibiendo la altura y la base como parámetros y otra función que calcule el área de un círculo recibiendo el radio del mismo.
'''
altura = int(input('Altura del triángulo: '))
base = int(input('Base del triángulo: '))
def areatri(base, altura):
  print('Área del triángulo: ', (base*altura)/2)

areatri(base,altura)

from math import pi
radio = float(input('Escribe el radio del círculo: '))
def areacir(radio):
  print('Área del círculo: ', (pi*(radio**2)))
  
areacir(radio)


'''
RETO 13
Escribe una función que use la función del área del círculo para devolver el volumen de un cilindro, obteniendo por parámetro la longitud del mismo.
'''
circulo = pi * radio**2
altura = float(input('Escribe la altura del cilindro: '))
def cilindro (circulo, altura):
  print('Volumen del cilindro: ', circulo*altura)

cilindro(circulo, altura)

'''
RETO 14
Escribe una función que reciba una muestra de números en una lista y devuelva otra lista con sus cuadrados.
'''
def square(*sample):
    list = []
    for i in sample:
        list.append(i**2)
    return list

print(square(1, 2, 3, 4, 5))


'''
RETO 15
Crea un script que sea capaz de restar dos fechas y muestra el resultado por consola
'''
import datetime
hoy = datetime.date.today()
fecha = datetime.date(2021,7,23)
print(hoy-fecha)


'''
RETO 16
Partiendo de la siguiente tupla:
tupla = (2, 4, 3, 5, 4, 6, 7, 8, 6, 1)
Realiza las siguientes operaciones:
Encontrar los elementos de 3 a 5
Encontrar los 6 primeros elementos
Muestra la tupla desde el 5 elemento hasta el final
Muestra toda la tupla haciendo uso de [:]
Muestra todos los elementos desde la posición 2 a la 9 de dos en dos
Devuelve la tupla con un salto cada 4 elementos
Usa un step negativo para mostrar la tupla desde la posición 9 a la 2
'''
nums = 2,4,3,5,4,6,7,8,6,1
print(nums[3:6])
print(nums[:6])
print(nums[5:])
print(nums[:])
print(nums[2:9:2])
print(nums[::4])
print(nums[9:1:-1])


'''
RETO 17
Crea una función que sea capaz de eliminar un caracter concreto de una cadena de texto. La función debe tener la siguiente forma:
def eliminar(str, n):
    # TODO: Esto debes completarlo
    # Pista, haz uso de [start:end:step]

# De modo que:
print(eliminar('Madrid', 0)) #adrid
print(eliminar('Madrid', 3)) #Madid
print(eliminar('Madrid', 5)) #Madri
'''
def eliminar(str, n):
  return str.replace(str[n], "", 1)

print(eliminar('Madrid', 0))
print(eliminar('Madrid', 3))
print(eliminar('Madrid', 5))