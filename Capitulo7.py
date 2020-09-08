##Capítulo 7: Trabajando con Loops Dentro de Python
#Mientras que las sentencias de control de decisiones añadir un poco de buena
#potencia al código y pueden ayudarle a hacer mucho más que antes, es
#definitivamente una buena idea trabajar con los bucles dentro del programa
#Python

#¿Cuál es el bucle while?
#Uno de los tipos de bucle que son capaces de trabajar en la que se conoce
#como el bucle while. Esta es la que tendrá que utilizar cada vez que el código
#debe pasar por el ciclo de una cantidad fija de veces.

counter = 1
while(counter <= 3):
    principal = int(input(“Enter the principal amount:”))
    numberofyeras = int(input(“Enter the number of years:”))
    rateofinterest = float(input(“Enter the rate of interest:”))
    simpleinterest = principal * numberofyears * rateofinterest/100
    print(“Simple interest = %.2f” %simpleinterest)
    #increase the counter by 1
    counter = counter + 1
    print(“You have calculated simple interest for 3 time!”)

#¿Cómo es el bucle diferente?
#Hay muchas veces que el bucle while será su amigo y puede ayudarle a
#obtener una gran cantidad de cosas, pero hay otras veces cuando el bucle es
#útil. El bucle se considera de una manera más tradicional para escribir el
#bucle, pero hay muchas ocasiones en las que se desea utilizarlo
# Measure some strings:
words = [‘apple’, ‘mango’, ‘banana’, ‘orange’]
for w in words:
print(w, len(w))

#El bucle anidado
#El último tipo de bucle que puede resultar útil usar dentro de su código Python
#es el bucle anidado. Cuando se está utilizando un bucle anidado, que son
#básicamente tomando un bucle y colocándola en el interior del otro y luego
#permitir a ambos a seguir corriendo hasta que se hacen. Hay varias ocasiones
#en que esto puede ser útil para ayudarle a hacer las cosas. Un buen ejemplo
#sería cuando se desea escribir una tabla de multiplicar que comienza en 1 y va
#todo el camino a 10. Aquí está un ejemplo de cómo funcionaría:
#write a multiplication table from 1 to 10
For x in xrange(1, 11):
For y in xrange(1, 11):
Print ‘%d = %d’% (x, y, x*x)

