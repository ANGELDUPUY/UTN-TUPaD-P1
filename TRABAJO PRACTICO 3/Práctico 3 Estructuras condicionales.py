#TECNICATURA UNIVERSITARIA EN PROGRAMACIÓN A DISTANCIA 
#Alumno: Manuel Angel Dupuy
#Materia: Programación I 
#Práctico 3: Estructuras condicionales
#Objetivo:
# Comprender y aplicar las estructuras condicionales en la programación, desarrollando algoritmos que involucren tomas de decisiones.

# Actividad 1 - Mayor de edad

edad = int(input("Ingrese su edad: "))
if edad > 18:
    print("Es mayor de edad")


# Actividad 2 - Aprobado/Desaprobado

nota = float(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")


# Actividad 3 - Números pares

numero = int(input("Ingrese un número par: "))
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")


# Actividad 4 - Categorías por edad

edad = int(input("Ingrese su edad: "))
if edad < 12:
    print("Niño/a")
elif 12 <= edad < 18:
    print("Adolescente")
elif 18 <= edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")


# Actividad 5 - Validación de contraseña

contraseña = input("Ingrese una contraseña (8-14 caracteres): ")
if 8 <= len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


# Actividad 6 - Análisis estadístico

from statistics import mode, median, mean
import random

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

if media > mediana > moda:
    print("Sesgo positivo")
elif media < mediana < moda:
    print("Sesgo negativo")
else:
    print("Sin sesgo")


# Actividad 7 - Frases con vocales

texto = input("Ingrese una frase o palabra: ")
vocales = ('a', 'e', 'i', 'o', 'u')
if texto.lower().endswith(vocales):
    print(texto + "!")
else:
    print(texto)


# Actividad 8 - Formateo de nombre

nombre = input("Ingrese su nombre: ")
opcion = input("Elija opción (1: MAYÚSCULAS, 2: minúsculas, 3: Primera mayúscula): ")

if opcion == "1":
    print(nombre.upper())
elif opcion == "2":
    print(nombre.lower())
elif opcion == "3":
    print(nombre.title())
else:
    print("Opción no válida")


# Actividad 9 - Escala de Richter

magnitud = float(input("Ingrese magnitud del terremoto: "))

if magnitud < 3:
    print("Muy leve (imperceptible)")
elif 3 <= magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif 4 <= magnitud < 5:
    print("Moderado (sentido por personas)")
elif 5 <= magnitud < 6:
    print("Fuerte (daños en estructuras débiles)")
elif 6 <= magnitud < 7:
    print("Muy fuerte (daños significativos)")
else:
    print("Extremo (graves daños a gran escala)")


# Actividad 10 - Estaciones del año

hemisferio = input("¿En qué hemisferio está? (N/S): ").upper()
mes = int(input("Ingrese mes (1-12): "))
dia = int(input("Ingrese día (1-31): "))

if (mes == 12 and dia >= 21) or (mes <= 3 and dia <= 20):
    estacion = "Invierno" if hemisferio == "N" else "Verano"
elif (mes == 3 and dia >= 21) or (mes <= 6 and dia <= 20):
    estacion = "Primavera" if hemisferio == "N" else "Otoño"
elif (mes == 6 and dia >= 21) or (mes <= 9 and dia <= 20):
    estacion = "Verano" if hemisferio == "N" else "Invierno"
else:
    estacion = "Otoño" if hemisferio == "N" else "Primavera"

print(f"Estación actual: {estacion}")