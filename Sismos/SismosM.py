def registrarSismo(ciudades: dict):
    for ciudad in ciudades:
        nCiudad = ciudad
        magnitudSismo = float(input(f"Ingrese la magnitud del sismo en la ciudad {nCiudad}: "))
        ciudades[ciudad]["sismos"]["magnitudSismo"].append(magnitudSismo)
        fechaSismo = input(f"Ingrese la fecha del sismo en la ciudad {nCiudad}: ")
        ciudades[ciudad]["sismos"]["fechaSismo"].append(fechaSismo)