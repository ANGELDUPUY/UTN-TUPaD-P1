#TECNICATURA UNIVERSITARIA EN PROGRAMACIÓN A DISTANCIA 
#Alumno: Manuel Angel Dupuy
#Materia: Programación I 
#Práctico 4: Estructuras Repetitivas


# Ejercicio 1: Números de 0 a 100
print("Ejercicio 1:")
for i in range(101):
    print(i)
print("\n" + "="*50 + "\n")

# Ejercicio 2: Contar dígitos de un número
print("Ejercicio 2:")
numero = int(input("Ingrese un número entero: "))
print(f"El número {numero} tiene {len(str(abs(numero))} dígitos")
print("\n" + "="*50 + "\n")

# Ejercicio 3: Sumar entre dos números (excluyéndolos)
print("Ejercicio 3:")
inicio = int(input("Ingrese el primer número: "))
fin = int(input("Ingrese el segundo número: "))
suma = sum(range(min(inicio, fin)+1, max(inicio, fin)))
print(f"La suma entre {inicio} y {fin} (excluyéndolos) es: {suma}")
print("\n" + "="*50 + "\n")

# Ejercicio 4: Sumar números hasta ingresar 0
print("Ejercicio 4:")
total = 0
while True:
    num = int(input("Ingrese un número (0 para terminar): "))
    if num == 0:
        break
    total += num
print(f"La suma total es: {total}")
print("\n" + "="*50 + "\n")

# Ejercicio 5: Adivinar número aleatorio
print("Ejercicio 5:")
numero_secreto = random.randint(0, 9)
intentos = 0
while True:
    intento = int(input("Adivina el número (0-9): "))
    intentos += 1
    if intento == numero_secreto:
        print(f"¡Correcto! Adivinaste en {intentos} intentos.")
        break
    print("Incorrecto, intenta nuevamente.")
print("\n" + "="*50 + "\n")

# Ejercicio 6: Números pares 100 a 0
print("Ejercicio 6:")
for i in range(100, -1, -2):
    print(i)
print("\n" + "="*50 + "\n")

# Ejercicio 7: Suma hasta un número
print("Ejercicio 7:")
limite = int(input("Ingrese un número entero positivo: "))
print(f"La suma desde 0 hasta {limite} es: {sum(range(limite+1))}")
print("\n" + "="*50 + "\n")

# Ejercicio 8: Estadísticas de 100 números
print("Ejercicio 8:")
numeros = []
for i in range(5):  # Cambiar a 100 para la versión final
    numeros.append(int(input(f"Ingrese número {i+1}/5: ")))
    
pares = sum(1 for n in numeros if n % 2 == 0)
impares = len(numeros) - pares
positivos = sum(1 for n in numeros if n > 0)
negativos = sum(1 for n in numeros if n < 0)

print(f"Pares: {pares}, Impares: {impares}")
print(f"Positivos: {positivos}, Negativos: {negativos}")
print("\n" + "="*50 + "\n")

# Ejercicio 9: Media de 100 números
print("Ejercicio 9:")
numeros = []
for i in range(5):  # Cambiar a 100 para la versión final
    numeros.append(int(input(f"Ingrese número {i+1}/5: ")))
print(f"La media es: {sum(numeros)/len(numeros)}")
print("\n" + "="*50 + "\n")

# Ejercicio 10: Invertir número
print("Ejercicio 10:")
numero = input("Ingrese un número: ")
print(f"Número invertido: {numero[::-1]}")