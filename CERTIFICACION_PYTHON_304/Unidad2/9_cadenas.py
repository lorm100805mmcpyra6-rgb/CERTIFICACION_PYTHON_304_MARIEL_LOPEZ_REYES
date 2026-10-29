#cadenas y concatenacion(+)
cadena1='hola'
cadena2= 'mundo'
multilinea= """esto es una cadena 
de varias lineas"""
print(cadena1+cadena2+multilinea)#print
#cadenas y repeticion
eco='jaa'*3
print(eco)
#Cambiar una cadena miniscula a mayuscula
tu_nombre="mariel"
print(tu_nombre.upper())
#Cambiar una cadena mayuscula a minuscula
print(tu_nombre.lower())
#remplazar texto de una cdena
frase="me gusta la programacion"
print(frase.replace("programacion","matematicas"))
#formato de cadenas(f-string)
edad=17
nombre="mariel"
mensaje=f"hola, me llamo\n{nombre}\ny tengo\n{edad} años"
print(mensaje)
texto="¡Felicidades por aun continuar en el CECy!!!"
print(texto)
cantidad_caracteres=len(texto)
print(cantidad_caracteres)
#comprobar si un texto contiene una palabra
oracion="aprender python no es divertido"
if"java" in oracion:
    print("encontrado")
else:
    print("no esta")
    #validar contenido de una cadena
nlista="13"
print(nlista.isalpha()) 
print(nlista.isdigit())

