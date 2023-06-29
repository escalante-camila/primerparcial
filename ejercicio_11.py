# EJERCICIO 11: Escribe un programa que muestre los números del 1 al 10. Además, el programa debe mostrar:
#  a. Si es número es par o impar.
#  b. Cuanto es la suma total de todos los números mostrados.
#  c. Cuanto es la suma total de todos los números pares mostrados.
#  d. Cuanto es la suma total de todos los números impares mostradoS.

#Introducción al programa
print("Programa iniciado: ")

numero = 1 #El contador "numero" inicia en 1 para poder entrar en el ciclo while.
suma_par = 0 #Acumulador de números pares.
suma_impar = 0 #Acumulador de números impares.

while numero <= 10: #Condición para que ingresen diez números al ciclo while.
    if numero % 2 == 0: #Evaluación si resto de la división del  número es 0 y mensaje de par o impar según corresponda.
        print ("El número ", numero, " es par.")
        suma_par = suma_par + numero #Acumula el número actual en el acumulador "par".
    else:
        print ("El número ", numero, " es impar.")
        suma_impar = suma_impar + numero #Acumula el número actual en el acumulador "impar".
    numero = numero + 1 #Suma en 1 el contador "numero".

#Mensajes con los resultados de sumas de números pares, impares y generales.
print ("El resultado de la suma de todos los números es: ", suma_impar + suma_par)
print ("El resultado de la suma de los número impares es: ", suma_par)
print ("El resultado de la suma de los número impares es: ", suma_impar)

#Mensaje de fin del programa.
print("Fin del programa.")

