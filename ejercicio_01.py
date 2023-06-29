# EJERCICIO 1: Escribe un programa que calcule la edad que cumplió o debe cumplir este año la persona, basado en el año de nacimiento.

#Introducción al programa.
print("A continuación calcularemos una edad según su fecha de nacimiento y el año actual: ")

#El usuario ingresa su año de nacimiento.
anio_nacimiento = int(input("Ingrese su año de nacimiento: "))
#El usuario ingresa el año actual.
anio_actual = int(input("Ingrese el año actual: "))
 #Cálculo para saber la edad a cumplir en el año actual.
edad = anio_actual - anio_nacimiento

print ("En este año deberías cumplir ", edad, " años.")  #Imprime por pantalla mensaje con edad a cumplir o cumplida.