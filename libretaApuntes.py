>>> 2 + 2
4
>>> 50 - 5*6
20
>>> (50 - 5*6) / 4
5.0
>>> 8 / 5 # la división simpre retorna un número de punto flotante 1.6
>>> 17 / 3 # la división clásica retorna un punto flotante 5.666666666666667
>>>
>>> 17 // 3 # la división entera descarta la parte fraccional 5

>>> 17 % 3 # el operado % retorna el resto de la división
2
>>> 5 * 3 + 2 # resultado * divisor + resto
17

#Con Python, es posible usar el operador ** para calcular potencias 2:
>>> 5 ** 2 # 5 al cuadrado
25
>>> 2 ** 7 # 2 a la potencia de 7
128

# El signo igual (=) es usado para asignar un valor a una variable. Luego, ningún resultado es mostrado antes del próximo
# prompt
>>> ancho = 20
>>> largo = 5 * 9
>>> ancho * largo
900

#Hay soporte completo de punto flotante; operadores con operando mezclados convertirán los enteros a punto flotante:
>>> 4 * 3.75 - 1
14.0

# Cadenas de caracteres
# Además de números, Python puede manipular cadenas de texto, las cuales pueden ser expresadas de distintas formas.
# Pueden estar encerradas en comillas simples ('...') o dobles ("...") con el mismo resultado 3
# . \ puede ser usado para
# escapar comillas:

>>> 'huevos y pan' # comillas simples
'huevos y pan'
>>> 'doesn\'t' # usa \' para escapar comillas simples...
"doesn't"
>>> "doesn't" # ...o de lo contrario usa comillas doblas
"doesn't"
>>> '"Si," le dijo.'
'"Si," le dijo.'
>>> "\"Si,\" le dijo."
'"Si," le dijo.'
>>> '"Isn\'t," she said.'
'"Isn\'t," she said.'

# En el intéprete interactivo, la salida de cadenas está encerrada en comillas y los caracteres especiales son escapados con
# barras invertidas. Aunque esto a veces luzca diferente de la entrada (las comillas que encierran pueden cambiar), las dos
# cadenas son equivalentes. La cadena se encierra en comillas dobles si la cadena contiene una comilla simple y ninguna
# doble, de lo contrario es encerrada en comillas simples. La función print() produce una salida más legible, omitiendo las
# comillas que la encierran e imprimiendo caracteres especiales y escapados

>>> '"Isn\'t," she said.'
'"Isn\'t," she said.'
>>> print('"Isn\'t," she said.')
"Isn't," she said.
>>> s = 'Primerea línea.\nSegunda línea.' # \n significa nueva línea
>>> s # sin print(), \n es incluído en la salida
'Primera línea.\nSegunda línea.'
>>> print(s) # con print(), \n produce una nueva línea
Primera línea.
Segunda línea.

#Si no querés que los caracteres antepuestos por \ sean interpretados como caracteres especiales, podés usar cadenas
#crudas agregando una r antes de la primera comilla:
>>> print('C:\algun\nombre') # aquí \n significa nueva línea!
C:\algun
ombre
>>> print(r'C:\algun\nombre') # nota la r antes de la comilla
C:\algun\nombre

#Las cadenas de texto literales pueden contener múltiples líneas. Una forma es usar triple comillas: """...""" o
#'''...'''. Los fin de línea son incluídos automáticamente, pero es posible prevenir esto agregando una \ al final de la
#línea. Por ejemplo:
print("""\
Uso: algo [OPTIONS]
 -h Muestra el mensaje de uso
 -H nombrehost Nombre del host al cual conectarse
""")
#produce la siguiente salida: (nota que la línea inicial no está incluída)
Uso: algo [OPTIONS]
 -h Muestra el mensaje de uso
 -H nombrehost Nombre del host al cual conectarse
#Las cadenas de texto pueden ser concatenadas (pegadas juntas) con el operador + y repetidas con *:
>>> # 3 veces 'un', seguido de 'ium'
>>> 3 * 'un' + 'ium'
'unununium'
>>> 'Py' 'thon'
'Python'

#Si querés concatenar variables o una variable con un literal, usá +:
>>> prefix + 'thon'
'Python'

#Esta característica es particularmente útil cuando querés separar cadenadas largas:
>>> texto = ('Poné muchas cadenas dentro de paréntesis '
... 'para que ellas sean unidas juntas.')
>>> texto
'Poné muchas cadenas dentro de paréntesis para que ellas sean unidas juntas.'

