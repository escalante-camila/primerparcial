# EJERCICIO 12: . Escribe un programa que permita ingresar las edades de las personas, hasta que el usuario decida no
# hacerlo más, y muestre, al final, un promedio de las edades ingresadas y el total de personas ingresadas.


#Introducción al programa.
print("A continuación, ingresar las edades deseadas: ")

edades = 0          #Contador.
personas = 0        #Acumulador.
continuamos = "si"  #Condición inicia en "si" para entrar en el ciclo while .

while continuamos == "si": #Evaluación de condición: mientras el usuario responda "si" entrará al ciclo.
    edad = int(input("Ingresar edad: ")) #Ingresa edad.
    personas = personas + 1 #Suma en 1 a personas con cada edad ingresada. 
    edades = edades + edad #Acumula la edad ingresada en edades.

    continuamos = input("¿Desea ingresar otra edad? si / no: ") #Consulta si desea continuar.

promedio_edades = edades / personas #Cálculo de promedio de edades ingresadas.

if continuamos == "no": #Evaluación y mensaje correspondiente según respuesta distinta que "si".
    print("Cantidad de personas ingresadas: ", personas, ". Promedio de edades ingresadas: ", promedio_edades)
    print("Fin del programa. ¡Muchas gracias por su colaboración!.")
else:
    print ("El programa solo soporta los valores << si >> o << no >>. Inténtelo nuevamente.")




