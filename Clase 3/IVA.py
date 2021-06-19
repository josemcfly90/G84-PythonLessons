precio_producto = input('Digite el precio: ')
precio_producto = float(precio_producto)
iva = 0.19
print('El IVA es: ' + str(precio_producto * iva))
print('El valor total es: ' + str(precio_producto + (precio_producto * iva)))