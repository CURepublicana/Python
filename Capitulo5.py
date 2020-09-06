#Capítulo 5: Control de excepciones
#A medida que vaya a trabajar en su código, se puede encontrar que hay algunos
#momentos en los que tendrá que trabajar con excepciones en el código. Esto
#puede ser confuso para el principiante, pero es muy importante aprender cómo
#manejar estos para que pueda ir a su alrededor, o al menos no tener el
#programa de cierre hacia abajo cuando la excepción se eleva por el
#ordenador. En algunos casos, que son capaces de plantear algunas de sus
#propias excepciones, incluso si son vistos como normales por el compilador,
#en base a lo que le gustaría que suceda dentro de nuestro código. Vamos a
#echar un vistazo a cómo el manejo de excepciones y cómo se puede tratar con
#ellos en su código.

#Si hay una condición anormal que está pasando con su código, ya sea los que
#el compilador reconoce automáticamente o te prepara para su programa,
#tendrá que utilizar la idea de excepciones en este código. Como se ha
#mencionado, hay algunas de estas condiciones que el compilador y el código
#no permitirá que hagas. Por ejemplo, si se añade a la declaración equivocada
#al código, se escribe incorrectamente algunas de las palabras y no puede
#encontrar la función o variable que se quiere o intenta dividir por cero, es
#posible que el intérprete no es capaz de manejar la petición y se produce una
#excepción.
#Además, hay algunas ocasiones en las que decidir que el programa o
#aplicación que se está trabajando deben tener una nueva excepción. Éste puede
#ser visto como muy bien por el intérprete, sino por lo que le gustaría hacer el
#programa, que desea asegurarse de que el código levanta una excepción. Por
#ejemplo, usted puede estar trabajando en un sitio web que sólo se va a
#permitir a los usuarios que tengan 18 años o más en la misma. Se podría lanzar
#una excepción que aparece cuando el usuario pone su edad en menores de 18
#años como para que el programa sabe cómo manejar esto.
#Como vas a través del programa de Python, echar un vistazo a través de la
#biblioteca que está ahí y que está seguro de notar que las excepciones ya están
#presentes en ese país. Esto puede ayudarle a escribir su código mucho mejor,
#ya que será capaz de llevar a cabo y utilizarlos como desee. Una de las
#excepciones que usted está seguro de correr en en algún momento y que ya se
#encuentran en la biblioteca de Python incluye cuando intenta dividir por cero o
#cuando intenta leer a un punto que está más allá del final de su archivo.
#En algunos casos, es posible que desee permitir que estas cosas suceden y
#aquí es donde el manejo de excepciones vendrá. Si intenta dividir por cero,
#por ejemplo, y no se trabaja en el manejo de excepciones, sólo se va a tener un
#error que se acaba de cerrar el programa. Esta no es la mejor idea cuando se
#está trabajando en un nuevo código; normalmente se desea algo que aparece en
#lugar de la computadora acaba de abandonar. Con la ayuda de manejo de
#excepciones, usted será capaz de decirle a la computadora para escribir un
#mensaje, tal como “usted está tratando de dividir por cero!” Para que el
#usuario sepa lo que están haciendo mal, en lugar de sólo la sensación de que
#algo está mal con el ordenador.
x = 10
y = 0
result = 0
try:
    result = x/y
    print(result)
except ZeroDivisionError:
    print(“You are trying to divide by zero.”)

#Definición de algunos de sus propias excepciones
#Con el ejemplo que nos miramos arriba, estábamos hablando de lo que ocurre
#cuando el compilador ve y error que no es capaz de manejar. Pero a veces
#usted va a escribir un código que va a necesitar algunas excepciones
#especiales para ayudar a que funcione correctamente. Estas excepciones
#pueden parecer como que funcionará bien en el interior del compilador, pero
#debido al código que está tratando de escribir, que desee incrementar estos
#errores en base a las respuestas que el usuario le da.

class CustomException(Exception):
    def_init_(self, value):
    self.parameter = value
    def_str_(self):
return repr(self.parameter)
try:
    raise CustomException(“This is a CustomError!”)
except CustomException as ex:
    print(“Caught:”, ex.parameter)

#Dentro de este código, se ha configurado una de sus propias excepciones y el
#mensaje “Atrapados: Este es un CustomError!” Es lo que se mostrará cuando,
#o incluso el usuario, lugares en la información que pone en marcha el
#error. Esta es una buena manera de mostrar su excepción personalizada en el
#interior delprograma, especialmente si es algo que desea sólo para el
#programa, y no una excepción que es particular de Python.

