#1. Crear una lista para guardar las ventas de 3 dias, 4 stands y 3 productos.
ventas = []
for dia in range(3):
    stands_dia = []
    print("Dia", dia + 1)
    for stand in range(4):
        productos_stand = []
        print("Stand", stand + 1)
        for producto in range(3):
            monto = float(input("Ventas del producto: " + str(producto + 1) + ": "))
            productos_stand.append(monto)
        stands_dia.append(productos_stand)
    ventas.append(stands_dia)

#2. Mostrar resumenes
print("\n--- RESULTADOS ---")

# Por dia
for dia in range(3):
    total_dia = 0
    for stand in range(4):
        total_dia += sum(ventas[dia][stand])
    print("Dia", dia + 1, "Total: $", total_dia)

# Por stand, en cada dia.
for dia in range(3):
    print("\nDia", dia + 1)
    for stand in range (4):
        total_stand = sum(ventas[dia][stand])
        print("Stand", stand + 1, "Total: $", total_stand)

#Total General
total_feria = 0
for dia in ventas:
    for stand in dia:
        total_feria += sum(stand)
print("\nTOTAL GENERAL DE LA FERIA: $", total_feria)