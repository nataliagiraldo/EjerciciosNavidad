#reporte ejercicio 4
numIngresado = 0
totalNumeros = 0
numPares = []
numImpares = []
menores = 0
medio = 0
altos = 0
while numIngresado>=0 :
    try:
        numIngresado = int(input("Ingrese un numero "))
    except ValueError:
        print ("Ingrese un dato valido")
        numIngresado = int(input("Ingrese un numero "))
    totalNumeros = totalNumeros + 1 

    if numIngresado % 2 == 0 and numIngresado > 0:
        numPares.append(numIngresado)

    elif numIngresado % 2 != 0 and numIngresado > 0:
        numImpares.append(numIngresado)

    if numIngresado<10 and numIngresado > 0:
        menores = menores + 1

    elif numIngresado in range(20,50):
        medio = medio + 1

    elif numIngresado > 100:
        altos = altos + 1
        
cantidadPares = len(numPares) 
if cantidadPares>0:       
    sumaPares = sum(numPares)
    promedioPares = sumaPares/cantidadPares
else:
    sumaPares = 0
    promedioPares = 0

cantidadImpares = len(numImpares)
if cantidadImpares>0:
    sumaImpares = sum(numImpares)
    promedioImpares = sumaImpares/cantidadImpares 
else:
    sumaImpares = 0
    promedioImpares = 0

print(f"En total se ingresaron {totalNumeros-1} numeros, Se ingresaron {cantidadPares} numeros pares y el promedio de numeros pares fue {promedioPares}, el promedio de numeros impares fue {promedioImpares}, se ingresaron {menores} numeros menores a 10, se ingresaron {medio} numeros entre 20 y 50, se ingresaron {altos} numeros mayores a 100 ")




