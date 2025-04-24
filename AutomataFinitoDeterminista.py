# Automata Finito Determinista en Python
# Autor: Juan Carlos Guerrero Davila

# Definicion de los elementos de la maquina de estados

estados = []
alfabeto = []
estadoFinal = []
estadoInicial = ""
transiciones = {}

palabra = ""

print("Escribe los estados del automata separados por espacio: ", end="")
estados = input().split()

print("Escribe el alfabeto del automata separados por espacio: ", end="")
alfabeto = input().split()

print("Escribe el estado inicial: ", end="")
estadoInicial = input()

print("Escribe los estados finales separados por espacio: ", end="")
estadoFinal = input().split()

print("Escribe las transiciones del automata en el formato (estado, simbolo, estado) separados por espacio: ", end="")
for state in estados:
    for alpha in alfabeto:
        print(f"\t  {alpha}")
        print(f"{state}\t---->\t", end="")
        dest = input()

        if dest == ".":
            transiciones[(state, alpha)] = None
        else:
            transiciones[(state, alpha)] = dest

print("Escribe la palabra a evaluar: ", end="")
palabra = input()

estadoActual = estadoInicial

for char in palabra:
    estadoActual = transiciones[estadoActual, char]

    if estadoActual is None:
        print("Cadena no aceptada")
        break
else:
    if (estadoActual in estadoFinal):
        print("Palabra aceptada")
    else:
        print("palabra no aceptada")