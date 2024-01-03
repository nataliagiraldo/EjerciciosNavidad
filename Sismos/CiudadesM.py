def registrarCiudad(ciudades : dict) -> dict:
   contCiudad = 0
   while contCiudad < 5:
    ciudad = input("Ingrese el nombre de la ciudad: ")
    print(f"La ciudad {ciudad} ha sido registrada exitosamente.")
    ciudades[ciudad] = {
        "sismos": {
            "magnitudSismo": [],
            "fechaSismo": []
        }
    }
    contCiudad += 1

def buscarCiudad(ciudades: dict):
    ciudad_buscar = input("Ingrese el nombre de la ciudad que desea buscar: ")

    if ciudad_buscar in ciudades:
        info_ciudad = ciudades[ciudad_buscar]
        print(f"Información de la ciudad {ciudad_buscar}:")
        print(f"Sismos registrados: {len(info_ciudad['sismos']['magnitudSismo'])}")

        if len(info_ciudad['sismos']['magnitudSismo']) > 0:
            print("Detalles de los sismos:")
            for i in range(len(info_ciudad['sismos']['magnitudSismo'])):
                magnitud = info_ciudad['sismos']['magnitudSismo'][i]
                fecha = info_ciudad['sismos']['fechaSismo'][i]
                print(f"  Sismo {i + 1}: Magnitud {magnitud}, Fecha {fecha}")
    else:
        print(f"La ciudad {ciudad_buscar} no está registrada.")