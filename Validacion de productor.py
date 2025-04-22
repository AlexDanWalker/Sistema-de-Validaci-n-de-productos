# Función para obtener y validar el nombre del producto
def obtener_nombre_producto():
    # Solicita al usuario el nombre del producto y elimina espacios en blanco
    nombre = input("Ingresa el nombre del producto: ").strip()
    
    # Valida que el nombre no esté vacío
    while not nombre:
        print("El nombre no puede estar vacío.")
        nombre = input("Ingresa el nombre del producto: ").strip()
    
    return nombre  # Devuelve el nombre válido

# Función para obtener y validar el precio unitario
def obtener_precio_unitario():
    while True:
        try:
            # Solicita el precio y lo convierte a tipo float
            precio = float(input("Ingresa el precio unitario del producto: "))
            
            # Verifica que el precio sea positivo
            if precio > 0:
                return precio
            else:
                print("El precio debe ser un número positivo.")
        except ValueError:
            # Captura errores si el usuario no ingresa un número
            print("Entrada no válida. Ingresa un número.")

# Función para obtener y validar la cantidad de productos
def obtener_cantidad():
    while True:
        try:
            # Solicita la cantidad y la convierte a entero
            cantidad = int(input("Ingresa la cantidad de productos adquiridos: "))
            
            # Verifica que la cantidad sea un número entero positivo
            if cantidad > 0:
                return cantidad
            else:
                print("La cantidad debe ser un número entero positivo.")
        except ValueError:
            # Captura errores si no se ingresa un número válido
            print("Entrada no válida. Ingresa un número entero.")

# Función para obtener y validar el porcentaje de descuento
def obtener_descuento():
    while True:
        try:
            # Solicita el porcentaje de descuento y lo convierte a float
            descuento = float(input("Ingresa el porcentaje de descuento (0-100): "))
            
            # Verifica que el descuento esté dentro del rango permitido
            if 0 <= descuento <= 100:
                return descuento
            else:
                print("El descuento debe estar entre 0 y 100.")
        except ValueError:
            # Captura errores si no se ingresa un número válido
            print("Entrada no válida. Ingresa un número.")

# Función que calcula el subtotal, descuento y total a pagar
def calcular_costo_total(precio, cantidad, descuento):
    subtotal = precio * cantidad  # Calcula el subtotal
    monto_descuento = subtotal * (descuento / 100)  # Calcula el valor del descuento
    total = subtotal - monto_descuento  # Calcula el total a pagar después del descuento
    return subtotal, monto_descuento, total  # Retorna los 3 valores

# Función que imprime el resumen de la compra
def mostrar_resultado(nombre_producto, subtotal, descuento, total):
    print("\n--- Detalle de la compra ---")
    print(f"Producto: {nombre_producto}")  # Muestra el nombre del producto
    print(f"Subtotal: ${subtotal:.2f}")    # Muestra el subtotal con dos decimales
    print(f"Descuento aplicado: {descuento:.2f}%")  # Muestra el descuento aplicado
    print(f"Total a pagar: ${total:.2f}")  # Muestra el total a pagar
    print("-----------------------------")

# Función principal que orquesta todo el proceso
def main():
    # Se obtienen y validan todos los datos del usuario
    nombre_producto = obtener_nombre_producto()
    precio_unitario = obtener_precio_unitario()
    cantidad = obtener_cantidad()
    descuento = obtener_descuento()

    # Se calcula el total de la compra
    subtotal, monto_descuento, total = calcular_costo_total(precio_unitario, cantidad, descuento)
    
    # Se muestra el resultado al usuario
    mostrar_resultado(nombre_producto, subtotal, descuento, total)

# Esta condición asegura que el programa solo se ejecute si es el archivo principal
if __name__ == "__main__":
    main()
