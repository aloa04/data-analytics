'''
Write a program that is able to ask a user by console** to enter a password and as long as the password is not "admin", the program will keep asking for it.
'''

def task5():
  pswd = ''
  while pswd != "admin":
    pswd = input('Intruduzca contraseña: ')
    if pswd != "admin":
        print('Error')
    if pswd == "admin":
        print("Bienvenido al programa señor ADMIN")
    break