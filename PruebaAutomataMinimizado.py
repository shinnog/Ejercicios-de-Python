# Minimización de un Autómata Finito Determinista (AFD)

# Definición de elementos de la máquina de estados
estados = []
alfabeto = []
estadoFinal = []
estadoInicial = ""
transiciones = {}

# Entrada de datos
print("Escribe los estados del autómata separados por espacio: ", end="")
estados = input().split()

print("Escribe el alfabeto del autómata separados por espacio: ", end="")
alfabeto = input().split()

print("Escribe el estado inicial: ", end="")
estadoInicial = input()

print("Escribe los estados finales separados por espacio: ", end="")
estadoFinal = input().split()

print("Escribe las transiciones del autómata en el formato (estado, símbolo, estado destino).")
for state in estados:
    for alpha in alfabeto:
        print(f"Desde estado '{state}' con símbolo '{alpha}', va a: ", end="")
        dest = input()
        if dest == ".":
            transiciones[(state, alpha)] = None
        else:
            transiciones[(state, alpha)] = dest

P = [set(estadoFinal), set([s for s in estados if s not in estadoFinal])]

def obtenerClase(estado, particiones):
    for i, grupo in enumerate(particiones):
        if estado in grupo:
            return i
    return None

cambio = True
while cambio:
    cambio = False
    nuevasParticiones = []

    for grupo in P:
        
        # Subdividir grupo en subgrupos
        subdivisiones = {}

        for estado in grupo:
            firma = []
            for simbolo in alfabeto:
                destino = transiciones.get((estado, simbolo))
                clase_destino = obtenerClase(destino, P) if destino else None
                firma.append(clase_destino)
            firma = tuple(firma)

            if firma not in subdivisiones:
                subdivisiones[firma] = set()
            subdivisiones[firma].add(estado)

        if len(subdivisiones) > 1:
            cambio = True

        nuevasParticiones.extend(subdivisiones.values())

    P = nuevasParticiones

    print("\nParticiones actuales:")
    for grupo in P:
        print(grupo)

# Generar el nuevo autómata minimizado
nuevosEstados = ["Q" + str(i) for i in range(len(P))]
representantes = [list(grupo)[0] for grupo in P]  # Elegimos un representante de cada grupo

estadoEquivalente = {}
for nombre, grupo in zip(nuevosEstados, P):
    for estado in grupo:
        estadoEquivalente[estado] = nombre

nuevoEstadoInicial = estadoEquivalente[estadoInicial]
nuevoEstadosFinales = list(set([estadoEquivalente[s] for s in estadoFinal]))

nuevasTransiciones = {}
for nombre, representante in zip(nuevosEstados, representantes):
    for simbolo in alfabeto:
        destino = transiciones.get((representante, simbolo))
        if destino:
            nuevasTransiciones[(nombre, simbolo)] = estadoEquivalente[destino]

# Mostrar el AFD minimizado
print("\n--- Resultado Final del AFD Minimizado ---")
print(f"Estados: {nuevosEstados}")
print(f"Alfabeto: {alfabeto}")
print(f"Estado Inicial: {nuevoEstadoInicial}")
print(f"Estados Finales: {nuevoEstadosFinales}")
print("Transiciones:")
for (origen, simbolo), destino in nuevasTransiciones.items():
    print(f"  ({origen}, {simbolo}) -> {destino}")
