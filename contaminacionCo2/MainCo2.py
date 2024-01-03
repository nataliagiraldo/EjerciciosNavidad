from dependencias import registrarDependencia, registrarConsumo
from CalculosCo2 import co2Producido, mayorCo2

isActive = True
dependencias = {}

while isActive:
    print("\nMenú Principal:")
    print("1. Registrar Dependencia")
    print("2. Registrar Consumo por Dependencia")
    print("3. Ver CO2 Producido")
    print("4. Dependencia que Produce Mayor CO2")
    print("5. Salir")

    opcion = int(input("Ingrese el número de la opción deseada: "))

    if opcion == 1:
        registrarDependencia(dependencias)
    elif opcion == 2:
        registrarConsumo(dependencias)
    elif opcion == 3:
        co2Producido(dependencias)
    elif opcion == 4:
        mayorCo2(dependencias)
    elif opcion == 5:
        print("Saliendo del programa. ¡Hasta luego!")
        isActive = False
    else:
        print("Opción no válida. Por favor, ingrese un número del 1 al 5.")
        