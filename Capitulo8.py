#Capítulo 8: archivo de entrada y de salida Dentro de Python
#Cuando se trata de trabajar en un código dentro de Python, hay momentos en
#los que desea almacenar los datos de modo que esté disponible para su uso
#más adelante, cuando sea necesario. 

#Cómo crear un nuevo archivo
#Una de las primeras cosas que vamos a hablar acerca de esto es cómo se
#puede crear un nuevo archivo de marca de aferrarse a su código. Si desea
#crear un nuevo archivo y ser capaz de escribir en él, primero tiene que abrirlo
#en el interior de su IDE y después elija el modo que desea utilizar para
#escribir en ella; hay algunas opciones que puede elegir. Las tres opciones que
#usted como el programador es capaz de elegir cuando se escribe en el código
#incluyen el modo (x), escribir (w), y añadir (a). Si tros tiempos eare cuando se
#quieren hacer nuevos cambios en un archivo que ha abierto, puede utilizar la
#opción (w), ya que es la más fácil.

#file handling operations
#writing to a new file hello.txt
f = open(‘hello.txt’, ‘w’, encoding = ‘utf-8’)
f.write(“Hello Python Developers!”)
f.write(“Welcome to Python World”)
f.flush()
f.close()

#Tómese el tiempo para agregar esto en el compilador y cuando se hace, que
#son básicamente está asegurando que toda la información que se está creando
#va a ir dentro del directorio actual por lo que es posible que desee asegurarse
#de que usted está en un directorio que va a funcionar para su almacenamiento o
#al menos uno que está ableto recuerde. Así que cualquier directorio que está
#en este momento es el que va a haber existido para volver a cuando se está
#buscando el archivo, en este caso, el archivo hola.txt
#file handling operations
#writing to a new file hello.txt
f = open(‘hello.txt’, ‘w’, encoding = ‘utf-8’)
f.write(“Hello Python Developers!”)
f.write(“Welcome to Python World”)
mylist = [“Apple”, “Orange”, “Banana”]
#writelines() is used to write multiple lines in to the file
f.write(mylist)
f.flush()
f.close()

#Cómo trabajar con archivos binarios
#Otra cosa que puede que tenga que hacer frente a cuando se está trabajando en
#estos archivos es cuando se desea escribir sus datos de manera que se
#considera un archivo binario. Este es un proceso sencillo que hacer dentro de
#Python, ya que sólo tendrá que tomar los datos y escribirlo como un archivo de
#sonido o imagen en lugar de un archivo de texto. Usted puede cambiar
#cualquier texto que está escribiendo en el interior de Python en un archivo
#binario, sin importar si se trataba de un sonido, una imagen o archivo de texto
#en el principio. Lo más importante que usted entienda en este es que se debe
#suministrar los datos dentro del objeto de modo que más tarde puede ser
#expuesto como un bocado. La sintaxis que se puede utilizar con el fin de
#escribir el texto como un archivo binario incluye:
# Escribir datos binarios en un archivo
# write binary data to a file
# writing the file hello.dat write binary mode
F = open(‘hello.dat’, ‘wb’)
# writing as byte strings
f.write(b”I am writing data in binary file!/n”)
f.write(b”Let’s write another list/n”)
f.close()

#Antes de seguir adelante, tomar algún tiempo para abrir el compilador y
#escriba todo esto. Asegúrese de que tiene las funciones de codificación y
#decodificación en su lugar para que sea más fácil para escribir e incluso rad el
#texto en el archivo de modo binario. Si desea permitir que esto suceda dentro
#de su código, asegúrese de que usted escribe el siguiente código de ejemplo:
# write binary data to a file
# writing the file hello.dat write binary mode
f = open(‘hello.dat’, ‘wb’)
text = “Hello World”
f.write(text.encode(‘utf-8’))
f.close()

#La apertura de un archivo
#En los dos ejemplos que estaban por encima, pasamos un tiempo hablando
#acerca de cómo escribir las palabras que van en el archivo y cómo cambiar el
#texto de manera que es una función binaria. Ahora no van a haber momentos en
#los que le gustaría abrir un archivo para que usted es capaz de utilizarlo de
#nuevo. El código que se escribe se almacena en juego el equipo por lo que
#sólo tiene que encontrar estos con el fin de abrirlos de nuevo. Aquí está un
#ejemplo de cómo podría hacer esto
# read binary data to a file
#writing the file hello.dat write append binary mode
with open(“hello.dat”, ‘rb’) as f:
    data = f.read()
    text = data.decode(‘utf-8’(
        print(text)

#La búsqueda de uno de sus archivos
#Además de hacer algunas de las tareas que hemos hablado anteriormente,
#también hay momentos en que es posible que desee realizar cambios en
#algunos de sus archivos o encontrar una manera de moverse
