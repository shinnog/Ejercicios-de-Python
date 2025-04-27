# Minimización de un Autómata Finito Determinista (AFD)
# Algoritmo de partición iterativa

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

# Inicializar particiones: finales y no finales
P = [set(estadoFinal), set([s for s in estados if s not in estadoFinal])]

def obtener_clase(estado, particiones):
    for i, grupo in enumerate(particiones):
        if estado in grupo:
            return i
    return None

cambio = True
while cambio:
    cambio = False
    nuevas_particiones = []

    for grupo in P:
        # Subdividir grupo en subgrupos
        subdivisiones = {}

        for estado in grupo:
            firma = []
            for simbolo in alfabeto:
                destino = transiciones.get((estado, simbolo))
                clase_destino = obtener_clase(destino, P) if destino else None
                firma.append(clase_destino)
            firma = tuple(firma)

            if firma not in subdivisiones:
                subdivisiones[firma] = set()
            subdivisiones[firma].add(estado)

        if len(subdivisiones) > 1:
            cambio = True

        nuevas_particiones.extend(subdivisiones.values())

    P = nuevas_particiones

    print("\nParticiones actuales:")
    for grupo in P:
        print(grupo)

# Generar el nuevo autómata minimizado
nuevos_estados = ["Q" + str(i) for i in range(len(P))]
representantes = [list(grupo)[0] for grupo in P]  # Elegimos un representante de cada grupo

estado_equivalente = {}
for nombre, grupo in zip(nuevos_estados, P):
    for estado in grupo:
        estado_equivalente[estado] = nombre

nuevo_estado_inicial = estado_equivalente[estadoInicial]
nuevo_estados_finales = list(set([estado_equivalente[s] for s in estadoFinal]))

nuevas_transiciones = {}
for nombre, representante in zip(nuevos_estados, representantes):
    for simbolo in alfabeto:
        destino = transiciones.get((representante, simbolo))
        if destino:
            nuevas_transiciones[(nombre, simbolo)] = estado_equivalente[destino]

# Mostrar el AFD minimizado
print("\n--- Resultado Final del AFD Minimizado ---")
print(f"Estados: {nuevos_estados}")
print(f"Alfabeto: {alfabeto}")
print(f"Estado Inicial: {nuevo_estado_inicial}")
print(f"Estados Finales: {nuevo_estados_finales}")
print("Transiciones:")
for (origen, simbolo), destino in nuevas_transiciones.items():
    print(f"  δ({origen}, {simbolo}) -> {destino}")
