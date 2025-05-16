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
def llenar_laboratorio(laboratorio):
    fila = 0
    while fila < 5: # Hay 5 filas
        columna = 0
        while columna < 4:
            laboratorio[fila][columna] = random.randint(0, 1) # Hay 4 columnas
            columna += 1
        fila += 1

# Función para contar y mostrar la cantidad de computadoras libres y ocupadas
def mostrar_estado(lab, nombre):
    ocupadas = 0
    libres = 0

    fila = 0
    while fila < 5:
        columna = 0
        while columna < 4:
            if lab[fila][columna] == 1:
                ocupadas += 1  # Si es 1, está ocupada
            else:
                libres += 1   # Si es 0, está libre
            columna += 1
        fila += 1

        # Mostrar resultados
    print(f"\nResumen del {nombre}:")
    print(f"Computadoras ocupadas: {ocupadas}")
    print(f"Computadoras libres: {libres}")

# Llenamos ambos laboratorios con valores aleatorios
llenar_laboratorio(laboratorio1)
llenar_laboratorio(laboratorio2)

# Mostramos los resultados
mostrar_estado(laboratorio1, "Laboratorio 1")
mostrar_estado(laboratorio2, "Laboratorio 2")



