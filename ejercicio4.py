# Código del ejercicio 4
edificios = 4
dias = 7
turnos = ["mañana", "tarde", "noche"]


consumos_totales = []

for e in range(edificios):
    print(f"\nEdificio {e + 1}:")
    total = 0
    for d in range(dias):
        print(f"  Día {d + 1}:")
        for t in turnos:
            consumo = float(input(f"    Consumo en {t} (kW): "))
            total += consumo
    consumos_totales.append(total)

for i in range(edificios):
    promedio = consumos_totales[i] / dias
    print(f"\nEdificio {i + 1}:")
    print(f"  Consumo total semanal: {consumos_totales[i]:.2f} kW")
    print(f"  Promedio diario: {promedio:.2f} kW")
