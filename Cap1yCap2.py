#Las palabras clave de Python
#Al igual que muchos de los otros lenguajes de programación que va a utilizar,
#Python tiene algunas palabras clave que son específicas sólo para él y que no
#se puede utilizar en otras partes del código. Estas palabras clave dan
#comandos al compilador para que sepa cómo reaccionar a los códigos que
#está escribiendo. Por eso están reservados; Si usted comienza a utilizarlos en
#otras partes del código, usted va a confundir al compilador y podría tener
#algunos problemas con el código que trabaja la manera que usted quisiera.
#NO USAR CLASS|FUNCTION|PROGRAM|DEF|INT|FLOAT

#Nombrar los identificadores
#Mientras está trabajando dentro de Python, o cualquier otro lenguaje de
#programación, hay muchos identificadores con los que trabajará. Estos van por
#muchos nombres diferentes, incluyendo clases, entidades, funciones y
#variables. Cuando intenta nombrar uno de estos identificadores, podrá utilizar
#la misma información y reglas para cada uno de ellos. Algunas de las reglas
#que debe seguir cuando trabaja en python incluyen:
#Puede utilizar una amplia gama de opciones de nomenclatura, incluidas las
#letras minúsculas y minúsculas, así como los números y el símbolo de
#subrayado. Usted puede utilizar cualquier combinación de estos que usted
#quisiera, usted apenas necesita cerciorarse de que usted no agrega en espacios
#en el nombre si usted tiene más de una palabra para ella.
#Sus identificadores no deben comenzar con un número. Puede tener un número
#en otro lugar del código, no puede ser el primer carácter en el nombre
#Hay algunas otras cosas que usted debe considerar al nombrar los
#identificadores también, aunque éstos no afectarían el código de una manera de
#darle un error, siguen siendo importantes hacer las cosas más fáciles. Por
#ejemplo, desea asegurarse de que el nombre es fácil de leer porque desea
#permitir que otros lean el código sin tener problemas para entender lo que está
#intentando hacer. Escoger un nombre que sea descriptivo puede ayudar
#también porque le permitirá recordar lo que quería hacer el identificador en
#primer lugar.
#NO USAR LA SIGUIENTES VARIABLES COMO
#1VALOR ERROR
#VAR    ERROR
#int    ERROR
#$VALOR ERROR
#_Valor Valido
#PrimeraLetraEnMayuscula Valido
#camelCaseEjemplo        Valido


#Flujo de control en Python
#El flujo de control es importante dentro de un lenguaje de codificación, ya que
#le ayuda a determinar cómo debe escribir el código que desea haber
#hecho. Para Python, va a leer los códigos de arriba a abajo, de una manera
#similar a la que leería un libro en casa. Y para asegurarse de que va a
#mantener el código funcionando tan bien como sea posible, debe escribir las
#diferentes partes como si fuera una lista de supermercado. Algunas personas
#les gusta escribir todos los comandos justo al lado del otro y hacer un lío, pero
#esto no sólo es difícil de leer, pero también hace que el código causa más
#errores. Escriba cada una de las partes del código en una línea separada para
#ayudar al flujo de control a ir lo más suavemente posible y para asegurarse de
#que otros puedan leerlo correctamente.

#Declaraciones
#Las declaraciones pueden ser realmente útiles dentro de su código porque le
#ayudan a escribir su código. Estas serán las cadenas de código que escribirá
#para decirle al compilador lo que le gustaría haber hecho cuando se ejecutó el
#código. Siempre y cuando se configuran de una manera que el compilador es
#capaz de entender, usted va a obtener un buen código que funcionará bien en el
#equipo. La declaración puede ser corta, sólo tiene unas pocas líneas en ellos o
#pueden ser realmente largas y contienen un bloque completo de código.

#Comentarios
#Hay veces en que usted querrá escribir comentarios dentro de su código. Estos
#son útiles porque pueden ayudarle a nombrar el código o dejar otra
#información en el código para que otros programadores son capaces de llegar
#a él y entender lo que está sucediendo dentro del código. Encontrará que el
#compilador buscará el signo de comentario (que es el signo #) y luego saltará
#el comentario y pasará a la siguiente línea del código. Esto significa que los
#comentarios no afectarán a lo que se ejecuta dentro del código, sino que estará
#allí para que otros lo utilicen.
#TODO ESTO ES UN COMENTARIO ... INCLUSO LA PALABRA RESERVADA TO DO 

#Funciones en Python
#Cuando hablamos de una función dentro de nuestro lenguaje de codificación,
#estamos hablando de un bloque de código que puede reutilizar y que se
#utilizará para realizar una sola acción. Las funciones le ayudarán a reutilizar
#su código mucho mejor que antes y proporcionará más eficiencia en todo el
#código. Hay muchas funciones que ya están dentro del código de Python, pero
#obtienes la ventaja de crear algunas de las tuyas propias si quieres agregarlas
#en ti mismo.
#DEF F(X)

#  * Necesita usar la palabra clave "def"para comenzar el bloque de la
#  * función. Entonces necesitaría tener el nombre de la función así como algunos
#  * paréntesis para sostener los parámetros que usted utilizará más adelante.
#  * Cualquier argumento de entrada debe colocarse en esos paréntesis desde
#    arriba. También puede utilizarlos para los parámetros.
#  * La primera declaración que está dentro de la función se permite que sea
#    sólo una instrucción opcional si usted necesita.
#  * El bloque de código que se encuentra dentro de todas las funciones se
#    iniciará con dos puntos y luego se indentará.
#!/usr/bin/python
# Function definition is here
def printme( str ):
    "This prints a passed string into this function"
    print str
return;

# Now you can call printme function
    printme("I'm first call to user defined function!")
    printme("Again second call to the same function")

#Variables
#Las variables son básicamente las ubicaciones en la memoria de nuestro
#ordenador que están reservadas para almacenar algunos valores. Cada vez que
#decida crear una nueva variable, se va a reservar un poco de espacio dentro
#de su memoria. Dependiendo del tipo de datos que coloque en la variable, su
#intérprete podrá decidir dónde se almacenará para que lo encuentre más
#adelante. Esto facilita la asignación de todos los tipos de datos a las variables,
#incluidos los caracteres, los decimales y los enteros.
#!/usr/bin/python
counter = 100 # An integer assignment
miles = 1000.0 # A floating point
name = "John" # A string
print counter
print miles
print name

