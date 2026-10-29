#declarando una lista
try:
    materias=["Programacion","Filosofia","Matematicas","Ingles"]
    print(materias[3])
    materias.append("Lengua y comunicacion")
    print(materias)
    materias[1]="biologia"
    print(materias)
    materias.remove("Ingles")
    print(materias)
except IndexError:
    print("fuera de rango")