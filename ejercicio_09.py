# EJERCICIO 9: Escribe un programa que solicite y muestre por pantalla nombre, apellido y edad de una cantidad
# de personas ingresada por el usuario.


#Introducción al programa.
print("A continuación, ingresar nombre, apellido y edad de una persona: ")

continuamos = "si" #Continuamos inicia con el valor "si" para poder ingresar al ciclo while. 

while continuamos == "si" : #Evaluación de condición e ingreso de datos.
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    edad = int(input("Edad:"))
    
    print ("Nombre: ", nombre, " Apeliido: ", apellido, " Edad: ", edad) #Mensaje de datos.
    continuamos = input("¿Continuamos? si / no: ") #Pregunta al usuario si desea continuar.

if continuamos == "no": #Evaluación de mensaje a realizar según respuesta distinta a "si" y su mensaje correspondiente.
    print("¡Muchas gracias por su colaboración!.")
else: 
    print("El programa solo admite los valores << si >> o << no >>. Inténtelo nuevamente.")

print("Fin del programa.")