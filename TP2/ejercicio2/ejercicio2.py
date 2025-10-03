from pulp import *
import time

t1 = time.time()

PARADAS_MAXIMAS = 200
INCOMPATIBLES = [("A", "D"), ("B1", "B2")]

clientes = []

arch = open("clientes.csv", "r")
linea = arch.readline()
while linea != '':
    lista = linea.split(',')
    clientes.append({"Cliente" : lista.pop(0), 
                     "Paradas" : int(lista.pop(0)),
                     "Propuesta" : int(lista.pop(0))})
    linea = arch.readline()
arch.close()    

nombres = [c["Cliente"] for c in clientes]

#Crear modelo (maximizar ganancias):
prob = LpProblem("Concesiones", LpMaximize)

#Definir variables (una para cada propuesta de cliente):
Y = LpVariable.dicts("Y", nombres, 0, 1, cat = "Binary")

#Funcional:
prob += lpSum(Y[c["Cliente"]] * c["Propuesta"] for c in clientes)

#Restriciones:
prob += lpSum(Y[c["Cliente"]] * c["Paradas"] for c in clientes) <= PARADAS_MAXIMAS    # Limite de paradas

for c1, c2 in INCOMPATIBLES:
    prob += Y[c1] + Y[c2] <= 1  # Competidores y unico cliente (Casos A-D y B1-B2)

prob.writeLP("Concesiones.lp")

#Resolver:
status = prob.solve()

#Imprimir resultados
if LpStatus[status] == "Optimal":
    print("Variables iguales a 1")
    total_paradas = 0
    for c in clientes:
        if Y[c["Cliente"]].varValue == 1:
            print(f"Cliente {c['Cliente']}: {c['Paradas']} paradas, USD {c['Propuesta']}")
            total_paradas += c["Paradas"]
    print("---")
    print("Solucion")
    print("Z =", value(prob.objective))
    print("Paradas usadas:", total_paradas)
    print("---")
    
t2=time.time()
print("Tiempo de ejecucion: ", t2-t1)

# --- Exportar resultados a JSON ---
"""
import json

resultados = {
    "variables": {},
    "valor_maximo": None,
    "paradas_usadas": None
}

if LpStatus[status] == "Optimal":
    total_paradas = 0
    for c in clientes:
        valor = int(Y[c["Cliente"]].varValue)
        resultados["variables"][c["Cliente"]] = valor
        if valor == 1:
            total_paradas += c["Paradas"]
    resultados["valor_maximo"] = value(prob.objective)
    resultados["paradas_usadas"] = total_paradas

    with open("resultados.json", "w") as f:
        json.dump(resultados, f, indent=4)
"""
# --- Fin exportación JSON ---