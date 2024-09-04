from myfuntions import operAritmetic
from myfuntions import calcIva as Iva
print("Hola Mundo desde Python")
'''
Este es un comentario de una línea
'''
# Éste es un comentario de una línea
# Definición de variables
firstName = "Pedro"
lastName = "Gomez"
print(type(firstName))
salaryEmployee = 5000000
gender = False
# Lista
numbers = [1, 2 , 3, 4, 5, 6, 7]
# Tupla
todd = (1, 3, 5, 7, 9)
# Set
tpair = {10, 20, 30, 40}
# Diccionario
person = {"cc":"1234","name":"Jonh Doe","phone":"3105632147","gender":False,"salary":3200000}
# Arreglo de objetos
persons = [
    {"id":3,"firstName":"Jane Doe","address":"Calle 8 # 8-8"},
    {"id":4,"firstName":"Peter Parker","address":"Kra 9 # 10-14"},
    {"id":6,"firstName":"Simone Biles","address":"Trans 2 # 7-8"},
]
# Condicional
'''
if not gender:
    print("El empleado es Hombre")
else:
    print("El empleado es Mujer")
'''
# Operador ternario u operador condicional
print("Es Hombre" if not gender else "Es Mujer")
comission = salaryEmployee * 10/100 if gender and salaryEmployee > 4000000 else salaryEmployee * 2/100
print(f"Comision: {comission}")
print("Comision otra vez: ", comission)
category = "A"
valuePay = 0
if category == "A":
    valuePay = 5000
elif category == "B":
    valuePay = 10000
elif category == "C":
    valuePay = 20000
elif category == "D":
    valuePay = 30000
else:
    valuePay = 1000
    
    print(f"Valor a pagar: {valuePay}")
# Ciclo para (for)
initial = 1
limit = 6

for i in range(initial,limit):
    #Éste código es más rápido
    '''
    if i < limit - 1:
    print(i,end=",")
else:
    print(i)
    '''
    # Éste código es más corto
    print(i, end=", " if i < limit -1 else "")
    
    # Ciclos para recorrer objetos iterables
    print("iteración en listas, tuplas, diccionario, etc")
    for nro in numbers:
        print(nro)
print("____________")
for i in range(0,len(numbers)):
     print(numbers[i])

# Cantidad de numeros pares e impares

countEven = 0,
countDdd = 0
for num in numbers:
    if num % 2 == 0:
        countEven += 1
    else:
        countDdd += 1
        # Prueba de cambio para este archivo
        print("Estamos haciendo prueba con el sistema de control de versiones")
        
        