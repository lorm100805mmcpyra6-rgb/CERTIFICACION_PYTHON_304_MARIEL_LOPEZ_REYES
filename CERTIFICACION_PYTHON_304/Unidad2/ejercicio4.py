#el mapa de tesoro
mapa=[
    [".",".",".","."],
    [".",".","X","."],
    [".",".",".","."],
    [".",".",".","."],
]
filas=len(mapa)
columnas=len(mapa)
#recorriendo la matriz con ciclos anidados
#ciclo externa para mabenar filas(i)
for i in range(filas):
    #ciclo externo para manejar columnas(j)
    for j in range(columnas):
        if mapa[i][j]=="X":
            print(f"tesoro encontrado en la pocicion = [{i}][{j}]")
