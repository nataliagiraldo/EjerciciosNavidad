def informeRiesgo(ciudades: dict):
    for ciudad in ciudades:
        suma = sum(ciudades[ciudad]["sismos"]["magnitudSismo"])
        riesgo = suma / len(ciudades[ciudad]["sismos"]["magnitudSismo"])
        if riesgo < 2.5:
            categoriaRiesgo = "Amarillo: sin riesgo"
        elif 2.5 <= riesgo < 4.5:
            categoriaRiesgo = "Naranja: riesgo medio"
        else:
            categoriaRiesgo = "Rojo: riesgo alto"
        print(f"La ciudad {ciudad} tiene un promedio de sismos de {riesgo} lo que la clasifica en un factor de riesgo {categoriaRiesgo}")
