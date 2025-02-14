import math
# Se desea calcular la distancia recorrida (D) por un automóvil que tiene velocidad constante
# (m/s) durante un tiempo T (Sg), considerar que es un MRU (Movimiento Rectilíneo
# Uniforme). Tenga en cuenta que la formula del movimiento rectilíneo es:


# v = int(input("Ingresa la velocidad del vehiculo: "))
# t = int(input("Ingrese el tiempo: "))

# d = v * t
# print("La distancia recorrida es de:", d)

# Se necesita obtener el promedio de un estudiante a partir de sus tres notas parciales. El
# estudiante debe digitar sus tres notas y el sistema deberá darle el promedio del semestre.

nota1 = float(input("Ingrese la nota 1: "))
nota2 = float(input("Ingrese la nota 2: "))
nota3 = float(input("Ingrese la nota 3: "))

notas = nota1+ nota2 + nota3
promedio = notas / 3
print("Su promedio es:", promedio)

# Elaborar un algoritmo que permita ingresar el número de partidos ganados, perdidos y
# empatados, de un equipo en un torneo de futbol. Se debe de imprimir el puntaje total del
# equipo, tenga en cuenta que:
# a. Por cada partido ganado obtendrá 3 puntos.
# b. Por cada partido empatado 1 punto.
# c. Por cada partido perdido 0 puntos.
# Se desea imprimir la cantidad de partidos ganados, perdidos, empatados y el cálculo
# completo de la cantidad de puntos obtenidos del equipo de futbol.

ganados = int(input("Ingrese el numero de partidos ganados: "))
perdidos = int(input("Ingrese el numero de partidos perdidos: "))
empatados = int(input("Ingrese el numero de partidos empatados: "))

gano = ganados*3
empato = empatados*1
perdio = perdidos*0

puntos = gano+empato+perdio
print("Partidos Ganados:", ganados)
print("Partidos Perdidos:", perdidos)
print("Partidos Empatados:", empatados)
print("El total de puntos de su equipo es:",puntos)

# Se requiere el algoritmo para elaborar la planilla de un empleado. Para ello se debe digitar:
# nombre del empleado, la cantidad de horas laboradas en el mes y la tarifa por hora. Se debe
# calcular el total devengado por el empleado en el mes e imprimir: Nombre del empleado,
# cantidad de horas laboradas y total devengado.

nombre = input("Ingrese el nombre del empleado: ")
horas = int(input("Ingrese la cantidad de horas laboradas en el mes: "))
tarifa = int(input("Ingrese la tarifa por hora: "))

devengado = horas * tarifa
print(f"Nombre del empleado: {nombre}, Horas Trabajadas: {horas}, Devengado: {devengado}")

# Se tiene un triángulo rectángulo cuyos lados deberán ser digitados por el usuario. Se debe
# hallar la hipotenusa teniendo en cuenta la formula: H = raíz cuadrada (a**2 + b**2)

a = int(input("Ingrese la medida del lado 1: "))
b = int(input("Ingrese la medida del lado 2: "))
h = math.sqrt(a**2 + b**2)
print("La hipotenusa del triangulo es: ", h)

# Se tiene un horno en casa con temperaturas en grados Celsius centígrado), requiere
# transformar la temperatura de 70°C a grados Fahrenheit. Para ello tenga en cuenta la
# siguiente fórmula.

c = int(input("Ingrese la temperatura en grados centigrados: "))
f = (c * 1.8) + 32
print(f"La temperatura de {c}°C a grados Fahrenheit es: {f}")

