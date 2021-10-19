#Task 1
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

#Task 2
print ('\n---- TASK 2----\n')
start, end = 1, 32
for num in range(start, end + 1):
	if num % 2 != 0:
		print(num, end = " ")

#Task 3
print ('\n---- TASK 3----\n')
my_range = range(1, 101)
reversed_range = reversed(my_range)
for number in reversed_range:
    print(number)

#Task 4
print ('\n---- TASK 4----\n')
number_list = [1, 2, 3, 4, 5]
print(*number_list[::-1])

#Task 5
print ('\n---- TASK 5----\n')
password = ""
while password != "admin":
    password = input("Please enter the password: ")
    if password == "admin":
        print("Perfectteh password is correct.")
    else:
        print("Ups... The password is incorrect, you have to try again")