from productos import (
    registrarProducto,
    visualizacionProducto,
    actualizacionStock,
    productosCriticos,
    gananciaPotencial
)
import os
productos = {} 
isActive = True

print("MENU PRINCIPAL")
while isActive:
    print("1. Registrar Productos\n2. Visualizar Productos\n3. Actualizar Stock\n4. Informe de Productos Críticos\n5. Calcular Ganancia Potencial\n6. Salir")
    rta = int(input("Seleccione la opcion a realizar "))
    if rta == 1:
        os.system('clear')
        productoRegistrado = registrarProducto(productos)
    if rta == 2:
        os.system('clear')
        visualizacionProducto(productoRegistrado)
    if rta == 3:
        os.system('clear')
        actualizacionStock(productoRegistrado)
    if rta == 4:
        os.system('clear')
        productosCriticos(productoRegistrado)
    if rta == 5:
        os.system('clear')
        gananciaPotencial(productoRegistrado)
    if rta == 6:
        os.system('clear')
        isActive = False