# EJERCICIO 5: Escribe un programa que calcule el sueldo de un empleado basándose en la cantidad de horas 
# y muestre por pantalla el resultado, considerando lo siguiente:
#  a. Si trabajo más de 120hs por mes, la hora tiene un valor de $1500.
#  b. Si trabajo entre 80 y 120hs por mes, la hora tiene un valor de $1300.
#  c. Si trabajo menos de 80 horas por mes, la hora tiene un valor de $1100.

#Introducción al programa.
print("Realizaremos el cálculo del sueldo de un empleado según sus horas trabajadas: ")
#Ingresa las horas trabajadas.
horas_trabajadas = float(input("Ingrese la candidad de horas trabajadas en el mes: "))

#Cálculo de sueldo si trabajó más de 120hs al mes.
sueldo1 = horas_trabajadas * 1500
#Cálculo de sueldo si trabajó entre 80hs y 120hs al mes.
sueldo2 = horas_trabajadas * 1300
#Cálculo de sueldo si trabajó menos de 80hs al mes.
sueldo3 = horas_trabajadas * 1100

#Evaluación de horas trabajadas y mensaje de sueldo según horas trabajadas.
if horas_trabajadas > 120:
    print("Su sueldo es: $", sueldo1) #Mensaje de sueldo con horas trabajadas mayor a 120.
elif horas_trabajadas <= 120 and horas_trabajadas >= 80: 
    print("Su sueldo es: $", sueldo2) #Mensaje de sueldo con horas trabajadas entre 80hs y 120hs.
else:
    print("Su sueldo es: $", sueldo3) #Mensaje de sueldo con horas trabajadas menor a 80hs.

print("Fin del programa.")