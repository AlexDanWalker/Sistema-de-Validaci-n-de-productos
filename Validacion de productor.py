# Función para obtener y validar el nombre del producto
def obtener_nombre_producto():
    nombre = input("Ingresa el nombre del producto: ").strip()
    while not nombre:
        print("El nombre no puede estar vacío.")
        nombre = input("Ingresa el nombre del producto: ").strip()
    return nombre

# Función para obtener y validar el precio
def obtener_precio_unitario():
    while True:
        try:
            precio = float(input("Ingresa el precio unitario del producto: "))
            if precio > 0:
                return precio
            else:
                print("El precio debe ser un número positivo.")
        except ValueError:
            print("Entrada no válida. Ingresa un número.")

# Función para obtener y validar la cantidad
def obtener_cantidad():
    while True:
        try:
            cantidad = int(input("Ingresa la cantidad de productos adquiridos: "))
            if cantidad > 0:
                return cantidad
            else:
                print("La cantidad debe ser un número entero positivo.")
        except ValueError:
            print("Entrada no válida. Ingresa un número entero.")

# Función para obtener y validar el descuento
def obtener_descuento():
    while True:
        try:
            descuento = float(input("Ingresa el porcentaje de descuento (0-100): "))
            if 0 <= descuento <= 100:
                return descuento
            else:
                print("El descuento debe estar entre 0 y 100.")
        except ValueError:
            print("Entrada no válida. Ingresa un número.")

# Función para calcular el total
def calcular_costo_total(precio, cantidad, descuento):
    subtotal = precio * cantidad
    monto_descuento = subtotal * (descuento / 100)
    total = subtotal - monto_descuento
    return subtotal, monto_descuento, total

# Función para mostrar el resultado
def mostrar_resultado(nombre_producto, subtotal, descuento, total):
    print("\n--- Detalle de la compra ---")
    print(f"Producto: {nombre_producto}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Descuento aplicado: {descuento:.2f}%")
    print(f"Total a pagar: ${total:.2f}")
    print("-----------------------------")

# Función principal que une todo
def main():
    nombre_producto = obtener_nombre_producto()
    precio_unitario = obtener_precio_unitario()
    cantidad = obtener_cantidad()
    descuento = obtener_descuento()

    subtotal, monto_descuento, total = calcular_costo_total(precio_unitario, cantidad, descuento)
    mostrar_resultado(nombre_producto, subtotal, descuento, total)

# Verifica si el archivo está siendo ejecutado directamente
if __name__ == "__main__":
    main()

