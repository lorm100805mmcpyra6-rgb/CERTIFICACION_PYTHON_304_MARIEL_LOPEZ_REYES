#Creando un diccionario
persona={
    "nombre":"mariel",
    "edad":16,
    "profesion":"programador",
    "estudiante":True
}
print(persona)
#accediendo a un valor en especifico
print(persona["nombre"])
#se puede usar el metodo get()
#es util por que no marca error si el valor no existe
print(persona.get("profesion"))
#modificar un valor existente
persona["edad"]=12
print(persona["edad"])
#agregar un par(clave:valor)
persona["ciudad"]="san pepp"
print(persona)
#recorrer un diccionario con un bucle 