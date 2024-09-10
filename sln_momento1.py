
'''
#Ejercicio1
num_primero = 5
num_segundo = 8
lista_e1 = [5,8]
for i in range(98):
    num_ronda = num_primero + num_segundo
    if num_ronda!=13:
       lista_e1.append(num_ronda)
    
    num_primero = num_segundo
    num_segundo = num_ronda
print(lista_e1)
'''    

'''
#Ejercicio2
registro = {}

def llenar_registro(clave):
    if clave == 'nombre':
        registro[clave] = input("Ingrese el nombre: ")
    elif clave == 'salario_base':
        registro[clave] = float(input("Ingrese el salario base: "))
    elif clave == 'seguridad_social':
        registro[clave] = registro['salario_base']*0.185
    elif clave == 'salario_total': 
        registro[clave] = registro['salario_base'] + registro['seguridad_social'] + registro['comisiones']   
    else:
        registro[clave] = float(input("Ingrese total comisiones del mes: "))


n = int(input("Introduzca la cantidad de registros que desee crear: ")) #aquí se puede indicar que son los 1897 empleados

ArrDict = []
i = 0
while i < n:
    print(f"Registro {i + 1}:")
    # Crear un nuevo diccionario para cada registro
    registro = {}
    llenar_registro('nombre')
    llenar_registro('salario_base')
    llenar_registro('seguridad_social')
    llenar_registro('comisiones')
    llenar_registro('salario_total')
    # Añadir el registro a la lista
    ArrDict.append(registro.copy())    
    i += 1

print("Registros completos:")
print(ArrDict)
'''

'''
#Ejercicio3
n = int(input("Introduzca la cantidad de números a ingresar: "))  #aquí se puede indicar que se van a introducir 400 números
numeros = []

i=0
while i < n:
    numeros.append(int(input("ingrese un número: ")))
    i += 1

pares = []
impares = []
for i in range(len(numeros)):
    if numeros[i]%2==0:
        pares.append(numeros[i])
    else: impares.append(numeros[i])

print(f"Cantidad de números pares: {len(pares)}")
print("Listado de los números pares")
print(pares)

print(f"Cantidad de números impares: {len(impares)}")
print("Listado de los números impares")
print(impares)
'''

'''
#Ejercicio4
#Código para hacer el llenado de los niveles de leucemia de 803 pacientes
registro = {}

def llenar_registro(clave):
    if clave == 'nombre':
        registro[clave] = input("Ingrese el nombre del paciente: ")   
    else:
        registro[clave] = float(input("Ingrese el puntaje para determinar el nivel de leucemia del paciente: "))


n = int(input("Introduzca la cantidad de registros que desee crear: ")) #aquí se puede indicar que son los 803 empleados

ArrDict = []
i = 0
while i < n:
    print(f"Registro {i + 1}:")
    # Crear un nuevo diccionario para cada registro
    registro = {}
    llenar_registro('nombre')
    llenar_registro('puntaje')
    # Añadir el registro a la lista
    ArrDict.append(registro.copy())    
    i += 1

print("Registros completos:")
print(ArrDict)

#Código para recorrer cada registro y clasificar a los pacientes en algún nivel de leucemia de acuerdo con el puntaje dado
for j in range(len(ArrDict)):
    puntaje = ArrDict[j]['puntaje']
    nombre = ArrDict[j]['nombre']
    if puntaje <= 10:
        print(f"{nombre} no tiene leucemia")
    elif 11 <= puntaje < 40:
        print(f"{nombre} nivel bajo de leucemia")
    elif 40 <= puntaje < 69:
        print(f"{nombre} nivel moderado de leucemia")
    else:
        print(f"{nombre} nivel grave de leucemia")
'''

'''
#Ejercicio5
#Código para hacer el llenado del puntaje de funcionamiento de 407 cabinas de metroclave
registro = {}

def llenar_registro(clave):
    if clave == 'cabina_numero':
        registro[clave] = input("Ingrese el número de la cabina de metro cable: ")   
    else:
        registro[clave] = float(input("Ingrese el puntaje para determinar el funcionamiento de la cabina: "))


n = int(input("Introduzca la cantidad de registros que desee crear: ")) #aquí se puede indicar que son las 407 cabinas del metro cable

ArrDict = []
i = 0
while i < n:
    print(f"Registro {i + 1}:")
    # Crear un nuevo diccionario para cada registro
    registro = {}
    llenar_registro('cabina_numero')
    llenar_registro('puntaje')
    # Añadir el registro a la lista
    ArrDict.append(registro.copy())    
    i += 1

print("Registros completos:")
print(ArrDict)

#Código para recorrer cada registro y clasificar a los pacientes en algún nivel de leucemia de acuerdo con el puntaje dado
for j in range(len(ArrDict)):
    puntaje = ArrDict[j]['puntaje']
    nombre = ArrDict[j]['cabina_numero']
    if puntaje == 2:
        print(f"Cabina número {ArrDict[j]['cabina_numero']} tiene funcionamiento defectuoso")
    elif puntaje == 3:
        print(f"Cabina número {ArrDict[j]['cabina_numero']} tiene funcionamiento moderado")
    else:
        print(f"Cabina número {ArrDict[j]['cabina_numero']} tiene funcionamiento óptimo")
'''