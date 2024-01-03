def registrarProducto(productos: dict) -> dict:
     
    try:
        codigo = input("Ingrese el código del producto a ingresar: ")

        if codigo in productos:
            print("Error: El código ya existe para otro producto.")
            return productos

        nombreProducto = input("Ingrese el nombre del producto a registrar: ")
        valorCompra = float(input("Ingrese el valor de compra del producto: "))
        valorVenta = float(input("Ingrese el valor de venta del producto: "))
        stockMinimo = int(input("Ingrese el stock mínimo del producto: "))
        stockMaximo = int(input("Ingrese el stock máximo del producto: "))
        stockActual = int(input("Ingrese el stock actual del producto: "))
        nombreProveedor = input("Ingrese el nombre del proveedor del producto: ")

    except ValueError:
        print("Error: Ingrese un valor numérico válido para el precio y el stock.")
        return productos
    producto = {
        "nombre producto": nombreProducto,
        "codigo": codigo,
        "valor compra": valorCompra,
        "valor venta": valorVenta,
        "stock minimo": stockMinimo,
        "stock maximo": stockMaximo,
        "stock actual": stockActual,
        "nombre proveedor": nombreProveedor
    }

    
    productos[codigo] = producto

    return productos


def visualizacionProducto(productos: dict):
    print("Listado de Productos:")
    print("{:<15} {:<30} {:<15} {:<15} {:<15} {:<15} {:<15} {:<30}".format(
        "Código", "Nombre Producto", "Valor Compra", "Valor Venta",
        "Stock Mínimo", "Stock Máximo","Stock Actual", "Proveedor"
    ))
    
    print("-" * 123)
    for producto, infoProducto in productos.items():
       
        print("{:<15} {:<30} {:<15} {:<15} {:<15} {:<15} {:<15} {:<30}".format(
            infoProducto["codigo"],
            infoProducto["nombre producto"],
            infoProducto["valor compra"],
            infoProducto["valor venta"],
            infoProducto["stock minimo"],
            infoProducto["stock maximo"],
            infoProducto["stock actual"],
            infoProducto["nombre proveedor"]
        ))

def actualizacionStock(productos: dict):
    productoBuscar = input("Ingrese el codigo del producto cuyo stock desea actualizar ")
    if productoBuscar in productos:
       modificacionStock = int(input("Ingrese la cantidad a modificar escriba -(suma a restar del stock) o un numero entero positivo para incrementar el stock "))
       productos[productoBuscar]['stock actual'] +=  modificacionStock
       nuevoValor = productos[productoBuscar]['stock actual']
       nombreProducto = productos[productoBuscar]['nombre producto']
       print(f"El stock actualizado para {nombreProducto} es {nuevoValor}")
    else:
        print("El producto no se ha creado ")


def productosCriticos(productos: dict):
    for productos, producto in productos.items():
        stockA = producto['stock actual']
        stockMin = producto['stock minimo']
        if stockA<stockMin:
            nombreP = producto['nombre producto']
            print(f"El producto {nombreP} esta por debajo del limite establecido. El stock actual es {stockA} y el stock minimo es {stockMin}")
       
def gananciaPotencial(productos: dict):
    for productos, producto in productos.items():
        gananciaP = (producto['valor venta'] - producto['valor compra']) * producto ['stock actual']
        nombreP = producto['nombre producto']
        print(f"La ganancia potencial para {nombreP} es {gananciaP}")