# EJERCICIO 4: Escribe un programa que calcule el promedio final de una materia, basado en 3 notas de parciales,
# indicando por pantalla si el alumno aprobó o debe recursar la materia (se aprueba con 6).

#Introducción al programa.
print("A continuacion, calcularemos tu promedio según las notas de tres parciales y si aprobaste la materia: ")
#Ingresa la primer nota.
nota_primer_parcial = float(input("Ingrese la nota del primer parcial: "))
#Ingresa la segunda nota.
nota_segundo_parcial = float(input("Ingresa la nota del segundo parcial: "))
#Ingresa la tercer nota.
nota_tercer_parcial = float(input("Ingrese la nota del tercer parcial: "))
#Cálculo de promedio de notas.
promedio = (nota_primer_parcial + nota_segundo_parcial + nota_tercer_parcial) / 3
#Evaluación si las notas son mayores a 6 y mensaje de promedio aprobación ó recursada según corresponda.
if nota_primer_parcial >= 6 and nota_segundo_parcial >= 6 and nota_tercer_parcial >= 6:
    print("Tu promedio es: ", promedio, ". ¡Felicidades, aprobaste la materia!.")
else: 
    print ("Tu promedio es: ", promedio, ". Lo siento, pero deberás recursar la materia por no aprobar todos los parciales.")
