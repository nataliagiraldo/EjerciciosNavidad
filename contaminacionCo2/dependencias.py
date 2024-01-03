def registrarDependencia(dependencias : dict)->dict:
    nombreDependencia =input("Ingrese el nombre de la dependencia: ")
    dependencia = {
        "Nombre dependencia" : nombreDependencia

    }
    dependencias[nombreDependencia] = dependencia
    return dependencias

def registrarConsumo(dependencias : dict):
    dependenciaBuscar = input("Ingrese el nombre de su dependencia: ")
    if dependenciaBuscar in dependencias:
        try:
            print("\nPara conocer las emisiones de co2 por electricidad vamos a solicitarle algunos datos: ")
            factorEmisionArea = float(input("\nIngrese el factor de emision por electricidad de su area: "))
            facturaE = float(input("\nIngrese el total de kWh utilizados durante el periodo facturado en su ultimo recibo de luz: "))
            periodoF = int(input("\nIngrese cuantos meses pasaron en la facturacion de el recibo de la luz: "))
            emisionElectricidad = factorEmisionArea * (facturaE/periodoF)
            print("\nPara conocer las emisiones de co2 asociadas al transporte vamos a solicitarle algunos datos ")
            factorEmsionTransporte = float(input("\nIngrese el factor de emision de su medio de el medio de transporte que utliza: "))
            kmRecorridos = int(input("\nIngrese cuantos km recorrio en el medio de transporte que utiliza: "))
            emisionTransporte = factorEmsionTransporte * kmRecorridos
            print("\nPara conocer las emisiones de co2 asociadas al uso de dispositivos o electrodomesticos vamos a solicitarle algunos datos ")
            cantidadD = int(input("\nIngrese la cantidad de dispsitivos y/o electrodomesticos que usa cotidianamente en su dependencia: "))
            for dispositivo in range (cantidadD):
                potenciaD = int(input(f"\nIngrese la potencia del dispositivo {dispositivo + 1}: "))
                tiempoUso = int(input(f"\nIngrese el tiempo de uso del dispositivo {dispositivo + 1}: "))
                consumoDisp = (potenciaD * tiempoUso) / 1000
                dependencias[dependenciaBuscar]['Consumo Dispositivos'] = consumoDisp
            emisionT = emisionElectricidad + emisionTransporte
            dependencias[dependenciaBuscar]['Emision total'] = emisionT
        except ValueError:
            print("Ingrese un dato valido")
    else:
        print(f"la dependencia {dependenciaBuscar} no esta registrada ")

