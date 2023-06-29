# EJERCICIO 8: Escribe un programa solicite y muestre por pantalla el nombre, apellido y edad de 5 personas.

#Introducción al programa.
print("Ingresa el nombre, apellido y edad de cinco personas: ")

personas = 0 

while personas < 5: #Ciclo para ingresar los datos de cinco personas.
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    edad = int(input("Edad: ")) 
    personas = personas + 1 #Suma en 1 el valor del contador personas.
    print("Persona Nro ", personas , " Nombre: ", nombre, " Apellido: ", apellido, " . Edad: ", edad ) #Mensaje de datos en pantalla.

print ("Fin del programa. ¡Muchas gracias por completar los datos!.") #Mensaje de cierre del programa.
