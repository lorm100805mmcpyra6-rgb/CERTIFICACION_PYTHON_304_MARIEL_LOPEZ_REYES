#ciclo externo para el numero de la base de la tabla
for i in range(1,4):
    print(f"--tabla de {i}--")
    #ciclo interno nos meltiplica la base(i) por el numero(j)
    for j in range(1,11):
        print(f"{i} x {j} ={i*j}")
    print(f" aqui termina la tabla del {i}")


