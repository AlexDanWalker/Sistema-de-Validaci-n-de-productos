# Sistema-de-Validaci-n-de-productos
Se trata de un sistema que valida productor, preguntando su preico y haciendo operaciones para dar un resultado total a una compra aplicando descuentos según oferta del cliente

Pruebas:

Prueba 1: Datos válidos
Entradas:

Nombre: Laptop

Precio: 800.50

Cantidad: 2

Descuento: 10

Esperado:

Subtotal: 1601.00

Descuento: 160.10

Total: 1440.90

Prueba 2: Nombre vacío (validación)
Entradas:

Nombre: (presionar Enter varias veces) → Luego: Teclado

Esperado:

Mensaje: "El nombre no puede estar vacío."

Prueba 3: Precio negativo
Entradas:

Precio: -100 → 0 → abc → 50

Esperado:

Mensaje de error para cada entrada inválida hasta ingresar 50.

Prueba 4: Cantidad inválida
Entradas:

Cantidad: -2 → 0 → abc → 3

Esperado:

Mensaje: "La cantidad debe ser un número entero positivo." hasta ingresar 3.

Prueba 5: Descuento fuera de rango
Entradas:

Descuento: -5 → 105 → abc → 15

Esperado:

Mensaje: "El descuento debe estar entre 0 y 100." hasta ingresar 15.
