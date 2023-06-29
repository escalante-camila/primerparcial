# EJERCICIO 2: Escribe un programa que calcule el área y el perímetro de un cuadrado
# y muestre los resultados (indicando cuál es cuál) por pantalla.

#Introducción al programa.
print("Calcularemos el área y perímetro de un cuadrado con el dato que nos brindes a continuación: ")

lado_cuadrado = float(input("Ingrese la medida de un lado de un cuadrado: ")) #El usuario ingresa un lado de un cuadrado.
area_cuadrado = lado_cuadrado * lado_cuadrado #Cálculo para área del cuadrado.
perimetro_cuadrado = lado_cuadrado * 4 #Cálculo para perímetro del cuadrado.

#Mensaje con los resultados del área y perímetro del cuadrado.
print ("El área del cuadrado es: ", area_cuadrado, " y su perímetro es ", perimetro_cuadrado)

#Mensaje del fin del programa.
print("Fin del programa.")