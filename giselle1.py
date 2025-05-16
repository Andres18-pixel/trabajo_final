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
    for seccion in secciones:
        print(f"Asistencia para sección {seccion}: ")
        
        asistencia_dia=0
        for estudiante in range(1, estudiantes_por_seccion + 1):
            asistencia=input(f"Estudiante {estudiante} estuvo presente? (s/n): ")
            if asistencia.lower()=='s':
                asistencia_dia +=1
                
        asistencias[seccion] +=asistencia_dia
        print(f"Total de asistencias en sección {seccion} para el día {dia}: {asistencia_dia}")
        
print("\nResumen de asistencias:")
total_general=0
for seccion, total in asistencias.items():
    print(f"Sección {seccion}: {total} asistencias")
    total_general += total
    
print(f"Total general de asistencias de la semana: {total_general}")
        