#Las cadenas de texto se pueden indexar (subíndices), el primer carácter de la cadena tiene el índice 0. No hay un tipo de
#dato para los caracteres; un carácter es simplemente una cadena de longitud uno:
>>> palabra = 'Python'
>>> palabra[0] # caracter en la posición 0
'P'
>>> palabra[5] # caracter en la posición 5
'n'

#Además de los índices, las rebanadas también están soportadas. Mientras que los índices son usados para obtener
#caracteres individuales, las rebanadas te permiten obtener sub-cadenas:
>>> palabra[0:2] # caracteres desde la posición 0 (incluída) hasta la 2 (excluída)
'Py'
>>> palabra[2:5] # caracteres desde la posición 2 (incluída) hasta la 5 (excluída)
'tho'

#Una forma de recordar cómo funcionan las rebanadas es pensar en los índices como puntos entre caracteres, con el punto a
#la izquierda del primer carácter numerado en 0. Luego, el punto a la derecha del último carácter de una cadena de n
#caracteres tienen índice n, por ejemplo:
 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
   0   1   2   3   4   5   6
  -6  -5  -4  -3  -2  -1

#La función incorporada len() devuelve la longitud de una cadena de texto:
>>> s = 'supercalifrastilisticoespialidoso'
>>> len(s)
33

#Listas
#Python tiene varios tipos de datos compuestos, usados para agrupar otros valores. El más versátil es la lista, la cual puede
#ser escrita como una lista de valores separados por coma (ítems) entre corchetes. Las listas pueden contener ítems de
#diferentes tipos, pero usualmente los ítems son del mismo tipo:
>>> cuadrados = [1, 4, 9, 16, 25]
>>> cuadrados
[1, 4, 9, 16, 25]


#Como las cadenas de caracteres (y todos los otros tipos sequence integrados), las listas pueden ser indexadas y rebanadas:
>>> cuadrados[0] # índices retornan un ítem
1
>>> cuadrados[-1]
25
>>> cuadrados[-3:] # rebanadas retornan una nueva lista
[9, 16, 25]

#Todas las operaciones de rebanado devuelven una nueva lista conteniendo los elementos pedidos. Esto significa que la
#siguiente rebanada devuelve una copia superficial de la lista:
>>> cuadrados[:]
[1, 4, 9, 16, 25]

#Las listas también soportan operaciones como concatenación:
>>> cuadrados + [36, 49, 64, 81, 100]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#A diferencia de las cadenas de texto, que son immutable, las listas son un tipo mutable, es posible cambiar un su contenido:
>>> cubos = [1, 8, 27, 65, 125] # hay algo mal aquí
>>> 4 ** 3 # el cubo de 4 es 64, no 65!
64

