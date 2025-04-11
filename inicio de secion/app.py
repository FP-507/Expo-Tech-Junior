"""ESTA ES UNA VERSION BASICA, SE VA A CREAR UNA VERSION MAS ESTETICA Y MEJORADA CON FLET, TAMBIEN SE INTENTARA AÑADIR EL SISTEMA DE MEDALLAS A LA BASE DE DATOS Y ENLAZARLO CON ESTO"""

import csv 

def Autenticar(user,password): 

    with open('inicio de secion\BaseDeDatos.csv', 'r') as archivo: 
        lector = csv.DictReader(archivo)
        
        for fila in lector:

            if fila["username"] == user and fila["password"] == password:

                return True
        
        return False


usuario = input('Cual es tu nombre de usuario: ')

contrasena = input('Cual es tu contraseña: ')

if Autenticar(usuario,contrasena):

    print("Bienvenido al programa")
else:

    print("Usuario o contrasena incorrectas")
      
