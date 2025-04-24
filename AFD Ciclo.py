# Automata Finito Determinista en Python
# Autor: Juan Carlos Guerrero Davila

# Definicion de los elementos de la maquina de estados

estados = []
alfabeto = []
estadoFinal = []
estadoInicial = ""
transiciones = {}

print("Escribe los estados del automata separados por espacio: ", end="")
estados = input().split()

print("Escribe el alfabeto del automata separados por espacio: ", end="")
alfabeto = input().split()

print("Escribe el estado inicial: ", end="")
estadoInicial = input()

print("Escribe los estados finales separados por espacio: ", end="")
estadoFinal = input().split()

print("Escribe las transiciones del automata en el formato (estado, simbolo, estado):")
for state in estados:
    for alpha in alfabeto:
        print(f"\t  {alpha}")
        print(f"{state}\t---->\t", end="")
        dest = input()

        if dest == ".":
            transiciones[(state, alpha)] = None
        else:
            transiciones[(state, alpha)] = dest

# Ciclo para evaluar múltiples palabras
while True:
    print("\nEscribe la palabra a evaluar (o escribe 'salir' para terminar): ", end="")
    palabra = input()
    if palabra.lower() == "salir":
        print("Fin del programa.")
        break

    estadoActual = estadoInicial
    aceptada = True

    for char in palabra:
        try:
            estadoActual = transiciones[(estadoActual, char)]
            if estadoActual is None:
                print("Cadena no aceptada (transición vacía).")
                aceptada = False
                break
        except KeyError:
            print(f"Cadena no aceptada (no hay transición definida para ({estadoActual}, {char})).")
            aceptada = False
            break

    if aceptada:
        if estadoActual in estadoFinal:
            print("Palabra aceptada")
        else:
            print("Palabra no aceptada")
