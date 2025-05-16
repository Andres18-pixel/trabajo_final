#Ejercicio 2: Uso de computadoras en laboratorios
#Implemente un programa que simule el estado de uso de computadoras en dos laboratorios del campus. 
# #Cada laboratorio contiene cinco filas de cuatro computadoras. 
# #Por cada computadora se debe registrar si está ocupada o libre (puede ingresarse manualmente o simularse con valores aleatorios). 
# Al finalizar, el programa debe mostrar el resumen de computadoras ocupadas y libres por laboratorio.


# Creamos dos matrices vacías para los laboratorios
laboratorio1 = [[0 for _ in range(4)] for _ in range(5)]
laboratorio2 = [[0 for _ in range(4)] for _ in range(5)]

# Función para llenar manualmente los datos de un laboratorio
def llenar_laboratorio_manual(lab_numero, lab):
    print(f"\nIngrese los datos para el Laboratorio {lab_numero}:")
    for fila in range(5):
        for columna in range(4):
            while True:
                try:
                    estado = int(input(f"Computadora en fila {fila + 1}, columna {columna + 1} (0 = libre, 1 = ocupada): "))
                    if estado in [0, 1]:
                        lab[fila][columna] = estado
                        break
                    else:
                        print("Solo se permite 0 (libre) o 1 (ocupada).")
                except ValueError:
                    print("Por favor, ingrese un número válido (0 o 1).")

# Función para contar computadoras ocupadas y libres
def contar_estado(lab):
    ocupadas = 0
    libres = 0
    for fila in range(5):
        for columna in range(4):
            if lab[fila][columna] == 1:
                ocupadas += 1
            else:
                libres += 1
    return ocupadas, libres

# Llenar los dos laboratorios manualmente
llenar_laboratorio_manual(1, laboratorio1)
llenar_laboratorio_manual(2, laboratorio2)

# Contar ocupadas y libres en cada laboratorio
ocupadas1, libres1 = contar_estado(laboratorio1)
ocupadas2, libres2 = contar_estado(laboratorio2)

# Mostrar resultados
print("\nResumen de uso:")
print("Laboratorio 1:")
print(f"Computadoras ocupadas: {ocupadas1}")
print(f"Computadoras libres: {libres1}")

print("\nLaboratorio 2:")
print(f"Computadoras ocupadas: {ocupadas2}")
print(f"Computadoras libres: {libres2}")



