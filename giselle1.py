# Ejercicio 1: Registro de asistencia académica
# Desarrolle un programa que registre la asistencia de estudiantes en tres secciones distintas de la UAM, durante cinco días de clases. 
# Cada día se tomará asistencia a seis estudiantes por sección. 
# El programa deberá contabilizar y mostrar el total de asistencias registradas por sección, así como el total general de la semana.

secciones = ['A', 'B', 'C']
dias=5
estudiantes_por_seccion=6

asistencias = {seccion:0 for seccion in secciones}

for dia in range (1,dias+1):
    print(f"\nDía {dia}: ")