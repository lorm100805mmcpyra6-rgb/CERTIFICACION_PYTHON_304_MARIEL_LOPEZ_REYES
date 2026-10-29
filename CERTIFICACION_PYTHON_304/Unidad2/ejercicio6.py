tabla = [
    ["nombre", "edad", "calificacion"],
    ["darina", 16, 8.0],
    ["karla", 16, 8.5],
    ["dulce", 16, 9.5],
    ["carlos", 16, 7.0],
    ["oscar", 16, 6.0],
    ["sherlyn", 16, 9.0],
    ["jorge", 16, 7.0],
    ["jesus", 15, 7.0],
    ["melisa", 16, 8.0],
    ["ximena", 16, 8.0]
]

filas = len(tabla)
columnas = len(tabla[0])
buscar = input("Introduce el nombre: ")
for i in range(0,11):
    for j in range(0,3):
        if tabla[i][j] == buscar:
            print(f"Nombre encontrado: {buscar}")
            print(f"encontrado en: [{i}][{j}]")