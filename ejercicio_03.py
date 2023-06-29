# EJERCICIO 3: Escribe un programa que calcule la equivalencia a pesos de los dólares ingresados por pantalla.
# El programa debe preguntar el tipo de cambio a convertir (es decir, cuánto cotiza el dólar).

#Introducción al programa.
print("Calcularemos la equivalencia de dólar a peso agentino de un monto específico") 
#Ingresa el valor actual del dólar.
valor_dolar = float(input("Ingrese el valor actual del dólar: "))
#Ingresa la cantidad de dólares que quiere convertir a pesos argentinos.
cantidad_de_dolares = float(input("Ingrese la cantidad de dólares a convertir a pesos argentinos: ")) 
#Cálculo de conversión de dólares a pesos.
equivalencia_a_pesos = valor_dolar * cantidad_de_dolares 
 #Mensaje con el resultado de la equivalencia.
print("La equivalencia de US$", cantidad_de_dolares, " serían AR$", equivalencia_a_pesos)
