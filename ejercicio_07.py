# EJERCICIO 7: Del punto anterior, y considerando que durante 12 meses el empleado trabajó las mismas cantidades
# de horas, escribe un programa que calcule el descuento anual a realizarse, considerando: 
#  a. Si el sueldo anual es mayor a $2.000.000, el descuento es del %5.
#  b. Si el sueldo anual esta entre $1.000.000 y $2.000.000, debe aplicarse un descuento del %3.
#  c. Si el sueldo anual es menor a $1.000.000, debe aplicarse un descuento del %1. 
#  d. El programa debe mostrar el salario anual bruto, el monto anual de bonificaciones, el monto anual 
# a descontarse y las horas trabajadas en todo el año.

#Introducción al programa.
print(" Realizaremos el cálculo del sueldo bruto, las bonificaciones y los descuentos anuales de un empleado: ")

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
    print("Sueldo anual bruto: $", sueldo1 * 12) #Mensajes y cálculo de sueldo bruto anual.
    print("Bonificación anual: $", bonificacion18 * 12) #Mensaje y cálculo de bonificación anual corresponiente.
    print("Descuento anual del 5%: $", (sueldo1 * 12) * 0.5) #Mensaje y cálculos de descuento anual del 5%
    print("Horas anuales trabajadas: ", horas_trabajadas * 12) 
elif horas_trabajadas <= 120 and horas_trabajadas >= 80: 
    print("Sueldo anual bruto: $", sueldo2 * 12) #Mensaje y cálculo de sueldo anual.
    print("Bonificación anual: $", bonificacion15 * 12) #Mensaje y cálculo de bonificación anual corresponiente.
    print("Descuento anual del 3% : $", (sueldo2 * 12 ) * 0.3) #Mensaje y cálculo de descuento anual del 3%.
    print("Horas anuales trabajadas: ", horas_trabajadas * 12) #Mensaje de horas anuales trabajadas.
else:
    print("Sueldo anual bruto: $", sueldo3 * 12) #Mensaje y cálculo de sueldo anual.
    print("Bonificación anual: $", bonificacion13 * 12) #Mensaje y cálculo de bonificación anual correspondiente.
    print("Descuento anual del 1%: $", (sueldo3 * 12) * 0.1) #Mensaje y cálculo de descuento anual del 1%.
    print("Horas anuales trabajadas: ", horas_trabajadas * 12) #Mensajes de horas anuales trabajadas.

#Mensaje de fin del programa.
print("Fin del programa.")