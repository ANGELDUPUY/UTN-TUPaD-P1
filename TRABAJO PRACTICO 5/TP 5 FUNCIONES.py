import math

# Ejercicio 1
def imprimir_hola_mundo():
    print("Hola Mundo!")

# Ejercicio 2
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

# Ejercicio 3
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# Ejercicio 4
def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

# Ejercicio 5
def segundos_a_horas(segundos):
    return segundos / 3600

# Ejercicio 6
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# Ejercicio 7
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "No se puede dividir por cero"
    return suma, resta, multiplicacion, division

# Ejercicio 8
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# Ejercicio 9
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Ejercicio 10
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

if __name__ == "__main__":
    # Ejemplos de cómo llamar a las funciones
    imprimir_hola_mundo()  # Ejercicio 1
    print(saludar_usuario("Angel"))  # Ejercicio 2
    informacion_personal("Juan", "Elesperado", 30, "Buenos Aires")  # Ejercicio 3
    print(f"Área: {calcular_area_circulo(5):.2f}")  # Ejercicio 4
    print(f"Horas: {segundos_a_horas(7200):.2f}")  # Ejercicio 5
    tabla_multiplicar(5)  # Ejercicio 6
    print(operaciones_basicas(10, 2))  # Ejercicio 7
    print(f"IMC: {calcular_imc(70, 1.75):.2f}")  # Ejercicio 8
    print(f"Fahrenheit: {celsius_a_fahrenheit(25):.2f}")  # Ejercicio 9
    print(f"Promedio: {calcular_promedio(10, 20, 30):.2f}")  # Ejercicio 10