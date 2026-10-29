#ejemlplo 1 sin manejo de excepciones

try:
    numero1=float(input("ingresa el primer numero"))
    numero2=float(input("ingresa el segundo numero"))
    resultado=numero1/numero2
    print(resultado)
except ZeroDivisionError:
    print("error:no puede dividir entre cero")
except ValueError:
    print("error:no puede ingresar letras")
