#Ejercicio 2: Uso de computadoras en laboratorios
#Implemente un programa que simule el estado de uso de computadoras en dos laboratorios del campus. 
# #Cada laboratorio contiene cinco filas de cuatro computadoras. 
# #Por cada computadora se debe registrar si está ocupada o libre (puede ingresarse manualmente o simularse con valores aleatorios). 
# Al finalizar, el programa debe mostrar el resumen de computadoras ocupadas y libres por laboratorio.

import random # Importamos el módulo random para generar números aleatorios

# Crear dos matrices para los laboratorios, llenas con ceros inicialmente
laboratorio1 = [[0, 0, 0, 0] for _ in range(5)]
laboratorio2 = [[0, 0, 0, 0] for _ in range(5)]

# Función para llenar una matriz con valores aleatorios entre 0 y 1
def llenar_aleatorio(laboratorio):
    fila = 0
    while fila < 5: # Hay 5 filas
        columna = 0
        while columna < 4:
            laboratorio[fila][columna] = random.randint(0, 1) # Hay 4 columnas
            columna += 1
        fila += 1



