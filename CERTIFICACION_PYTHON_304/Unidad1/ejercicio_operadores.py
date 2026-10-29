#realizar un programa que calcule
#la compra total de 4 productos, sila compra total
#es mayor a 2000 pesos me haga un descuento
#del 10%
# DATOS DE ENTRADA
precio1=float(input("Introduce el precio del producto 1:"))
precio2=float(input("Introduce el precio del producto 2:"))
precio3=float(input("Introduce el precio del producto 3:"))
precio4=float(input("Introduce el precio del producto 4:"))
#proceso
total=precio1+precio2+precio3+precio4
if total>2000:
    total=(total-(total*.10))
    #total=(total-(3000*.10)) total=2700
    print(total)
else:
    print("no tienes descuento")
producto=input("introduce tu producto:")
presio=float(input("introduce el precio:"))
cantidad=int(input("introduce la cantidad:"))
total = presio * cantidad
print("producto:", producto)
print("cantidad a pagar:", total)
