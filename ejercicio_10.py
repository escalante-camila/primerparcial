#EJERCICIO 10: Escribe un programa que calcule el promedio general de una clase.

#Introducción
print("A continuación calcularemos el promedio general de una clase: ")

alumnos = int(input("¿Cuántos alumnos hay en la clase?: ")) #Ingresa la cantidad de alumnos de la clase
alumno = 1
notas= 0

while alumno <= alumnos: #Evaluación e ingreso de notas de cada alumno.
    nota =float(input("Ingresar nota: "))
    notas = notas + nota #acumula la nota del alumno al acumulador "notas".
    alumno = alumno + 1 #suma en 1 la cantidad de alumnos en cada repetición.
    print ("Nota individual: ", nota) #Mensaje de nota individual.

promedio_clase = notas / alumnos #Cálculo de promedio general de notas.
print("Total de alumnos: ", alumnos, " Promedio general: ", promedio_clase) #Mensaje de promedio general.

#Mensaje de fin del programa.
print("Fin del programa.")