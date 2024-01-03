def co2Producido(dependencias : dict):
    for dependencias, infoDependencia in dependencias.items():
        nombreDependencia = infoDependencia["Nombre dependencia"]
        consumoDisp = infoDependencia["Consumo Dispositivos"]
        emisionT = infoDependencia["Emision total"]
        print(f"\nNombre depencia: {nombreDependencia}")
        print(f"Consumo Dispositivos: {consumoDisp}")
        print(f"Emision total: {emisionT}")
        
def compararDependencias(dependencia):
    return dependencia[1].get('Emision total', 0)

def mayorCo2(dependencias: dict):
    dependenciasS = sorted(dependencias.items(), key=compararDependencias, reverse=True)
    if dependenciasS:
        mayorD = dependenciasS[0]
        print("\nLa dependencia que más CO2 produce es:")
        print(f"Nombre dependencia: {mayorD[1]['Nombre dependencia']}")
    else:
        print("No hay dependencias registradas.")