#calculadora imc ejercicio 2 y 3
def calculadoraImc():
    pesoNormal = 0
    sobrepeso = 0
    obesidad1 = 0
    obesidad2 = 0
    obesidad3 = 0
    estudiantes = 0
    while estudiantes <20 :
        nombre = input("ingrese el nombre del estudiante ")
        while True:
            try:
                edad = int(input("Ingrese la edad del estudiante: "))
                break
            except ValueError:
                print("Ingrese un número entero para la edad.")

        while True:
            try:
                peso = float(input("Ingrese el peso del estudiante (kg): "))
                break
            except ValueError:
                print("Ingrese un número válido para el peso.")

        while True:
            try:
                altura = float(input("Ingrese la altura del estudiante (m): "))
                if altura>0:
                    break
            except ValueError:
                print("Ingrese un número válido para la altura.")

        imc = (peso/altura**2)
        tipoImc = ""
        if imc<18.49:
            print("imc no clasificado")
        elif imc>=18.5 and imc<=24.9:
            tipoImc = "normal"
            pesoNormal = pesoNormal + 1
        elif imc>=25 and imc<=29.9:
            tipoImc = "sobrepeso"
            sobrepeso = sobrepeso + 1
        elif imc>=30 and imc<=34.9:
            tipoImc = "obesidad 1"
            obesidad1 = obesidad1 + 1 
        elif imc>=35 and imc<=39.9:
            tipoImc = "obesidad 2"
            obesidad2 = obesidad2 + 1
        else:
            tipoImc = "obesidad 3"   
            obesidad3 = obesidad3 + 1 
        print(f"el imc del estudiante {nombre} con edad {edad} años es {imc} y esta en la categoria {tipoImc} ")
        estudiantes = estudiantes + 1   
    print(f"la cantidad de estudiantes con peso normal es {pesoNormal}")
    print(f"la cantidad de estudiantes con sobrepeso es {sobrepeso}")
    print(f"la cantidad de estudiantes con obesidad1 es {obesidad1}")
    print(f"la cantidad de estudiantes con obesidad2 es {obesidad2}")
    print(f"la cantidad de estudiantes con obesidad3 es {obesidad3}")
calculadoraImc()
