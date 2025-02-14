# 1. Desarrolle un algoritmo que lea un número, en caso de ser negativo lo
# imprima junto con su positivo.

numero = int(input("Ingrese un numero: "))
if(numero < 0):
    print(f"Negativo: {numero} Positivo: {numero.__abs__()}")

# 2. desarrollar un programa que, dado una calificación de un alumno en un
# parcial, escribe aprobado si la calificación es superior a 3.

nota = int(input("Ingrese la nota del parcial: "))

if(nota >= 3):
    print("Aprobado")
else:
    print("No Aprobado")

# 3. desarrollar el algoritmo dado como dato el sueldo de un trabajador, le aplica
# un aumento del 15% si su sueldo es inferior a $300.000

sueldo = float(input("Ingrese el sueldo del trabajador: "))
if(sueldo < 300000):
    nuevo = sueldo*1.15
    print("Su sueldo es inferior a $300.000 por lo que ha recibido un aumento y ahora es de: ", nuevo)
else: print(f"Su sueldo es de: {sueldo}")

# 4. desarrollar un algoritmo que asigne el sueldo a cinco empleados, teniendo
# en cuenta su categoría.

for i in range(5):
    categoria = int(input("Ingrese la categoria del empleado (1, 2, 3, 4, 5): "))
    match categoria:
        case 1:
            sueldo = 1000000
            print(f"Su categoria es {categoria} y su sueldo es de {sueldo}")
        case 2: 
            sueldo = 1500000 
            print(f"Su categoria es {categoria} y su sueldo es de {sueldo}")
        case 3: 
            sueldo = 1700000
            print(f"Su categoria es {categoria} y su sueldo es de {sueldo}")
        case 4: 
            sueldo = 2500000 
            print(f"Su categoria es {categoria} y su sueldo es de {sueldo}")
        case 5: 
            sueldo = 2700000 
            print(f"Su categoria es {categoria} y su sueldo es de {sueldo}")

# 5. desarrollar un programa que capture tres números e imprima por pantalla
# cual es el número mayor, el menor, cuales son iguales, si los tres
# diferentes.

numero1 =  int(input("Ingrese el primer numero: "))
numero2 =  int(input("Ingrese el segundo numero: "))
numero3 =  int(input("Ingrese el tercer numero: "))

mayor = max(numero1, numero2, numero3)
menor = min(numero1, numero2, numero3)

if (numero1 == numero2 == numero3):
    print("Los 3 números son iguales")
elif (numero1 == numero2):
    print(f"El primer y segundo numero son iguales, el mayor es {mayor} y el menor es {menor}")
elif (numero1 == numero3):
    print(f"El primer y tercer numero son iguales, el mayor es {mayor} y el menor es {menor}")
elif (numero2 == numero3):
    print(f"El segundo y tercer numero son iguales, el mayor es {mayor} y el menor es {menor}")
else:
    print(f"Los 3 numeros son diferentes, el mayor es {mayor} y el menor es {menor}")

# 6. Escriba el algoritmo que al capturar un numero entero convierta grados
# centígrados a kelvin, si captura un numero flotante diga si es mayor a 10.5,
# y si captura un carácter escriba su nombre.

numero = float(input("Ingrese el numero que desea convertir: "))
kelvin = (numero + 273.15)

print(kelvin)

if(kelvin > 10.5):
    print("Es mayor a 10.5")

# 7. Desarrolle un algoritmo que lea de un registro: el nombre, la edad, el sexo,
# el estado civil de cualquier persona e imprima el nombre de la persona, si
# corresponde a un hombre casado mayor de 40 años o a una mujer soltera
# menor de 50 años.

nombre = input("Ingrese el nombre: ")
edad =  int(input("Ingrese la edad: "))
sexo = input("Ingrese el sexo: ")
estado = input("Ingrese el estado civil: ")

if (estado == 'casado' and edad > 40 and sexo == 'hombre' or estado == 'soltera' and edad < 50 and sexo == 'mujer'):
    print(nombre)

# 8. Prepare un algoritmo que identifique e imprima el número medio de un
# conjunto de tres números únicos. El número medio es aquel que no es el
# menor ni el mayor.

numero1 =  int(input("Ingrese el primer numero: "))
numero2 =  int(input("Ingrese el segundo numero: "))
numero3 =  int(input("Ingrese el tercer numero: "))

if(numero1 > numero2 and numero1 < numero3 or numero1 < numero2 and numero1 > numero3):
    print(f"El numero medio es: {numero1}")
elif(numero2 > numero1 and numero2 < numero3 or numero2 < numero1 and numero2 > numero3):
    print(f"El numero medio es: {numero2}")
elif(numero3 > numero1 and numero3 < numero2 or numero3 < numero1 and numero3 > numero2):
    print(f"El numero medio es: {numero3}")
else:
    print("Digite 3 numeros unicos")
    
# 9. Dados tres números enteros únicos, a, b y c. Elabore un algoritmo que los
# ordene de mayor a menor e imprímalos.

numero1 =  int(input("Ingrese el primer numero: "))
numero2 =  int(input("Ingrese el segundo numero: "))
numero3 =  int(input("Ingrese el tercer numero: "))

mayor = max(numero1, numero2, numero3)
menor = min(numero1, numero2, numero3)


if(numero1 > numero2 and numero1 < numero3 or numero1 < numero2 and numero1 > numero3):
    medio = numero1
elif(numero2 > numero1 and numero2 < numero3 or numero2 < numero1 and numero2 > numero3):
    medio = numero2
else:
    medio = numero3
print(f"Mayor: {mayor}, Medio: {medio}, Menor: {menor}")

# 10.A ciertos estudiantes se les dice que su calificación final será el promedio
# de las dos calificaciones más altas de entre las tres que se han obtenido en
# el curso. Haga un algoritmo que permita a un estudiante efectuar el cálculo
# correspondiente a su nota final.

nota1 =  int(input("Ingrese la nota 1: "))
nota2 =  int(input("Ingrese la nota 2: "))
nota3 =  int(input("Ingrese la nota 3: "))

if(nota1 <= nota2 and nota1 <= nota3):
    suma = nota2 + nota3
elif(nota2 <= nota1  and nota2 <= nota3):
    suma = nota1 + nota3
else:
    suma = nota1 + nota2
promedio = suma/2
print(f"La suma de sus notas es: {suma} y su promedio es: {promedio}")





