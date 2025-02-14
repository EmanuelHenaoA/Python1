import math

# # 11.Escriba un algoritmo que acepte o rechace una pieza en forma de varilla,
# # para una empresa de acuerdo a los siguientes criterios:
# # a. Su longitud debe ser mayor de 7.5 cm pero no exceder los 9 cm
# # b. Su diámetro no debe ser menor que 0.5 cm ni mayor de 1.3 cm.
# # c. Por ningún motivo su masa debe exceder los 5.8 cm
# # i. Nota: masa = diámetro * longitud / densidad; densidad = 3.5
# # Gr/cm

longitud = float(input("Ingrese la longitud de la varilla: "))
diametro = float(input("Ingrese el diametro de la varilla: "))
densidad = 3.5
masa = diametro * longitud / densidad


if(longitud > 7.5 and longitud < 9 and diametro > 0.5 and diametro < 1.3 and masa < 5.8):
    print("Pieza Aceptada")
else: 
    print("Pieza Rechazada")

# # 12.Un vendedor desea calcular su comisión total sobre las ventas de varios
# # artículos. Al vendedor le corresponde el 3% de comisión sobre artículos
# # cuyo precio es menor de $2.000.oo y el 5% de comisión sobre artículos
# # cuyo precio es de $2000.oo o más. El vendedor hizo 50 ventas y desea
# # saber también cuántas ventas hizo menores de 2000 y cuantas mayores o
# # iguales a 2000.

comisionTotal = 0
mayores = 0
menores = 0

for i in range(5):
    precio = float(input(f"Ingrese el valor de la venta {i+1}: "))

    if precio < 2000:
        comision = precio*0.03
        menores += 1
    else: 
        comision = precio*0.05
        mayores += 1
    comisionTotal += comision

print(f"Ventas menores (2000): {menores}")
print(f"Ventas Mayores o iguales (2000): {mayores}")
print(f"La comision de todas las ventas es de: {comisionTotal}")

# # 13.desarrollar un algoritmo que halle la nota total de una materia en el SENA, y
# # determine si la gano o la reprobó

notas = 3
suma = 0

for i in range (notas):
    nota = float(input(f"Ingrese la nota {i+1}: "))

    if(nota > 5):
        print("Solo digite notas de 1 a 5")
    else:
        suma += nota
        promedio = suma/notas

if(promedio >= 3):
    print("Aprobado")
    print(f"Nota total: {promedio}")
else:
    print("Reprobado")
    print(f"Nota total: {promedio}")

# 14. Desarrollar un algoritmo que evalué la siguiente expresión aritmética 1/n.

n = int(input("Ingrese un numero para calcular: "))
expresion = 1 / n
print(f"El resultado es: {expresion}")

# 15. desarrollar el algoritmo que evalué la formula cuadrática o general.

a = float(input("Ingrese el numero a: "))
b = float(input("Ingrese el numero b: "))
c = float(input("Ingrese el numero c: "))

discriminante = b**2 - 4*a*c

if discriminante >= 0:
  x1 = (-b+ math.sqrt(discriminante)) / (2*a)
  x2 = (-b- math.sqrt(discriminante)) / (2*a)
  print(f"X1: {x1} X2: {x2}")
else:
  print("No tiene solucion")


# 16.desarrollar un algoritmo que capture un número y diga si es par o impar.

numero = int(input("Ingrese un numero: "))

if (numero % 2 == 0):
    print(f"{numero} Es Numero Par")
else:
    print(f"{numero} Es Numero Impar")

# 17.desarrollar el algoritmo que lea tres números y diga si uno es divisible del
# otro.

numero1 =  int(input("Ingrese el primer numero: "))
numero2 =  int(input("Ingrese el segundo numero: "))
numero3 =  int(input("Ingrese el tercer numero: "))

if(numero1 % numero2):
    print("Primer y Segundo Numero Son Divisibles")
elif(numero1 % numero3):
    print("Primer y Tercer Numero Son Divisibles")
elif(numero2 % numero3):
    print("Segundo y Tercer Numero Son Divisibles")
else:
    print("No hay numeros divisibles entre si")
    
# 18.Desarrollar un algoritmo que capture un número y diga si negativo o
# positivo.

numero =  int(input("Ingrese un numero: "))

if numero < 0:
    print(f"El número {numero} es Negativo")
else: 
    print(f"El número {numero} es Positivo")