#También es posible asignar a una rebanada, y esto incluso puede cambiar la longitud de la lista o vaciarla totalmente:
>>> letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> letras
['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> # reemplazar algunos valores
>>> letras[2:5] = ['C', 'D', 'E']
>>> letras
['a', 'b', 'C', 'D', 'E', 'f', 'g']
>>> # ahora borrarlas
>>> letras[2:5] = []
>>> letras
['a', 'b', 'f', 'g']
>>> # borrar la lista reemplzando todos los elementos por una lista vacía
>>> letras[:] = []
>>> letras
[]

#La función predefinida len() también sirve para las listas:
>>> letras = ['a', 'b', 'c', 'd']
>>> len(letras)
4

# Por supuesto, podemos usar Python para tareas más complicadas que sumar dos y dos. Por ejemplo, podemos escribir una
# subsecuencia inicial de la serie de Fibonacci así:
>>> # Series de Fibonacci:
... # la suma de dos elementos define el siguiente
... a, b = 0, 1
>>> while b < 10:
... print(b)
... a, b = b, a+b

# LA IDENTACIÓN: la sangría es la forma que usa Python para agrupar declaraciones. En el intérprete
# interactivo debés teclear un tab o espacio(s) para cada línea sangrada. En la práctica vas a preparar entradas más
# complicadas para Python con un editor de texto; todos los editores de texto decentes tienen la facilidad de agregar la
# sangría automáticamente. Al ingresar una declaración compuesta en forma interactiva, debés finalizar con una línea en
# blanco para indicar que está completa (ya que el analizador no puede adivinar cuando tecleaste la última línea). Notá
# que cada línea de un bloque básico debe estar sangrada de la misma forma.

# La función print() escribe el valor de el o los argumentos que se le pasan. Difiere de simplemente escribir la
# expresión que se quiere mostrar (como hicimos antes en los ejemplos de la calculadora) en la forma en que maneja
# múltiples argumentos, cantidades en punto flotante, y cadenas. Las cadenas de texto son impresas sin comillas, y un
# espacio en blanco es insertado entre los elementos, así podés formatear cosas de una forma agradable:
>>> i = 256*256
>>> print('El valor de i es', i)
El valor de i es 65536

#La sentencia 
#Tal vez el tipo más conocido de sentencia sea el if. Por ejemplo:
>>> x = int(input("Ingresa un entero, por favor: "))
Ingresa un entero, por favor: 42
>>> if x < 0:
... x = 0
... print('Negativo cambiado a cero')
...     elif x == 0:
    ... print('Cero')
...         elif x == 1:
        ... print('Simple')
            ... else:
            ... print('Más')
                ...                  
                'Mas'

#FOR
# La sentencia for en Python difiere un poco de lo que uno puede estar acostumbrado en lenguajes como C o Pascal. En
# lugar de siempre iterar sobre una progresión aritmética de números (como en Pascal) o darle al usuario la posibilidad de
# definir tanto el paso de la iteración como la condición de fin (como en C), la sentencia for de Python itera sobre los ítems de
# cualquier secuencia (una lista o una cadena de texto), en el orden que aparecen en la secuencia. Por ejemplo:
#ESTE ES MUCHO MÁS PARECIDO A FOR EACH
>>> # Midiendo cadenas de texto
... palabras = ['gato', 'ventana', 'defenestrado']
>>> for p in palabras:
... print(p, len(p))
...
gato 4
ventana 7
defenestrado 12

#Si se necesita iterar sobre una secuencia de números, es apropiado utilizar la función integrada range(), la cual genera
#progresiones aritméticas:
>>> for i in range(5):
... print(i)
...
0
1
2
3
4

for i in range(5, 10): 
    print(i)
#DESDE 0 hasta la posición 10, 3 pasos del vigía
for i in range(0, 10, 3):
    print(i)
    0, 3, 6, 9
//desde -10 hasta -100, paso de -30
for i in range(-10, -100, -30):
    print(i)
 -10, -40, -70

#iterar
>>> a = ['Mary', 'tenia', 'un', 'corderito']
>>> for i in range(len(a)):
... print(i, a[i])
...
0 Mary
1 tenia
2 un
3 corderito

# La sentencia break, como en C, termina el lazo for o while más anidado.
# Las sentencias de lazo pueden tener una cláusula else que es ejecutada cuando el lazo termina, luego de agotar la lista
# (con for) o cuando la condición se hace falsa (con while), pero no cuando el lazo es terminado con la sentencia break. Se
# ejemplifica en el siguiente lazo, que busca números primos:
>>> for n in range(2, 10):
...     for x in range(2, n):
...         if n % x == 0:
...             print(n, 'es igual a', x, '*', n/x)
...             break
...         else:
...             # sigue el bucle sin encontrar un factor
...             print(n, 'es un numero primo')

#PASS
# La sentencia pass no hace nada. Se puede usar cuando una sentencia es requerida por la sintáxis pero el programa no
# requiere ninguna acción. Por ejemplo:
>>> while True:
...     pass # Espera ocupada hasta una interrupción de teclado (Ctrl+C)
...

# Definiendo funciones
# Podemos crear una función que escriba la serie de Fibonacci hasta un límite determinado:
>>> def fib(n): # escribe la serie de Fibonacci hasta n
...     """Escribe la serie de Fibonacci hasta n."""
...         a, b = 0, 1
...             while a < n:
...                 print(a, end=' ')
...                     a, b = b, a+b
...                     print()
...
>>> # Ahora llamamos a la funcion que acabamos de definir:
... fib(2000)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597

# La palabra reservada def se usa para definir funciones. Debe seguirle el nombre de la función y la lista de parámetros
# formales entre paréntesis. Las sentencias que forman el cuerpo de la función empiezan en la línea siguiente, y deben estar
# con sangría.
# La primer sentencia del cuerpo de la función puede ser opcionalmente una cadena de texto literal; esta es la cadena de texto
# de documentación de la función, o docstring.

#DOCString
# Hay herramientas que usan las docstrings para producir automáticamente documentación en línea o imprimible, o para
# permitirle al usuario que navegue el código en forma interactiva; es una buena práctica incluir docstrings en el código que
# uno escribe, por lo que se debe hacer un hábito de esto

# Más sobre definición de funciones
# También es posible definir funciones con un número variable de argumentos. Hay tres formas que pueden ser combinadas.
# La forma más útil es especificar un valor por omisión para uno o más argumentos. Esto crea una función que puede ser
# llamada con menos argumentos que los que permite. 
def pedir_confirmacion(prompt, reintentos=4, recordatorio='Por favor, intente nuevamente!'):
    while True:
        ok = input(prompt)
            if ok in ('s', 'S', 'si', 'Si', 'SI'):
                return True
             if ok in ('n', 'no', 'No', 'NO'):
                return False
                reintentos = reintentos - 1
            if reintentos < 0:
                raise ValueError('respuesta de usuario inválida')
                    print(recordatorio)

# Expresiones lambda
# Pequeñas funciones anónimas pueden ser creadas con la palabra reservada lambda. Esta función retorna la suma de sus
# dos argumentos: lambda a, b: a + b. Las funciones Lambda pueden ser usadas en cualquier lugar donde sea
# requerido un objeto de tipo función. Están sintácticamente restringidas a una sola expresión. Semánticamente, son solo
# azúcar sintáctica para definiciones normales de funciones. Al igual que las funciones anidadas, las funciones lambda pueden
# hacer referencia a variables desde el ámbito que la contiene:
>>> def hacer_incrementador(n):
... return lambda x: x + n
...
>>> f = hacer_incrementador(42)
>>> f(0)
42
>>> f(1)
43

#Cadenas de texto de documentación
#pg 32

>>> def f(jamon: str, huevos: str = 'huevos') -> str:
... print("Anotaciones:", f.__annotations__)
... print("Argumentos:", jamon, huevos)
... return jamon + ' y ' + huevos
...
>>> f('carne')
Anotaciones: {'jamon': <class 'str'>, 'huevos': <class 'str'>, 'return': <class 'str'>}
Argumentos: carne huevos
'carne y huevos'
>>>

#Intermezzo: Estilo de codificación
# Ahora que estás a punto de escribir piezas de Python más largas y complejas, es un buen momento para hablar sobre estilo
# de codificación. La mayoría de los lenguajes pueden ser escritos (o mejor dicho, formateados) con diferentes estilos; algunos
# son mas fáciles de leer que otros. Hacer que tu código sea más fácil de leer por otros es siempre una buena idea, y adoptar
# un buen estilo de codificación ayuda tremendamente a lograrlo.
# Para Python, PEP 8 se erigió como la guía de estilo a la que más proyectos adhirieron; promueve un estilo de codificación
# fácil de leer y visualmente agradable. Todos los desarrolladores Python deben leerlo en algún momento; aquí están
# extraídos los puntos más importantes:
# • Usar sangrías de 4 espacios, no tabs.
# 4 espacios son un buen compromiso entre una sangría pequeña (permite mayor nivel de sangrado)y una sangría
# grande (más fácil de leer). Los tabs introducen confusión y es mejor dejarlos de lado.
# • Recortar las líneas para que no superen los 79 caracteres.
# Esto ayuda a los usuarios con pantallas pequeñas y hace posible tener varios archivos de código abiertos, uno al lado
# del otro, en pantallas grandes.
# • Usar líneas en blanco para separar funciones y clases, y bloques grandes de código dentro de funciones.
# • Cuando sea posible, poner comentarios en una sola línea.
# • Usar docstrings.
# • Usar espacios alrededor de operadores y luego de las comas, pero no directamente dentro de paréntesis:
# a = f(1, 2) + g(3, 4).
# • Nombrar las clases y funciones consistentemente; la convención es usar NotacionCamello para clases y
# minusculas_con_guiones_bajos para funciones y métodos. Siempre usá self como el nombre para el primer
# argumento en los métodos (mirá Un primer vistazo a las clases para más información sobre clases y métodos).
# • No uses codificaciones estrafalarias si esperás usar el código en entornos internacionales. El default de Python,
# UTF-8, o incluso ASCII plano funcionan bien en la mayoría de los casos.

##Más sobre listas
#El tipo de dato lista tiene algunos métodos más. Aquí están todos los métodos de los objetos lista:
list.append (x)
#Agrega un ítem al final de la lista. Equivale a a[len(a):] = [x].
list.extend (iterable)
#Extiende la lista agregándole todos los ítems del iterable. Equivale a a[len(a):] = iterable.
list.insert (i, x)
# Inserta un ítem en una posición dada. El primer argumento es el índice del ítem delante del cual se insertará, por lo tanto
# a.insert(0, x) inserta al principio de la lista, y a.insert(len(a), x) equivale a a.append(x).
list.remove (x)
#Quita el primer ítem de la lista cuyo valor sea x. Es un error si no existe tal ítem.
list.pop ([, i])
# Quita el ítem en la posición dada de la lista, y lo devuelve. Si no se especifica un índice, a.pop() quita y devuelve el
# último ítem de la lista. (Los corchetes que encierran a i en la firma del método denotan que el parámetro es opcional, no
# que deberías escribir corchetes en esa posición. Verás esta notación con frecuencia en la Referencia de la Biblioteca de
# Python.)
list.clear ()
#Quita todos los elementos de la lista. Equivalente a del a[:].
list.index (x[, start[, end]])
# Devuelve un índice basado en cero en la lista del primer ítem cuyo valor sea x. Levanta una excepción ValueError si no
# existe tal ítem.
# Los argumentos opcionales start y end son interpetados como la notación de rebanadas y se usan para limitar la
# búsqueda a una subsecuencia particular de la lista. El index retornado se calcula de manera relativa al inicio de la
# secuencia completa en lugar de con respecto al argumento start.
list.count (x)
#Devuelve el número de veces que x aparece en la lista.
list.sort (key=None, reverse=False)
# Ordena los ítems de la lista in situ (los argumentos pueden ser usados para personalizar el orden de la lista, ve sorted()
# para su explicación).
list.reverse ()
#Invierte los elementos de la lista in situ.
list.copy ()
#Devuelve una copia superficial de la lista. Equivalente a a[:].

#Un ejemplo que usa la mayoría de los métodos de lista:
>>> frutas = ['naranja', 'manzana', 'pera', 'banana', 'kiwi', 'manzana', 'banana']
>>> frutas.count('manzana')
2
>>> frutas.count('mandarina')
0
>>> frutas.index('banana')
3
>>> frutas.index('banana', 4) # Find next banana starting a position 4
6
>>> frutas.reverse()
>>> frutas
['banana', 'manzana', 'kiwi', 'banana', 'pera', 'manzana', 'naranja']
>>> frutas.append('uva')
>>> frutas
 ['banana', 'manzana', 'kiwi', 'banana', 'pera', 'manzana', 'naranja', 'uva']
>>> frutas.sort()
>>> frutas
['manzana', 'manzana', 'banana', 'banana', 'uva', 'kiwi', 'naranja', 'pera']
>>> frutas.pop()
'pera'

# Usando listas como pilas
# Los métodos de lista hacen que resulte muy fácil usar una lista como una pila, donde el último elemento añadido es el primer
# elemento retirado ("último en entrar, primero en salir"). Para agregar un ítem a la cima de la pila, use append(). Para retirar
# un ítem de la cima de la pila, use pop() sin un índice explícito. Por ejemplo:

>>> stack = [3, 4, 5]
>>> stack.append(6)
>>> stack.append(7)
>>> stack
[3, 4, 5, 6, 7]
>>> stack.pop()
7
>>> stack
[3, 4, 5, 6]
>>> stack.pop()
6
>>> stack.pop()
5
>>> stack
[3, 4]

# Usando listas como colas
# También es posible usar una lista como una cola, donde el primer elemento añadido es el primer elemento retirado ("primero
# en entrar, primero en salir"); sin embargo, las listas no son eficientes para este propósito. Agregar y sacar del final de la lista
# es rápido, pero insertar o sacar del comienzo de una lista es lento (porque todos los otros elementos tienen que ser
# desplazados por uno).
# Para implementar una cola, usá collections.deque el cual fue diseñado para agregar y sacar de ambas puntas de forma
# rápida. Por ejemplo:
>>> from collections import deque
>>> queue = deque(["Eric", "John", "Michael"])
>>> queue.append("Terry") # llega Terry
>>> queue.append("Graham") # llega Graham
>>> queue.popleft() # el primero en llegar ahora se va
'Eric'
>>> queue.popleft() # el segundo en llegar ahora se va
'John'
>>> queue # el resto de la cola en órden de llegada
['Michael', 'Terry', 'Graham']

# Comprensión de listas
# Las comprensiones de listas ofrecen una manera concisa de crear listas. Sus usos comunes son para hacer nuevas listas
# donde cada elemento es el resultado de algunas operaciones aplicadas a cada miembro de otra secuencia o iterable, o para
# crear una subsecuencia de esos elementos para satisfacer una condición determinada.
# Por ejemplo, asumamos que queremos crear una lista de cuadrados, como:
>>> cuadrados = []
>>> for x in range(10):
... cuadrados.append(x**2)
...
>>> cuadrados
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Nota que esto crea (o sobreescribe) una variable llamada x que sigue existiendo luego de que el bucle haya terminado.
# Podemos calcular la lista de cuadrados sin ningun efecto secundario haciendo:
cuadrados = list(map(lambda x: x**2, range(10)))

#o, un equivalente:
cuadrados = [x ** 2 for x in range(10)]

# Una lista de comprensión consiste de corchetes rodeando una expresión seguida de la declaración for y luego cero o más
# declaraciones for o if. El resultado será una nueva lista que sale de evaluar la expresión en el contexto de los for o if
# que le siguen. Por ejemplo, esta lista de comprensión combina los elementos de dos listas si no son iguales:
>>> [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
#y es equivalente a:
>>> combs = []
>>> for x in [1,2,3]:
... for y in [3,1,4]:
... if x != y:
... combs.append((x, y))
...
>>> combs
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

# Listas por comprensión anidadas
# La expresión inicial de una comprensión de listas puede ser cualquier expresión arbitraria, incluyendo otra comprensión de
# listas.
# Considerá el siguiente ejemplo de una matriz de 3x4 implementada como una lista de tres listas de largo 4:
>>> matriz = [
... [1, 2, 3, 4],
... [5, 6, 7, 8],
... [9, 10, 11, 12],
... ]

# La instrucción
# Hay una manera de quitar un ítem de una lista dado su índice en lugar de su valor: la instrucción del. Esta es diferente del
# método pop(), el cual devuelve un valor. La instrucción del también puede usarse para quitar secciones de una lista o
# vaciar la lista completa (lo que hacíamos antes asignando una lista vacía a la sección). Por ejemplo:
>>> a = [-1, 1, 66.25, 333, 333, 1234.5]
>>> del a[0]
>>> a
[1, 66.25, 333, 333, 1234.5]
>>> del a[2:4]
>>> a
[1, 66.25, 1234.5]
>>> del a[:]
>>> a
[]
#del puede usarse también para eliminar variables:
>>> del a

# Tuplas y secuencias
# Vimos que las listas y cadenas tienen propiedades en común, como el indizado y las operaciones de seccionado. Estas son
# dos ejemplos de datos de tipo secuencia (ver Tipos integrados). Como Python es un lenguaje en evolución, otros datos de
# tipo secuencia pueden agregarse. Existe otro dato de tipo secuencia estándar: la tupla.
# Una tupla consiste de un número de valores separados por comas, por ejemplo:
>>> t = 12345, 54321, 'hola!'
>>> t[0]
12345
>>> t
(12345, 54321, 'hola!')
>>> # Las tuplas pueden anidarse:
... u = t, (1, 2, 3, 4, 5)
>>> u
((12345, 54321, 'hola!'), (1, 2, 3, 4, 5))
>>> # Las tuplas son inmutables:
... t[0] = 88888
Traceback (most recent call last):
 File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> # pero pueden contener objetos mutables:
... v = ([1, 2, 3], [3, 2, 1])
>>> v
([1, 2, 3], [3, 2, 1])

# Conjuntos
# Python también incluye un tipo de dato para conjuntos. Un conjunto es una colección no ordenada y sin elementos repetidos.
# Los usos básicos de éstos incluyen verificación de pertenencia y eliminación de entradas duplicadas. Los conjuntos también
# soportan operaciones matemáticas como la unión, intersección, diferencia, y diferencia simétrica.
# Las llaves o la función set() pueden usarse para crear conjuntos. Notá que para crear un conjunto vacío tenés que usar
# set(), no {}; esto último crea un diccionario vacío, una estructura de datos que discutiremos en la sección siguiente.
#Una pequeña demostración:
>>> canasta = {'manzana', 'naranja', 'manzana', 'pera', 'naranja', 'banana'}
>>> print fruta # muestra que se removieron los duplicados
{'pera', 'manzana', 'banana', 'naranja'}
>>> 'naranja' in canasta # verificación de pertenencia rápida
True
>>> 'yerba' in canasta
False
>>> # veamos las operaciones para las letras únicas de dos palabras
...
>>> a = set('abracadabra')
>>> b = set('alacazam')
>>> a # letras únicas en a
{a', 'r', 'b', 'c', 'd'}
>>> a - b # letras en a pero no en b
{'r', 'b', 'd'}
>>> a | b # letras en a o en b o en ambas
{'a', 'c', 'b', 'd', 'm', 'l', 'r', 'z'}
>>> a & b # letras en a y en b
{'a', 'c'}
>>> a ^ b # letras en a o b pero no en ambos
{'b', 'd', 'm', 'l', 'r', 'z'}

# Diccionarios
# Otro tipo de dato útil incluído en Python es el diccionario (ver Tipos integrados). Los diccionarios se encuentran a veces en
# otros lenguajes como "memorias asociativas" o "arreglos asociativos". A diferencia de las secuencias, que se indexan
# mediante un rango numérico, los diccionarios se indexan con claves, que pueden ser cualquier tipo inmutable; las cadenas y
# números siempre pueden ser claves. Las tuplas pueden usarse como claves si solamente contienen cadenas, números o
# tuplas; si una tupla contiene cualquier objeto mutable directa o indirectamente, no puede usarse como clave. No podés usar
# listas como claves, ya que las listas pueden modificarse usando asignación por índice, asignación por sección, o métodos
# como append() y extend().
# Lo mejor es pensar en un diccionario como un conjunto no ordenado de pares clave: valor, con el requerimiento de que las
# claves sean únicas (dentro de un diccionario en particular). Un par de llaves crean un diccionario vacío: {}. Colocar una lista
# de pares clave:valor separados por comas entre las llaves añade pares clave:valor iniciales al diccionario; esta también es la
# forma en que los diccionarios se presentan en la salida.
# Las operaciones principales sobre un diccionario son guardar un valor con una clave y extraer ese valor dada la clave.
# También es posible borrar un par clave:valor con del. Si usás una clave que ya está en uso para guardar un valor, el valor
# que estaba asociado con esa clave se pierde. Es un error extraer un valor usando una clave no existente.
# Hacer list(d.keys()) en un diccionario devuelve una lista de todas las claves usadas en el diccionario, en un orden
# arbitrario (si las querés ordenadas, usá en cambio sorted(d.keys()).
# 6
#  Para controlar si una clave está en el diccionario,
# usá el in. Un pequeño ejemplo de uso de un diccionario:

>>> tel = {'jack': 4098, 'sape': 4139}
>>> tel['guido'] = 4127
>>> tel
{'sape': 4139, 'jack': 4098, 'guido': 4127}
>>> tel['jack']
4098
>>> del tel['sape']
>>> tel['irv'] = 4127
>>> tel
{'jack': 4098, 'irv': 4127, 'guido': 4127}
>>> list(tel.keys())
['irv', 'guido', 'jack']
>>> sorted(tel.keys())
['guido', 'irv', 'jack']
>>> 'guido' in tel
True
>>> 'jack' not in tel
False

#El constructor dict() crea un diccionario directamente desde secuencias de pares clave-valor:
>>> dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
{'sape': 4139, 'jack': 4098, 'guido': 4127}
# Además, las comprensiones de diccionarios se pueden usar para crear diccionarios desde expresiones arbitrarias de clave y
# valor:
>>> {x: x ** 2 for x in (2, 4, 6)}
{2: 4, 4: 16, 6: 36}
# Cuando las claves son cadenas simples, a veces resulta más fácil especificar los pares usando argumentos por palabra
# clave:
>>> dict(sape=4139, guido=4127, jack=4098)
{'sape': 4139, 'jack': 4098, 'guido': 4127}

#Página 41

