# Trabajo Practico 5: Listas en Python

## Actividad 1: Lista de multiplos de 4 del 1 al 100

multiplos_de_4 = list(range(4, 101, 4))
print(multiplos_de_4)


## Actividad 2: Mostrar el penúltimo elemento de una lista
mi_lista = ['libro', 'computadora', 'música', 'café', 'python']
penultimo = mi_lista[-2]  # Indexing negativo: -1 es último, -2 penúltimo
print(penultimo)

## Actividad 3: Lista vacía con append
lista_vacia = []
lista_vacia.append('hola')
lista_vacia.append('mundo')
lista_vacia.append('python')
print(lista_vacia)


## Actividad 4: Reemplazar elementos en lista de animales
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"    # Segundo elemento (índice 1)
animales[-1] = "oso"    # Último elemento (índice -1)
print(animales)


## Actividad 5: Análisis del programa
# El programa:
# 1. Crea una lista de números `[8, 15, 3, 22, 7]`
# 2. Encuentra y elimina el valor máximo de la lista (22) usando `remove(max(numeros))`
# 3. Imprime la lista resultante: `[8, 15, 3, 7]`

## Actividad 6: Lista con saltos de 5

numeros = list(range(10, 31, 5))
print(numeros[:2])  # Muestra los dos primeros elementos


## Actividad 7: Reemplazar valores centrales en lista de autos

autos = ["sedan", "polo", "suran", "gol"]
autos[1:3] = ["camioneta", "pickup"]  # Reemplaza índices 1 y 2
print(autos)


## Actividad 8: Lista de dobles

dobles = []
dobles.append(5*2)
dobles.append(10*2)
dobles.append(15*2)
print(dobles)


## Actividad 9: Manipulación de lista de compras

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

# a) Agregar "jugo" al tercer cliente
compras[2].append("jugo")

# b) Reemplazar "fideos" por "tallarines"
compras[1][1] = "tallarines"

# c) Eliminar "pan" del primer cliente
compras[0].remove("pan")

# d) Imprimir lista resultante
print(compras)


## Actividad 10: Lista anidada compleja

lista_anidada = [
    15,
    True,
    [25.5, 57.9, 30.6],
    False
]
print(lista_anidada) 