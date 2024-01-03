#sumatoria ejercicio 1
def suma():
    
    try:
        a = int(input("Ingrese un numero "))
    except ValueError:
        print ("Ingrese un dato valido")
        a = int(input("Ingrese un numero "))

    try:
        b = int(input("Ingrese un numero "))
    except ValueError:
        print ("Ingrese un dato valido")
        b = int(input("Ingrese un numero "))

    try:
        c = int(input("Ingrese un numero "))
    except ValueError:
        print ("Ingrese un dato valido")
        c = int(input("Ingrese un numero "))

        
    resultado = a + b + c
    print(f"El resultado de la suma es {resultado}")

suma()