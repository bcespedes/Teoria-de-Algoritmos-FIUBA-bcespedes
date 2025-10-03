# PROBLEMA 2
## Supuestos 
+ El algoritmo planteado recibe un archivo con el nombre "clientes.csv", con el formato: `cliente, paradas, propuesta`. Donde **cliente** representa el nombre del cliente, **paradas** la cantidad de paradas que desea ocupar, y **propuesta** la oferta económica por dicha ocupación.
+ Las restricciones entre propuestas se consideran únicamente de a pares, se conocen de antemano y se encuentran en forma de constante en el código (e.g Clientes **A** y **D** son competidores, y por ende no pueden tomarse ofertas de ambos a la vez).
+ Cada propuesta es indivisible: se acepta por completo o se descarta.
+ Se busca maximizar las ganancias sin superar el máximo de 200 paradas disponibles.

## Variables 
+ `Y_i = 1` Las variables son de decisión binaria, y cada una representa si se acepta o no la propuesta de un cliente (1 para afirmativo, 0 para negativo).
+ Las variables consideradas son: `A, B1, B2, C, D, E, F, G`

## Modelo de Programación Lineal ##
**Funcion objetivo:** 
- La función objetivo busca maximizar las ganancias totales a partir de aceptar propuestas de clientes con una cantidad finita de paradas.
`MaxZ = 50000 x Y_A + 100000 x Y_B1 + 120000 x Y_B2 + 100000 x Y_C + 80000 x Y_D + 5000 x Y_E + 40000 x Y_F + 90000 x Y_G `

**Restricciones:**
- Las paradas concesionadas no pueden superar la cantidad máxima de paradas disponibles: 
`30 x Y_A + 100 x Y_B1 + 120 x Y_B2 + 75 x Y_C + 50 x Y_D + 2 x Y_E + 20 x Y_F + 100 x Y_G `
- Clientes A y D no se pueden publicitar simultáneamente: `Y_A + Y_D <= 1`
- Solo una propuesta por cliente: `Y_B1 + Y_B2 <= 1`

## Solución Obtenida ##
**Variables iguales a 1**

Cliente A: 30 paradas, USD 50000

Cliente B1: 80 paradas, USD 100000

Cliente C: 75 paradas, USD 100000

Cliente E: 2 paradas, USD 5000

---
**Solución**

Z = 255000.0

Paradas usadas: 187

---

**Interpretación**
+ Se aceptan las propuestas de los clientes: A, B1, C, E.
+ No se acepta la de D (por competencia directa con A), ni la de B2 (ya que se aceptó la propuesta B1).
+ Se maximizan los beneficios a USD 255.000 dentro del límite de 200 paradas.
+ Se respetan todas las restricciones del problema (capacidad máxima e incompatibilidad entre propuestas).
+ Todo lo planteado garantiza que la solución es factible y se encuentra dentro del dominio del problema, es decir, dentro del conjunto de combinaciones válidas de decisiones que cumplen con las restricciones detalladas.

Además, se justifica el uso de la programación lineal para este tipo de problemas de asignación y optimización, dado que, según Mitchell et al. (2011), herramientas como PuLP permiten modelar y resolver de manera eficiente problemas lineales con restricciones múltiples, facilitando la obtención de soluciones óptimas en contextos como el presente.

## Referencias ##
+ Mitchell, S., et al. (s.f.). PuLP: A linear programming toolkit for Python. COIN-OR. Recuperado el 23 de mayo de 2025, de https://coin-or.github.io/pulp/index.html