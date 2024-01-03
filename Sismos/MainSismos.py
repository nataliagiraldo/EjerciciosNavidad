from CiudadesM import registrarCiudad, buscarCiudad
from SismosM import registrarSismo
from MRiesgos import informeRiesgo



ciudades = {}
isActive = True

while (isActive):

    print("MENU PRINCIPAL ")
    print("""
            1. Registrar Ciudad
            2. Registrar Sismo
            3. Buscar sismos por ciudad
            4. Informe de riesgo
            5. Salir 
          """)
    try:
        opMenu = int(input("Selecciona una opción "))
    except ValueError:
        print("Ingrese un dato válido")
        opMenu = int(input("Selecciona una opción "))

    if opMenu == 1:
        if len(ciudades) < 5:
            registrarCiudad(ciudades)
        else:            
            print("Ya se ha alcanzado el maximo de ciudades registradas ") 
    elif opMenu == 2: 
        registrarSismo(ciudades)   
    elif opMenu == 3:
        buscarCiudad(ciudades)
    elif opMenu == 4:
        informeRiesgo(ciudades)
    elif opMenu == 5:
        isActive = False
