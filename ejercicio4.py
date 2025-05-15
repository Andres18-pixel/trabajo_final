NUM_EDIFICIOS = 4
DIAS_SEMANA = 7
TURNOS = ["mañana", "tarde", "noche"]

consumo = [[[0 for _ in range(3)] for _ in range(DIAS_SEMANA)] for _ in range(NUM_EDIFICIOS)]


for edificio in range(NUM_EDIFICIOS):
    print(f"\nEdificio {edificio + 1}:")
    for dia in range(DIAS_SEMANA):
        print(f"  Día {dia + 1}:")
        for turno in range(3):
            kilovatios = float(input(f"    Consumo en turno {TURNOS[turno]} (kWh): "))
            consumo[edificio][dia][turno] = kilovatios

for edificio in range(NUM_EDIFICIOS):
    total_edificio = 0
    for dia in range(DIAS_SEMANA):
        total_dia = sum(consumo[edificio][dia])
        total_edificio += total_dia
    promedio_semanal = total_edificio / DIAS_SEMANA
    print(f"\nEdificio {edificio + 1}:")
    print(f"  Consumo total semanal: {total_edificio:.2f} kWh")
    print(f"  Promedio diario semanal: {promedio_semanal:.2f} kWh")
