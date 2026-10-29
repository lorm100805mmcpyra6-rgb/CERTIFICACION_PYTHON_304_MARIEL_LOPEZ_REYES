abecedario =[
    ['a','b','c','d'],
    ['e','f','g','h'],
    ['i','j','k','l'],
    ['m','ñ','n','o'],
    ['p','q','r','s'],
    ['t','u','v','W'],
    ['x','y','z',',']   
]
filas = len(abecedario)
columnas = len(abecedario[1])

for i in range(0,7):
    for j in range(0,4):
        print(f"[{i}] [{j}]= {abecedario[i][j]}")