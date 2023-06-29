# EJERCICIO 6: Del punto anterior, calcular y mostrar por pantalla el sueldo bruto, el monto a bonificar 
# y el sueldo neto (bruto + bonif), considerando:
#  a. Si trabajo más de 120hs, la bonificación es de %18
#  b. Si trabajo entre 80 y 120 horas, la bonificación es de %15
#  c. Si trabajo menos de 80 horas, la bonificación es de %13.


#Introducción al programa.
print("Realizaremos el cálculo del sueldo bruto, bonificación y sueldo neto de un empleado según sus horas trabajadas: ")
#Ingresa las horas trabajadas.
horas_trabajadas = float(input("Ingrese la candidad de horas trabajadas en el mes: "))

#Cálculo de sueldo si trabajó más de 120hs al mes.
sueldo1 = horas_trabajadas * 1500
#Cálculo de sueldo si trabajó entre 80hs y 120hs al mes.
sueldo2 = horas_trabajadas * 1300
#Cálculo de sueldo si trabajó menos de 80hs al mes.
sueldo3 = horas_trabajadas * 1100

#Cálculo de bonificación del 18% a sueldo mayor de 120hs trabajadas.
bonificacion18 = sueldo1 * 0.18 
#Cálculo de bonificación del 15% a sueldo entre 80hs a 120hs trabajadas.
bonificacion15 = sueldo2 * 0.15
#Cálculo de bonificación del 13% a sueldo menor de 80hs trabajadas.
bonificacion13 = sueldo3 * 0.13 

#Cálculo del sueldo neto si trabajó más de 120hs.
sueldo_neto1 = sueldo1 + bonificacion18
#Cálculo del sueldo neto si trabajó entre 80hs y 120hs.
sueldo_neto2 = sueldo2 + bonificacion15
#Cálculo del sueldo neto si trabajó menos de 80hs.
sueldo_neto3 = sueldo3 + bonificacion13

#Evaluación de horas trabajadas y mensaje de sueldo según corresponda.
if horas_trabajadas > 120:
    print("Sueldo bruto: $", sueldo1) #Mensajes de sueldo con horas trabajadas mayor a 120.
    print("Bonificación del 18% por horas trabajadas: ", bonificacion18)
    print("Sueldo neto: ", sueldo_neto1) 
elif horas_trabajadas <= 120 and horas_trabajadas >= 80: 
    print("Sueldo bruto: $", sueldo2) #Mensaje de sueldo con horas trabajadas entre 80hs y 120hs.
    print("Bonificación del 15% por horas trabajadas: ", bonificacion15)
    print("Sueldo neto: ", sueldo_neto2) 
else:
    print("Sueldo bruto: $", sueldo3) #Mensaje de sueldo con horas trabajadas menor a 80hs.
    print("Bonificación del 13% por horas trabajadas: ", bonificacion13)
    print("Sueldo neto: ", sueldo_neto3) 

#Mensaje de fin del programa.
print("Fin del programa.")