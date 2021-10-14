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